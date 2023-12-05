function d(){
    let fdata = document.getElementById("fdata").getAttribute('d');
    var cleanedString = fdata.replace(/[\[\]']+/g, '');
    alert(cleanedString);
    fdata=fdata.split(",")
    alert(fdata);
    let data = document.getElementById("wrap");
    data.style.display="block";
    if (data ===null){
        for(b=0;b<fdata.length;b++){

            var c=document.createElement("span");
        
            c.textContent=fdata[b];
        
            data.appendChild(c);
            }
    }
    else{
        while (data.firstChild) {
            data.removeChild(data.firstChild);
            for(b=0;b<fdata.length;b++){

                var c=document.createElement("span");
            
                c.textContent=fdata[b];
            
                data.appendChild(c);
                }
        }
        }
    }
   