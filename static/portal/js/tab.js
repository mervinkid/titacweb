function activeTab(parm) {
    tabButtons = $("a[id^='tab-button-']");
    tabButtons.attr("class", "");
    tabls = $("div[id^='tab-content-']");
    tabls.slideUp(400);
    contentId = '#tab-content-' + parm;
    $(contentId).slideDown(400)
    buttonId = '#tab-button-' + parm;
    $(buttonId).attr("class", "active");
}