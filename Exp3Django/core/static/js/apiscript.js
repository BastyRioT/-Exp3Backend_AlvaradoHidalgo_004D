function guid() {
  function S4() {
    return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
  }
  return (S4() + S4() + "-" + S4() + "-4" + S4() + "-" + S4() + "-" + S4() + S4() + S4());
}
var Generator = document.getElementById('button1');
var input = document.getElementById('input');
Generator.onclick = function event() {
  return input.value = guid();
}
function copyToClipboard(element) {
  var $temp = $("<input>");
  $("body").append($temp);
  $temp.val($(element).val()).select();
  document.execCommand("copy");
  $temp.remove();
}