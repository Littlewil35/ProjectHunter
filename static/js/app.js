$(document).ready(function() {

	$('form').on('submit', function(event) {
    console.log("Hello")
		$.ajax({
			data : {
				postname : $('#postname').val(),
				tags : $('#tags').val(),
				body : $('#posttext').val()

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

/*$(function() {
      $("#button").click( function(){
                console.log(document.getElementById('input').value);

           }
      );
});*/



