const minAmountRange = document.getElementById("minAmountRange");
const maxAmountRange = document.getElementById("maxAmountRange");
const minAmount = document.getElementById("minAmount");
const maxAmount = document.getElementById("maxAmount");
const thumbLeft = document.querySelector(".slider-a > .thumb.left");
const thumbRight = document.querySelector(".slider-a > .thumb.right");
const range = document.querySelector(".slider-a > .range");

function setMinValue() {
  let _this = minAmountRange,
    min = parseInt(_this.min),
    max = parseInt(_this.max);

  _this.value = Math.min(
    parseInt(_this.value),
    parseInt(maxAmountRange.value) - 1
  );

  let percent = ((_this.value - min) / (max - min)) * 100;

  thumbLeft.style.left = percent + "%";
  range.style.left = percent + "%";
  minAmount.value = _this.value;
}
setMinValue();

function setMaxValue() {
  var _this = maxAmountRange,
    min = parseInt(_this.min),
    max = parseInt(_this.max);

  _this.value = Math.max(
    parseInt(_this.value),
    parseInt(minAmountRange.value) + 1
  );

  var percent = ((_this.value - min) / (max - min)) * 100;

  thumbRight.style.right = 100 - percent + "%";
  range.style.right = 100 - percent + "%";

  maxAmount.value = _this.value;
}

setMaxValue();

function controlMin(e) {
  // if (minAmount.value <= 0) {
  //   minAmount.value = 0;
  // }
  //  else if (minAmount.value >= 100000) {
  //   minAmount.value = 100000;
  // }
  minAmountRange.value = e.target.value;
  let percent =
    ((minAmountRange.value - minAmountRange.min) /
      (minAmountRange.max - minAmountRange.min)) *
    100;
  thumbLeft.style.left = percent +"%";
  range.style.left = percent + "%";
}

function controlMax(e) {
  if (maxAmount.value >= 100000) {
    maxAmount.value = 100000;
  }

  maxAmountRange.value = e.target.value;

  let percent =
    100 -
    ((maxAmountRange.value - maxAmountRange.min) /
      (maxAmountRange.max - maxAmountRange.min)) *
      100;

  thumbRight.style.right = percent + "%";
  range.style.right = percent + "%";
}

minAmountRange.addEventListener("input", setMinValue);
maxAmountRange.addEventListener("input", setMaxValue);

minAmount.addEventListener("input", controlMin);
maxAmount.addEventListener("input", controlMax);

// minAmountRange.addEventListener("mouseover", function () {
//   thumbLeft.classList.add("hover");
// });
// minAmountRange.addEventListener("mouseout", function () {
//   thumbLeft.classList.remove("hover");
// });
// minAmountRange.addEventListener("mousedown", function () {
//   thumbLeft.classList.add("active");
// });
// minAmountRange.addEventListener("mouseup", function () {
//   thumbLeft.classList.remove("active");
// });

// maxAmountRange.addEventListener("mouseover", function () {
//   thumbRight.classList.add("hover");
// });
// maxAmountRange.addEventListener("mouseout", function () {
//   thumbRight.classList.remove("hover");
// });
// maxAmountRange.addEventListener("mousedown", function () {
//   thumbRight.classList.add("active");
// });
// maxAmountRange.addEventListener("mouseup", function () {
//   thumbRight.classList.remove("active");
// });
