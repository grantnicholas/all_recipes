$(document).ready(function($){
	$('.button').click(function(){
		console.log(this.id);
		$.post('/button/'+ this.id, function(res){
			$('#whole_page').hide().html(res).fadeIn('fast')
		});
	});	
});
