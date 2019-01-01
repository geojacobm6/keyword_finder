pyinstaller backend/engine.py --distpath dist --paths=backend
rm -rf build/
rm -rf engine.spec
#electron-packager .
npm run package-mac
npm run create-installer-mac