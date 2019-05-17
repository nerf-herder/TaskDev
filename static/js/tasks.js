$(document).ready(
  () => {
		$('#quad-0, #quad-1, #quad-2, #quad-3').sortable({connectWith: ".shortcutsSorting", placeholder: "dropPlaceHolder"});
		//$('.shortcutsSorting').disableSelection();

		$('.shortcutsSorting').on("sortstop",
			function(event, ui)
			{
				saveOrder();
			});
	}
);

// renaming todo entires
$(document).on('click', '.todoLabel',
  function () {
    theLi = $(this).parents('li').first();
    $(this).replaceWith(`<input type="text" class="renameTodo" value="${$(this).text()}" />`);
    $('.renameTodo', theLi).select();
  });
$(document).on('keyup', '.renameTodo',
  function (e) {
    if (e.which == 13) {$(this).trigger('blur');}
  });
$(document).on('blur', '.renameTodo',
  function () {
    renameInput = $(this);

    $.ajax({
			   type: 'GET',
			   url: '/task/',
			   data: { renameTodo: 1, todoId: renameInput.parents('[data-todoid]').attr('data-todoid'), newLabel: renameInput.val() },
    }).done(
      (returnData) => {

					if (returnData['msgType'] == 'success')
						renameInput.replaceWith('<span class="todoLabel">'+renameInput.val()+'</span>');
				}
);
  });

// save to-dos order
function saveOrder() {
  newOrders = Array(4);
  $('.shortcutsSorting').each(
    function () {
      currQuad = parseInt($(this).attr('data-quad'));
      newOrders[currQuad] = Array();

      $('li', this).each(
        function () {
          newOrders[currQuad].push($(this).attr('data-toDoId'));
        }
);
    }
);

  $.ajax({
		   type: 'GET',
		   url: '/task/',
		   data: { saveToDoOrder: 1, quad0Order: newOrders[0].toString(), quad1Order: newOrders[1].toString(), quad2Order: newOrders[2].toString(), quad3Order: newOrders[3].toString() },
  }).done(
    (returnData) => {
				// alertMessage(returnData['msg'], returnData['msgType']);
			}
);
}

// delete to-do
$(document).on('click', '.delShortcut',
  function () {
    delToDoLi = $(this).parents('li');
    delToDoId = delToDoLi.attr('data-toDoId');

    conf = confirm('Are you sure?');
    if (conf) {
      $.ajax({
				   type: 'GET',
				   url: '/task/',
				   data: { delToDo: delToDoId },
      }).done(
        (returnData) => {
						// alertMessage(returnData['msg'], returnData['msgType']);
						if (returnData['msgType'] == 'success')
							delToDoLi.animate({'height' : 0, 'margin' : 0, 'padding-top' : 0, 'padding-bottom' : 0, 'opacity' : 0}, {'duration' : 300, 'complete' : function(){ delToDoLi.remove(); } });
					}
);
    }
  });

$(document).on('click', '.showAddFormButton',
  function () {
    showAddForm($(this).attr('data-showQuad'), $(this));
  });

// show add new form
function showAddForm(quad, linkClicked) {
  $(`#quad-${  quad}`).prepend('<li><span></span><input name="newToDoLabel" value="" type="text"></li>');
  // $('[name="newToDoQuad"]').val(quad);
  // $('.addNewShortcutFormSpace').appendTo('#addNewQuad' + quad).show();
  $('[name="newToDoLabel"]').trigger('focus');
}

$(document).on('keyup', '[name="newToDoLabel"]',
  function (e) {
    console.log($(this), $(this).parents('ul.shortcutsSorting').attr('data-quad'));
    if (e.keyCode == 13) {
      createToDo($(this).parents('ul.shortcutsSorting').attr('data-quad'));
    } else if (e.keyCode == 27) {
      $(this).parent('li').remove();
    }
  });

// creating new to-do
function createToDo(quad) {
  $.ajax({
		   type: 'GET',
		   url: '/task/',
		   data: { createToDo: 1, label: $('[name="newToDoLabel"]').val(), quad },
  }).done(
    (returnData) => {
			//	alert(returnData['msg']);
				if (returnData['msgType'] == 'success')
					location.reload();
			}
);
}
