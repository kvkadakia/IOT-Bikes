var express = require('express');
var fs = require('fs');
var router = express.Router();
var axios = require('axios');


router.post('/', /*async*/ function (req, responseMain) {
    // var data = req.body;
    console.log(req.body);
    // console.log("longitude:"+req.body.longitude);
    // console.log("latitude:"+req.body.latitude);

    //console.log(req.headers);
    //fs.writeFileSync('./public/json/' + data.deviceId + '.json', JSON.stringify(req.body, undefined, 2));

    // axios.get('https://smart-bike-share.appspot.com/updateLocation?authuser='+req.body.userId+'&lat='+req.body.lat+'&longi='+req.body.long+'&cycleID='+req.body.deviceId)
    //     .then(function(response){
    //         console.log(response.data);
    //         res.send('respond with a resource:'+response.data);
    //     }).catch(function(error){
    //     console.log(error);
    // });

    /*console.log(JSON.stringify(
        {
            authuser: req.body.authuser,
            lat: req.body.lat,
            longi: req.body.longi,
            cycleID: req.body.cycleID
        }));*/

     /*await */axios.post('https://smart-bike-share.appspot.com/updateLocations',
        {
            authuser: req.body.authuser,
            lat: req.body.lat,
            longi: req.body.longi,
            cycleID: req.body.cycleID
        })
    // console.log("Completed");
        .then(function(response){
            console.log(response.data);
            responseMain.send('respond with a resource:'+response.data);
        }).catch(function(error){
        console.log(error);
    });
    // responseMain.send("Success");
});
module.exports = router;