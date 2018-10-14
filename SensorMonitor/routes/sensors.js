var express = require('express');
var router = express.Router();
var fs = require("fs");

/* GET users listing. */
router.post('/', function (req, res) {
    try {
        res.setHeader('Content-Type', 'application/json');
        console.log("Sensor data", req.body);
        let eachObj = req.body;
        if (parseInt(eachObj.light) > 300) {
            eachObj.alert = "Beep due to light intensity greater than 300";
        }
        else if (parseInt(eachObj.temperature) > 10) {
            eachObj.alert = "Beep is due to temperature difference greater than 10F";
        }
        else {
            eachObj.alert = "-";
        }
        fs.writeFileSync('./public/json/sensorsData.json', JSON.stringify(req.body, undefined, 2));
        console.log("Sensor done");
        res.send();
    } catch (e) {
        console.log(e);
    }
// res.send(JSON.stringify({name: "AmrishJ", surname: "Jhaveri"}));
});

module.exports = router;