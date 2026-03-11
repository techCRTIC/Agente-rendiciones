# Catálogo de Paquetes Visuales (UI) para React Native

Esta referencia debe usarse para mostrar a los usuarios las opciones disponibles para construir la interfaz de usuario de su aplicación Android. A continuación se presentan las librerías de UI más recomendadas para aplicaciones modernas.

## 1. NativeWind (Tailwind CSS para React Native)
- **Usos**: Para desarrolladores familiarizados con Tailwind CSS en la web, que quieren usar exactamente las mismas clases de utilidad en React Native.
- **Pros**:
  - Curva de aprendizaje cero si ya conoces Tailwind.
  - Altamente personalizable y sin componentes prescritos.
  - Excelente rendimiento (compila las clases en estilos durante la construcción).
- **Contras**:
  - Requiere configuración inicial (babel, tailwind.config.js).
  - No provee componentes hechos (modales, menús, etc.), solo utilidades de estilo.
- **Especialidad**: Consistencia visual rápida, diseño desde cero.

## 2. React Native Paper
- **Usos**: Para aplicaciones que requieren seguir estrictamente las guías de Material Design de Google.
- **Pros**:
  - Implementación impecable de Material Design 3.
  - Muy estable y respaldado por una gran comunidad (Callstack).
  - Componentes accesibles y con soporte para temas oscuros/claros de serie.
- **Contras**:
  - Difícil de personalizar si quieres un diseño que se aleje de Material Design.
- **Especialidad**: Aplicaciones corporativas o de utilerías que necesitan fluir como apps nativas de Android estándar.

## 3. Tamagui
- **Usos**: Aplicaciones universales (Web y Native) que requieren animaciones complejas y máxima velocidad.
- **Pros**:
  - Rendimiento extremadamente alto gracias a su compilador optimizado.
  - Creado específicamente para mantener 100% el mismo código entre Web y Native.
  - Sistema de temas y variantes potentísimo.
- **Contras**:
  - Curva de aprendizaje empinada para entender su configuración y compilador.
  - Es relativamente nuevo, el ecosistema completo sigue creciendo.
- **Especialidad**: Apps de muy alto rendimiento, animaciones complejas, y código compartido Web/Mobile.

## 4. Gluestack UI (Antiguo NativeBase)
- **Usos**: Para quienes quieren componentes accesibles, tematizables y listos para usar sin atarse a un estilo como Material Design.
- **Pros**:
  - Diseño agnóstico (fácil de adaptar a cualquier marca).
  - Alta accesibilidad de serie.
  - Preparado para aplicaciones universales.
- **Contras**:
  - Puede resultar pesado si solo necesitas un par de componentes.
  - Migración desde NativeBase puede ser compleja si ya hay un proyecto existente (no aplica en proyectos nuevos).
- **Especialidad**: Construcción rápida de MVP (Producto Mínimo Viable) con un sistema de diseño sólido y flexible.
