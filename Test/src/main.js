
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
  const handleSuccess = function(stream) {
    if (window.URL) {
      streamplayer.srcObject = stream;
    } else {
      streamplayer.src = stream;
    }
  };

  navigator.mediaDevices.getUserMedia({ audio: true, video: false })
      .then(handleSuccess);
