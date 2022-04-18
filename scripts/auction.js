
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
    "id-announcement":document.getElementById("id-announcement").value,
    "valor":document.getElementById("valor").value};
    var jsondata = JSON.stringify(data);
    var url = "https://8lgilyyfp0.execute-api.us-east-1.amazonaws.com/UAT-auction";
    xhttp.open("POST", url);
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8", "Access-Control-Allow-Methods", "header('Access-Control-Allow-Methods");
    xhttp.send(jsondata);
}

  function imprimeResposta(xml) {
    var xmlDoc = xml.responseXML;
    document.getElementById("resposta").innerHTML = xmlDoc;
  }