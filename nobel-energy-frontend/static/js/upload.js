const upload_fields = document.querySelectorAll(".g-upload input"),
  upload_labels = document.querySelectorAll(".g-upload__label"),

  showUploadFile = (field, i) => {
    const file = field.files[0],
      name = file.name;

    upload_labels[i].innerHTML = name;
    upload_labels[i].style.color = "#2f2f30";
  };

[...upload_fields].forEach((field, i) => {
  field.addEventListener("input", () => showUploadFile(field, i))
})
