$(document).on('click', '#close-edit-todo-form', function() {
  const formContainer = $(this).closest(".container")
  formContainer.closest(".todo").find('.todo-item').show();


  formContainer.hide();
});

$(document).on('click', '#close-description-form', function() {
  const formContainer = $(this).closest(".container");
  formContainer.hide();
  $(".desc-button").show();
  $("#description").show();
});

$(document).on('click', '#close-create-todo-form', function() {
  const formContainer = $(this).closest(".container")
  $(this).closest(".button-container").find('#show-create-form').show();
  formContainer.hide();
});

