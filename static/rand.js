function randomNumber(min, max) {
        return parseInt(Math.random() * (max - min) + min);
    }  

function d(){
    var fdata = document.getElementById("fdata").getAttribute('d');
    var cleanedString = fdata.replace(/[\[\]']+/g, '');
    var fdata=cleanedString.split(",")
    var sec = document.getElementById("fname");
    for(i=0;i<100;i++){
        setTimeout(function(){
                var a=randomNumber(0,fdata.length);
                sec.innerText=fdata[a];
                },100*i)
    }
    
}
   
    
    
    // if (sec) {
    //     // 將元素的 display 屬性設置為 "block"
    //     sec.style.display = "block";
    // }
//     if (sec ===null){
//        alert("請輸入位址");
//     }
//     else{
//             for(b=0;b<fdata.length;b++){

//                 var c=document.createElement("span");
            
//                 c.textContent=fdata[b];
            
//                 sec.appendChild(c);
//                 }
//         }


   