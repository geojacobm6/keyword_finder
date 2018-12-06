const path = require('path')
const {app, BrowserWindow, ipcMain} = require('electron')
const url = require('url')
let {PythonShell} = require('python-shell')


function searchKeyword(value) {
    var python = require('child_process').spawn('python', ['./backend/finder.py', value]);
    python.stdout.on('data', function(data){
        window.loadURL("data:text/html;charset=utf-8," + encodeURI(data));
    });
  }

app.on('ready', createWindow)

app.on('window-all-closed', () => {
    // On macOS it is common for applications and their menu bar
    // to stay active until the user quits explicitly with Cmd + Q
    if (process.platform !== 'darwin') {
      app.quit()
    }
  })


function createWindow () {

//    window.loadURL(url.format({
//        pathname: path.join(__dirname, '..', 'backend', 'templates', 'index.html'),
//        protocol: 'file:',
//        slashes: true
//      }));
    PythonShell.run('./backend/engine.py',  function  (err, results)  {
     if  (err)  console.log(err);
    });

    window = new BrowserWindow({width: 800, height: 600,
                                frame: true,
                                webPreferences: {
                                    webSecurity: false,
                                    plugins: true
                                    }
                                });
    window.webContents.openDevTools()
//    window.loadURL(url.format({
//        pathname: path.join(__dirname, '..', 'image', 'youtube.jpg'),
//        protocol: 'file:',
//        slashes: true
//    }));
    window.loadURL(url.format({
        pathname: path.join(__dirname, '..', 'backend', 'templates', 'starter.html'),
        protocol: 'file:',
        slashes: true
    }));

//    setTimeout(function() {
//        window.loadURL("http://127.0.0.1:5000/");
//    }, 7000);

 }

ipcMain.on('search-keyword-event', function(event, title) {
    searchKeyword(title);
//    event.sender.send("search-keyword-event-finished", "dataaaa");
});