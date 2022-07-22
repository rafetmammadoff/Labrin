const related_label = document.querySelectorAll(".related-label"),
  target_field = document.querySelectorAll(".target-field"),
  events = ["focus", "blur"];


const animateLabel = (field, index, type) => {
  const label = related_label[index];
  const value = field.value;
  switch (type) {
    case "focus":
      if (!label.classList.contains("active")) {
        label.classList.add("active");
      }
      break;
    case "blur":
      if (value !== "" && !label.classList.contains("active")) {
        label.classList.add("active");
      } else if (value === "") {
        label.classList.remove("active");
      }
      break;
  }
};

const initAnimation = () => [...target_field].forEach((field, index) => {
  events.forEach(event => {
    field.addEventListener(event, () => animateLabel(field, index, event))
  })
})

window.onload = initAnimation()
