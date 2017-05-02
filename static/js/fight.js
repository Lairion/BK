$(document).ready(function(){

	$(".click_me_player").click(function(){
		$(".clicked_player").toggleClass("clicked_player");
		$(this).toggleClass("clicked_player");
	});
	$(".click_me_enemy").click(function(){
		$(".clicked_enemy").toggleClass("clicked_enemy");
		$(this).toggleClass("clicked_enemy");
	});
	$("#fight").click(function(){
        a=$("#player_name").data("id");
        b =$("#emeny_name").data("id")
		$.ajax({
            type: "GET",
            url: "/attack/",
            data:{
                'partEnemy':$(".clicked_enemy").data('part'),
                'partPlayer':$(".clicked_player").data('part'),
                // Допонительные параметры для поиска персонажей в базе данных
                'enemyId':$(".player_name").data('id'),
                'playerId':$(".enemy_name").data('id'),
            },
            cache:false,
            success:
            function(data){
            	console.log(data)
            	var obj = jQuery.parseJSON( data );
            	$("#enemy").css("width",obj.healthEnemy+"%");
            	$("#player").css("width",obj.healthPlayer+"%");    
            }
       });
	})
})