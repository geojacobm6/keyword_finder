pyinstaller backend/engine.py --distpath dist --paths=backend
rm -rf build/
rm -rf engine.spec
npm run package-mac
npm run create-installer-mac
npm run package-win
node installers/windows/createinstaller.js
npm run package-linux
npm run create-debian-installer
