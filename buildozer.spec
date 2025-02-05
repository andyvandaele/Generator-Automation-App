[app]
# Locatie van de bronbestanden
source.dir = .

# Naam van de app zoals weergegeven op Android
title = GeneratorAutomationApp

# Unieke pakketnaam (gebruik een eigen domein als je dit later in de Play Store wilt zetten)
package.name = generatorautomationapp
package.domain = org.myapp

# Versienummer van de app
version = 1.0.0

# Python-versie (gebruik 3.9 voor compatibiliteit)
python.version = 3.9

# Welke bestanden moeten worden meegenomen in de build?
source.include_exts = py,png,jpg,kv,atlas

# Vereisten: welke Python-pakketten moeten worden geïnstalleerd?
requirements = python3,kivy,requests

# Android-permissies (pas aan als je extra toegang nodig hebt, zoals Bluetooth of GPS)
android.permissions = INTERNET,ACCESS_NETWORK_STATE,BLUETOOTH,BLUETOOTH_ADMIN

# Android-architectuur instellen voor compatibiliteit
android.arch = arm64-v8a

# Forceer het gebruik van de nieuwste NDK
android.ndk = 23b

# (Optioneel) Pad naar Android SDK en NDK (indien Buildozer deze niet automatisch vindt)
# android.sdk_path = $HOME/.android/sdk
# android.ndk_path = $HOME/.android/ndk

# (Optioneel) Geef aan of je een fullscreen-app wilt
fullscreen = 1

# (Optioneel) Minimale Android-versie waarop de app draait
android.minapi = 21

# (Optioneel) Logniveau (zet op 2 voor minder meldingen, 1 voor meer details)
log_level = 2
