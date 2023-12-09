window.onkeydown = console.log("hello");
let a = document.getElementById("sig");
let b = document.getElementById("log");
let c = document.getElementById("col");

function togg1() {
  a.style.left = "0%";
  b.style.left = "0%";
  c.style.left = "0%";
}
function togg2() {
  b.style.left = "-50%";
  a.style.left = "-50%";
  c.style.left = "50%";
}
