
    var marriage_obj = document.getElementById('marriage');
    marriage_obj.onchange = function () {
        var marriage = document.getElementById('marriage').value;
        if (marriage == '已婚' || marriage == '离婚') {
            document.getElementById('child').style.display = "";
        }
        else if (marriage == '未婚' || marriage == '同居') {
            document.getElementById('child').style.display = "none";
            document.getElementById('child_sex').style.display = "none";                   
            document.getElementById('child_birthday').style.display = "none";             
        }
    }


var child_numbers_obj = document.getElementById('child_numbers'); 
child_numbers_obj.onchange = function () { 
    var child_numbers = document.getElementById('child_numbers').value;
    if (child_numbers == '1') { 
        document.getElementById('child_sex').style.display = ""; 
        document.getElementById('child_birthday').style.display = ""; 
    } 
    else if(child_numbers != '1'){
        document.getElementById('child_sex').style.display = "none";          
        document.getElementById('child_birthday').style.display = "none";
    }
}