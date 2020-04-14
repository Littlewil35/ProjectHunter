// pulls data from various textboxes and sends it to the backend
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
// animates the pop up box
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

// communicates the search function to the backend
function mSearch(){
	var searchText = document.getElementById("searchBox").value.replace(" ", "+");
	document.getElementById("searchButt").setAttribute("href", "/search?param=" + searchText);
	return false;
}

// deletes project given its id
function deleteProjo(id) {
	$.ajax({
		data : {
			id : id
		},
		type : 'POST',
		url : '/delete'
	})
	console.log("delete successful");
}
