// JavaScript Document for Theflow
$(document).ready(function() {
    //full width slider on home page
    $('.slider').flexslider({
    	animation: "slide",
		slideshowSpeed: 4000,
		animationDuration: 500,
    	controlNav: true,
    	keyboardNav: true,
    	directionNav: false,
		pauseOnHover: true,
		pauseOnAction: true    
    });
    //full width slider on home page
    $('.slider-testimonial').flexslider({
    	animation: "fade",
		slideshowSpeed: 4000,
		animationDuration: 500,
    	controlNav: false,
    	keyboardNav: true,
    	directionNav: false,
		pauseOnHover: true,
		pauseOnAction: true    
    });
    //full width slider on home page
    $('.slider-small').flexslider({
    	animation: "fade",
		slideshowSpeed: 4000,
		animationDuration: 500,
    	controlNav: true,
    	keyboardNav: true,
    	directionNav: false,
		pauseOnHover: true,
		pauseOnAction: true    
    });
    // Create the dropdown menu for responsive
    $("<select />").appendTo("#menu");
	$("<option />", {
	    "selected": "selected",
	    "value"   : "",
	    "text"    : "Menu"
	}).appendTo("#menu select");
	// Populate dropdown with menu items
	$("#menu a").each(function() {
	    var el = $(this);
	    $("<option />", {
	        "value": el.attr("href"),
	        "text" : el.text()
	    }).appendTo("#menu select");
	});
	// To make dropdown actually work
	// To make more unobtrusive: http://css-tricks.com/4064-unobtrusive-page-changer/
	$("#menu select").change(function() {
	    window.location = $(this).find("option:selected").val();
    });
    //Search Box
    var search = $('#search_text');
    search.focus(function(){
        search.attr('placeholder', '');
    });
    search.focusout(function(){
        search.attr('placeholder', '搜索');
    });
}); //close document.ready

    // Below scripts do not require modification

    /* IE Image Resizing - by Ethan Marcotte - http://unstoppablerobotninja.com/entry/fluid-images/ */
var imgSizer = {
	Config : {
		imgCache : []
		,spacer : "../images/spacer.gif"
	}

	,collate : function(aScope) {
		var isOldIE = (document.all && !window.opera && !window.XDomainRequest) ? 1 : 0;
		if (isOldIE && document.getElementsByTagName) {
			var c = imgSizer;
			var imgCache = c.Config.imgCache;

			var images = (aScope && aScope.length) ? aScope : document.getElementsByTagName("img");
			for (var i = 0; i < images.length; i++) {
				images[i].origWidth = images[i].offsetWidth;
				images[i].origHeight = images[i].offsetHeight;

				imgCache.push(images[i]);
				c.ieAlpha(images[i]);
				images[i].style.width = "100%";
			}

			if (imgCache.length) {
				c.resize(function() {
					for (var i = 0; i < imgCache.length; i++) {
						var ratio = (imgCache[i].offsetWidth / imgCache[i].origWidth);
						imgCache[i].style.height = (imgCache[i].origHeight * ratio) + "px";
					}
				});
			}
		}
	}

	,ieAlpha : function(img) {
		var c = imgSizer;
		if (img.oldSrc) {
			img.src = img.oldSrc;
		}
		var src = img.src;
		img.style.width = img.offsetWidth + "px";
		img.style.height = img.offsetHeight + "px";
		img.style.filter = "progid:DXImageTransform.Microsoft.AlphaImageLoader(src='" + src + "', sizingMethod='scale')"
		img.oldSrc = src;
		img.src = c.Config.spacer;
	}

	// Ghettomodified version of Simon Willison's addLoadEvent() -- http://simonwillison.net/2004/May/26/addLoadEvent/
	,resize : function(func) {
		var oldonresize = window.onresize;
		if (typeof window.onresize != 'function') {
			window.onresize = func;
		} else {
			window.onresize = function() {
				if (oldonresize) {
					oldonresize();
				}
				func();
			}
		}
	}
}

/**
 * jQuery.ScrollTo - Easy element scrolling using jQuery.
 * Copyright (c) 2007-2009 Ariel Flesler - aflesler(at)gmail(dot)com | http://flesler.blogspot.com
 * Dual licensed under MIT and GPL.
 * Date: 5/25/2009
 * @author Ariel Flesler
 * @version 1.4.2
 *
 * http://flesler.blogspot.com/2007/10/jqueryscrollto.html
 */
;(function(d){var k=d.scrollTo=function(a,i,e){d(window).scrollTo(a,i,e)};k.defaults={axis:'xy',duration:parseFloat(d.fn.jquery)>=1.3?0:1};k.window=function(a){return d(window)._scrollable()};d.fn._scrollable=function(){return this.map(function(){var a=this,i=!a.nodeName||d.inArray(a.nodeName.toLowerCase(),['iframe','#document','html','body'])!=-1;if(!i)return a;var e=(a.contentWindow||a).document||a.ownerDocument||a;return d.browser.safari||e.compatMode=='BackCompat'?e.body:e.documentElement})};d.fn.scrollTo=function(n,j,b){if(typeof j=='object'){b=j;j=0}if(typeof b=='function')b={onAfter:b};if(n=='max')n=9e9;b=d.extend({},k.defaults,b);j=j||b.speed||b.duration;b.queue=b.queue&&b.axis.length>1;if(b.queue)j/=2;b.offset=p(b.offset);b.over=p(b.over);return this._scrollable().each(function(){var q=this,r=d(q),f=n,s,g={},u=r.is('html,body');switch(typeof f){case'number':case'string':if(/^([+-]=)?\d+(\.\d+)?(px|%)?$/.test(f)){f=p(f);break}f=d(f,this);case'object':if(f.is||f.style)s=(f=d(f)).offset()}d.each(b.axis.split(''),function(a,i){var e=i=='x'?'Left':'Top',h=e.toLowerCase(),c='scroll'+e,l=q[c],m=k.max(q,i);if(s){g[c]=s[h]+(u?0:l-r.offset()[h]);if(b.margin){g[c]-=parseInt(f.css('margin'+e))||0;g[c]-=parseInt(f.css('border'+e+'Width'))||0}g[c]+=b.offset[h]||0;if(b.over[h])g[c]+=f[i=='x'?'width':'height']()*b.over[h]}else{var o=f[h];g[c]=o.slice&&o.slice(-1)=='%'?parseFloat(o)/100*m:o}if(/^\d+$/.test(g[c]))g[c]=g[c]<=0?0:Math.min(g[c],m);if(!a&&b.queue){if(l!=g[c])t(b.onAfterFirst);delete g[c]}});t(b.onAfter);function t(a){r.animate(g,j,b.easing,a&&function(){a.call(this,n,b)})}}).end()};k.max=function(a,i){var e=i=='x'?'Width':'Height',h='scroll'+e;if(!d(a).is('html,body'))return a[h]-d(a)[e.toLowerCase()]();var c='client'+e,l=a.ownerDocument.documentElement,m=a.ownerDocument.body;return Math.max(l[h],m[h])-Math.min(l[c],m[c])};function p(a){return typeof a=='object'?a:{top:a,left:a}}})(jQuery);

/*global jQuery */
/*! 
* FitVids 1.0
*
* Copyright 2011, Chris Coyier - http://css-tricks.com + Dave Rupert - http://daverupert.com
* Credit to Thierry Koblentz - http://www.alistapart.com/articles/creating-intrinsic-ratios-for-video/
* Released under the WTFPL license - http://sam.zoy.org/wtfpl/
*
* Date: Thu Sept 01 18:00:00 2011 -0500
*/

(function( $ ){
    $.fn.fitVids = function( options ) {
        var settings = {
        customSelector: null
    }
    
    var div = document.createElement('div'),
        ref = document.getElementsByTagName('base')[0] || document.getElementsByTagName('script')[0];
        
  	div.className = 'fit-vids-style';
    div.innerHTML = '&shy;<style>       \
        .fluid-width-video-wrapper {      \
            width: 100%;                  \
            position: relative;           \
            padding: 0;                   \
        }                                 \
                                          \
        .fluid-width-video-wrapper iframe,  \
        .fluid-width-video-wrapper object,  \
        .fluid-width-video-wrapper embed {  \
            position: absolute;             \
            top: 0;                         \
            left: 0;                        \
            width: 100%;                    \
            height: 100%;                   \
        }                                   \
    </style>';
                      
    ref.parentNode.insertBefore(div,ref);
    
    if ( options ) { 
      $.extend( settings, options );
    }
    
    return this.each(function(){
        var selectors = [
            "iframe[src*='player.vimeo.com']",
            "iframe[src*='www.youtube.com']",
            "iframe[src*='www.kickstarter.com']",
            "object",
            "embed"
        ];
      
        if (settings.customSelector) {
            selectors.push(settings.customSelector);
        }
      
        var $allVideos = $(this).find(selectors.join(','));

        $allVideos.each(function(){
            var $this = $(this);
            if (this.tagName.toLowerCase() == 'embed' && $this.parent('object').length || $this.parent('.fluid-width-video-wrapper').length) { return; }
            var height = this.tagName.toLowerCase() == 'object' ? $this.attr('height') : $this.height(),
            aspectRatio = height / $this.width();
		    if(!$this.attr('id')){
			    var videoID = 'fitvid' + Math.floor(Math.random()*999999);
			    $this.attr('id', videoID);
		    }
            $this.wrap('<div class="fluid-width-video-wrapper"></div>').parent('.fluid-width-video-wrapper').css('padding-top', (aspectRatio * 100)+"%");
            $this.removeAttr('height').removeAttr('width');
        });
    });
  
}
})( jQuery );


// Basic FitVids Test
$(".container").fitVids();
// Custom selector and No-Double-Wrapping Prevention Test
$(".container").fitVids({ customSelector: "iframe[src^='http://socialcam.com']"});