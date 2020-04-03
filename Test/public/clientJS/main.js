
/*Collapses panels when clicked on sub header*/
var coll = document.getElementsByClassName("collapse");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "none") {
      content.style.display = "block";
    } else {
      content.style.display = "none";
    }
  });
}

/*Hides and shows nav bar when scrolling*/
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (currentScrollPos < 10){
    document.getElementById("navbar").style.top = "0";
  } else{
    if (prevScrollpos > currentScrollPos) {
      document.getElementById("navbar").style.top = "0";
    } else {
      document.getElementById("navbar").style.top = "-80px";
    }
  }
  prevScrollpos = currentScrollPos;

}

/*Audio Recording Script */
const recorder = document.getElementById('filerecorder');
const streamplayer = document.getElementById('player');
const fileplayer = document.getElementById('fileplayer');


//Audio File
recorder.addEventListener('change', function(e) {
  const file = e.target.files[0];
  const url = URL.createObjectURL(file);
  // Do something with the audio file.
  fileplayer.src = url;
});

//Microphone Streaming
//webkitURL is deprecated but nevertheless 
URL = window.URL || window.webkitURL;
var gumStream;
//stream from getUserMedia() 
var rec;
//Recorder.js object 
var input;
//MediaStreamAudioSourceNode we'll be recording 
// shim for AudioContext when it's not avb. 
var AudioContext = window.AudioContext || window.webkitAudioContext;
var audioContext
//new audio context to help us record 
var recordButton = document.getElementById("start-btn");
var stopButton = document.getElementById("stop-btn");
var pauseButton = document.getElementById("pause-btn");
//add events to those 3 buttons 
recordButton.addEventListener("click", startRecording);
stopButton.addEventListener("click", stopRecording);
pauseButton.addEventListener("click", pauseRecording);

function startRecording() { 
  console.log("recordButton clicked");
  var constraints = {audio: true,video: false} 
  /* Disable the record button until we get a success or fail from getUserMedia() */

  recordButton.disabled = true;
  stopButton.disabled = false;
  pauseButton.disabled = false

  /* We're using the standard promise based getUserMedia()

  https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia */

  navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
    console.log("getUserMedia() success, stream created, initializing Recorder.js ..."); 
    /* assign to gumStream for later use */
    audioContext = new AudioContext();
    gumStream = stream;
    /* use the stream */
    input = audioContext.createMediaStreamSource(stream);
    /* Create the Recorder object and configure to record mono sound (1 channel) Recording 2 channels will double the file size */
    rec = new Recorder(input, {numChannels:1}) 
    //start the recording process 
    rec.record()
    console.log("Recording started");
  }).catch(function(err) {
    //enable the record button if getUserMedia() fails 
    recordButton.disabled = false;
    stopButton.disabled = true;
    pauseButton.disabled = true
    console.log(err)
  });
}

function pauseRecording() {
  console.log("pauseButton clicked rec.recording=", rec.recording);
  if (rec.recording) {
      //pause 
      rec.stop();
      pauseButton.innerHTML = "Resume";
  } else {
      //resume 
      rec.record()
      pauseButton.innerHTML = "Pause";
  }
}

function stopRecording() {
  console.log("stopButton clicked");
  //disable the stop button, enable the record too allow for new recordings 
  stopButton.disabled = true;
  recordButton.disabled = false;
  pauseButton.disabled = true;
  //reset button just in case the recording is stopped while paused 
  pauseButton.innerHTML = "Pause";
  //tell the recorder to stop the recording 
  rec.stop(); //stop microphone access 
  gumStream.getAudioTracks()[0].stop();
  //create the wav blob and pass it on to createDownloadLink 
  rec.exportWAV(createDownloadLink);
}

function createDownloadLink(blob) {
  var url = URL.createObjectURL(blob);
  var au = document.createElement('audio');
  var li = document.createElement('li');
  var link = document.createElement('a');
  //add controls to the <audio> element 
  au.controls = true;
  au.src = url;
  //link the a element to the blob 
  link.href = url;
  link.download = new Date().toISOString() + '.wav';
  link.innerHTML = link.download;
  //add the new audio and a elements to the li element 
  li.appendChild(au);
  li.appendChild(link);
  //add the li element to the ordered list 
  recordingsList.appendChild(li);
}
