const language_dropdown = document.querySelector(".language-dropdown"),
  language_dropdown_btn = language_dropdown.querySelector(".btn"),
  langauge_options = language_dropdown.querySelectorAll(".dropdown-menu a"),

  addClassToSelected = (option, lang) => {
    if (option.dataset['lang'] === lang) {
      option.classList.add("active");
    }
  },
  setSelectedLanguage = (option) => {
    const language = getCookie("language") || langauge_options[0].dataset["lang"];

    language_dropdown_btn.innerHTML = language;
    addClassToSelected(option, language)
  },

  changeLanguage = (e, option, lang) => {
    e.preventDefault();

    createCookie("language", lang, 20);
    setSelectedLanguage(option, lang)

    window.location.reload();
  },

  initLanguage = () => [...langauge_options].forEach(option => {
    const lang = option.dataset['lang'];

    option.addEventListener("click", (e) => changeLanguage(e, option, lang))
    setSelectedLanguage(option, lang)
  })

initLanguage()
