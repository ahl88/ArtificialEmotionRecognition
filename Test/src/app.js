const PORT = 80;
var express = require("express"),
	app = express(),
	http = require("http").Server(app).listen(PORT),
	upload = require("express-fileupload");

app.use(upload())
app.use(express.json());
app.use(express.static('../public'));


console.log("Server Started!")
console.log("Listening on port " + PORT + "...")

app.get("/", function(req,res){
	res.sendFile(__dirname+"/index.html")
})

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
				res.send("Done!")
			}
		})

	}
})