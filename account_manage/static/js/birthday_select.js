
var selYear = window.document.getElementById("selYear");
var selMonth = window.document.getElementById("selMonth");
var selDay = window.document.getElementById("selDay");
// 新建一个DateSelector类的实例，将三个select对象传进去
new DateSelector(selYear, selMonth, selDay, 1995, 1, 17);

