// JavaScript source code

var recordingblob = null;

audioRecorder && audioRecorder.exportWAV(function (blob) {
    recordingblob = blob;
});

$("#myform").submit(function () {
    event.preventDefault();

    var formData = new FormData($(this)[0]);

    if (recordingblob) {
        var recording = new Blob([recordingblob], { type: "audio/wav" });
        formData.append("recording", recording);
    }
    $.ajax({
        url: myurl,   //server URL
        type: 'POST',
        data: formData,
     
    });
}
