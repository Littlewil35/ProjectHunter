$(document).ready(function() {

	$('form').on('submit', function(event) {
	    console.log("post successful")
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
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$('#successAlert').text(data.name).show();
				$('#errorAlert').hide();
			}

		});

		event.preventDefault();

	});

});
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