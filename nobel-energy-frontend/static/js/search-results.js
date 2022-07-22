const result_keyword = document.querySelector("[result-keyword]"),
  search_results = document.querySelectorAll("[search-result]"),

  keyword = result_keyword.textContent.toLowerCase(),
  results = [...search_results],

  regex = new RegExp(keyword),

  initSearch = () => results.forEach(result_w => {
    const str = result_w.textContent.toLowerCase()
    const result = [];

    const index = str.search(regex)

    result_w.innerHTML = "..." + str.slice(index, 180);

  });

initSearch();