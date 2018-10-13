var express = require('express');
var router = express.Router();
var axios = require('axios');


/* GET users listing. */
router.get('/', function (req, res, next) {


    axios.get('https://smart-bike-share.appspot.com/two?authuser=0')
        .then(function(response){
            console.log(response.data);
            res.send('respond with a resource');
        }).catch(function(error){
            console.log(error);
    });
});

module.exports = router;
