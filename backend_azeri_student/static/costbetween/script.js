// window.addEventListener('DOMContentLoaded', () => {
// 	new dualRangeSlider(document.querySelector(".dual-range"))
// })






// class dualRangeSlider {
// 	constructor(rangeElement) {
// 		this.range = rangeElement
// 		this.min = Number(rangeElement.dataset.min)
// 		this.max = Number(rangeElement.dataset.max)
// 		this.handles = [...this.range.querySelectorAll(".handle")]
// 		this.startPos = 0;
// 		this.activeHandle;
		
// 		this.handles.forEach(handle => {
// 			handle.addEventListener("mousedown", this.startMove.bind(this))
// 			handle.addEventListener("touchstart", this.startMoveTouch.bind(this))
// 		})
		
// 		window.addEventListener("mouseup", this.stopMove.bind(this))
// 		window.addEventListener("touchend", this.stopMove.bind(this))
// 		window.addEventListener("touchcancel", this.stopMove.bind(this))
// 		window.addEventListener("touchleave", this.stopMove.bind(this))
		
// 		const rangeRect = this.range.getBoundingClientRect();
// 		const handleRect = this.handles[0].getBoundingClientRect()
// 		this.range.style.setProperty("--x-1", "0px");
// 		this.range.style.setProperty("--x-2", rangeRect.width - handleRect.width/2 + "px");
// 		// this.handles[0].dataset.value = this.range.dataset.min;
// 		// this.handles[1].dataset.value = this.range.dataset.max;
// 	}
	
// 	startMoveTouch(e) {
// 		const handleRect = e.target.getBoundingClientRect()
// 		this.startPos = e.touches[0].clientX - handleRect.x;
// 		this.activeHandle = e.target;
// 		this.moveTouchListener = this.moveTouch.bind(this)
// 		window.addEventListener("touchmove", this.moveTouchListener);
// 	}
	
// 	startMove(e) {
// 		this.startPos = e.offsetX;
// 		this.activeHandle = e.target;
// 		this.moveListener = this.move.bind(this)
// 		window.addEventListener("mousemove", this.moveListener);
// 	}
	
// 	moveTouch(e) {
// 		this.move({clientX: e.touches[0].clientX})
// 	}
	
// 	move(e) {
// 		const isLeft = this.activeHandle.classList.contains("left")
// 		const property = isLeft ? "--x-1" : "--x-2";
// 		const parentRect = this.range.getBoundingClientRect();
// 		const handleRect = this.activeHandle.getBoundingClientRect();
// 		let newX = e.clientX - parentRect.x - this.startPos;
// 		if(isLeft) {
// 			const otherX = parseInt(this.range.style.getPropertyValue("--x-2"));
// 			newX = Math.min(newX, otherX - handleRect.width)
// 			newX = Math.max(newX, 0 - handleRect.width/2)
// 		} else {
// 			const otherX = parseInt(this.range.style.getPropertyValue("--x-1"));
// 			newX = Math.max(newX, otherX + handleRect.width)
// 			newX = Math.min(newX, parentRect.width - handleRect.width/2)
// 		}
// 		// this.activeHandle.dataset.value = this.calcHandleValue((newX + handleRect.width/2) / parentRect.width)
// 		this.range.style.setProperty(property, newX + "px");

// 	}
	
// 	calcHandleValue(percentage) {
// 		return Math.round(percentage * (this.max - this.min) + this.min)
// 	}
	
// 	stopMove() {
// 		window.removeEventListener("mousemove", this.moveListener);
// 		window.removeEventListener("touchmove", this.moveTouchListener);
// 	}
// }



(function() {
	const parent = document.querySelector('.range-slider');

	if (!parent) {
		return;
	}

	const rangeS = parent.querySelectorAll('input[type="range"]'),
	      numberS = parent.querySelectorAll('input[type="number"]');

	rangeS.forEach((el) => {
		el.oninput = () => {
			let slide1 = parseFloat(rangeS[0].value),
				slide2 = parseFloat(rangeS[1].value);

			if (slide1 > slide2) {
				[slide1, slide2] = [slide2, slide1];
			}

			numberS[0].value = slide1;
			numberS[1].value = slide2;
		}
	});

	numberS.forEach((el) => {
		el.oninput = () => {
			let number1 = parseFloat(numberS[0].value),
				number2 = parseFloat(numberS[1].value);

			if (number1 > number2) {
				let tmp = number1;
				numberS[0].value = number2;
				numberS[1].value = tmp;
			}

			rangeS[0].value = number1;
			rangeS[1].value = number2;
		}
	});
})();


function updateSymbol(e) {
	var selected = $(".currency-selector option:selected");
	$(".currency-symbol").text(selected.data("symbol"));
	$(".currency-amount").prop("placeholder", selected.data("placeholder"));
	$('.currency-addon-fixed').text(selected.text());
  }
  
  $(".currency-selector").on("change", updateSymbol);
  
  updateSymbol();

