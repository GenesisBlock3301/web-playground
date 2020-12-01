
$(document).ready(function () {
    $('#createBtn').click(function (e) {
        const serializedData = $('#createTaskForm').serialize();
        $.ajax({
            //the url where i'm sending the form to
            url: $('#createTaskForm').data('url'),
            data: serializedData,
            type: 'POST',
            success: function (response) {
                const createdTask = '<div class="card mb-3" id="taskCard" data-id="' + response.task.id + '><div class="card-body outline-info">' +
                    response.task.title +
                    '<button type="button" class="close float-right" data-id="' + response.task.id + '"><span aria-hidden="true">&times;</span></button></div></div>'
                $('#todos-list').append(createdTask);
            }
        });
        //to cleare the form's input
        $('#createTaskForm')[0].reset()
    });

    $('#todos-list').on('click', '.card', function () {
        const dataID = $(this).data('id');
        $.ajax({
            url: '/todos/' + dataID + '/completed/',
            data: {
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
                id: dataID,
            },
            type: 'POST',
            success: function () {
                const cardItem = $('#taskCard[data-id="' + dataID + '"]');
                //cardItem.classList.toggle('done');
                cardItem.css('text-decoration', 'line-through').hide().slideDown();
                $('#todos-list').append(cardItem);
            }
        });
    }).on('click', 'button.close', function (event) {
        event.stopPropagation();
        const dataID = $(this).data('id');
        $.ajax(
            {
                url: '/todos/' + dataID + '/deleted/',
                data: {
                    csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
                    id: dataID
                },
                type: 'POST',
                dataType: 'json',
                success: function () {
                    $('#taskCard[data-id="' + dataID + '"]').remove();
                }
            }
        )
    })


});
//Django AJAX tutorial: TODO app with JQuery