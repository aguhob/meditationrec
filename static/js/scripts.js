// this jquery code makes all of the items fade in one at a time

$( document ).ready( function () {

    $("#chakras dt").click( function (e) {

        console.log($(this).next().html() );
        
        if ( $(this).next().css("display") == "none") { 
            $(this).next().fadeIn(2000).show();
        } else {
            $(this).next().css("display", "none");
        }
        
    });
});

/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */

function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

function myFunction2() {
    document.getElementById("myDropdown2").classList.toggle("show");
}


// Close the dropdown if the user clicks outside of it

window.onclick = function(e) {
  if (!e.target.matches('.dropbtn')) {
    var myDropdown = document.getElementById("myDropdown");
      if (myDropdown.classList.contains('show')) {
        myDropdown.classList.remove('show');
      }
  }
}
