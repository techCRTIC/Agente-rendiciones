# Agente de Rendiciones | Ecosistema CRTIC

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Node Version](https://img.shields.io/badge/node-%3E%3D20.0-blue)
![License](https://img.shields.io/badge/license-MIT-blue)
![Ecosistema CRTIC](https://img.shields.io/badge/ecosistema-tecnocreativo-%23ff4613)

Un sistema de **Inteligencia Artificial** diseñado para optimizar, centralizar y automatizar la gestión de rendiciones de gastos corporativos, orquestado a través de n8n y accesible íntegramente vía WhatsApp. Construido bajo los estándares tecnológicos de **CRTIC**.

## 🚀 Innovación en Procesos Financieros

El sistema se integra directamente a WhatsApp, permitiendo a los usuarios enviar fotografías de recibos y documentos financieros de forma rápida y ubicua. El agente actúa como el motor principal que, mediante **visión artificial y procesamiento del lenguaje natural (NLP)**, extrae los datos relevantes de las imágenes y los estructura en la base de datos de la organización.

La arquitectura del ecosistema está concebida bajo un enfoque de **microservicios**, lo que garantiza alta escalabilidad y robustez frente a un gran volumen de transacciones. El resultado global de esta implementación es una reducción drástica en el tiempo de procesamiento de las rendiciones y una mejora significativa en la integridad de los datos financieros.

### Características Principales:
* **Autenticación Segura**: Verificación de identidades corporativas en tiempo real.
* **OCR Inteligente**: Extracción quirúrgica de data transaccional mediante Modelos Fundacionales (Google Gemini / OpenAI).
* **State Machine Conversacional**: Un manejo de estados innovador sobre WhatsApp soportado por Bases de Datos NoSQL / Sheets.
* **Detección de Anomalías**: Algoritmos de verificación orientados a blindar contra fraudes e inconsistencias humanas.
* **Enrutamiento Automático**: Sorteo y guardado definitivo de la metadata en las sub-cajas contables respectivas sumado al almacenamiento físico de respaldos en la Nube (Drive).

---

## 🏗️ Arquitectura del Sistema

El flujo, compuesto por casi 300 nodos, dibuja el siguiente ecosistema:

```mermaid
graph TD
    A[Usuario WhatsApp] -->|Envía Foto Boleta| B(Trigger Webhook)
    B --> C{Autenticación Sheet}
    C -->|No Autorizado| X[Cierra Conexión]
    C -->|Autorizado| D[IA Visión Analítica]
    D --> E[Regex Sanitización JSON]
    E --> F[Memoria de Estados Temporal]
    F <-->|Push/Pull Mensajes/Datos| G{Usuario Valida}
    G -->|Clasificación Manual| F
    G -->|Aprobación Final| H[Drive Upload Respaldo]
    H --> I{Enrutador de Rendición}
    I --> J[Caja Chica]
    I --> K[Fondo por Rendir]
    I --> L[Reembolso]
    J --> M((Fin Flujo - Notificación))
    K --> M
    L --> M
    M --> N[Cleaner de Estados Temporales]
```

## 🎨 Frontend y Estética (CRTIC Style)

Este proyecto y su documentación interna adhieren de manera estricta a la **Esencia CRTIC**. 
Consulte el archivo `Documentacion-del-proyecto.html` incluido en la raíz para la presentación oficial interactiva.

* **Tipografía**: Manrope.
* **Estilizado**: Light Theme Refinado, Esquinas Afiladas (`border-radius: 0px`).
* **Energía**: Acentos vibrantes `#ff4613` (Naranja Transaccional) y `#3bd4ae` (Mint Tecnológico).

---
> *El Futuro sí existe.* - Centro para la Revolución Tecnológica en Industrias Creativas.
