$(document).ready(function() {
	$("button.hide").click(function() {
		$("p.sample").hide(5000);
	});
		
	$("button.show").click(function() {
		$("p.sample").show("fast");
	});

	$("button.toggle").click(function() {
		$("p.sample").toggle("fast",function() {$("p.expression").text("toggling");});
	});	
	
	$("button.fadein").click(function() {
		$("p.fade").fadeIn("fast");
	});
		
	$("button.fadeout").click(function() {
		$("p.fade").fadeOut(5000);
	});

	$("button.fadetoggle").click(function() {
		$("p.fade").fadeToggle("fast",function() {$("p.expression").text("toggling");});
	});

	$("button.fadeto").click(function() {
		$("p.fade").fadeTo("slow",0.1);
	});

	$("button.slidedown").click(function() {
		$("p.slide").slideDown(5000);
	});
		
	$("button.slideup").click(function() {
		$("p.slide").css("color","red")	
			.fadeTo("fast",0.1)
			.slideUp(5000)
			.slideDown(5000);
	});

	$("button.slidestop").click(function() {
		$("p.slide").stop();
	});


	$("button.slidetoggle").click(function() {
		$("p.slide").slideToggle("fast",function() {$("p.expression").text("toggling");});
	});	
	
	$("button.text").click(function() {
		alert($("p.access").text("access:new text"));
	});

	$("button.html").click(function() {
		alert($("p.access").html());
	});

	$("button.val").click(function() {
		alert($("input.access").val());
	});

	$("button.attr").click(function() {
		alert($("p.access").attr("name"));
	});


	

});


