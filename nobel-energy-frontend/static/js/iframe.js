const tag = document.createElement('script');
const play_btn = document.getElementById("play-video");
const thumbnail = document.querySelector(".presentation-section__video");
const player = document.getElementById("player");
const iframe = player.querySelector("iframe")

tag.src = "https://www.youtube.com/iframe_api";
const firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

play_btn.addEventListener("click", () => {
  thumbnail.style.background = "none";
  player.classList.remove("hidden");
  play_btn.classList.add("hidden");
  iframe.src += "?autoplay=1";
})
