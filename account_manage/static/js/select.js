


// for (var i of cityDatas){
//     var pro_option = document.createElement("option");
//     pro_option.innerHTML=i['name'];
//     province.appendChild(pro_option);
// }


        var data = cityDatas;
        var province=document.getElementById('province');
        var city=document.getElementById('city');
        var county=document.getElementById('county');
        var option = "<option value='请选择'>请选择</option>";
        province.innerHTML = option;
        city.innerHTML = option;
        county.innerHTML = option;

        // 生成省列表
        for(var i=0;i<data.length;i++){
            var option_province=document.createElement('option');
            option_province.value=data[i].name;
            option_province.innerText=data[i].name;
            province.appendChild(option_province);
        }
        // 根据选择的省生成相应的城市列表
        province.onchange=function(e){
            for(var i=0;i<data.length;i++){
                if(data[i].name == e.target.value){
                    var data_city=data[i].regions;
                    var option_city=data_city.map(function(item){
                        return `<option value="${item.name}">${item.name}</option>`
                    }).join('');
                    // 根据选择的城市生成相应的县级列表
                    city.onchange=function(evt){
                        for(var j=0;j<data_city.length;j++){
                            if(data_city[j].name == evt.target.value){
                                var data_county=data_city[j].regions;
                                var option_count=data_county.map(function(items){
                                    return `<option value="${items.name}">${items.name}</option>`
                                }).join('');
                            }
                        }
                        county.innerHTML="<option value='请选择'>请选择</option>"+option_count;
                    }
                }
            }
            city.innerHTML="<option value='请选择'>请选择</option>"+option_city;
            county.innerHTML="<option value='请选择'>请选择</option>"
        }
    

