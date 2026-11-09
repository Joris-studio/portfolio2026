// Video in a phone frame: poster with a play button, no autoplay, no sound.
// Without JavaScript the video keeps its native controls.
document.querySelectorAll('video[data-player]').forEach(function (video) {
  var button = video.parentElement.querySelector('.video-play');
  if (!button) return;

  video.controls = false;
  button.hidden = false;

  button.addEventListener('click', function () {
    button.hidden = true;
    video.controls = true;
    video.muted = true;
    var played = video.play();
    if (played && played.catch) {
      played.catch(function () { button.hidden = false; });
    }
    video.focus();
  });

  video.addEventListener('ended', function () {
    video.controls = false;
    video.currentTime = 0;
    video.load();          // back to the poster
    button.hidden = false;
    button.textContent = '';
    button.insertAdjacentHTML('beforeend',
      '<svg aria-hidden="true" viewBox="0 0 20 20" fill="currentColor"><path d="M6 4.2v11.6a.8.8 0 0 0 1.2.7l9.4-5.8a.8.8 0 0 0 0-1.4L7.2 3.5A.8.8 0 0 0 6 4.2Z"/></svg>Play again');
    button.focus();
  });
});
