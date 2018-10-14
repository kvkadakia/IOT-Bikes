var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function (req, res, next) {
    var devicesJson = [{
        "deviceId": "1",
        "deviceType": "Location",
        "deviceStatus": "Healthy",
        "page": "here.html"
    }, {"deviceId": "2", "deviceType": "Temperature, Light", "deviceStatus": "Healthy", "page": "sensorsPage.html"}];
    res.setHeader('Content-Type', 'application/json');
    res.send(JSON.stringify(devicesJson));
});

module.exports = router;
