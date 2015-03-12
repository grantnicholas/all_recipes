$(document).ready(function($){
	$('.button').click(function(){
		console.log(this.id);
		$.post('/button/'+ this.id, function(){
			alert('complete');
		});
	});	
});
