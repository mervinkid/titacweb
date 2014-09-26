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
    //search
    var search_text = $('#search_text');
    var search_submit = $('#search_submit');
    search_text.focus(function(){
        search_text.attr('placeholder', '');
        search_text.attr('style', 'border-color:#df3a65;');
    });
    search_text.focusout(function(){
        search_text.attr('placeholder', '搜索');
        search_text.attr('style', 'border-color:#b6b6b6;');
    });
    search_submit.click(function(){
        var query_string = search_text.val();
        query_string = query_string.trim();
        if(query_string == '')
            return false;
        return true;
    })
});