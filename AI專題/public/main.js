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
        $("#reportHere").append(res['name'] + "   " + res['symptom'] + "   " + res['urgency'] + '\n');
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
  // $("#okButton").on("click", function () {
  //   // cameraCanvas
  //   var viewContext = viewPort.getContext('2d')
  //   // console.log(viewPort);
  //   document.getElementById("okButton").disabled = true;
  //   Webcam.snap(function (snappedImage) {
  //     // console.log(snappedImage);
  //     let bufferImage = new Image();
  //     bufferImage.src = snappedImage;
  //     bufferImage.onload = function () {
  //       viewContext.drawImage(bufferImage, 0, 0, 320, 240);
  //       // 將 Canvas 轉成 Blob，然後 POST 給 Face API:
  //       var data = viewPort.toDataURL('image/jpeg');

  //       fetch(data)
  //         .then(function (res) {
  //           return res.blob()
  //         })
  //         .then(function (blobData) {
  //           document.getElementById("checkButton").disabled = false;
  //           let b = document.getElementById('checkButton');
  //           b.addEventListener('click', checkButton);
  //           // const cors = 'https://cors-anywhere.herokuapp.com/';
  //           $("#reportHere").empty();
  //           $.ajax({
  //             type: 'GET',
  //             url: "http://localhost:5000/gg",
  //             success:function(res){
  //               // console.log(res);
  //               for (var i=0;i<res.length;i++){
  //                 // console.log(res[i][0])
  //                 $("#reportHere").append(res[i]['name']+"   "+res[i]['address'] + '\n');
  //               }
  //             }
  //           }).then(function (e) {
  //             // console.log(e);
  //           })

  //           function checkButton() {
  //             // downloadCanvasIamge('checkButton', '圖片名稱')
  //             var a = document.createElement('a');
  //             a.download = 'test1.jpg';
  //             a.href = data;
  //             // console.log(data)
  //             a.click();
  //             // console.log(a)
  //             document.getElementById("checkButton").disabled = true;
  //             document.getElementById("okButton").disabled = false;
  //             b.removeEventListener('click', checkButton);
  //           }
  //         });
  //     }

  //   });  // End of Webcam.snap

  // });

});