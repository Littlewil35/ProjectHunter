function submitProjo() {
	console.log("post successful");
	$.ajax({
		data : {
			postname : $('#postname').val(),
			tags : $('#tags').val(),
			body : $('#posttext').val(),
			status : $('#status').val()

		},
		type : 'POST',
		url : '/process'
	})
}

var visible = false;
$(function() {
      $("#showHide").click( function(){
      if (visible){
            document.getElementById("form").style.display = "none";
            visible = false;
      }else{
            document.getElementById("form").style.display = "block";
            visible = true;
      }
           }
      );
});


function mSearch(){
	var searchText = document.getElementById("searchBox").value.replace(" ", "+");
	document.getElementById("searchButt").setAttribute("href", "/search?param=" + searchText);
	return false;
}

