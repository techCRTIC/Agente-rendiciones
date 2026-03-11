---
name: android-app-setup
description: Initiates a perfect Expo/React Native app structure tailored strictly for generating Android .apk files. Use this skill when the user wants to start a new Android application project or create an .apk. It guides the user through selecting ui/functional packages and prepares visualizers.
license: Complete terms in LICENSE.txt
---

# Android App Setup (.apk)

This skill provides a structured workflow for initializing a new Android Application project using React Native and Expo, which is the most efficient way to generate an Android `.apk` file and visualize changes instantly.

## Workflow

When triggered, always follow these steps exactly in order:

### 1. Present Options to the User
Before running any scripts, you MUST ask the user about their preferred tech stack for this app.
Read the catalog files and present a concise summary of the options (with their pros/cons) to the user:
- For UI Packages, read and summarize: `references/visual_packages.md`
- For Functional Packages, read and summarize: `references/functional_packages.md`

Ask the user to select:
1. One UI Library (or 'none')
2. One Routing system (or 'none')
3. One State Management (or 'none')
4. One Fetching Library (or 'none')
5. One Storage Library (or 'none')
6. What should the name of the project folder be?

**Wait for the user's response before proceeding to Step 2.**

### 2. Initialize the Project
Once the user has made their selections, use the initialization script to scaffold the app and install the chosen packages.
Run the script as follows, omitting arguments the user didn't want:

```bash
python scripts/init_android_project.py <project_folder_name> \\
  --ui <nativewind|paper|tamagui|gluestack|none> \\
  --routing <expo-router|react-navigation|none> \\
  --state <zustand|redux|none> \\
  --fetching <tanstack|axios|none> \\
  --storage <mmkv|asyncstorage|none>
```

Wait for the script to finish. It will automatically scaffold the app, install dependencies, and configure `eas.json` to output an APK format instead of an AAB format.

### 3. Setup Visualizers & Next Steps
After initialization is complete, explain to the user how they can visualize their app.

**Visualizer Options:**
Tell the user they have two ways to see their app instantly:
1. **Expo Go (Physical Device):** Instruct them to run `npx expo start` in the terminal from the new folder, download the "Expo Go" app on their Android phone, and scan the QR code.
2. **Android Emulator (Local PC):** Instruct them that if they have Android Studio installed, they can press `a` in the terminal after running `npx expo start` to open the app in a virtual emulator.

**Generating the `.apk` in the Cloud (EAS):**
Instruct the user that when they are ready to build the app, they must run:
`eas build -p android --profile preview`
This will compile the code and return a link to download the final `.apk` wrapper, as configured automatically by the script.

**Generating & Launching the `.apk` Locally (The Ninja Way):**
If the user prefers to compile locally (much faster for iteration), the script has already configured the environment with:
- Redirección de paths a `C:/tmp` (para evitar errores de OneDrive/LongPaths).
- Arquitectura `arm64-v8a` (más rápido).
- Configuración de memoria optimizada.

Para lanzar en el celular conectado:
```bash
npm run android
# o directamente npx expo run:android
```

**Si algo falla (Troubleshooting):**
Si el dispositivo aparece como `unauthorized` o hay errores de "variant", consulta:
`references/troubleshooting.md`

Para asegurar un estado limpio en caso de errores persistentes:
```bash
npx expo install --fix
npx expo prebuild --platform android --clean
npm run android
```

**Configuración inicial del entorno (Solo una vez):**
Si el usuario aún no tiene Java/SDK en su PC:
```bash
powershell -ExecutionPolicy Bypass -File scripts/setup_local_env.ps1
```
