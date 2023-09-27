
$(document).ready(function () {
    $('#show-create-form').click(function (event) {
        event.preventDefault();
        const href = $(this).attr('href');
        $.ajax({
            url: href,
            type: 'GET',
            dataType: 'html',
            success: function (data) {
                $('#create-form-container').html(data);
                $('#show-create-form').hide();
            }
        });
    });
});

$(document).on('submit', 'form', function(event) {
        event.preventDefault();

        var formData = $(this).serialize();
        var actionUrl = $(this).attr('action');
        const form = $(this);
        $.ajax({
            type: "POST",
            url: actionUrl,
            data: formData,
            success: function(response) {
                if (response.form){
                form.parent().parent().html(response.form);
                }
                else if (response.redirect) {
                    window.location.href = response.redirect;
                }

            }
        });
    });