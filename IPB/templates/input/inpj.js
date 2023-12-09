var tog = false;
function togg() {
  if (tog == false) {
    document.getElementById("men").style.transform = "translateY(38vh)";
    tog = true;
  } else {
    document.getElementById("men").style.transform = "translateY(0vh)";
    tog = false;
  }
}
