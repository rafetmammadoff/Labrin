// OPEN NAVBAR
document.querySelector(".navbar-toggler").onclick = function () {
    document.querySelector(".navbar nav").classList.toggle("active")
    this.classList.toggle("active")
    document.body.classList.toggle("active")
    window.scrollTo(0, 0)
}

document.querySelectorAll("header nav li a").forEach((item) => {
    item.onclick = () => {
        if (window.innerWidth < 1200) {
            document.querySelector(".navbar-toggler").click()
        }
    }
})



// TAB
function openInvestorTab(evt, index) {
    var i, tabcontent, tablinks;
  
    tabcontent = document.querySelectorAll("#investors .section-content");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    tablinks = document.querySelectorAll("#investors .tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    document.getElementById(index).style.display = "flex";
    evt.currentTarget.className += " active";

  }
  document.getElementById("investor-active-tab").click();









  
  function openInnovationTab(evt, index, imgindex) {
    var i, tabcontent, tablinks, tabImgs;
  
    tabcontent = document.querySelectorAll("#innovation-programs .section-content");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    tablinks = document.querySelectorAll("#innovation-programs .tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    tabImgs = document.querySelectorAll("#innovation-programs .innovation-tab-img");

    console.log(tabImgs)

    for (i = 0; i < tabImgs.length; i++) {
      tabImgs[i].style.display = "none";
    }

    document.getElementById(index).style.display = "flex";
    document.getElementById(imgindex).style.display = "flex";
    evt.currentTarget.className += " active";

  }
  
  document.getElementById("innovation-active-tab").click();


