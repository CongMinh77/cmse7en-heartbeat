$(document).ready(function () {
  const element = {
    title: $(".title"),
    progress: $("#progress"),
    wrapMessage: $("#wrapMessage"),
    wrapProgressBar: $("#wrapProgressBar"),
    cancelButton: $("#cancelButton"),
    main: $("#main"),
    acceptButton: $("#acceptButton"),
  };

  const timeProgress = 5000;

  element.progress.animate({ width: "100%" }, timeProgress);

  setInterval(function () {
    element.wrapProgressBar.css("display", "none");
    element.wrapMessage.css("display", "inline-block");
  }, timeProgress);

  element.acceptButton.on("click", function () {
    const url = window.location.href;
    axios({
      method: "get",
      url: `${url}/HeartbeatWebs/LibraryHeartbeat/heartType6.html`,
      responseType: "stream",
    }).then(function (response) {
      const a = response.data;
      element.main.html(a);
    });
  });

  element.cancelButton.on("mousemove", function () {
    let width = $(this).width();
    width -= 10;
    if (width <= 0) {
      $(this).hide();
    } else {
      $(this).css({
        width: width + "px",
        left: Math.random() * (window.innerWidth - width) + "px",
        top: Math.random() * (window.innerHeight - $(this).height()) + "px",
      });
    }
  });
});
