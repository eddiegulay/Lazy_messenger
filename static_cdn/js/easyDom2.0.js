/**************************************************************************************
 * file name: easyDom.js
 * creator: edgar gulay
 * description: Js file containing a list of functions to reduce redundant code writing
 ***************************************************************************************/

/****console manipulation****/

//show text on console
function consolePrint(msg) {
    console.log(msg);
}
//display error in console
function consoleError(errorTitle, errorMessage) {
    console.error(errorTitle + ":", errorMessage);
}
//display warning in console
function consoleWarn(warnTitle, warnMessage) {
    console.warn(warnTitle + ":", warnMessage);
}

/****DOM manipulation****/

//get elements
function getById(id) {
    return document.getElementById(id);
}
function getByClass(className) {
    return document.getElementsByClassName(className);
}
function getByName(name) {
    return document.getElementsByName(name);
}
function getByTag(tagName) {
    return document.getElementsByTagName(tagName);
}

//window manipulation
//page dimension 
function innerwidth() {
    return window.innerWidth;
}
function outerwidth() {
    return window.outerWidth;
}
function innerheight() {
    return window.innerHeight;
}
function outerheight() {
    return window.outerHeight;
}

//window information
function vendor() {
    return navigator.vendor;
}
function appVersion() {
    return navigator.appVersion;
}
function currentLanguage() {
    return navigator.language;
}
//document information
//get document information
var doc = {
    getTitle: function () { return document.title },
    getHost: function () { return document.location.host },
    getUrl: function () { return document.location.href },
    getProtocal: function () { return document.location.protocol },
    getPath: function () { return document.location.pathname }
};

//getting time and date
var date = new Date;
window.setInterval(function(){date = new Date;}, 1000);//update time
var time = {
    hour: function () { return date.getHours() },
    minute: function () { return date.getMinutes() },
    second: function () { return date.getSeconds() },
    milisecond: function () { return date.getMilliseconds() },
    date: function () { return date.getDate() },
    month: function () { return date.getMonth() },
    year: function () { return date.getFullYear() },
    day: function () {
        switch (date.getDay()) {
            case 0:
                return "Sunday";
                break;
            case 1:
                return "Monday";
                break;
            case 2:
                return "Tuesday";
                break;
            case 3:
                return "wednesday";
                break;
            case 4:
                return "Thursday";
                break;
            case 5:
                return "Friday";
                break;
            case 6:
                return "Saturday";
                break;
        }
    },
    timezone: function () { return date.getTimezoneOffset() }

};
//set document information
var docSet = {
    setTitle: function (title) { document.title = title },
    setUrl: function (url) { document.location.href = url },
    newPage: function (url) { document.open(url) }
}

//element manipulation

//manipulation element attributes
function newAttribute(element, attributeName, attributeValue) {
    element.setAttribute(attributeName, attributeValue);
}
function removeAttribute(element, attributeName) {
    element.removeAttribute(attributeName);
}

function addClass(element, newClassName) {
    element.classList.add(newClassName);
}
function removeClass(element, oldClassName) {
    element.classList.remove(oldClassName);
}
function classToggle(element, classToken) {
    element.classList.toggle(classToken);
}
function containClassName(element, requiredClassName) {
    var isFound = false;
    for (var i = 0; i < element.classList.length; i++) {
        if (requiredClassName == element.classList[i]) {
            isFound = true;
            break;
        } else {
            continue;
        }
    }
    return isFound;
}

//create an element
function newChild(base_parent, elementTag, newChildId, newChildClassList, attributeName, attributeValue) {
    var element = document.createElement(elementTag);
    base_parent.append(element);
    if (newChildId != undefined) {
        element.id = newChildId;
    }
    if (newChildClassList != undefined) {
        element.className = newChildClassList;
    }
    if(attributeName != undefined || attributeValue != undefined){
        newAttribute(element, attributeName, attributeValue)
    }
    return element;
}
//remove child element
function removeElement(parent, child) {
    parent.removeChild(child);
}


//writing in elements
function printIn(element, text) {
    element.innerHTML = text;
}
function addPrintIn(element, text) {
    element.innerHTML += text;
}
function writeIn(element, text) {
    element.textContent = text;
}
function writeInAll(className, text) {
    var elem = getByClass(className);
    for (var i = 0; i < elem.length; i++) {
        elem[i].textContent = text;
    }
}
function addWriteInAll(className, text) {
    var elem = getByClass(className);
    for (var i = 0; i < elem.length; i++) {
        elem[i].textContent += " " + text;
    }
}
function typewriter(elementId, text, speed) {
    var pad = getById(elementId), i = 0;
    var interval = window.setInterval(function () {
        pad.textContent += text.charAt(i);
        i++;
        if (i >= text.lenght) {
            clearInterval(interval);
        }
    }, speed)

}

/***w3 slideshow modified to fit one use***/
function showSlides() {
    var slides = getByClass('status')
    var i;
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}
    slides[slideIndex-1].style.display = "block";
    setTimeout(showSlides, 5000); // Change image every 2 seconds
}