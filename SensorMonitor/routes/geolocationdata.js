var express = require('express');
var fs = require('fs');
var router = express.Router();

router.post('/', function (req, res) {
    var data = req.body;
    //console.log(req.body);
    console.log(req.headers);
    fs.writeFileSync('./public/json/' + data.deviceId + '.json', JSON.stringify(req.body, undefined, 2));
    res.send("Success");
});
module.exports = router;