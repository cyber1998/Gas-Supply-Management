$(function(){
	$('sbbtn').click(function()	{

		var user = $('#uname').val();
		var pass = $('#pass').val();

		$.ajax({
			url: '/signupuser',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error)	{
				console.log(error);
			}
		});
	});
});
