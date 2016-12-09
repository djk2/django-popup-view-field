// Author: Grzegorz Tężycki
// https://github.com/djk2/django-popup-view-field

if ("undefined"==typeof jQuery) {
    throw new Error("django-popup-view-field - requires jQuery");
}

$(document).ready(function(){

    var dialog_counter = 0;

    var get_url = function($button){
        var url = $button.data("url");
        return url;
    };

    var get_content = function($dialog, $button, url){
        var $dial_body = $dialog.find(".modal-body");
        var request = $.ajax({
            url : url,
            method : "GET",
            cache : false,
        });

        request.done(function(response){
            $dial_body.html(response);
        });
        request.fail(function(response){
            $dialog.modal('hide');
            throw new Error("django-popup-view-field - Ajax request to url: " + url);
        });
    };

    var create_dialog = function($button){
        var dialog_template = $("#template-django-popup-view-field").html();
        var $dialog_window = $(dialog_template);
        var dial_id = $dialog_window.attr("id") + dialog_counter;
        var dial_title = $button.data('popup-dialog-title');
        var dial_body = gettext('Data is loading ...');
        var dial_close = gettext('Close');
        $dialog_window.attr("id", dial_id);
        $dialog_window.find(".modal-title").html(dial_title);
        $dialog_window.find(".modal-body").html(dial_body);
        $dialog_window.find(".modal-footer-close").html(dial_close);
        dialog_counter++;
        return $dialog_window;
    };

    $(".popup-view-btn-load").on("click", function(){
        var $button = $(this);
        var $dialog = create_dialog($button);
        var url = get_url($button);
        $dialog.modal({ backdrop:false });
        $dialog.on('hidden.bs.modal', function (e) {
            $(this).remove();
        });
        get_content($dialog, $button, url);
    });

    $(".popup-view-btn-clear").on("click", function(){
        var $button = $(this);
        var target_id = $button.data("target");
        var $target = $("#" + target_id);
        $target.val("");
    });

});
