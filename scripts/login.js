const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});




function createUser() {
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
  
    var data = {
    "name":document.getElementById("nome").value,
    "email":document.getElementById("email").value,
    "password":document.getElementById("password").value};
    var jsondata = JSON.stringify(data);
    var url = "https://plu3h0jkz5.execute-api.us-east-1.amazonaws.com/create_user";
    xhttp.open("POST", url);
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8", "Access-Control-Allow-Methods", "header('Access-Control-Allow-Methods");
    xhttp.send(jsondata);
    alert("mensagem enviada");
}

  function imprimeResposta(xml) {
    var xmlDoc = xml.responseXML;
    document.getElementById("resposta").innerHTML = xmlDoc;
  }





document.getElementById('login').addEventListener('click', login);

function login() {
    const xhttp = new XMLHttpRequest();
 

  
    var data = {
    "email":document.getElementById("lemail").value,
    "password":document.getElementById("lpassword").value};
    var jsondata = JSON.stringify(data);
    var url = "https://ughm1hlp0d.execute-api.us-east-1.amazonaws.com/login";
    xhttp.open("POST", url);
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8", "Access-Control-Allow-Methods", "header('Access-Control-Allow-Methods");
    xhttp.send(jsondata);
    alert("mensagem enviada");

      
    xhttp.onreadystatechange = function() {
      console.log("readyState:" + this.readyState);
      console.log("status:" + this.status);

      var jsonResponse = JSON.parse(this.responseText);
      var stat = jsonResponse["statusCode"];
      var b = jsonResponse["body"];
      console.log("body:" + b.nome);

      if (this.readyState == 4 && this.status == 200) {
      alert(this.responseText);
      }
      
      if (this.readyState == 4 && stat == 200) {
        let userid = "username=" + document.getElementById("lemail").value;

        let d = new Date();
        d.setTime( d.getTime() + 10 * 60 * 1000 ); // Este cookie expira em 10 minutos (10*60*1000 miliseg.)
        let expires = "expires="+ d.toUTCString();
      
        let c  = userid + ";" + expires + ";path=/";
        document.cookie = c;
        window.location.href = "./index.html";
      }
    
    };
}


