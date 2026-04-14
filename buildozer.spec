[app]

title = Calculatrice Kivy
package.name = calculatricekivy
package.domain = org.elisee

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.exclude_dirs = tests,.git,.github,__pycache__,venv,.venv

version = 1.0.0

requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 0

android.permissions =
android.accept_sdk_license = True
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

# Keep this if you later add Java/Kotlin jars.
android.add_jars =

# Faster iterative builds.
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
