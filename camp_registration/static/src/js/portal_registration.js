$(document).ready(function () {
	
	$(function() {
	    $('#camp_date_time').datepicker({
	        dateFormat: 'yy-mm-dd',
	        onSelect: function(datetext) {
	            var d = new Date(); // for now

	            var h = d.getHours();
	            h = (h < 10) ? ("0" + h) : h ;

	            var m = d.getMinutes();
	            m = (m < 10) ? ("0" + m) : m ;

	            var s = d.getSeconds();
	            s = (s < 10) ? ("0" + s) : s ;

	            datetext = datetext + " " + h + ":" + m + ":" + s;

	            $('#camp_date_time').val(datetext);
	        }
	    });
	});
	
	
	$(function() {
	  $(".if_camp_organizer").hide();	
	  $("#is_camp_organizer").click(function() {
	    if ($(this).is(":checked")) {
	      $(".if_camp_organizer").show();
	    } else {
	      $(".if_camp_organizer").hide();
	    }
	  });
	});

	
	//$(function() {
	//	$("#week_am_1").click(function() {
	//		if ($(this).is(":checked")) {
	//		  $("#week_pm_1").not(this).prop('checked', false);//uncheck other checkboxes
	//		  $("#week_full_1").not(this).prop('checked', false);//uncheck other checkboxes
	//		}
	//	});
	//	$("#week_pm_1").click(function() {
	//		if ($(this).is(":checked")) {
	//		  $("#week_am_1").not(this).prop('checked', false);//uncheck other checkboxes
	//		  $("#week_full_1").not(this).prop('checked', false);//uncheck other checkboxes
	//		}
	//	});
	//	$("#week_full_1").click(function() {
	//		if ($(this).is(":checked")) {
	//		  $("#week_am_1").not(this).prop('checked', false);//uncheck other checkboxes
	//		  $("#week_pm_1").not(this).prop('checked', false);//uncheck other checkboxes
	//		}
	//	});
//
	//});

	
	
});

