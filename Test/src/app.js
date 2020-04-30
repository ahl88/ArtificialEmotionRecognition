const PORT = process.env.PORT || 80;
var express = require("express"),
	app = express(),
	http = require("http").Server(app).listen(PORT),
	upload = require("express-fileupload"),
	path = require('path');

app.use(upload())
app.use(express.json());
app.use(express.static('../public'));


console.log("Server Started!")
console.log("Listening on port " + PORT + "...")

//Home Route
app.get("/", function(req,res){
	res.sendFile(__dirname+"/index.html")
})

//Load  View Engine
app.set('views', path.join(__dirname, '../views'));
app.set('view engine', 'pug')

app.post("/", function(req,res){
	if(req.files){
		var file = req.files.filename,
			filename = req.files.filename.name
		file.mv("./upload/" + filename,function(err){
			if(err){
				console.log(err)
				res.send("error occured")
			}
			else{
				//run python code on filename
				//get array of emotion levels
				var results = [0.5,0.0,0.5,0.0,0.0,0.0,0.0,0.0]
				var resultsStr = percentString(results);
				console.log(resultsStr);
				console.log('sending')
				res.render('result', {
					numNeutral:resultsStr[0],
					numCalm:resultsStr[1],
					numHappy:resultsStr[2],
					numSad:resultsStr[3],
					numAngry:resultsStr[4],
					numFearful:resultsStr[5],
					numDisgust:resultsStr[6],
					numSurprised:resultsStr[7],
					textString: 'Im so hungry Im so excited to eat',
				});
			}
		})

	}
})

function percentString(result) {
	var output  = []
	for (let index = 0; index < result.length; index++) {
		output[index] = ""+(result[index]*100)+"%";
	}
	return output;
}