document.addEventListener("DOMContentLoaded", function() {
  const startEndButton = document.getElementById("startEndButton");
  const rateCourseModal = new bootstrap.Modal(document.getElementById("rateCourseModal"));
  const easyButton = document.getElementById("easyButton");
  const mediumButton = document.getElementById("mediumButton");
  const hardButton = document.getElementById("hardButton");

  startEndButton.addEventListener("click", function() {
    if (startEndButton.textContent === "Start") {
      startEndButton.textContent = "End";
    } else {
      startEndButton.textContent = "Start";
      rateCourseModal.show();
    }
  });

  easyButton.addEventListener("click", function() {
    rateCourseModal.hide();
  });

  mediumButton.addEventListener("click", function() {
    rateCourseModal.hide();
  });

  hardButton.addEventListener("click", function() {
    rateCourseModal.hide();
  });
});

document.addEventListener("DOMContentLoaded", function() {
  const subscribeButton = document.getElementById("subscribeButton");

  subscribeButton.addEventListener("click", function() {
    if (subscribeButton.textContent === "Subscribe") {
      subscribeButton.textContent = "Subscribed";
    } else {
      subscribeButton.textContent = "Subscribe";
    }
  });
});
