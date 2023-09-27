$(document).ready(function () {
        $('.show-edit-form').click(function (event) {
            event.preventDefault();
            const parent = $(this).parent().parent();
            const href = $(this).attr('href');
            $.ajax({
            url: href,
            type: 'GET',
            dataType: 'html',
            success: function (data) {
                parent.children('.todo-item').hide();
                parent.children('.edit-form-container').html(data);
            }
        });

        });
 });