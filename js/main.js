//handle setupevents as quickly as possible
const setupEvents = require('../installers/setupEvents')
if (setupEvents.handleSquirrelEvent()) {
    // squirrel event handled and app will exit in 1000ms, so don't do anything else
    return;
}

const path = require('path')
const {app, BrowserWindow, ipcMain} = require('electron')
const url = require('url')
const getPort = require('get-port')

const PY_DIST_FOLDER = 'dist'
const PY_FOLDER = 'backend'
const PY_MODULE = 'engine' // without .py suffix

const guessPackaged = () => {
  const fullPath = path.join(__dirname, '..', PY_DIST_FOLDER)
  return require('fs').existsSync(fullPath)
}

const getScriptPath = () => {
  if (!guessPackaged()) {
    return path.join(__dirname, '..', PY_FOLDER, PY_MODULE + '.py')
  }
  if (process.platform === 'win32') {
    return path.join(__dirname, '..', PY_DIST_FOLDER, PY_MODULE, PY_MODULE + '.exe')
  }
  return path.join(__dirname, '..', PY_DIST_FOLDER, PY_MODULE, PY_MODULE)
}


let {PythonShell} = require('python-shell')

app.on('ready', createWindow)

app.on('window-all-closed', () => {
    // On macOS it is common for applications and their menu bar
    // to stay active until the user quits explicitly with Cmd + Q
    if (process.platform !== 'darwin') {
      app.quit()
    }
  })

app.on('quit', function() {
    global.py_proc.kill('SIGINT');
    PythonShell.end(function (err,code,signal) {
      if (err) throw err;
    });
});

function createWindow () {
    (async () => {
        let port = await getPort()
        let script = getScriptPath()
        global.port = port;
        var options = {
          args: [port]
        };
        console.log(script)
        console.log(script)
        if (guessPackaged()) {
            global.py_proc = require('child_process').execFile(script, [port])
        } else {
            global.py_proc = PythonShell.run(script, options,  function  (err, results)  {
             if  (err)  console.log(err);
            });
        }
//        PythonShell.run('./backend/engine.py', options,  function  (err, results)  {
//         if  (err)  console.log(err);
//        });

        window = new BrowserWindow({width: 800, height: 600,
                                    frame: true,
                                    webPreferences: {
                                        webSecurity: false,
                                        plugins: true
                                        },
                                    });
//        window.webContents.openDevTools()

        window.loadURL(url.format({
            pathname: path.join(__dirname, '..', 'templates', 'starter.html'),
            protocol: 'file:',
            slashes: true
        }));
    })();
 }