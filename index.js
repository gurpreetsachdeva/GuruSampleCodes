var express = require('express');
var app = express();
var defaulturl='http://google.co.in'
var defaultbrowser='"Google Chrome"'
var exec = require('child_process').exec;
var bodyParser=require("body-parser")

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get('/start', function (req, res) {

	//var url=
	//var browser=
	console.log(req.query)
	var url = req.query.url;
    var browser = req.query.browser;

    if( url==undefined)
    	url=defaulturl;
    if( browser==undefined || browser=='chrome')
    	browser=defaultbrowser;

    var cmd='open -a ' +browser+' '+url;
   //exec('open -a "Google Chrome" https://stackoverflow.com', function callback(error, stdout, stderr){
    // result
    console.log(cmd)
    exec(cmd, function callback(error, stdout, stderr){
});
   console.log("Successfully started");
   res.send('started');
})

app.get('/stop', function (req, res) {

	console.log(req.query)

	//kill $(pgrep -x "Google Chrome")
	var browser = req.query.browser;
	if( browser==undefined || browser=='chrome')
    	browser=defaultbrowser;

	var cmd='kill $(pgrep -x ' +browser+")";
	console.log(cmd);
	exec(cmd, function callback(error, stdout, stderr){
});
	res.send('stopped');
})


app.get('/cleanup', function (req, res) {

	console.log(req.query);

	var browser = req.query.browser;
	var cmd=""
	if( browser==undefined || browser=='chrome')
    	browser=defaultbrowser;
    if(browser==defaultbrowser)
   	{ 	
    	// cmd="rmdir -f ~/Library/Caches/Google/Chrome/'"
    	console.log(cmd);
    }
    else
    {
    	cmd='rm -rf  ~/Library/Application\ Support/Firefox/Profiles/*';
    }
    console.log(cmd);

	exec(cmd, function callback(error, stdout, stderr){
});
	res.send('Cleaned up');
})

app.get('/geturl', function (req, res) {
	var browser = req.query.browser;
	console.log(req.query)
	
	var cmd="";
	var url="";
	if( browser==undefined || browser=='chrome')
    	browser=defaultbrowser;
    //Command to fetch the last url and return
    cmd="sqllite3 /Users/gurpreetsachdeva/Library/Application Support/Google/Chrome/<your profile>/History/"
   
    exec(cmd, function callback(error, stdout, stderr){
    	url=stdout;
});

    console.log(cmd);
    url="http://myntra.com";
	res.send(String(url));




})

var server = app.listen(8081, function () {
   var host = server.address().address
   var port = server.address().port
   
   console.log("Example app listening at http://%s:%s", host, port)
})
