document.getElementById("app").innerHTML = `
<div class="d1">
  <h5>白頭翁不吃小米<div class="circle"></div></h5>
  <label for="burger" id="box1" onclick="chickOn()">☰</label>
  <label for="burger" id="box2" onclick="chickOff()">X</label>
  <input type="checkbox" id="burger">

  <div>
    <ul class="table" style="padding-left:100px;list-style-type:none;">
      <li>白頭翁的特性</li>
      <li>白頭翁的故事</li>
      <li>白頭翁的美照</li>
      <li>白頭翁的危機</li>
      <div id="fa">
        <div>c</div>
      </div>
    </ul>
  </div>
</div>
<div class="d2">
  <div><img id="img1" src="./img/KfUmCKk.jpg"</div>
  <div class="tests">
    <div class="test1">
      <h2 id="t1">外觀<div class="circle2"></div></h2>
      <div class="testd">白頭鵯體長約17到22公分，額至頭頂純黑色而富有光澤，兩眼上方至後枕白色，形成一白色枕環。耳羽後部有一白斑，此白環與白斑在黑色的頭部均極為醒目，老鳥的枕羽(後頭部)更潔白，所以又叫「白頭翁」。</div>
    </div>
    <div class="test2">
      <h2 id="t2">棲地<div class="circle2"></div></h2>
      <div class="testd">白頭翁和麻雀、綠繡眼合稱「城市三寶」，常成群出現在平原區灌木叢、丘陵樹林地帶，以及校園、公園、庭院、行道中的各種高高的電線與樹上。</div>
    </div>
    <div class="test3">
      <h2 id="t3">食性<div class="circle2"></div></h2>
      <div class="testd">以果樹的漿果和種子為主食，並時常飛入果園偷吃果實，還會吃嫩葉嫩芽，尤其是胡蝶蘭的嫩葉嫩芽葉，偶爾啄食昆蟲。</div>
    </div>
    
  </div>
</div>
`;
function chickOn(){
  document.getElementById("box1").style.display = "none";
  document.getElementById("box2").style.display = "block";
  document.querySelector("ul").style.display = "block";
}

function chickOff(){
  document.getElementById("box1").style.display = "block";
  document.getElementById("box2").style.display = "none";
  document.querySelector("ul").style.display = "none";
}
