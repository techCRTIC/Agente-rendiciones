import os
import sys
import subprocess
import argparse

def run_command(command, cwd=None):
    """Ejecuta un comando en la terminal y devuelve el código de salida."""
    try:
        print(f"\\n> Ejecutando: {command}")
        result = subprocess.run(
            command,
            cwd=cwd,
            shell=True,
            check=True,
            text=True
        )
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"\\n[ERROR] Falló la ejecución del comando: {command}")
        sys.exit(e.returncode)

def main():
    parser = argparse.ArgumentParser(description="Inicializa un proyecto base para Android (.apk) con Expo/React Native")
    parser.add_argument("project_name", help="Nombre de la carpeta del proyecto a crear")
    parser.add_argument("--ui", choices=["nativewind", "paper", "tamagui", "gluestack", "none"], default="none", help="Librería de UI a instalar")
    parser.add_argument("--routing", choices=["expo-router", "react-navigation", "none"], default="expo-router", help="Sistema de enrutamiento a instalar")
    parser.add_argument("--state", choices=["zustand", "redux", "none"], default="none", help="Librería de estado a instalar")
    parser.add_argument("--fetching", choices=["tanstack", "axios", "none"], default="none", help="Librería de fetching a instalar")
    parser.add_argument("--storage", choices=["mmkv", "asyncstorage", "none"], default="none", help="Librería de almacenamiento a instalar")
    args = parser.parse_args()

    project_name = args.project_name
    print(f"\\n\\U0001f680 Creando proyecto Android Base '{project_name}' con Expo...")

    # 1. Crear la app usando create-expo-app
    if args.routing == "expo-router":
        run_command(f"npx create-expo-app@latest {project_name}")
    else:
        run_command(f"npx create-expo-app@latest {project_name} --template blank")

    # 2. Preparar los paquetes adicionales
    packages_to_install = []
    
    if args.ui == "nativewind":
        packages_to_install.extend(["nativewind", "tailwindcss", "react-native-reanimated", "react-native-safe-area-context"])
    elif args.ui == "paper":
        packages_to_install.extend(["react-native-paper", "react-native-safe-area-context", "react-native-vector-icons"])
    elif args.ui == "tamagui":
        packages_to_install.extend(["tamagui", "@tamagui/config", "@tamagui/core"])
    elif args.ui == "gluestack":
        packages_to_install.extend(["@gluestack-ui/themed"])

    if args.routing == "react-navigation" and args.routing != "expo-router":
        packages_to_install.extend(["@react-navigation/native", "@react-navigation/native-stack", "react-native-screens", "react-native-safe-area-context"])

    if args.state == "zustand":
        packages_to_install.append("zustand")
    elif args.state == "redux":
        packages_to_install.extend(["@reduxjs/toolkit", "react-redux"])

    if args.fetching == "tanstack":
        packages_to_install.append("@tanstack/react-query")
    elif args.fetching == "axios":
        packages_to_install.append("axios")

    if args.storage == "mmkv":
        packages_to_install.append("react-native-mmkv")
    elif args.storage == "asyncstorage":
        packages_to_install.append("@react-native-async-storage/async-storage")

    # 3. Instalar paquetes si se seleccionaron
    if packages_to_install:
        print(f"\\n\\U0001f4e6 Instalando paquetes seleccionados: {', '.join(packages_to_install)}")
        packages_str = " ".join(packages_to_install)
        run_command(f"npx expo install {packages_str}", cwd=project_name)
    
    # 4. Configurar eas.json para generar APK directamente (en lugar de AAB)
    eas_json_content = '''{
  "build": {
    "preview": {
      "android": {
        "buildType": "apk"
      }
    },
    "preview2": {
      "android": {
        "gradleCommand": ":app:assembleRelease"
      }
    },
    "preview3": {
      "developmentClient": true
    },
    "production": {
      "android": {
        "buildType": "apk"
      }
    }
  }
}'''
    
    eas_path = os.path.join(project_name, "eas.json")
    with open(eas_path, "w") as f:
        f.write(eas_json_content)
        
    print(f"\\n\\U00002705 Configurado eas.json para generar .apk por defecto.")

    # 5. Optimizar localmente para Windows (Ninja Fixes)
    print(f"\\n\\U0001f527 Aplicando optimizaciones 'Ninja' para Windows...")
    
    # Asegurar que existan las carpetas de redirección de build (C:/tmp/)
    tmp_folders = ["C:\\tmp\\yolo26\\build", "C:\\tmp\\y26\\cxx"]
    for folder in tmp_folders:
        try:
            if not os.path.exists(folder):
                os.makedirs(folder, exist_ok=True)
                print(f"   - Creada carpeta temporal: {folder}")
        except Exception as e:
            print(f"   - [AVISO] No se pudo crear {folder}: {e}")

    # Ejecutar prebuild para generar la carpeta android si no existe
    print("   - Generando archivos nativos (expo prebuild)...")
    run_command("npx expo prebuild --platform android --no-install", cwd=project_name)

    gradle_props_path = os.path.join(project_name, "android", "gradle.properties")
    if os.path.exists(gradle_props_path):
        ninja_settings = [
            "\\n# === Windows Ninja Optimizations (Aadded by skill) ===",
            "org.gradle.project.buildDir=C:/tmp/yolo26/build",
            "android.externalNativeBuild.buildStagingDirectory=C:/tmp/y26/cxx",
            "reactNativeArchitectures=arm64-v8a",
            "org.gradle.jvmargs=-Xmx2048m -XX:MaxMetaspaceSize=512m",
            "org.gradle.parallel=true"
        ]
        with open(gradle_props_path, "a") as f:
            f.write("\\n".join(ninja_settings) + "\\n")
        print("   - Configurado android/gradle.properties con redirección de paths y arm64-v8a.")

    print(f"\\n\\U0001f389 Proyecto '{project_name}' inicializado correctamente.")
    print("\\nPróximos pasos:")
    print(f"  cd {project_name}")
    print("  npx expo start (Para visualizar la app)")
    print("  eas build -p android --profile preview (Para compilar el .apk en la nube)")
    print("  npx expo run:android (Para compilar y lanzar localmente)")

if __name__ == "__main__":
    main()
