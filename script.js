 var menuBtn= document.getElementById("menuBtn")
  var sideNav= document.getElementById("sideNav")
  var menu= document.getElementById("menu")

  //sideNav.style.right== "-250px";

  menuBtn.onclick= function(){
    if (  sideNav.style.right   == "-250px"){
      sideNav.style.right = "0";
      menu.src="images/close.png"
    }
    else{
       sideNav.style.right = "-250px";
       menu.src="images/menu.png"
    }
  }


   function openImg(element){
    window.open(element.src);
}


//var t= document.getElementById("text").innerHTML;
var i=0;
var t= "Buy Cheap Text Books Online";

function typing()
{ 
  if(i < t.length)
  {
  document.getElementById("text").innerHTML += t.charAt(i);
  i++;
  setTimeout(typing, 100);
  }
}
typing();


