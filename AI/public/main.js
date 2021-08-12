$(document).ready(function () {

  Webcam.set({
    width: 320,
    height: 240,
    image_format: 'jpeg',
    jpeg_quality: 90
  });
  Webcam.attach('#cameraDiv');

  $("#romveButton").off('click').on("click", function () {
    document.getElementById("checkButton").disabled = true;
    document.getElementById("okButton").disabled = false;
  });
  $("#selectButton").off('click').on("click", function () {
    $("#reportHere").empty();
    $.ajax({
      type: 'GET',
      url: "http://localhost:5000/ss",
      success: function (res) {
        // console.log(res);
        $("#reportHere").append(res[0]['name'] + "   " + res[0]['symptom'] + "   " + res[0]['urgency'] + '\n');
      }
    }).then(function (e) {
      // console.log(e);
    });

  });
  $('#okButton').on("click", function () {
    $("#reportHere").empty();
    $.ajax({
      type: 'GET',
      url: "http://localhost:5000/gg",
      success: function (res) {
        console.log(res);
        for (var i = 0; i < res.length; i++) {
          // console.log(res[i][0])
          $("#reportHere").append(res[i]['name'] + "   " + res[i]['address'] + '\n');
        }
      }
    }).then(function (e) {
      // console.log(e);
    })
  })


});