import Modal from './modal.js';

const modal = Modal({ animateClasses: ['animate-pop', 'back'] })

document
  .querySelector('.open-modal')
  .addEventListener('click', modal.open)



document.getElementById('salvar').addEventListener('click', enviaMsg);

function enviaMsg() {
    const xhttp = new XMLHttpRequest();
  
    xhttp.onreadystatechange = function() {
      console.log("readyState:" + this.readyState);
      console.log("status:" + this.status);
  
      if (this.readyState == 4 && this.status == 200) {
        imprimeResposta(this);
      }
    };
  
    xhttp.onload = function() {
      alert(this.responseText);
    };
  
    alert("mensagem enviada");
    var data = {
    "name":document.getElementById("name").value,
    "date-announcement":document.getElementById("date-announcement").value,
    "min-value":document.getElementById("min-value").value,
    "description-announcement":document.getElementById("description-announcement").value};
    var jsondata = JSON.stringify(data);
    var url = "https://n2vjillsj1.execute-api.us-east-1.amazonaws.com/UAT-announcement-edit";
    xhttp.open("POST", url);
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8", "Access-Control-Allow-Methods", "header('Access-Control-Allow-Methods");
    xhttp.send(jsondata);
}

  function imprimeResposta(xml) {
    var xmlDoc = xml.responseXML;
    document.getElementById("resposta").innerHTML = xmlDoc;
  }

