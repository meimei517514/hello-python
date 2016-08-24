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

	$("button.append").click(function() {
		$("p.add").append("<b class='empty'>append in the end</b>");
	});

	$("button.prepend").click(function() {
		$("p.add").prepend("<b class='empty'>prepend in front</b>");
	});

	$("button.after").click(function() {
		var one="<b class='remove'>create by html</b>";
		var two=$("<b class='remove'></b>").text("create by jequery");
		var three=document.createElement("br");	
		$("input.add").after(one,two,three);
	});

	$("button.before").click(function() {
		$("p.add").before("<b class='reomve'>add before element</b>");
	});

	$("button.remove").click(function() {
		$("b").remove(".remove");
	});

	$("button.empty").click(function() {
		$("b").empty(".empty");
	});

	$("button.addclass").click(function() {
		$("b").addClass("jqcss");
	});

	$("button.removeclass").click(function() {
		$("b").removeClass("jqcss");
	});

	$("button.toggleclass").click(function() {
		$("b").toggleClass("jqcss");
	});

	$("button.css").click(function() {
		alert($("b,p").css("color"));
		$("b,p").css("front-size","40");
		$("b,p").css({"padding":"40","border":"5px solid pink"});
		
	});

	$("button.width").click(function() {
		$("p.size").text($("p.size").width());
	});

	$("button.height").click(function() {
		$("p.size").text($("p.size").height());
	});

	$("button.innerwidth").click(function() {
		$("p.size").text($("p.size").innerWidth());
	});

	$("button.innerheight").click(function() {
		$("p.size").text($("p.size").innerHeight());
	})

	$("button.outerwidth").click(function() {
		$("p.size").text($("p.size").outerWidth());
	});

	$("button.outerheight").click(function() {
		$("p.size").text($("p.size").outerHeight());
	});

	$("button.outerwidthmargin").click(function() {
		$("p.size").text($("p.size").outerWidth(true));
	});

	$("button.outerheightmargin").click(function() {
		$("p.size").text($("p.size").outerHeight(true));
	});

	$("button.window").click(function() {
		$("p.size").text($(window).width()+"x"+$(window).height());
	});

	$("button.document").click(function() {
		$("p.size").text($(document).width()+"x"+$(document).height());
	});

	$("button.changesize").click(function() {
		$("p.size").width(500);
		$("p.size").height(600);
	});

	$("button.parent").click(function() {
		$("p.travel").parentsUntil("body").css({"color":"gray","border":"5px solid gray"});
		$("p.travel").parent().css({"color":"red","border":"5px solid red"});
	});

	$("button.parents").click(function() {
		$("p.travel").parents().css({"color":"gray","border":"5px solid gray"});
		$("p.travel").parents().css({"color":"red","border":"5px solid red"});
	});

	$("button.parentsspecial").click(function() {
		$("p.travel").parentsUntil("body").css({"color":"gray","border":"5px solid gray"});
		$("p.travel").parents("ul").css({"color":"red","border":"5px solid red"});
	});

	$("button.parentsuntil").click(function() {
		$("p.travel").parentsUntil("body").css({"color":"gray","border":"5px solid gray"});
		$("p.travel").parentsUntil("ul").css({"color":"red","border":"5px solid red"});
	});

	$("button.children").click(function() {
		$("ul").children().css({"color":"red","border":"5px solid red"});
	
	});

	$("button.find").click(function() {
		$("li").find("ol").css({"color":"red","border":"5px solid red"});
	});

	$("button.findall").click(function() {
		$("li").find("*").css({"color":"red","border":"5px solid red"});
	});




});


