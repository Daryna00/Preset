/* ===================================
--------------------------------------
  NISSA - PHOTOGRAPHY STUDIO TEMPLATE
  Version: 1.0
 -------------------------------------
 =====================================*/


'use strict';

$(window).on('load', function() {
	/*------------------
		Preloder
	--------------------*/
	$(".loader").fadeOut();
	$("#preloder").delay(400).fadeOut("slow");

});

(function($) {
	/*------------------
		Navigation
	--------------------*/
	$('.nav-switch').on('click', function() {
		$('.main-site-warp').addClass('push-side');
		$('body').addClass('push-side');
		setTimeout(function(){
			hero_section();
		}, 400)
		
	});
	$('.close-menu').on('click', function() {
		$('.main-site-warp').removeClass('push-side');
		setTimeout(function(){
			$('body').removeClass('push-side');		
		}, 400);
	});


	/*------------------
		Background Set
	--------------------*/
	$('.set-bg').each(function() {
		var bg = $(this).data('setbg');
		$(this).css('background-image', 'url(' + bg + ')');
	});


	/*------------------
	   Custom Scrollbar
	--------------------*/
	function site_scrollbar() {

		if ($(window).width() > 991) {
			$(".main-sidebar").niceScroll({
				cursorborder:"",
				cursorcolor:"#f1f1f1",
				boxzoom:false,
				cursorwidth: 4,
				cursorborderradius:0,
			});

			$(".about-section, .contact-section, .elements-section").niceScroll({
				cursorborder:"",
				cursorcolor:"#f1f1f1",
				boxzoom:false,
				cursorwidth: 4,
				cursorborderradius:0,
			});

			$(".blog-posts").niceScroll({
				cursorborder:"",
				cursorcolor:"#242424",
				boxzoom:false,
				cursorwidth: 4,
				autohidemode:true,
				background: '#eeeeee',
				railoffset: { top: 50, right: 0, left: 40, bottom: 0 },
				railpadding: { top: 0, right: 0, left: 0, bottom: 100 },
			});

			$(".portfolio-section").niceScroll({
				cursorborder:"",
				cursorcolor:"#242424",
				boxzoom:false,
				cursorwidth: 4,
				autohidemode:true,
				background: '#eeeeee',
				railoffset: { top: 50, right: 0, left: -14, bottom: 0 },
				railpadding: { top: 0, right: 0, left: 0, bottom: 100 },
			});
		}

	}
	site_scrollbar();


	/*------------------
		Video Popup
	--------------------*/
	$('.video-popup').magnificPopup({
		type: 'iframe'
	});

	/*------------------
		Hero section
	--------------------*/
	function hero_section() {
		if ($(window).width() > 768) {

			var ps_w = $('.page-section').innerWidth();
			$('.hs-item').width(ps_w / 2);
			var trackW = (($('.hs-item').width()) * $('.hs-item').length) + ($('.hs-item').length * 50);
			$('.hero-track').width(trackW);

			var hs_width =  $(window).innerHeight() - 170;
			$('.hs-item').height(hs_width);

			$(".hero-scroll").niceScroll({
				cursorborder:"",
				cursorcolor:"#242424",
				boxzoom:false,
				cursorwidth: 4,
				autohidemode:false,
				background: '#eeeeee',
				cursorborderradius:0,
				railoffset: { top: 0, right: 50, left: 0, bottom: 0 },
				railpadding: { top: 0, right: 0, left: 0, bottom: 0 },
			});
		}
		if ($(window).width() < 768) {
			$('.hero-track').addClass('owl-carousel')
			$('.hero-track').owlCarousel({
				loop: true,
				margin: 0,
				nav: true,
				items: 1,
				dots: false,
				margin: 30,
				navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
			});
		}
	}

	hero_section();

	$(window).resize(function () {
		hero_section();
		site_scrollbar();
	});


	/*------------------
		Accordions
	--------------------*/
	$('.panel-link').on('click', function (e) {
		$('.panel-link').parent('.panel-header').removeClass('active');
		var $this = $(this).parent('.panel-header');
		if (!$this.hasClass('active')) {
			$this.addClass('active');
		}
		e.preventDefault();
	});

	/*------------------
		Progress Bar
	--------------------*/
	$('.progress-bar-style').each(function() {
		var progress = $(this).data("progress");
		var prog_width = progress + '%';
		if (progress <= 100) {
			$(this).append('<div class="bar-inner" style="width:' + prog_width + '"><span>' + prog_width + '</span></div>');
		}
		else {
			$(this).append('<div class="bar-inner" style="width:100%"><span>' + prog_width + '</span></div>');
		}
	});

	/*------------------
		Circle progress
	--------------------*/
	$('.circle-progress').each(function() {
		var cpvalue = $(this).data("cpvalue");
		var cpcolor = $(this).data("cpcolor");
		var cpid 	= $(this).data("cpid");

		$(this).prepend('<div class="'+ cpid +' circle-warp"></div><h2>'+ cpvalue +'<span>%</span></h2>');

		if (cpvalue < 100) {

			$('.' + cpid).circleProgress({
				value: '0.' + cpvalue,
				size: 84,
				thickness: 5,
				fill: cpcolor,
				emptyFill: "rgba(0, 0, 0, 0)"
			});
		} else {
			$('.' + cpid).circleProgress({
				value: 1,
				size: 84,
				thickness: 5,
				fill: cpcolor,
				emptyFill: "rgba(0, 0, 0, 0)"
			});
		}

});
});
$('#main-product').click(function () {
  console.log('aria clicked')
  let checkbox_list = $('.checkbox-category:checked').toArray()
  console.log(checkbox_list)
  let new_link = '?'

  if (checkbox_list.length > 0){
      console.log(checkbox_list[0].id)
      let list_of_ids = checkbox_list.map(el => el.id.replace('product', 'product='))
      console.log(list_of_ids)
      console.log(list_of_ids.join('&'))
      new_link = '?' + list_of_ids.join('&')

  }

  $('#product-filter-button').attr('href', new_link)
})
$('.change_merchan_count').click(function () {
  let order_id = $(this).attr('id').slice(8)
  let action = $(this).attr('id').slice(0, 8)
  let button  = $(this).siblings('.order_count')
  console.log(order_id)

  $.ajax({
    url: `/change_order_count/${order_id}`,
    method: 'GET',
    data: {
      'action': action
    },
    success: function (result) {
      if (result.status === 'ok'){
        console.log('ok to action');
        console.log(result.new_number)
        $(button).text(result.new_number)
        update_total()
      }
    }
  })



})


function update_total(){
  let orders = $('.order_row');
  let total_cost = 0;
  for (let order of orders){
    let count = $(order).find('.order_count').text()
    let cost = $(order).find('.order_cost').text()

    total_cost += (+count) * (+cost)
  }
  $('#total_cost').text(total_cost + '$')
}

$('.order_table').click(function () {
  update_total()
})

$(".delete_order").click(function () {
  let slug = $(this).attr('id').slice(6)
  let row = $(this).closest('.order_row')
  console.log(slug)

    $.ajax({
    url: `/delete_from_card/${slug}`,
    method: 'GET',
    success: function (result) {
      if (result.status === 'ok'){
        row.remove()
        update_total()
      }
    }
  })

})


(jQuery);
function searchToggle(obj, evt){
    var container = $(obj).closest('.search-wrapper');
        if(!container.hasClass('active')){
            container.addClass('active');
            evt.preventDefault();
        }
        else if(container.hasClass('active') && $(obj).closest('.input-holder').length == 0){
            container.removeClass('active');
            // clear input
            container.find('.search-input').val('');
        }
}



