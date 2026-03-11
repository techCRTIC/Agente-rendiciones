# Android Troubleshooting & Optimization (Ninja Fixes)

Guía para resolver los problemas más comunes al desarrollar para Android en Windows.

## 1. Dispositivo No Autorizado (ADB)

**Síntoma:** `adb devices` muestra `RFCY326S99A unauthorized`.
**Solución:**
1. Desconecta y vuelve a conectar el cable USB.
2. Mira la pantalla de tu celular. Debería aparecer un mensaje: `"¿Permitir depuración USB?"`.
3. Marca **"Permitir siempre desde esta computadora"** y dale a **Aceptar**.
4. Ejecuta `adb devices` de nuevo para confirmar que aparece como `device`.

## 2. No matching variant of project ... found (Gradle Error)

**Síntoma:** El build falla diciendo que no encuentra una "variant" compatible para módulos como `expo`, `async-storage`, etc.
**Causa:** Incompatibilidad entre la caché de Gradle y las dependencias instaladas, o desincronización de paquetes native.
**Solución:**
1. Ejecuta `npx expo install --fix` para sincronizar versiones.
2. Limpia el build: `cd android; ./gradlew clean; cd ..`.
3. Si persiste, recrea la carpeta nativa: `npx expo prebuild --platform android --clean`.

## 3. Errores de Rutas Largas en Windows

**Síntoma:** El build de C++ (Ninja/CMake) falla con errores crípticos de "file not found" o "mkdir failed".
**Causa:** Windows tiene un límite de 260 caracteres en rutas de archivos, y OneDrive a veces bloquea archivos temporales.
**Solución:**
Redirector de salida configurado en `android/gradle.properties`:
```properties
org.gradle.project.buildDir=C:/tmp/yolo26/build
android.externalNativeBuild.buildStagingDirectory=C:/tmp/y26/cxx
```
*Asegúrate de que estas carpetas existan en tu disco C:.*

## 4. Optimización de Arquitectura

Para acelerar las compilaciones locales en PC, compila solo para la arquitectura de tu teléfono (usualmente arm64):
```properties
reactNativeArchitectures=arm64-v8a
```
Esto evita compilar para x86/x86_64, ahorrando hasta un 70% de tiempo en el build nativo.
