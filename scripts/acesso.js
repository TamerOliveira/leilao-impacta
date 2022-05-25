
function verificaCookie() {
    if( getUser() == "" ) window.location.href = "./login.html";
  }


function getUser() { 
    let decodedCookie = decodeURIComponent(document.cookie); 
    let ca = decodedCookie.split( ';' );
    for( let i = 0; i < ca.length; i++ )
      if( ca[i].indexOf( "username=" ) == 0 ) 
        return ca[i].substring( "username=".length, ca[i].length ); 
  
    return ""; 
  }


function getExpires() { 
    let decodedCookie = decodeURIComponent(document.cookie); 
    let ca = decodedCookie.split( ';' ); 
    for( let i = 0; i < ca.length; i++ )
      if( ca[i].indexOf( "expires=" ) == 0 ) 
        return ca[i].substring( "expires=".length, ca[i].length ); 
  
    return ""; 
  }