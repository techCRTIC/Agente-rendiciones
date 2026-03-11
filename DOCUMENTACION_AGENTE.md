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

---

## English

# Documentation: Expense Agent (n8n)

This document explains in detail the operation of the "Expense Agent", an AI system designed to optimize the management of corporate expense reports, orchestrated through n8n.

## Project Context and Architecture

The system integrates directly with **WhatsApp**, allowing users to send photographs of receipts and financial documents quickly and easily. The agent acts as the main engine which, through **computer vision and natural language processing (NLP)**, extracts the relevant data from the images and structures it in the corporate database.

The ecosystem's architecture is conceived under a **microservices** approach, which guarantees high scalability and robustness against a large volume of transactions. In addition, the flow incorporates and relies on **anomaly detection** algorithms aimed at identifying possible fraud and errors in receipts, adding a vital layer of security and precision.

The overall result of this implementation is a **drastic reduction in processing time** for expense reports and a significant improvement in the **integrity of financial data**.

## 1. Flow Overview

The goal of the agent is to interact directly with users through WhatsApp. When a user sends a message (particularly an image of a receipt, ticket, or invoice), the system performs the following macro-tasks:

1. **Authentication**: Verifies if the sender's phone number is authorized.
2. **Extraction (AI)**: Analyzes the document image using Artificial Intelligence to extract the main data (Date, Tax ID, Provider, Amount, etc.).
3. **Interactive Validation (State)**: Sends the extracted data to the user via WhatsApp for approval and requests additional information (such as activity, document type, or expense type) through a conversational step system.
4. **Temporary Storage**: Saves the "State" of the conversation in a temporary spreadsheet ("Message Memory") to keep track of each user.
5. **Closure and Official Registration**: Once all information is gathered and confirmed, it uploads the image to Google Drive and registers the expense in the corresponding official sheet (Petty Cash, Fund to be Rendered, or Reimbursement) sending the confirmation link to the user.

---

## 2. Detailed Step-by-Step

Below is the logical detail of how the ~300 nodes defined in the flow operate:

### Step 1: Message Reception (WhatsApp)
- **WhatsApp Trigger**: Starts the flow every time a message arrives via webhook.
- **Initial Validation**: 
  - Connects to Google Sheets (`"Allowed Numbers"`) to verify that the number (`wa_id`) writing exists in the permitted database.
  - Verifies using `IF` Nodes that the message has the correct structure and analyzes if the user is mid-transaction by checking the `"Message Memory"` sheet.

### Step 2: Image Analysis and OCR (via AI)
- **If the message is an image** (`messages[0].type == image`):
  - The **Prueba (WhatsApp mediaUrlGet)** node downloads the media file (receipt photo).
  - Through an **HTTP Request** and AI connectors (`Google Gemini` or `OpenAI`), the image is analyzed.
  - The **Code** node takes the text interpreted by the AI and formats it as JSON. It extracts the following fields: Date, Document Type, Document Number, Provider, Provider Tax ID, Expense Detail, Activity, and Amount.

### Step 3: Approval and "States" Conversational System
Since WhatsApp does not natively preserve context in n8n as if it were an interactive chat, the flow uses a Google Sheets sheet called **"Message Memory"** as a state database (State Machine).

- The flow inserts or updates a temporary row for the user ID specifying its progress.
- **First Message to the User**: The agent sends a text via WhatsApp that says:
  > "Your document has been scanned, the results are as follows: ... Do you approve the data? Type Yes or No".
- **Cascade of `IF` and `Switch` Nodes**: Depending on whether the response is "*Yes*" or "*No*", and what saved "*State*" the user is in, the following occurs:
  - **Rejection (No)**: The temporary row and provisional file are deleted, asking the user to try again.
  - **Approval (Yes)**: The system moves on to ask for classified and categorization data.

### Step 4: Completing Manual Information
If data is missing or needs to be cataloged according to the business model, the flow sends buttons or numbered lists via WhatsApp:

1. **Document Type**: 
   - Asks what it is: (1) Ticket, (2) Invoice, (3) Bill, (4) Voucher, (5) Other.
2. **Expense Type**: 
   - Asks which box it belongs to: (1) Petty Cash, (2) Fund to be rendered, (3) Reimbursement.
3. **Specific Cases**:
   - For Funds to be Rendered and Reimbursements, an extra question is added about the "Origin" (National or International).
4. **Empty Fields Request**: 
   - There are massive logical derivations (multiple `Switch` and `Send Message` nodes) that validate each field of the table. If the AI failed to extract the Provider or Activity, it sends a message: *"Enter provider"* or *"Enter activity"*.

*Each answer given by the user reactivates the "WhatsApp Trigger", queries the "State" from Google Sheets, updates the missing value, and requests the next one.*

### Step 5: Consolidation (Drive and Official Sheets)
Once it is detected in the temporary sheet that there are no empty variables and the expense was cataloged:

- **Google Drive (Upload file2)**: The physical ticket/invoice is uploaded and a public/visible link is generated.
- **Final Insertion (Uploads to official spreadsheet)**: Depending on the "Expense Type", the data set plus the Drive Link are inserted into their respective tab (Petty Cash, Fund to be rendered, or Reimbursement).
- **Cleanup**: The temporary sheet `"Message Memory"` deletes the row of that number and ID to avoid duplicates in the future (`Delete rows or columns from sheet`).
- **Closing Response**: The WhatsApp bot finishes with a message: *"Done! Your expense has been uploaded, to make any changes enter here: [Spreadsheet Link]"*.

---

## 3. Summary and Reapplicable Best Practices
- **State Management with external DB:** It is an exceptionally astute approach to use a temporary external spreadsheet to handle the *step-by-step* when the client does not answer everything immediately. This pattern is easily migratable to other languages or flows (Node.js, Supabase, Firestore, etc.).
- **Error Cleanup with AI:** The Javascript block (`Code node`) has a smart system to filter the JSON generated by LLMs (using a regular expression `/{[\s\S]*}/`). This prevents the flow from collapsing if Gemini responds "Sure, here is your JSON: { ... }".
- **Pre-filter Security:** The first validation blocks any unwanted person, preventing ghost consumptions on the LLM APIs.
