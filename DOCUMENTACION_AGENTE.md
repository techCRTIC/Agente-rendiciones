# Documentación: Agente de Rendiciones (n8n)

Este documento explica de forma detallada el funcionamiento del "Agente rendiciones", un sistema de IA diseñado para optimizar la gestión de rendiciones de gastos corporativos, orquestado a través de n8n.

## Contexto del Proyecto y Arquitectura

El sistema se integra directamente a **WhatsApp**, permitiendo a los usuarios enviar fotografías de recibos y documentos financieros de forma rápida y sencilla. El agente actúa como el motor principal que, mediante **visión artificial y procesamiento del lenguaje natural (NLP)**, extrae los datos relevantes de las imágenes y los estructura en la base de datos corporativa.

La arquitectura del ecosistema está concebida bajo un enfoque de **microservicios**, lo que garantiza alta escalabilidad y robustez frente a un gran volumen de transacciones. Además, el flujo incorpora y se apoya en algoritmos de **detección de anomalías** orientados a identificar posibles fraudes y errores en los comprobantes, sumando una vital capa de seguridad y precisión. 

El resultado global de esta implementación es una **reducción drástica en el tiempo de procesamiento** de las rendiciones y una mejora significativa en la **integridad de los datos financieros**.


## 1. Visión General del Flujo

El objetivo del agente es interactuar directamente con los usuarios a través de WhatsApp. Cuando un usuario envía un mensaje (particularmente una imagen de un recibo, boleta o factura), el sistema realiza las siguientes macro-tareas:

1. **Autenticación**: Verifica si el número de teléfono del emisor está autorizado.
2. **Extracción (IA)**: Analiza la imagen del documento usando Inteligencia Artificial para extraer los datos principales (Fecha, RUT, Proveedor, Monto, etc.).
3. **Validación interactiva (Estado)**: Envía los datos extraídos al usuario por WhatsApp para que los apruebe y va solicitando información adicional (como la actividad, tipo de documento o tipo de rendición) mediante un sistema conversacional de pasos.
4. **Almacenamiento temporal**: Guarda el "Estado" de la conversación en una hoja de cálculo temporal ("Memoria Mensajes") para llevar el hilo de cada usuario.
5. **Cierre y Registro Oficial**: Una vez recopilada y confirmada toda la información, sube la imagen a Google Drive y registra la rendición en la hoja oficial correspondiente (Caja chica, Fondo por rendir o Reembolso) enviando el enlace de confirmación al usuario.

---

## 2. Paso a Paso Detallado

A continuación, el detalle lógico de cómo operan los ~300 nodos definidos en el flujo:

### Paso 1: Recepción del Mensaje (WhatsApp)
- **WhatsApp Trigger**: Inicia el flujo cada vez que llega un mensaje vía webhook.
- **Validación Inicial**: 
  - Se conecta a Google Sheets (`"Numeros Autorizados"`) para verificar que el número (`wa_id`) que escribe, exista en la base de datos permitida.
  - Verifica mediante Nodos `IF` que el mensaje tenga la estructura correcta y analiza si el usuario está a media transacción revisando la hoja `"Memoria Mensajes"`.

### Paso 2: Análisis de Imágenes y OCR (A través de IA)
- **Si el mensaje es una imagen** (`messages[0].type == image`):
  - El nodo **Prueba (WhatsApp mediaUrlGet)** descarga el archivo multimedia (foto del recibo).
  - Mediante un **HTTP Request** y conectores de IA (`Google Gemini` o `OpenAI`), se analiza la imagen.
  - El nodo de **Código (Code)** toma el texto interpretado por la IA y lo formatea como JSON. Extrae los siguientes campos: Fecha, Tipo de documento, N° de documento, Proveedor, RUT proveedor, Detalle de gasto, Actividad y Monto.

### Paso 3: Aprobación y Sistema Conversacional de "Estados"
Dado que WhatsApp no preserva el contexto nativamente en n8n como si fuera un chat interactivo, el flujo utiliza una hoja de Google Sheets llamada **"Memoria Mensajes"** como base de datos de estado (State Machine).

- El flujo inserta o actualiza una fila temporal para el ID de usuario especificando su avance.
- **Primer Mensaje al Usuario**: El agente envía un texto por WhatsApp que reza:
  > "Su documento ha sido escaneado, los resultados son los siguientes: ... Aprueba los datos? Escriba Si o No".
- **Cascada de Nodos `IF` y `Switch`**: Dependiendo de si la respuesta es "*Si*" o "*No*", y en qué "*Estado*" guardado se encuentra el usuario, ocurre lo siguiente:
  - **Rechazo (No)**: Se elimina la fila temporal y el archivo provisional, pidiéndole al usuario que lo vuelva a intentar.
  - **Aprobación (Si)**: El sistema pasa a pedir datos clasificados y de categorización.

### Paso 4: Completando la Información Manual
Si faltan datos o se requiere catalogarlos de acuerdo al modelo de negocio, el flujo envía botones o listas numeradas por WhatsApp:

1. **Tipo de Documento**: 
   - Pregunta qué es: (1) Boleta, (2) Invoice, (3) Factura, (4) Comprobante, (5) Otro.
2. **Tipo de Rendición**: 
   - Pregunta a qué caja corresponde: (1) Caja chica, (2) Fondo por rendir, (3) Reembolso.
3. **Casos Específicos**:
   - Para Fondos por Rendir y Reembolsos, se añade una pregunta adicional sobre la "Proveniencia" (Nacional o Internacional).
4. **Petición de campos vacíos**: 
   - Existen masivas derivaciones lógicas (múltiples `Switch` y `Send Message`) que validan cada campo de la tabla. Si la IA falló en extraer el Proveedor o la Actividad, envía un mensaje: *"Ingrese proveedor"* o *"Ingrese actividad"*.

*Cada respuesta dada por el usuario reactiva el "WhatsApp Trigger", consulta el "Estado" desde Google Sheets, actualiza el valor faltante y solicita el siguiente.*

### Paso 5: Consolidación (Drive y Hojas Oficiales)
Una vez que en la hoja temporal se detecta que no hay variables vacías y que la rendición fue catalogada:

- **Google Drive (Upload file2)**: Se sube la boleta/factura física y se genera un link público/visible.
- **Inserción Final (Sube a planilla oficial)**: Dependiendo del "Tipo de Rendición", el conjunto de datos más el Link de Drive se insertan en su respectiva pestaña (Caja chica, Fondo por rendir o Reembolso).
- **Limpieza**: La hoja temporal `"Memoria Mensajes"` borra la fila de ese número e ID para evitar duplicados en el futuro (`Delete rows or columns from sheet`).
- **Respuesta de Cierre**: El bot de WhatsApp termina con un mensaje: *"Listo! Su rendición ha sido subida, para hacer cualquier cambio ingrese aquí: [Link a la Planilla]"*.

---

## 3. Resumen y Buenas Prácticas Reaplicables
- **Manejo de Estados con BD externa:** Es un enfoque excepcionalmente astuto utilizar una planilla externa temporal para manejar el *paso a paso* cuando el cliente no responde todo de inmediato. Este patrón es fácilmente migrable a otros lenguajes o flujos (Node.js, Supabase, Firestore, etc.).
- **Limpieza de Errores con IA:** El bloque Javascript (`Code node`) tiene un sistema inteligente para filtrar el JSON generado por los LLM (mediante una expresión regular `/{[\s\S]*}/`). Esto evita que si Gemini responde "Claro, aquí tienes tu JSON: { ... }", el flujo colapse.
- **Seguridad Pre-filtro:** La primera validación bloquea a cualquier persona no deseada impidiendo consumos fantasmas en la API de los LLMs.
