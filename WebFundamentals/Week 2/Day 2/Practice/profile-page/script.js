function deletee(element){
    //console.log(element.parentNode.parentNode);
    element.parentNode.parentNode.remove()
}
var nameee=document.querySelector("#namee")
function change(){
    nameee.innerText="amenallah brahim"
}
var nc = document.querySelector(".connects")
function accept(el){
    el.parentNode.parentNode.remove()
    //console.log(nc.innerText);
    //console.log(parseInt(nc.innerText.split('+')[0]));
    nc.innerText = parseInt(nc.innerText.split('+')[0])+1+"+"
}