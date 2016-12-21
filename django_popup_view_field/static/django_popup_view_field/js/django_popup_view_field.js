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

    // Bind all events for dialog content after content loaded
    // bind click to elements
    // override behavior for anchors (all anchors loaded by ajax)
    // override behavior for submit buttons for forms
    var bind_events = function($dialog, $button){
        var $dial_body = $dialog.find(".modal-body");

        // Click to evrithing
        $dial_body.find("*").on("click", function(event){
            var target_id = null, $target = null;
            var $elem = $(this);
            var value = $elem.data("popup-view-value");

            // Set value in field
            if (value !== undefined) {

                // If data-popup-view-value is html() then
                // full html content of element is set as value
                if ( value === "html()" ) {
                    value = $elem.html();
                    if (value) {
                        value = value.trim();
                    }
                }

                target_id = $button.data("target");
                target = $("#" + target_id);
                event.stopPropagation();
                $dialog.modal('hide');
                target.val(value);
            }

            // Override behavior for anchors
            if ($elem.is("a[href]") === true) {
                var href = $elem.prop("href");
                event.stopPropagation();
                get_content($dialog, $button, href, "GET", null);
                return false;
            }
        });

        $dial_body.find("form").on("submit", function(event){
            var $form = $(this);
            var method = $form.attr("method") || "POST";
            var action = $form.attr("action") || ".";
            var data = $form.serialize();
            event.stopPropagation();
            get_content($dialog, $button, action, method, data);
            return false;
        });
    };

    // Load content for dialog from popup view by ajax request
    var get_content = function($dialog, $button, url, method, data){

        var ajax_param = {
            'url' : url,
            'method' : method,
            'cache' : false
        };

        if (data != null) {
            ajax_param['data']=data;
        }

        var request = $.ajax(ajax_param);

        request.done(function(response){
            $dialog.find(".modal-body").html(response);
            bind_events($dialog, $button);
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
        get_content($dialog, $button, url, "GET", null);
    });

    $(".popup-view-btn-clear").on("click", function(){
        var $button = $(this);
        var target_id = $button.data("target");
        var $target = $("#" + target_id);
        $target.val("");
    });

});
