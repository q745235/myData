var a;
var c;
var sum = document.getElementById('demo').innerText;
var btnZ = false;

// + - * /
function btnChar(str) {

    btnResult();

    a = parseFloat(document.getElementById('demo').innerText);
    console.log("a" + a);
    c = str;
    // 點+，把畫面清空
    document.getElementById('demo').innerText = "";
    btnZ = false;
}
// console.log(document.getElementById('demo').innerText);

// = 呼叫
function btnResult() {
    var result = parseFloat(document.getElementById('demo').innerText);
    switch (c) {
        case '+':
            result = a + result;
            console.log("b1:" + a);
            break;
        case '-':
            result = a - result;
            console.log("b2:" + a);
            break;
        case '*':
            result = a * result;
            console.log("b3:" + a);
            break;
        case '/':
            result = a / result;
            break;
        case 'CE':
            document.getElementById('demo').innerText = "";
            a = 0;
            c = null;
            break;
    }
    document.getElementById('demo').innerText = result;
    result = 0;
    a = 0;
    c = null;
    btnZ = true;
}



function showNum(item) {
    // console.log(item.id);
    // console.log(item.innerText);
    if (btnZ) {
        btnZ = false;
        document.getElementById('demo').innerText = "";
    };
    if (!document.getElementById("demo").innerText) {
        document.getElementById("demo").innerText = item.innerText;
    } else {
        document.getElementById('demo').innerText =
        document.getElementById('demo').innerText + item.innerText;
    }
}

// function showNum(str) {

//     //避免填入運算後的數字的後面

//     if (c == null) {
//         document.getElementById("demo").innerText = str.innerText;
//         c = 0;
//         return;
//     };

//     if (!document.getElementById("demo").innerText) {
//         document.getElementById("demo").innerText = str.innerText;
//     } else {
//         document.getElementById("demo").innerText += str.innerText;
//     }

// }
