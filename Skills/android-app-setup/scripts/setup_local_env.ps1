# setup_local_env.ps1

Write-Host "Installing Microsoft OpenJDK 17..."
winget install --id Microsoft.OpenJDK.17 -e --accept-package-agreements --accept-source-agreements

# Refresh Environment Variables in the current session
$env:JAVA_HOME = [Environment]::GetEnvironmentVariable("JAVA_HOME", "Machine")
if (-not $env:JAVA_HOME) {
    # Try guessing path if winget didn't update machine env immediately
    $javaPath = (Get-ChildItem -Path "C:\Program Files\Microsoft\jdk-17*" | Select-Object -First 1).FullName
    if ($javaPath) {
        $env:JAVA_HOME = $javaPath
        [Environment]::SetEnvironmentVariable("JAVA_HOME", $javaPath, "Machine")
    }
}
$env:Path += ";$env:JAVA_HOME\bin"

Write-Host "Creating Android SDK directories..."
$androidHome = "$env:LOCALAPPDATA\Android\Sdk"
if (!(Test-Path $androidHome)) {
    New-Item -ItemType Directory -Force -Path $androidHome | Out-Null
}

$cmdlineToolsZip = "$env:TEMP\cmdline-tools.zip"
$cmdlineToolsDir = "$androidHome\cmdline-tools"
if (!(Test-Path "$cmdlineToolsDir\latest\bin\sdkmanager.bat")) {
    Write-Host "Downloading Android Command Line Tools..."
    Invoke-WebRequest -Uri "https://dl.google.com/android/repository/commandlinetools-win-11076708_latest.zip" -OutFile $cmdlineToolsZip
    
    Write-Host "Extracting Command Line Tools..."
    if (!(Test-Path $cmdlineToolsDir)) {
        New-Item -ItemType Directory -Force -Path $cmdlineToolsDir | Out-Null
    }
    Expand-Archive -Path $cmdlineToolsZip -DestinationPath "$cmdlineToolsDir" -Force
    
    # Needs to be inside 'latest' folder
    Rename-Item -Path "$cmdlineToolsDir\cmdline-tools" -NewName "latest" -Force
}

$env:ANDROID_HOME = $androidHome
$env:ANDROID_SDK_ROOT = $androidHome
[Environment]::SetEnvironmentVariable("ANDROID_HOME", $androidHome, "User")
[Environment]::SetEnvironmentVariable("ANDROID_SDK_ROOT", $androidHome, "User")

# Accept licenses recursively
Write-Host "Accepting licenses..."
$sdkmanager = "$cmdlineToolsDir\latest\bin\sdkmanager.bat"
$yes = "y`n" * 10 
$yes | & $sdkmanager --licenses | Out-Null

Write-Host "Installing SDK tools..."
& $sdkmanager "platform-tools" "platforms;android-34" "build-tools;34.0.0" | Out-Null

Write-Host "Adding platform-tools to User PATH..."
$adbPath = "$androidHome\platform-tools"
$currentPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($currentPath -notlike "*$adbPath*") {
    [Environment]::SetEnvironmentVariable("Path", "$currentPath;$adbPath", "User")
    $env:Path += ";$adbPath"
    Write-Host "Added $adbPath to User PATH."
}

Write-Host "Creating Ninja optimization folders @ C:\tmp..."
$tmpFolders = @("C:\tmp\yolo26\build", "C:\tmp\y26\cxx")
foreach ($folder in $tmpFolders) {
    if (!(Test-Path $folder)) {
        New-Item -ItemType Directory -Force -Path $folder | Out-Null
        Write-Host "Created $folder"
    }
}

Write-Host "Setup Completed Successfully! You can now compile Android .apk files locally."
