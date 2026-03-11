# Catálogo de Paquetes Funcionales para React Native

Esta referencia describe los paquetes fundamentales de arquitectura y funcionalidad para aplicaciones Expo/React Native. Se debe ofrecer al usuario elegir entre estas opciones para establecer la base lógica de su `.apk`.

---

## 1. Enrutamiento y Navegación

### Expo Router
- **Usos**: Enrutamiento basado en sistema de archivos (similar a Next.js).
- **Pros**: 
  - Archivos = Pantallas. Muy intuitivo.
  - Deep linking automático (enlaces profundos).
  - Estándar oficial moderno recomendado por Expo.
- **Contras**: 
  - Puede ser restrictivo si necesitas una lógica de navegación muy poco convencional.
- **Especialidad**: Apps modernas, migración web a móvil, deep-linking complejo.

### React Navigation
- **Usos**: Enrutamiento declarativo basado en código tradicional.
- **Pros**: 
  - El estándar de la industria por años. Absoluta flexibilidad.
  - Enorme cantidad de tutoriales y soluciones en foros.
- **Contras**: 
  - Configuración manual extensa, especialmente para Deep Linking.
- **Especialidad**: Aplicaciones con flujos de navegación dinámicos o condicionales complejos.

---

## 2. Gestión de Estado Global

### Zustand
- **Usos**: Gestión de estado ligera y sin *boilerplate*.
- **Pros**: 
  - Setup en menos de 5 minutos.
  - Sin necesidad de "Providers" envolviendo la app.
  - API sumamente sencilla e intuitiva.
- **Contras**: 
  - Puede desorganizarse en aplicaciones gigantes si no existen buenas convenciones de equipo.
- **Especialidad**: Estados globales rápidos, aplicaciones medianas o pequeñas, preferencias de usuario.

### Redux Toolkit (RTK)
- **Usos**: Gestión de estado predecible para aplicaciones de gran escala.
- **Pros**: 
  - RTK eliminó el 90% del boilerplate del Redux antiguo.
  - Incluye RTK Query para fetching de datos.
  - Herramientas de depuración (Redux DevTools) imbatibles.
- **Contras**: 
  - Sigue siendo más verboso que Zustand.
  - Curva de aprendizaje moderada para conceptos como `slices` y `thunks`.
- **Especialidad**: Aplicaciones enterprise, flujos financieros, lógica de estado muy compleja.

---

## 3. Fetching de Datos (API Requests)

### TanStack Query (React Query)
- **Usos**: Gestión de estado *asíncrono* (datos que vienen del servidor).
- **Pros**: 
  - Maneja automáticamente caché, reintentos, refetching en background.
  - Reduce drásticamente la lógica de `useEffect` e `isLoading` a mano.
- **Contras**: 
  - Es añadir un paquete grande si tu app solo hace una o dos peticiones en toda su vida útil.
- **Especialidad**: Cualquier aplicación que interactúe activamente con una base de datos o API remota.

### Axios (Convencional)
- **Usos**: Cliente HTTP simple para peticiones.
- **Pros**: 
  - Interceptores para autocompletar tokens de autenticación fácilmente.
  - Sintaxis probada y super conocida.
- **Contras**: 
  - No maneja caché visual ni estados de persistencia automática; se debe codificar manualmente.
- **Especialidad**: Aplicaciones que usan Redux/Zustand para manejar el estado pero necesitan un cliente HTTP robusto.

---

## 4. Almacenamiento Local (Persistencia)

### MMKV (React Native MMKV)
- **Usos**: Almacenar datos locales clave-valor instantáneamente.
- **Pros**: 
  - **30x más rápido que AsyncStorage**. Escrituras y lecturas síncronas.
  - Implementado en C++ (máxima eficiencia).
- **Contras**: 
  - Requiere prebuild o dev client en Expo (no funciona out-of-the-box en Expo Go gratuito sin configuración extra a veces).
- **Especialidad**: Apps de ultra rendimiento, guardar mucha data local.

### AsyncStorage (oficial)
- **Usos**: Almacenamiento estándar y asíncrono.
- **Pros**: 
  - 100% compatible con Expo Go sin pasos extras.
  - Funciona perfecto para el 90% de las necesidades (tokens, preferencias).
- **Contras**: 
  - Asíncrono (requiere `await`), más lento en benchmarks extremos en comparación a MMKV.
- **Especialidad**: Proyectos rápidos, facilidad máxima de uso.
