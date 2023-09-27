
$(document).ready(function () {
    $('#add-description-form').click(function (event) {
        event.preventDefault();
        const href = $(this).attr('href');
        $.ajax({
            url: href,
            type: 'GET',
            dataType: 'html',
            success: function (data) {
                $('#description-form-container').html(data);
                $('#add-description-form').hide();
            }
        });
    });
    $('#edit-description-form').click(function (event) {
        event.preventDefault();
        const href = $(this).attr('href');
        $.ajax({
            url: href,
            type: 'GET',
            dataType: 'html',
            success: function (data) {
                $('#description-form-container').html(data);
                $('#edit-description-form').hide();
                $('#description').hide();
            }
        });
    });


});


