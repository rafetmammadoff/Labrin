//uses classList, setAttribute, and querySelectorAll
//if you want this to work in IE8/9 youll need to polyfill these
(function () {
	// navtab
	let navtab = document.getElementById('nav-tab')
	fetch('https://azeristudent.az/faqapi/question-type/').then(res => res.json()).then(data => data.map((item, index) => {
		navtab.innerHTML += `
		<li><label for="tab${index + 1}" role="button"><span><a class="nav-item nav-link"  id="tab-${index + 1}"  aria-controls="nav-${index + 1}"><i class='${item.questionicon}'></i>${item.faqfor}</a></span></label></li>
		`;
		//An event to handle tab content data when the links are clicked
	})).then(() => {
		const navLinks = document.querySelectorAll(".nav-link");
		navLinks.forEach(navLink => {
			navLink.addEventListener("click", () => {
				const linkId = navLink.id.split("-")[1];
				document.querySelector(`#tab${linkId}`).checked = true;
			});
		})
	})

	// navitems
	// for couting accordions
	let counter = [1, 1, 1, 1, 1]
	fetch('https://azeristudent.az/faqapi/questions/').then(res => res.json()).then(data => data.map(item => {
		let needed = document.getElementById(`nav-${item.faqfor.id}`);
		needed.innerHTML += (`
	<dt>
		<a href="#accordion${counter[item.faqfor.id]}" aria-expanded="false" aria-controls="accordion${counter[item.faqfor.id]}" class="accordion-title accordionTitle js-accordionTrigger">
		${item.question_content}</a>
  	</dt>
  	<dd class="accordion-content accordionItem is-collapsed" id="accordion${counter[item.faqfor.id]}" aria-hidden="true">
		<p>${item.answer}</p>
	  </dd>`)
		counter[item.faqfor.id]++
	}))

	setTimeout(() => {
		var d = document,
			accordionToggles = d.querySelectorAll('.js-accordionTrigger'),
			setAria,
			setAccordionAria,
			switchAccordion,
			touchSupported = ('ontouchstart' in window),
			pointerSupported = ('pointerdown' in window);

		skipClickDelay = function (e) {
			e.preventDefault();
			e.target.click();
		}

		setAriaAttr = function (el, ariaType, newProperty) {
			el.setAttribute(ariaType, newProperty);
		};
		setAccordionAria = function (el1, el2, expanded) {
			switch (expanded) {
				case "true":
					setAriaAttr(el1, 'aria-expanded', 'true');
					setAriaAttr(el2, 'aria-hidden', 'false');
					break;
				case "false":
					setAriaAttr(el1, 'aria-expanded', 'false');
					setAriaAttr(el2, 'aria-hidden', 'true');
					break;
				default:
					break;
			}
		};
		//function
		switchAccordion = function (e) {
			console.log("triggered");
			e.preventDefault();
			var thisAnswer = e.target.parentNode.nextElementSibling;
			var thisQuestion = e.target;
			if (thisAnswer.classList.contains('is-collapsed')) {
				setAccordionAria(thisQuestion, thisAnswer, 'true');
			} else {
				setAccordionAria(thisQuestion, thisAnswer, 'false');
			}
			thisQuestion.classList.toggle('is-collapsed');
			thisQuestion.classList.toggle('is-expanded');
			thisAnswer.classList.toggle('is-collapsed');
			thisAnswer.classList.toggle('is-expanded');

			thisAnswer.classList.toggle('animateIn');
		};
		for (var i = 0, len = accordionToggles.length; i < len; i++) {
			if (touchSupported) {
				accordionToggles[i].addEventListener('touchstart', skipClickDelay, false);
			}
			if (pointerSupported) {
				accordionToggles[i].addEventListener('pointerdown', skipClickDelay, false);
			}
			accordionToggles[i].addEventListener('click', switchAccordion, false);
		}
	}, 1000)
})();

