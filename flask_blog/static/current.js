let on = 1; // on
function opens(){
    if(on == 1){ //on
        //console.log("a");
        document.body.classList.remove('listanime2-re');
        document.body.classList.add('listanime2'); //off
        document.getElementById("headeramine").classList.remove('listanime-re');
        document.getElementById("headeramine").classList.add('listanime');
       document.getElementById("ops").innerHTML ='<svg class="bi bi-arrow-bar-right" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M10.146 4.646a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708-.708L12.793 8l-2.647-2.646a.5.5 0 0 1 0-.708z"/><path fill-rule="evenodd" d="M6 8a.5.5 0 0 1 .5-.5H13a.5.5 0 0 1 0 1H6.5A.5.5 0 0 1 6 8zm-2.5 6a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 1 0v11a.5.5 0 0 1-.5.5z"/></svg>'
    on = 0;
    }else{ //off
        document.body.classList.remove('listanime2');
        document.body.classList.add('listanime2-re');
        document.getElementById("headeramine").classList.remove('listanime');    
        document.getElementById("headeramine").classList.add('listanime-re');    
    on = 1;
    document.getElementById("ops").innerHTML ='<svg class="bi bi-arrow-bar-left" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M5.854 4.646a.5.5 0 0 0-.708 0l-3 3a.5.5 0 0 0 0 .708l3 3a.5.5 0 0 0 .708-.708L3.207 8l2.647-2.646a.5.5 0 0 0 0-.708z"/><path fill-rule="evenodd" d="M10 8a.5.5 0 0 0-.5-.5H3a.5.5 0 0 0 0 1h6.5A.5.5 0 0 0 10 8zm2.5 6a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 1 0v11a.5.5 0 0 1-.5.5z"/></svg>';
    }
    //return false;
}
