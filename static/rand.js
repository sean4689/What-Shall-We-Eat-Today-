function d(){
    var fdata = document.getElementById("fdata").getAttribute('d');
    var cleanedString = fdata.replace(/[\[\]']+/g, '');
    var fdata=cleanedString.split(",")
    alert(fdata);
    var sec = document.getElementsByClassName("w1")[0];
    alert(sec)
    // if (sec) {
    //     // 將元素的 display 屬性設置為 "block"
    //     sec.style.display = "block";
    // }
    if (sec ===null){
       alert("請輸入位址");
    }
    else{
            for(b=0;b<fdata.length;b++){

                var c=document.createElement("span");
            
                c.textContent=fdata[b];
            
                sec.appendChild(c);
                }
        }
}

   