const express = require('express');

var app = express();
app.get('/', function(req, res){
  //res.send('abc');

var MongoClient = require('mongodb').MongoClient;
  f = require('util').format,
  assert = require('assert');

var url = 'mongodb://mongo:mongo@ec2-54-254-215-6.ap-southeast-1.compute.amazonaws.com:27017/?authMechanism=SCRAM-SHA-1&authSource=ads';

MongoClient.connect(url, function(err, db) {
  assert.equal(null, err);
  console.log("Connected correctly to server");
  var dbo = db.db("ads");
  //var querya = ({ DeptID:"CS"}, {DeptName: 1});
  dbo.collection("department").find({DeptID: 'CS'}, {_id: 1, DeptID: 0, DeptName: 1, Location: 0, Offers:0}).toArray(function(err, result){
      if (err) throw err;
      console.log(result);
      res.send(result);
  db.close();
});
});
});

app.listen(80, function(){
console.log('Web Server Start');


});
