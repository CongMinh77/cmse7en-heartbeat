$(document).ready(function () {
  const element = {
    title: $(".title"),
    progress: $("#progress"),
    wrapMessage: $("#wrapMessage"),
    wrapProgressBar: $("#wrapProgressBar"),
    cancelButton: $("#cancelButton"),
    main: $("#main"),
  };

  const timeProgress = 5000;

  element.progress.animate({ width: "100%" }, timeProgress);

  setInterval(function () {
    element.wrapProgressBar.css("display", "none");
    element.wrapMessage.css("display", "inline-block");
  }, timeProgress);

  element.cancelButton.on("click", function () {
    axios({
      method: "get",
      url: "http://127.0.0.1:5500/src/HeartbeatWebs/LibraryHeartbeat/heartType6.html",
      responseType: "stream",
    }).then(function (response) {
      const a = response.data;
      element.main.html(a);

      console.debug("a", a);
    });
  });
});
