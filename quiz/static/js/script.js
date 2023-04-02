// When back arrow is clicked, show previous section
//window.onpopstate = function(event) {
//   console.log(event.state.section);
//    showSection(event.state.section);
//}

//function showSection(section) {
//    fetch(`/sections/${section}`)
//    .then(response => response.text())
//    .then(text => {
//        console.log(text);
//        document.querySelector('#content').innerHTML = text;
//    });

//}

function quizfunc(data, level){
  datum = data.payload;
  document.querySelector("#question").innerHTML = `Question ${level + 1} : ${datum[level].question}`;
  document.querySelector("#op1").innerHTML = datum[level].option1;
  document.querySelector("#op2").innerHTML = datum[level].option2;
  document.querySelector("#op3").innerHTML = datum[level].option3;
  document.querySelector("#op4").innerHTML = datum[level].option4;
  answer = datum[level].answer;
  let buttons = document.querySelectorAll(".ops");
  var buttonsCount = buttons.length;
  for(var i = 0; i <= buttonsCount; i++){
    buttons[i].onclick = function(e) {
      if(this.id === answer ){
        level++;
        if(level < 10){
          console.log(level);
          quizfunc(data, level);
        }
        else{
          document.querySelector("#questiondiv").style.visibility = "hidden";
          document.querySelector("#message").innerHTML = "You Won!!!";
          document.querySelector("#message").style.color = "#4CAF50";
          document.querySelector('#start').innerHTML = "Start";
          document.querySelector('#start').style.visibility = "visible";
          document.querySelector('#message').style.visibility = "visible";
        }
      }
      else {
            document.querySelector("#questiondiv").style.visibility = "hidden";
            document.querySelector("#message").innerHTML = "You Lost";
            document.querySelector("#message").style.color = "#DB4437";
            document.querySelector('#start').innerHTML = "Try Again";
            document.querySelector('#start').style.visibility = "visible";
            document.querySelector('#message').style.visibility = "visible";
      }
    }
  }
}

document.addEventListener('DOMContentLoaded', function() {
    questionSection = document.querySelector("#questiondiv");
    questionSection.style.visibility = "hidden";
    btn = document.querySelector('#start');
    btn.onclick = () => {
        btn.style.visibility= 'hidden';
        document.querySelector('#message').style.visibility = "hidden";
        questionSection.style.visibility = "visible";
        fetch('/start')
        .then(response => response.json())
        .then(data => {
          quizfunc(data, 0);
        });
       };
});

