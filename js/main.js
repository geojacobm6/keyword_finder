const path = require('path')
const {app, BrowserWindow, ipcMain} = require('electron')
const url = require('url')
const getPort = require('get-port');

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
    PythonShell.end(function (err,code,signal) {
      if (err) throw err;
    });
});

function createWindow () {
    (async () => {
        let port = await getPort();
        global.port = port;
        var options = {
          args: [port]
        };
        PythonShell.run('./backend/engine.py', options,  function  (err, results)  {
         if  (err)  console.log(err);
        });

        window = new BrowserWindow({width: 800, height: 600,
                                    frame: true,
                                    webPreferences: {
                                        webSecurity: false,
                                        plugins: true
                                        },
                                    });
//        window.webContents.openDevTools()

        window.loadURL(url.format({
            pathname: path.join(__dirname, '..', 'backend', 'templates', 'starter.html'),
            protocol: 'file:',
            slashes: true
        }));
    })();
 }