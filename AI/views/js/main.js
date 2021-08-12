
$(document).ready(function () {
    
    // const { json } = require("body-parser")
    var total = ['']
    var temp = -1
    //醫院資訊收集系統
    $('#textBox1').off('click').on("click", () => {
        var i = 5
        $("#textBox1").hide()
        document.getElementById('textBox2').style.visibility = "visible"
        var interval = setInterval(function () {
            // console.log(i)
            document.getElementById('textBox2').innerHTML = i;
            i--;
            if (i < 0) {
                clearInterval(interval);
                // console.log(123)
                document.getElementById('textBox2').style.visibility = "hidden" //關閉提示文字
                $("#textBox2").text("開始")
                $(".note1").hide();
                $('.block2').css("visibility", "visible")
                $("#dgbk").show()
                $("#dgbk").css("opacity",1)
                // 準備拍照
                var viewContext = viewPort.getContext('2d')

                Webcam.snap(function (snappedImage) {
                    let bufferImage = new Image();
                    bufferImage.src = snappedImage;
                    bufferImage.onload = async function () {
                        viewContext.drawImage(bufferImage, 0, 0, 320, 240);
                        var data = viewPort.toDataURL('image/jpeg');
                        $("viewPort").hide();
                        $.ajax({
                            type: "post",
                            url: "http://localhost:5000/ss",
                            // data:{dataUrl:JSON.stringify({dataUrl:viewPort.toDataURL()})},
                            // data:{dataUrl:JSON.stringify(data)},
                            // data:{dataUrl:JSON.stringify(JSON.stringify({dataUrl:data}))},
                            data:JSON.stringify({dataUrl:data}),
                            cache:true,
                            processData:false,
                            dataType:"json",
                            contentType: "application/json",
                            success: function (res) {
                                console.log(res)
                                let name = res['name']
                                let symptom = res['symptom']
                                let urgency = res['urgency']
                                $('#dialog').empty()
                                $("#dialog").css('text-align', 'left')
                                $("#dialog").css('font-size', '38px')
                                $("#dialog").css('bottom', '40%')
                                $("#more").show()
                                $("#AI").attr('src', "img/AI-Bot-on2.png")
                                $("#dialogshow").show()
                                $("#dialogshow").css("visibility", "visible")
                                $("#dialog").append("[    Name  ]:" + name + '<br/>' + "[symptom]:" + '<br/>' + symptom + '<br/>' + "[urgency]:" + urgency + '<br/>')
                                // return res
                            },
                            error: function (err) {
                                console.log('fail')
                                console.log(err)
                            }

                        })

                    }

                });

                Webcam.reset(); //關閉攝像頭
            }
        }, 1000);

    })

    $("#more").off('click').on('click', async function () {
        $("#dialog").empty();
        $("#dialog").text("附近醫院資訊收集中...");
        if (temp == -1) {
            $.ajax({
                type: 'GET',
                url: "http://localhost:5000/gg",
                success: function (res) {
                    total = 0
                    temp = 0
                    total = res
                    $("#dialog").empty();
                    $("#dialog").css('text-align', 'left');
                    $("#dialog").css('font-size', '38px');
                    $("#dialog").css('bottom', '40%');

                    $("#more").show();
                    $("#AI").attr('src', "img/AI-Bot-on2.png")
                    getHos(temp)
                }
            })
            // $("#dialog").append(res[0]['name'] + "   " + res[0]['symptom'] + "   " + res[0]['urgency'] + '\n');
        } else {
            await getHos(temp)
        }

        async function getHos() {

            // let len = Object.keys(total).length-1   //資料讀取最大值
            let len = 10  //資料讀取最大值
            if (temp + 1 < len) $("#dialog").empty();
            for (var i = 0; i < 2; i++) {
                temp = temp + i
                // console.log(temp)
                if (temp < len) {
                    let name = total[temp]['name']
                    let level = total[temp]['level']
                    let address = total[temp]['address']
                    name = name.substring(0, name.indexOf("診所") + 2)
                    address = address.substring(address.indexOf("台"), address.length)
                    isNaN(level) ? level = " --- " : level = level + "分";
                    $("#dialog").append(name + '    [' + level + ']' + '<br/>' + address + '<br/>' + '<br/>');
                } else {
                    console.log(temp)
                    $("#dialog").hide();
                    $("#more").hide();
                    $("#dgbk").fadeTo(500, 0.1);
                    $(".block2").hide(800);
                    $("#AI").attr('src', "img/AI-Bot-on.png")

                    $("#AI").css("visibility", "hidden");
                    $("#textBox1").hide();
                    $(".note1").hide();
                    $('.mBtn').hide();
                    $('#mBtn1').click()
                    break;
                }
            }
            temp = temp + 1
        }
    })


    $("#goBack").off('click').on('click', function () {
        $("#AI").css("visibility", "hidden");
        $("#textBox1").hide();
        $(".note1").hide();
        Webcam.reset(); //關閉攝像頭
        $('.main').show(300);
    })

    //居家照護按鈕
    $('#mBtn1').click(() => {
        $("body").css("background-color", "black");
        $(".mBtn").hide();
        $('.main').hide(300);
        $("#AI").css("visibility", "visible");
        Webcam.set({
            width: 820,
            height: 430,
            image_format: 'jpeg',
            jpeg_quality: 90
        });
        $("#more").hide();
        Webcam.attach('#cameraDiv');
        $("#textBox1").show(900);
        $(".note1").show(900);

    })
    // 跌倒偵測按鈕
    $('#mBtn2').off("click").on("click",() => {
        // $.ajax({
        //     type: "post",
        //     url: "http://localhost:5000/falldown",
        //     contentType: "application/json",
        //     success: function (res) {
        //         console.log(res)
        //     }
        // })

        $("body").css("background-color", "pink");
        $(".mBtn").hide();
        $('.main').hide(300);
        $("#AI").css("visibility", "visible");
        Webcam.set({
            width: 820,
            height: 430,
            image_format: 'jpeg',
            jpeg_quality: 90
        });
        $("#more").hide();
        Webcam.attach('#cameraDiv');
        $("#textBox1").text("-----跌倒監測進行中-----")
        $("#textBox1").show(900);
        $("#textBox1").off("click")
        $(".note1").show(900);
        $('#noteText').html(
            "MEMO:" +
            '<br />' +
            '<br />' +
            "發現人員跌倒後，將立即記錄" +
            '<br />' +
            "並傳送Line通知使用者~"
        )
        $('#noteText').css('right', '10%')
    })

})