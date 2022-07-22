const text_nodes = document.querySelectorAll(".g-pages-component-element-content-text p");

let max = 350;
const { dot, indentation, space } = {
  dot: ".",
  indentation: "\n",
  space: " "
}

const texts = [...text_nodes].map(node => node.innerText);

const returnStr = (arr) => {
  const lastString = arr[arr.length - 1];

  return lastString;
}

const isIndentation = (strArr, nextStrArr) => {
  const prev = returnStr(strArr)
  const next = returnStr(nextStrArr)

  return !!(prev === indentation && next && indentation);
}

const textInner = (text, index, sliced = text) => {
  text = sliced

  text_nodes[index].innerHTML = text
}

const endOfSentence = (text, index) => {
  const slicedText = text.slice(0, max)
  const slicedNext = text.slice(0, max + 1)

  const strArr = slicedText.split("")
  const nextStrArr = slicedNext.split("")
  
  const lastStr = returnStr(strArr)
  
  if (lastStr === dot || isIndentation(strArr, nextStrArr)) {
    textInner(text, index, slicedText)
  } else {
    max++
    init()
  }
}

const init = () => texts.forEach((text, index) => {
  const length = text.length;

  if (length > max) {
    endOfSentence(text, index)
  } else {
    textInner(text, index)
  }
})

init()