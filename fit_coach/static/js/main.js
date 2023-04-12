function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader('X-CSRFToken', csrftoken);
        }
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const startEndButton = document.getElementById("startEndButton");
    const rateCourseModal = new bootstrap.Modal(document.getElementById("rateCourseModal"));
    const easyButton = document.getElementById("easyButton");
    const mediumButton = document.getElementById("mediumButton");
    const hardButton = document.getElementById("hardButton");

    startEndButton.addEventListener("click", function () {
        if (startEndButton.textContent === "Start") {
            startEndButton.textContent = "End";
        } else {
            startEndButton.textContent = "Start";
            rateCourseModal.show();
        }
    });

    easyButton.addEventListener("click", function () {
        rateCourseModal.hide();
    });

    mediumButton.addEventListener("click", function () {
        rateCourseModal.hide();
    });

    hardButton.addEventListener("click", function () {
        rateCourseModal.hide();
    });
});

function showFeedbackDialog() {
  $('#feedbackModal').modal('show');
}

document.addEventListener("DOMContentLoaded", function () {
    const subscribeButton = document.getElementById("subscribeButton");
    const courseId = $('#subscribeButton').data('course-id')

    subscribeButton.addEventListener("click", function () {
        if (subscribeButton.textContent.trim() === "Subscribe") {
            $.ajax({
                url: '/start/',
                type: 'POST',
                data: {
                    'course_id': courseId,
                },
                dataType: 'json',
                success: function (_) {
                    subscribeButton.textContent = "Terminate";
                }
            })
        } else if (subscribeButton.textContent.trim() == "Terminate") {
            showFeedbackDialog()
            subscribeButton.textContent = "Subscribe"
        }
    });
});


