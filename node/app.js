var express = require("express"),
	app = express(),
	http = require("http").Server(app).listen(80),
	upload = require("express-fileupload");

app.use(upload())


console.log("Server Started!")

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