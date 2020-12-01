var express = require('express'),
    mysql = require('mysql'),
    request = require('request'),
    cors = require('cors')
// var session = require("express-session");
var port = process.env.PORT || process.env.port || 5000;
var bodyParser = require('body-parser');
let { PythonShell } = require('python-shell');
// const { json } = require("body-parser")

var app = express();
var sickName=""
// 跨域
app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Headers", "X-Requested-With, Accept, Content-Type, Cookie");
    res.header("Access-Control-Allow-Origin", "*");
    // res.setHeader("Access-Control-Allow-Methods", "GET, HEAD, POST, PUT, DELETE, TRACE, OPTIONS, PATCH");
    next();
}); 

app.use(bodyParser.urlencoded());
app.use(bodyParser.json());
app.listen(port, function () {
    console.log(`[app.listen]Node app is running on port ${port}`);
});
app.set('view engine', 'ejs');
// app.set("views", __dirname + "/views");
app.set("views", "./views");
app.use(express.static('public'))

app.get("/", function (req, res) {
    app.use(express.static('./views'))
    res.render('index.ejs', {
        userName: "chen"
    })
});

app.get('/gg', async function (req, res) {
    res.set('Access-Control-Allow-Origin', '*')
    // 擷取醫院名稱及評論
    await runPy('app.py', ['皮膚']).then(async(result) => {
        let parsedString = JSON.parse(result[0]);
        let command = JSON.parse(result[1]);
        //整理分析所需格式
        // for (let i = 0; i < command.length; i++) {
        console.log("開始分析資料")
        
        for (let i = 0; i < 2; i++) {
            let temp = []
            for (let j = 0; j < command[i]['data'].length; j++) {
                temp.push(command[i]['data'][j])
            };

            await runPy('./dataCheck/4_runModel.py', temp).then((result)=>{
                let level=JSON.parse(result[result.length-1])
                parsedString[i]['level']= level['level']
                console.log(parsedString[i])
            })

            // //各醫院重新進行評分
            // await runPy("getCommand.py", temp).then((result)=>{
            //     let level=JSON.parse(result[0])
            //     parsedString[i]['level']= level['level']
            //     // console.log(parsedString[i])
            // })
            // 各醫院重新進行評分

            res.json(parsedString);
        };
        command = null
        parsedString = null
    })
})

app.post('/falldown', (req, res)=> {
    // app.use(express.static('./falldown'))
    app.use(express.static('./falldown/saved_model/my_model/'))
     runPy("./falldown/test.py",  ['皮膚']).then((result)=>{
        // let sickName=JSON.parse(result[result.length-1])
        console.log(result[result.length-1])
        // res.json(sickName);
    })
});


app.post('/ss', (req, res)=> {
    // temp =req.body.dataUrl.toDataURL()
     runPy("SickName.py", req.body.dataUrl).then((result)=>{
        // console.log(result)
        sickName=JSON.parse(result);
        // // sickName=JSON.parse(result);
        // // console.log(result)
        // console.log(sickName)
        res.json(sickName)
    })
});


async function runPy(path, code) {
    //'./dataCheck/4_runModel.py'
    const options = {
        args: code
    }
    const result = await new Promise((resolve, reject) => {
        PythonShell.run(path, options, function (err, results) {
            if (err) return reject(err);
            // console.log(results[results.length-1]['level'])
            return resolve(results);
        })
    })
    return result
}