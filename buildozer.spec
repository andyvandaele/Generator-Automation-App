[app]
# (str) Title of your application
title = GeneratorAutomationApp

# (str) Package name
package.name = generatorautomationapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.myapp

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy,requests

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Enable fullscreen mode (default: 1)
fullscreen = 1

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is ok for Kivy-based app
android.apptheme = "@android:style/Theme.NoTitleBar"

# (str) Presplash of the application
presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/data/icon.png

# (str) Supported Android API version (minimum: 21)
android.minapi = 21

# (str) Android SDK version to use (default: latest installed)
android.sdk = latest

# (str) Android NDK version to use (default: latest installed)
android.ndk = 23b

# (str) Android NDK API to use (default: android.minapi)
android.ndk_api = 21

# (str) Bootstraps to use for android builds (default: sdl2)
android.bootstrap = sdl2

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# (list) The list of supported architectures
android.archs = armeabi-v7a, arm64-v8a

# (list) Features you wish to use (android only)
android.features = onPause,onResume

# (str) The format used to package the app for android
# (one of: apk, aab)
android.package_type = apk
