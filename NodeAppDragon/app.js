var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

var indexRouter = require('./routes/index');
var gcpRouter = require('./routes/sendToGCP');
var geoRouter = require('./routes/geolocationdata');
var sensorsRouter = require('./routes/sensors');

var app = express();

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/sendToGCP', gcpRouter);
app.use('/geoData', geoRouter);
app.use('/sensorsData', sensorsRouter);

module.exports = app;
