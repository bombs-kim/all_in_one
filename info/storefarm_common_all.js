// Mozilla?
function am3(a, b, c, d, e, f) {
    var g = b & 16383,
        h = b >> 14;
    while (--f >= 0) {
        var i = this[a] & 16383;
        var j = this[a++] >> 14;
        var k = h * i + j * g;
        i = g * i + ((k & 16383) << 14) + c[d] + e;
        e = (i >> 28) + (k >> 14) + h * j;
        c[d++] = i & 268435455
    }
    return e
}

dbits = 28
BigInteger.prototype.am = am3;


function $() {
    var a = [];
    for (var b = 0; b < arguments.length; b++) {
        if (typeof arguments[b] == "string") {
            a[a.length] = document.getElementById(arguments[b]);
        } else {
            a[a.length] = arguments[b];
        }
    }
    return a[1] ? a : a[0];
}
// function resizePopup(w,h) {
// 	try {
// 		document.body.style.overflow='hidden';
// 		var clintAgent = navigator.userAgent;
//
// 		if ( clintAgent.indexOf("MSIE") != -1 ) {
// 			addheight = 50;
// 			if ( clintAgent.indexOf("MSIE 7") != -1 ) {
// 				addheight = 70;
// 			} else if ( clintAgent.indexOf("MSIE 8") != -1 ) {
// 				addheight = 80;
// 			} else if ( clintAgent.indexOf("MSIE 9") != -1 ) {
// 			}
// 			window.resizeTo(w, h+addheight);
// 		}
// 		else if(clintAgent.indexOf("Chrome") != -1 )
// 		{
// 			window.resizeTo(w, h+60);
// 		}
// 		else
// 		{
// 			window.resizeBy(w-window.innerWidth, h-window.innerHeight);
// 		}
// 	} catch (e) {
// 	}
// }
// function viewKeyboard()
// {
// 	var e = $('view_keyboard');
// 	if(e.className.indexOf(" btn_key_up") == -1) {
// 		e.className = "sp btn_key_up";
// 		e.innerHTML = pc_keyboard_close;
// 		show('keyboard_img');
// 	} else {
// 		e.className = "sp btn_key_down";
// 		hide('keyboard_img');
// 		e.innerHTML = pc_keyboard_open;
// 	}
// }
// function switchkeyboard()
// {
// 	var e = $('keyboard_img');
// 	var f = $('keyboard_switch');
// 	if(e.className.indexOf(" key_symbol") == -1) {
// 		e.className = "key key_symbol";
// 		f.className = "sp btn_symbol";
// 		f.innerHTML = view_char;
// 	} else {
// 		e.className = "key key_char";
// 		f.className = "sp btn_char";
// 		f.innerHTML = view_symbol;
// 	}
// }
// function switchlocale2(locale)
// {
// 	try {
// 	$("encpw").value="";
// 	$("encnm").value="";
// 	$("id").value="";
// 	$("pw").value="";
// 	}catch (e){}
// 	try {
// 	$("otp").value="";
// 	}catch (e){}
// 	$('locale').value = locale;
// 	$('localechange').value = "true";
// 	$("frmNIDLogin").submit();
// }
// function switchlocale()
// {
// 	try {
// 	$("encpw").value="";
// 	$("encnm").value="";
// 	$("id").value="";
// 	$("pw").value="";
// 	}catch (e){}
// 	try {
// 	$("otp").value="";
// 	}catch (e){}
// 	$('locale').value = $('locale_switch').value;
// 	$('localechange').value = "true";
// 	$("frmNIDLogin").submit();
// }
// function normal()
// {
// 	$("disposable_num").value="";
// 	$('mode').value = "";
// 	$("frmNIDLogin").submit();
// }
// function onetime()
// {
// 	$("encpw").value="";
// 	$("encnm").value="";
// 	$("id").value="";
// 	$("pw").value="";
// 	if ($("frmNIDLogin").action.indexOf("?")!=-1)
// 	{
// 		$("frmNIDLogin").action=$("frmNIDLogin").action+"&mode=number";
// 	}
// 	else
// 	{
// 		$("frmNIDLogin").action=$("frmNIDLogin").action+"?mode=number";
// 	}
// 	//$('mode').value = "number";
// 	$("frmNIDLogin").submit();
// }
// function show(id) {
// 	var e = $(id);
// 	if (e != null) {
// 		e.style.display = "block";
// 	}
// }
// function hide(id) {
// 	var e = $(id);
// 	if (e != null) {
// 		e.style.display = "none";
// 	}
// }
// function _addEvent(element, eventName, func) {
// 	if(element.attachEvent) {
// 		element.attachEvent("on" + eventName, func);
// 	} else if (element.addEventListener) {
// 		element.addEventListener(eventName, func, false);
// 	}
// }
// function _addInputEvent(elementId, setToFocusFunc, unsetToFocusFunc){
// 	var element = $(elementId);
// 	_addEvent(element, "focus", setToFocusFunc);
// 	_addEvent(element, "blur", unsetToFocusFunc);
// }
// function addInputEvent(inputId, borderId) {
// 	_addInputEvent(inputId, function(){borderOn(inputId,borderId);}, function(){borderOff(inputId,borderId);});
// }
// function addDeleteButtonEvent(inputId, buttonId) {
// 	var input = $(inputId);
// 	if (input == null) {
// 		return;
// 	}
// 	var button = $(buttonId);
//
// 	var buttonEnableEvent = function() {
// 		if(input.value != "") {
// 			button.style.display = "block";
// 		} else {
// 			button.style.display = "none";
// 		}
// 	};
//
// 	var buttonClickEvent = function() {
// 		input.value = "";
// 		buttonEnableEvent();
// 	};
//
// 	_addEvent(input, "input", buttonEnableEvent);
// 	_addEvent(input, "focus", buttonEnableEvent);
// 	_addEvent(input, "blur", buttonEnableEvent);
// 	_addEvent(button, "touchstart", buttonClickEvent);
//
// 	buttonEnableEvent();
// }
// function msieblur(a)
// {
//  	if (navigator.userAgent.indexOf("MSIE") != -1) {
//  		try{
//  			a.blur();
//  		}catch(e){}
//  	}
// }
// function borderOn(inputId,id) {
// 	var e = $(id);
// 	if (e.className.indexOf(" focus") == -1) {
// 		e.className = e.className + " focus";
// 	}
// 	try{
// 	hide('label_'+id);
// 	}catch(e){}
// }
// function borderOff(inputId,id) {
// 	var e = $(id);
// 	var f = $(inputId);
// 	e.className = e.className.replace(" focus", "");
// 	try{
// 	if (f.value.length==0){
// 		show('label_'+id);
// 	}
// 	}catch(e){}
// }
// function confirmSubmit() {
// 	var id = $("id");
// 	var pw = $("pw");
// 	var encpw = $("encpw");
//
// 	//if(id.value == "" && encpw.value == "") {
// 	if(id.value == "") {
// 		show("err_empty_id");
// 		hide("err_empty_pw");
// 		hide("err_common");
// 		id.focus();
// 		return false;
// 	//} else if(pw.value == "" && encpw.value == "") {
// 	} else if(pw.value == "") {
// 		hide("err_empty_id");
// 		show("err_empty_pw");
// 		hide("err_common");
// 		pw.focus();
// 		return false;
// 	}
// 	try{
// 		$("ls").value = localStorage.getItem("nid_t");
// 	}catch(e){}
//
// 	return encryptIdPw();
// }
// function encryptIdPw() {
// 	var id = $("id");
// 	var pw = $("pw");
// 	var encpw = $("encpw");
// 	var rsa = new RSAKey;
//
// 	if (keySplit(session_keys)) {
// 		rsa.setPublic(evalue, nvalue);
// 		try{
// 			encpw.value = rsa.encrypt(
// 				getLenChar(sessionkey) + sessionkey +
// 				getLenChar(id.value) + id.value +
// 				getLenChar(pw.value) + pw.value);
// 		} catch(e) {
// 			return false;
// 		}
// 		$('enctp').value = 1;
// 		id.value = "";
// 		pw.value = "";
// 		return true;
// 	}
// 	else
// 	{
// 		getKeyByRuntimeInclude();
// 		return false;
// 	}
//
// 	return false;
// }
// function getKeyByRuntimeInclude() {
// 	try {
// 		var keyjs  = document.createElement('script');
// 		keyjs.type = 'text/javascript';
// 		keyjs.src = '/login/ext/keys_js2.nhn';
// 		document.getElementsByTagName('head')[0].appendChild(keyjs);
// 	} catch (e) {
// 	}
// }
function clearErrorLayers() {
  var errors = new Array('err_empty_captcha', 'err_autologin', 'err_network_delay',
		'err_unsupport_browser', 'err_empty_id', 'err_empty_pw', 'err_idpw_incorrect', 'err_grpidpw_incorrect');

	for (var error in errors) {
		e = $(error);
		if (e != null) {
			e.style.display = "none";
		}
	}
}
function keySplit(a) {
	keys = a.split(",");
	if (!a || !keys[0] || !keys[1] || !keys[2] || !keys[3]) {
		return false;
	}
	sessionkey = keys[0];
	keyname = keys[1];
	evalue = keys[2];
	nvalue = keys[3];
	$("encnm").value = keyname;
	return true
}
function getLenChar(a) {
    a = a + "";
    return String.fromCharCode(a.length)
}
// function respSelect()
// {
// 	var chk = $("login_chk");
// 	if (chk == null) {
// 		return;
// 	}
//
// 	if( chk.checked == true ) {
// 		document.getElementById("resp").value = "";
// 	} else {
// 		document.getElementById("resp").value = "8";
// 	}
// }
// function nclk(name, obj, event) {
//     if (name == "") {
//         return;
//     }
//     try {
//         clickcr(obj,name,'','',event);
//     } catch(e) {
//     }
// }
// function nclk_clsnm(id, className, name, elseName, obj, event) {
//     nclk_if(className == $(id).className, name, elseName, obj, event);
// }
// function nclk_chk(id, name, elseName, obj, event) {
//     nclk_if($(id).checked, name, elseName, obj, event);
// }
// function nclk_if(success, name, elseName, obj, event) {
//     try {
//         if (success) {
//             nclk(name, obj, event);
//         } else {
//             nclk(elseName, obj, event);
//         }
//     } catch(e) {
//     }
// }
// var getkeyurl = '/login/ext/keys.nhn';
// var curtimecheck = 0;
// function getKeysv2() {
// 	var curtimes = new Date();
// 	if (curtimecheck == 0) {
// 		getAjaxResult(getkeyurl);
// 		curtimecheck = curtimes.getTime();
// 	} else if (curtimes.getTime() - curtimecheck > 60000) {
// 		curtimecheck = curtimes.getTime();
// 		getAjaxResult(getkeyurl);
// 	}
// }
// function getAjaxResult(urls) {
// 	try {
// 		var xmlhttp = getXmlHttp();
// 		xmlhttp.open("GET", urls);
// 		xmlhttp.onreadystatechange = function() {
// 			if (xmlhttp.readyState == 4) {
// 				session_keys = xmlhttp.responseText
// 			}
// 		}
// 		xmlhttp.send(null);
// 	} catch (e) {
// 		if (window.bridgeGotTime) {
// 			throw e;
// 		} else {
// 			// page reload?
// 		}
// 	}
// }
// function getXmlHttp() {
// 	var xmlhttp;
// 	try {
// 		xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");
// 	} catch (e) {
// 		try {
// 			xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
// 		} catch (E) {
// 			xmlhttp = false;
// 		}
// 	}
// 	if (!xmlhttp && typeof XMLHttpRequest != 'undefined') {
// 		xmlhttp = new XMLHttpRequest();
// 	}
// 	return xmlhttp;
// }
// function getCookie(a) {
//     var b = a + "=";
//     var c = b.length;
//     var d = document.cookie.length;
//     var e = 0;
//     while (e < d) {
//         var f = e + c;
//         if (document.cookie.substring(e, f) == b) {
//             var g = document.cookie.indexOf(";", f);
//             if (g == -1) g = document.cookie.length;
//             return unescape(document.cookie.substring(f, g))
//         }
//         e = document.cookie.indexOf(" ", e) + 1;
//         if (e == 0) break
//     }
//     return null
// }
// function savedLong(a) {
// 	var nvlong = $("login_chk");
// 	var label_nvlong = $("label_login_chk");
// 	if (a.checked == true) {
// 		nvlong.value='on';
// 		try{
// 		label_nvlong.className="sp on";
// 		}catch(e){}
// 		ipCheckOff();
// 	}
// 	else
// 	{
// 		nvlong.value='off';
// 		try{
// 		label_nvlong.className="sp";
// 		}catch(e){}
// 	}
// }
// function ipCheckOff() {
// 	var label_check = $("label_ip_on");
// 	var check = $("ip_on");
// 	if (check != null) {
// 		check.checked = false;
// 		label_check.className="sp";
// 	}
// 	setSmartLevel(-1);
// }
// function ipCheckOn(level) {
// 	var label_check = $("label_ip_on");
// 	var check = $("ip_on");
// 	if (check != null) {
// 		check.checked = true;
// 		label_check.className="sp on";
// 	}
// 	setSmartLevel(level);
// }
// function setSmartLevel(level) {
// 	try {
// 	$('smart_LEVEL').value = level;
// 	} catch(e) {}
// 	try {
// 	$('smart_LEVEL').value = level;
// 	} catch(e) {}
// 	var today = new Date();
// 	var expire = new Date(today.getTime() + 60 * 60 * 24 * 365 * 1000);
// 	var curCookie = "nid_slevel=" + escape(level) + "; expires="
// 			+ expire.toGMTString() + "; path=/; domain=.nid.naver.com;";
// 	document.cookie = curCookie;
// }
// function initSmartLevel()
// {
// 	smart_level = getCookie("nid_slevel") ? getCookie("nid_slevel") : 1;
// 	try{
// 	$('smart_level').value = smart_level;
// 	}catch (e){}
// 	try{
// 	$('smart_LEVEL').value = smart_level;
// 	}catch (e){}
// 	try{
// 	if (smart_level > 0) {
// 		ipCheckOn(smart_level);
// 	} else {
// 		ipCheckOff();
// 	}
// 	}catch(e){}
// }
// function ipCheck(a,e) {
// 	var check = $("label_ip_on");
// 	if (a.checked == true) {
// 		try{
// 		ipCheckOn(1);
// 		}catch(e){}
// 	} else {
// 		try{
// 		ipCheckOff();
// 		}catch(e){}
// 	}
// }
// var isshift = false;
// var userStrokes = false;
// function checkShiftUp(e) {
// 	if (e.which && e.which == 16) {
// 		isshift = false;
// 	}
// }
// function checkShiftDown(e) {
// 	var down_keyCode=0;
// 	if (e.which && e.which == 16) {
// 		isshift = true;
// 	}
// 	if (window.event) {
// 		down_keyCode = e.keyCode;
// 	}
// 	else if (e.which) {
// 		down_keyCode = e.which;
// 	}
//
// 	if (down_keyCode && down_keyCode == 20) {
// 		if (!is_capslockon)
// 		{
// 			is_capslockon=true;
// 			show('err_capslock');
// 			setTimeout("hide('err_capslock')",1500);
// 		}
// 		else
// 		{
// 			is_capslockon=false;
// 			hide('err_capslock');
// 		}
// 	}
// }
// var is_capslockon=false;
// function checkEnt(e) {
// 	if (window.event) { // IE
// 		myKeyCode = e.keyCode;
// 		myShiftKey = e.shiftKey;
// 	} else if (e.which) { // netscape ff opera
// 		myKeyCode = e.which;
// 		myShiftKey = isshift;
// 	}
// }
// function capslockevt(e) {
// 	userStrokes = true;
// 	var myKeyCode = 0;
// 	var myShiftKey = false;
// 	if (window.event) { // IE
// 		myKeyCode = e.keyCode;
// 		myShiftKey = e.shiftKey;
// 	} else if (e.which) { // netscape ff opera
// 		myKeyCode = e.which; // myShiftKey=( myKeyCode == 16 ) ? true :
// 								// false;
// 		myShiftKey = isshift;
// 	}
// 	if ((myKeyCode >= 65 && myKeyCode <= 90) && !myShiftKey) {
// 		is_capslockon=true;
// 		show('err_capslock');
// 		setTimeout("hide('err_capslock')",3000);
// 	} else if ((myKeyCode >= 97 && myKeyCode <= 122) && myShiftKey) {
// 		is_capslockon=true;
// 		show('err_capslock');
// 		setTimeout("hide('err_capslock')",3000);
// 	} else {
// 		is_capslockon=false;
// 		setTimeout("hide('err_capslock')",1500);
// 	}
// }
function BigInteger(a, b, c) {
    if (a != null)
        if ("number" == typeof a) this.fromNumber(a, b, c);
        else if (b == null && "string" != typeof a) this.fromString(a, 256);
        else this.fromString(a, b)
}
function nbi() {
    return new BigInteger(null)
}
function am1(a, b, c, d, e, f) {
    while (--f >= 0) {
        var g = b * this[a++] + c[d] + e;
        e = Math.floor(g / 67108864);
        c[d++] = g & 67108863
    }
    return e
}
function am2(a, b, c, d, e, f) {
    var g = b & 32767,
        h = b >> 15;
    while (--f >= 0) {
        var i = this[a] & 32767;
        var j = this[a++] >> 15;
        var k = h * i + j * g;
        i = g * i + ((k & 32767) << 15) + c[d] + (e & 1073741823);
        e = (i >>> 30) + (k >>> 15) + h * j + (e >>> 30);
        c[d++] = i & 1073741823
    }
    return e
}
// // Moved to the top
// function am3(a, b, c, d, e, f) {
//     var g = b & 16383,
//         h = b >> 14;
//     while (--f >= 0) {
//         var i = this[a] & 16383;
//         var j = this[a++] >> 14;
//         var k = h * i + j * g;
//         i = g * i + ((k & 16383) << 14) + c[d] + e;
//         e = (i >> 28) + (k >> 14) + h * j;
//         c[d++] = i & 268435455
//     }
//     return e
// }
function int2char(a) {
    return BI_RM.charAt(a)
}
function intAt(a, b) {
    var c = BI_RC[a.charCodeAt(b)];
    return c == null ? -1 : c
}
function bnpCopyTo(a) {
    for (var b = this.t - 1; b >= 0; --b) a[b] = this[b];
    a.t = this.t;
    a.s = this.s
}
function bnpFromInt(a) {
    this.t = 1;
    this.s = a < 0 ? -1 : 0;
    if (a > 0) this[0] = a;
    else if (a < -1) this[0] = a + DV;
    else this.t = 0
}
function nbv(a) {
    var b = nbi();
    b.fromInt(a);
    return b
}
function bnpFromString(a, b) {
    var c;
    if (b == 16) c = 4;
    else if (b == 8) c = 3;
    else if (b == 256) c = 8;
    else if (b == 2) c = 1;
    else if (b == 32) c = 5;
    else if (b == 4) c = 2;
    else {
        this.fromRadix(a, b);
        return
    }
    this.t = 0;
    this.s = 0;
    var d = a.length,
        e = false,
        f = 0;
    while (--d >= 0) {
        var g = c == 8 ? a[d] & 255 : intAt(a, d);
        if (g < 0) {
            if (a.charAt(d) == "-") e = true;
            continue
        }
        e = false;
        if (f == 0) this[this.t++] = g;
        else if (f + c > this.DB) {
            this[this.t - 1] |= (g & (1 << this.DB - f) - 1) << f;
            this[this.t++] = g >> this.DB - f
        } else this[this.t - 1] |= g << f;
        f += c;
        if (f >= this.DB) f -= this.DB
    }
    if (c == 8 && (a[0] & 128) != 0) {
        this.s = -1;
        if (f > 0) this[this.t - 1] |= (1 << this.DB - f) - 1 << f
    }
    this.clamp();
    if (e) BigInteger.ZERO.subTo(this, this)
}
function bnpClamp() {
    var a = this.s & this.DM;
    while (this.t > 0 && this[this.t - 1] == a)--this.t
}
function bnToString(a) {
    if (this.s < 0) return "-" + this.negate().toString(a);
    var b;
    if (a == 16) b = 4;
    else if (a == 8) b = 3;
    else if (a == 2) b = 1;
    else if (a == 32) b = 5;
    else if (a == 4) b = 2;
    else return this.toRadix(a);
    var c = (1 << b) - 1,
        d, e = false,
        f = "",
        g = this.t;
    var h = this.DB - g * this.DB % b;
    if (g-- > 0) {
        if (h < this.DB && (d = this[g] >> h) > 0) {
            e = true;
            f = int2char(d)
        }
        while (g >= 0) {
            if (h < b) {
                d = (this[g] & (1 << h) - 1) << b - h;
                d |= this[--g] >> (h += this.DB - b)
            } else {
                d = this[g] >> (h -= b) & c;
                if (h <= 0) {
                    h += this.DB;
                    --g
                }
            }
            if (d > 0) e = true;
            if (e) f += int2char(d)
        }
    }
    return e ? f : "0"
}
function bnNegate() {
    var a = nbi();
    BigInteger.ZERO.subTo(this, a);
    return a
}
function bnAbs() {
    return this.s < 0 ? this.negate() : this
}
function bnCompareTo(a) {
    var b = this.s - a.s;
    if (b != 0) return b;
    var c = this.t;
    b = c - a.t;
    if (b != 0) return b;
    while (--c >= 0) if ((b = this[c] - a[c]) != 0) return b;
    return 0
}
function nbits(a) {
    var b = 1,
        c;
    if ((c = a >>> 16) != 0) {
        a = c;
        b += 16
    }
    if ((c = a >> 8) != 0) {
        a = c;
        b += 8
    }
    if ((c = a >> 4) != 0) {
        a = c;
        b += 4
    }
    if ((c = a >> 2) != 0) {
        a = c;
        b += 2
    }
    if ((c = a >> 1) != 0) {
        a = c;
        b += 1
    }
    return b
}
function bnBitLength() {
    if (this.t <= 0) return 0;
    return this.DB * (this.t - 1) + nbits(this[this.t - 1] ^ this.s & this.DM)
}
function bnpDLShiftTo(a, b) {
    var c;
    for (c = this.t - 1; c >= 0; --c) b[c + a] = this[c];
    for (c = a - 1; c >= 0; --c) b[c] = 0;
    b.t = this.t + a;
    b.s = this.s
}
function bnpDRShiftTo(a, b) {
    for (var c = a; c < this.t; ++c) b[c - a] = this[c];
    b.t = Math.max(this.t - a, 0);
    b.s = this.s
}
function bnpLShiftTo(a, b) {
    var c = a % this.DB;
    var d = this.DB - c;
    var e = (1 << d) - 1;
    var f = Math.floor(a / this.DB),
        g = this.s << c & this.DM,
        h;
    for (h = this.t - 1; h >= 0; --h) {
        b[h + f + 1] = this[h] >> d | g;
        g = (this[h] & e) << c
    }
    for (h = f - 1; h >= 0; --h) b[h] = 0;
    b[f] = g;
    b.t = this.t + f + 1;
    b.s = this.s;
    b.clamp()
}
function bnpRShiftTo(a, b) {
    b.s = this.s;
    var c = Math.floor(a / this.DB);
    if (c >= this.t) {
        b.t = 0;
        return
    }
    var d = a % this.DB;
    var e = this.DB - d;
    var f = (1 << d) - 1;
    b[0] = this[c] >> d;
    for (var g = c + 1; g < this.t; ++g) {
        b[g - c - 1] |= (this[g] & f) << e;
        b[g - c] = this[g] >> d
    }
    if (d > 0) b[this.t - c - 1] |= (this.s & f) << e;
    b.t = this.t - c;
    b.clamp()
}
function bnpSubTo(a, b) {
    var c = 0,
        d = 0,
        e = Math.min(a.t, this.t);
    while (c < e) {
        d += this[c] - a[c];
        b[c++] = d & this.DM;
        d >>= this.DB
    }
    if (a.t < this.t) {
        d -= a.s;
        while (c < this.t) {
            d += this[c];
            b[c++] = d & this.DM;
            d >>= this.DB
        }
        d += this.s
    } else {
        d += this.s;
        while (c < a.t) {
            d -= a[c];
            b[c++] = d & this.DM;
            d >>= this.DB
        }
        d -= a.s
    }
    b.s = d < 0 ? -1 : 0;
    if (d < -1) b[c++] = this.DV + d;
    else if (d > 0) b[c++] = d;
    b.t = c;
    b.clamp()
}
function bnpMultiplyTo(a, b) {
    var c = this.abs(),
        d = a.abs();
    var e = c.t;
    b.t = e + d.t;
    while (--e >= 0) b[e] = 0;
    for (e = 0; e < d.t; ++e) b[e + c.t] = c.am(0, d[e], b, e, 0, c.t);
    b.s = 0;
    b.clamp();
    if (this.s != a.s) BigInteger.ZERO.subTo(b, b)
}
function bnpSquareTo(a) {
    var b = this.abs();
    var c = a.t = 2 * b.t;
    while (--c >= 0) a[c] = 0;
    for (c = 0; c < b.t - 1; ++c) {
        var d = b.am(c, b[c], a, 2 * c, 0, 1);
        if ((a[c + b.t] += b.am(c + 1, 2 * b[c], a, 2 * c + 1, d, b.t - c - 1)) >= b.DV) {
            a[c + b.t] -= b.DV;
            a[c + b.t + 1] = 1
        }
    }
    if (a.t > 0) a[a.t - 1] += b.am(c, b[c], a, 2 * c, 0, 1);
    a.s = 0;
    a.clamp()
}
function bnpDivRemTo(a, b, c) {
    var d = a.abs();
    if (d.t <= 0) return;
    var e = this.abs();
    if (e.t < d.t) {
        if (b != null) b.fromInt(0);
        if (c != null) this.copyTo(c);
        return
    }
    if (c == null) c = nbi();
    var f = nbi(),
        g = this.s,
        h = a.s;
    var i = this.DB - nbits(d[d.t - 1]);
    if (i > 0) {
        d.lShiftTo(i, f);
        e.lShiftTo(i, c)
    } else {
        d.copyTo(f);
        e.copyTo(c)
    }
    var j = f.t;
    var k = f[j - 1];
    if (k == 0) return;
    var l = k * (1 << this.F1) + (j > 1 ? f[j - 2] >> this.F2 : 0);
    var m = this.FV / l,
        n = (1 << this.F1) / l,
        o = 1 << this.F2;
    var p = c.t,
        q = p - j,
        r = b == null ? nbi() : b;
    f.dlShiftTo(q, r);
    if (c.compareTo(r) >= 0) {
        c[c.t++] = 1;
        c.subTo(r, c)
    }
    BigInteger.ONE.dlShiftTo(j, r);
    r.subTo(f, f);
    while (f.t < j) f[f.t++] = 0;
    while (--q >= 0) {
        var s = c[--p] == k ? this.DM : Math.floor(c[p] * m + (c[p - 1] + o) * n);
        if ((c[p] += f.am(0, s, c, q, 0, j)) < s) {
            f.dlShiftTo(q, r);
            c.subTo(r, c);
            while (c[p] < --s) c.subTo(r, c)
        }
    }
    if (b != null) {
        c.drShiftTo(j, b);
        if (g != h) BigInteger.ZERO.subTo(b, b)
    }
    c.t = j;
    c.clamp();
    if (i > 0) c.rShiftTo(i, c);
    if (g < 0) BigInteger.ZERO.subTo(c, c)
}
function bnMod(a) {
    var b = nbi();
    this.abs().divRemTo(a, null, b);
    if (this.s < 0 && b.compareTo(BigInteger.ZERO) > 0) a.subTo(b, b);
    return b
}
function Classic(a) {
    this.m = a
}
function cConvert(a) {
    if (a.s < 0 || a.compareTo(this.m) >= 0) return a.mod(this.m);
    else return a
}
function cRevert(a) {
    return a
}
function cReduce(a) {
    a.divRemTo(this.m, null, a)
}
function cMulTo(a, b, c) {
    a.multiplyTo(b, c);
    this.reduce(c)
}
function cSqrTo(a, b) {
    a.squareTo(b);
    this.reduce(b)
}
function bnpInvDigit() {
    if (this.t < 1) return 0;
    var a = this[0];
    if ((a & 1) == 0) return 0;
    var b = a & 3;
    b = b * (2 - (a & 15) * b) & 15;
    b = b * (2 - (a & 255) * b) & 255;
    b = b * (2 - ((a & 65535) * b & 65535)) & 65535;
    b = b * (2 - a * b % this.DV) % this.DV;
    return b > 0 ? this.DV - b : -b
}
function Montgomery(a) {
    this.m = a;
    this.mp = a.invDigit();
    this.mpl = this.mp & 32767;
    this.mph = this.mp >> 15;
    this.um = (1 << a.DB - 15) - 1;
    this.mt2 = 2 * a.t
}
function montConvert(a) {
    var b = nbi();
    a.abs().dlShiftTo(this.m.t, b);
    b.divRemTo(this.m, null, b);
    if (a.s < 0 && b.compareTo(BigInteger.ZERO) > 0) this.m.subTo(b, b);
    return b
}
function montRevert(a) {
    var b = nbi();
    a.copyTo(b);
    this.reduce(b);
    return b
}
function montReduce(a) {
    while (a.t <= this.mt2) a[a.t++] = 0;
    for (var b = 0; b < this.m.t; ++b) {
        var c = a[b] & 32767;
        var d = c * this.mpl + ((c * this.mph + (a[b] >> 15) * this.mpl & this.um) << 15) & a.DM;
        c = b + this.m.t;
        a[c] += this.m.am(0, d, a, b, 0, this.m.t);
        while (a[c] >= a.DV) {
            a[c] -= a.DV;
            a[++c]++
        }
    }
    a.clamp();
    a.drShiftTo(this.m.t, a);
    if (a.compareTo(this.m) >= 0) a.subTo(this.m, a)
}
function montSqrTo(a, b) {
    a.squareTo(b);
    this.reduce(b)
}
function montMulTo(a, b, c) {
    a.multiplyTo(b, c);
    this.reduce(c)
}
function bnpIsEven() {
    return (this.t > 0 ? this[0] & 1 : this.s) == 0
}
function bnpExp(a, b) {
    if (a > 4294967295 || a < 1) return BigInteger.ONE;
    var c = nbi(),
        d = nbi(),
        e = b.convert(this),
        f = nbits(a) - 1;
    e.copyTo(c);
    while (--f >= 0) {
        b.sqrTo(c, d);
        if ((a & 1 << f) > 0) b.mulTo(d, e, c);
        else {
            var g = c;
            c = d;
            d = g
        }
    }
    return b.revert(c)
}
function bnModPowInt(a, b) {
    var c;
    if (a < 256 || b.isEven()) c = new Classic(b);
    else c = new Montgomery(b);
    return this.exp(a, c)
}
function Arcfour() {
    this.i = 0;
    this.j = 0;
    this.S = new Array
}
function ARC4init(a) {
    var b, c, d;
    for (b = 0; b < 256; ++b) this.S[b] = b;
    c = 0;
    for (b = 0; b < 256; ++b) {
        c = c + this.S[b] + a[b % a.length] & 255;
        d = this.S[b];
        this.S[b] = this.S[c];
        this.S[c] = d
    }
    this.i = 0;
    this.j = 0
}
function ARC4next() {
    var a;
    this.i = this.i + 1 & 255;
    this.j = this.j + this.S[this.i] & 255;
    a = this.S[this.i];
    this.S[this.i] = this.S[this.j];
    this.S[this.j] = a;
    return this.S[a + this.S[this.i] & 255]
}
function prng_newstate() {
    return new Arcfour
}
function rng_seed_int(a) {
    rng_pool[rng_pptr++] ^= a & 255;
    rng_pool[rng_pptr++] ^= a >> 8 & 255;
    rng_pool[rng_pptr++] ^= a >> 16 & 255;
    rng_pool[rng_pptr++] ^= a >> 24 & 255;
    if (rng_pptr >= rng_psize) rng_pptr -= rng_psize
}
function rng_seed_time() {
    rng_seed_int((new Date).getTime())
}
function rng_get_byte() {
    if (rng_state == null) {
        rng_seed_time();
        rng_state = prng_newstate();
        rng_state.init(rng_pool);
        for (rng_pptr = 0; rng_pptr < rng_pool.length; ++rng_pptr) rng_pool[rng_pptr] = 0;
        rng_pptr = 0
    }
    return rng_state.next()
}
function rng_get_bytes(a) {
    var b;
    for (b = 0; b < a.length; ++b) a[b] = rng_get_byte()
}
function SecureRandom() {}
function parseBigInt(a, b) {
    return new BigInteger(a, b)
}
function linebrk(a, b) {
    var c = "";
    var d = 0;
    while (d + b < a.length) {
        c += a.substring(d, d + b) + "\n";
        d += b
    }
    return c + a.substring(d, a.length)
}
function byte2Hex(a) {
    if (a < 16) return "0" + a.toString(16);
    else return a.toString(16)
}
function pkcs1pad2(a, b) {
    if (b < a.length + 11) {
        alert("Message too long for RSA");
        return null
    }
    var c = new Array;
    var d = a.length - 1;
    while (d >= 0 && b > 0) c[--b] = a.charCodeAt(d--);
    c[--b] = 0;
    // var e = new SecureRandom;
    // var f = new Array;
    // while (b > 2) {
    //     f[0] = 0;
    //     while (f[0] == 0) e.nextBytes(f);
    //     c[--b] = f[0]
    // }

    while (b > 2) {
        c[--b] = Math.floor(1 + Math.random() * 254.99);
    }

    c[--b] = 2;
    c[--b] = 0;
    return new BigInteger(c)
}
function RSAKey() {
    this.n = null;
    this.e = 0;
    this.d = null;
    this.p = null;
    this.q = null;
    this.dmp1 = null;
    this.dmq1 = null;
    this.coeff = null
}
function RSASetPublic(a, b) {
    if (a != null && b != null && a.length > 0 && b.length > 0) {
        this.n = parseBigInt(a, 16);
        this.e = parseInt(b, 16)
    } else alert("Invalid RSA public key")
}
function RSADoPublic(a) {
    return a.modPowInt(this.e, this.n)
}
function RSAEncrypt(a) {
    var b = pkcs1pad2(a, this.n.bitLength() + 7 >> 3);
    if (b == null) return null;
    var c = this.doPublic(b);
    if (c == null) return null;
    var d = c.toString(16);
    var e = (this.n.bitLength() + 7 >> 3 << 1) - d.length;
    while (e-- > 0) d = "0" + d;
    return d
}
function hex2b64(a) {
    var b;
    var c;
    var d = "";
    for (b = 0; b + 3 <= a.length; b += 3) {
        c = parseInt(a.substring(b, b + 3), 16);
        d += b64map.charAt(c >> 6) + b64map.charAt(c & 63)
    }
    if (b + 1 == a.length) {
        c = parseInt(a.substring(b, b + 1), 16);
        d += b64map.charAt(c << 2)
    } else if (b + 2 == a.length) {
        c = parseInt(a.substring(b, b + 2), 16);
        d += b64map.charAt(c >> 2) + b64map.charAt((c & 3) << 4)
    }
    while ((d.length & 3) > 0) d += b64pad;
    return d
}
function b64tohex(a) {
    var b = "";
    var c;
    var d = 0;
    var e;
    for (c = 0; c < a.length; ++c) {
        if (a.charAt(c) == b64pad) break;
        v = b64map.indexOf(a.charAt(c));
        if (v < 0) continue;
        if (d == 0) {
            b += int2char(v >> 2);
            e = v & 3;
            d = 1
        } else if (d == 1) {
            b += int2char(e << 2 | v >> 4);
            e = v & 15;
            d = 2
        } else if (d == 2) {
            b += int2char(e);
            b += int2char(v >> 2);
            e = v & 3;
            d = 3
        } else {
            b += int2char(e << 2 | v >> 4);
            b += int2char(v & 15);
            d = 0
        }
    }
    if (d == 1) b += int2char(e << 2);
    return b
}
function b64toBA(a) {
    var b = b64tohex(a);
    var c;
    var d = new Array;
    for (c = 0; 2 * c < b.length; ++c) {
        d[c] = parseInt(b.substring(2 * c, 2 * c + 2), 16)
    }
    return d
}

// var isIE = navigator.appVersion.indexOf("MSIE") != -1 ? true : false;
// var isWin = navigator.appVersion.toLowerCase().indexOf("win") != -1 ? true : false;
// var isOpera = navigator.userAgent.indexOf("Opera") != -1 ? true : false;
// var dbits;

var canary = 0xdeadbeefcafe;
var j_lm = (canary & 16777215) == 15715070;
// if (j_lm && navigator.appName == "Microsoft Internet Explorer") {
//     BigInteger.prototype.am = am2;
//     dbits = 30
// } else if (j_lm && navigator.appName != "Netscape") {
//     BigInteger.prototype.am = am1;
//     dbits = 26
// } else {
//     BigInteger.prototype.am = am3;
//     dbits = 28
// }
BigInteger.prototype.DB = dbits;
BigInteger.prototype.DM = (1 << dbits) - 1;
BigInteger.prototype.DV = 1 << dbits;
var BI_FP = 52;
BigInteger.prototype.FV = Math.pow(2, BI_FP);
BigInteger.prototype.F1 = BI_FP - dbits;
BigInteger.prototype.F2 = 2 * dbits - BI_FP;
var BI_RM = "0123456789abcdefghijklmnopqrstuvwxyz";
var BI_RC = new Array;
var rr, vv;
rr = "0".charCodeAt(0);
for (vv = 0; vv <= 9; ++vv) BI_RC[rr++] = vv;
rr = "a".charCodeAt(0);
for (vv = 10; vv < 36; ++vv) BI_RC[rr++] = vv;
rr = "A".charCodeAt(0);
for (vv = 10; vv < 36; ++vv) BI_RC[rr++] = vv;
Classic.prototype.convert = cConvert;
Classic.prototype.revert = cRevert;
Classic.prototype.reduce = cReduce;
Classic.prototype.mulTo = cMulTo;
Classic.prototype.sqrTo = cSqrTo;
Montgomery.prototype.convert = montConvert;
Montgomery.prototype.revert = montRevert;
Montgomery.prototype.reduce = montReduce;
Montgomery.prototype.mulTo = montMulTo;
Montgomery.prototype.sqrTo = montSqrTo;
BigInteger.prototype.copyTo = bnpCopyTo;
BigInteger.prototype.fromInt = bnpFromInt;
BigInteger.prototype.fromString = bnpFromString;
BigInteger.prototype.clamp = bnpClamp;
BigInteger.prototype.dlShiftTo = bnpDLShiftTo;
BigInteger.prototype.drShiftTo = bnpDRShiftTo;
BigInteger.prototype.lShiftTo = bnpLShiftTo;
BigInteger.prototype.rShiftTo = bnpRShiftTo;
BigInteger.prototype.subTo = bnpSubTo;
BigInteger.prototype.multiplyTo = bnpMultiplyTo;
BigInteger.prototype.squareTo = bnpSquareTo;
BigInteger.prototype.divRemTo = bnpDivRemTo;
BigInteger.prototype.invDigit = bnpInvDigit;
BigInteger.prototype.isEven = bnpIsEven;
BigInteger.prototype.exp = bnpExp;
BigInteger.prototype.toString = bnToString;
BigInteger.prototype.negate = bnNegate;
BigInteger.prototype.abs = bnAbs;
BigInteger.prototype.compareTo = bnCompareTo;
BigInteger.prototype.bitLength = bnBitLength;
BigInteger.prototype.mod = bnMod;
BigInteger.prototype.modPowInt = bnModPowInt;
BigInteger.ZERO = nbv(0);
BigInteger.ONE = nbv(1);
Arcfour.prototype.init = ARC4init;
Arcfour.prototype.next = ARC4next;
// var rng_psize = 256;
// var rng_state;
// var rng_pool;
// var rng_pptr;
// if (rng_pool == null) {
//     rng_pool = new Array;
//     rng_pptr = 0;
//     var t;
//     if (navigator.appName == "Netscape" && navigator.appVersion < "5" && window.crypto) {
//         var z = window.crypto.random(32);
//         for (t = 0; t < z.length; ++t) rng_pool[rng_pptr++] = z.charCodeAt(t) & 255
//     }
//     while (rng_pptr < rng_psize) {
//         t = Math.floor(65536 * Math.random());
//         rng_pool[rng_pptr++] = t >>> 8;
//         rng_pool[rng_pptr++] = t & 255
//     }
//     rng_pptr = 0;
//     rng_seed_time()
// }
// SecureRandom.prototype.nextBytes = rng_get_bytes;
RSAKey.prototype.doPublic = RSADoPublic;
RSAKey.prototype.setPublic = RSASetPublic;
RSAKey.prototype.encrypt = RSAEncrypt;
var b64map = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
var b64pad = "=";
// var lcs_isie = navigator.appName == "Microsoft Internet Explorer";
// var lcs_isns = navigator.appName == "Netscape";
// var lcs_isopera = navigator.appVersion.indexOf("Opera") >= 0;
// var lcs_ismac = navigator.userAgent.indexOf("MAC") >= 0;
// var lcs_add = {};
// var lcs_bc = {};
// var lcs_ver = "v0.4.13";
// var lcs_cnt = 0;
// var keys = null;
// var keystr = null;
// var keyname = "";
// var evalue = "";
// var nvalue = "";
// var initEnc = 1;
// var is_ipcheck = getCookie("nid_slevel") ? getCookie("nid_slevel") : "-1";
// var enctp;
// var is_sid = getCookie("nid_sid") ? true : false;
// var is_spw = getCookie("nid_spw") ? true : false;
// var is_mid = getCookie("nid_msid") == "1" ? true : false;
// var is_mpw = getCookie("nid_mspw") == "1" ? true : false;
// var browser;
//
//
// if (typeof nclk == "undefined") {
// 	nclk = {}
// }
// if (typeof nclkMaxDepth == "undefined") {
// 	var nclkMaxDepth = 8
// }
// if (typeof ccsrv == "undefined") {
// 	var ccsrv = "cc.naver.com"
// }
// if (typeof nclkModule == "undefined") {
// 	var nclkModule = "cc"
// }
// if (typeof nsc == "undefined") {
// 	var nsc = "decide.me"
// }
// if (typeof g_pid == "undefined") {
// 	var g_pid = ""
// }
// if (typeof g_sid == "undefined") {
// 	var g_sid = ""
// }
// var nclkImg = [];
// nclk.version = "1.2.12";
// nclk.getScrollBarWidth = function() {
// 	var e = document.createElement("p");
// 	e.style.width = "200px";
// 	e.style.height = "200px";
// 	var f = document.createElement("div");
// 	f.style.position = "absolute";
// 	f.style.top = "0px";
// 	f.style.left = "0px";
// 	f.style.visibility = "hidden";
// 	f.style.width = "200px";
// 	f.style.height = "150px";
// 	f.style.overflow = "hidden";
// 	f.appendChild(e);
// 	document.body.appendChild(f);
// 	var b = e.offsetWidth;
// 	f.style.overflow = "scroll";
// 	var a = e.offsetWidth;
// 	if (b == a) {
// 		a = f.clientWidth
// 	}
// 	document.body.removeChild(f);
// 	return (b - a)
// };
// nclk.findPos = function(b) {
// 	var f = curtop = 0;
// 	try {
// 		if (b.offsetParent) {
// 			do {
// 				f += b.offsetLeft;
// 				curtop += b.offsetTop
// 			} while (b = b.offsetParent)
// 		} else {
// 			if (b.x || b.y) {
// 				if (b.x) {
// 					f += b.x
// 				}
// 				if (b.y) {
// 					curtop += b.y
// 				}
// 			}
// 		}
// 	} catch (a) {
// 	}
// 	return [ f, curtop ]
// };
// nclk.windowSize = function(e) {
// 	if (!e) {
// 		e = window
// 	}
// 	var a = 0;
// 	if (e.innerWidth) {
// 		a = e.innerWidth;
// 		if (typeof (e.innerWidth) == "number") {
// 			var b = nclk.getScrollBarWidth();
// 			a = e.innerWidth - b
// 		}
// 	} else {
// 		if (document.documentElement && document.documentElement.clientWidth) {
// 			a = document.documentElement.clientWidth
// 		} else {
// 			if (document.body
// 					&& (document.body.clientWidth || document.body.clientHeight)) {
// 				a = document.body.clientWidth
// 			}
// 		}
// 	}
// 	return a
// };
// nclk.checkIframe = function(i) {
// 	var f = document.URL;
// 	var h = i.parentNode;
// 	var a;
// 	var b;
// 	if (h == null || h == undefined) {
// 		return false
// 	}
// 	while (1) {
// 		if (h.nodeName.toLowerCase() == "#document") {
// 			if (h.parentWindow) {
// 				a = h.parentWindow
// 			} else {
// 				a = h.defaultView
// 			}
// 			try {
// 				if (a.frameElement != null && a.frameElement != undefined) {
// 					if (a.frameElement.nodeName.toLowerCase() == "iframe") {
// 						b = a.frameElement.id;
// 						if (!b) {
// 							return false
// 						}
// 						return b
// 					} else {
// 						return false
// 					}
// 				} else {
// 					return false
// 				}
// 			} catch (g) {
// 				return false
// 			}
// 		} else {
// 			h = h.parentNode;
// 			if (h == null || h == undefined) {
// 				return false
// 			}
// 		}
// 	}
// };
// nclk.absPath = function(a) {
// 	var e = window.location;
// 	var f = e.href;
// 	var b = e.protocol + "//" + e.host;
// 	if (a.charAt(0) == "/") {
// 		if (a.charAt(1) == "/") {
// 			return e.protocol + a
// 		} else {
// 			return b + a
// 		}
// 	}
// 	if (/^\.\//.test(a)) {
// 		a = a.substring(2)
// 	}
// 	while (/^\.\./.test(a)) {
// 		if (b != f) {
// 			f = f.substring(0, f.lastIndexOf("/"))
// 		}
// 		a = a.substring(3)
// 	}
// 	if (b != f) {
// 		if (a.charAt(0) != "?" && a.charAt(0) != "#") {
// 			f = f.substring(0, f.lastIndexOf("/"))
// 		}
// 	}
// 	if (a.charAt(0) == "/") {
// 		return f + a
// 	} else {
// 		if (a.charAt(0) == "?") {
// 			f = f.split("?")[0];
// 			return f + a
// 		} else {
// 			if (a.charAt(0) == "#") {
// 				f = f.split("#")[0];
// 				return f + a
// 			} else {
// 				return f + "/" + a
// 			}
// 		}
// 	}
// };
// function clickcr(g, H, u, D, E, A, P) {
// 	if (arguments.length == 1) {
// 		if (typeof nclk.generateCC != "undefined") {
// 			nclk.generateCC(arguments[0])
// 		}
// 		return
// 	}
// 	var F = navigator.userAgent.toLowerCase();
// 	var k = (F.indexOf("safari") != -1 ? true : false);
// 	var C = /msie/.test(F) && !/opera/.test(F);
// 	var l = (window.location.protocol == "https:") ? "https:" : "http:";
// 	var a = ccsrv.substring(ccsrv.indexOf(".") + 1);
// 	var t = window.event ? window.event : E;
// 	var s = -1;
// 	var q = -1;
// 	var p = -1;
// 	var n = -1;
// 	var S, f, i;
// 	var r, j, m;
// 	var M, J, I, L, z, B, w;
// 	var O;
// 	var G = 0;
// 	if (!A) {
// 		A = "0"
// 	} else {
// 		A = String(A)
// 	}
// 	if (!P) {
// 		P = ""
// 	}
// 	if (A.indexOf("n") == 0) {
// 		G = 0
// 	} else {
// 		if (window.g_ssc != undefined && window.g_query != undefined) {
// 			G = 1
// 		} else {
// 			G = 0
// 		}
// 	}
// 	try {
// 		L = nclk.windowSize(window);
// 		i = nclk.checkIframe(g);
// 		if (i) {
// 			var v = nclk.findPos(document.getElementById(i));
// 			if (t.clientX && t.clientX != undefined) {
// 				S = document.body;
// 				if (S.clientLeft && S.clientTop) {
// 					ifrSx = t.clientX - S.clientLeft;
// 					ifrSy = t.clientY - S.clientTop
// 				} else {
// 					ifrSx = t.clientX;
// 					ifrSy = t.clientY
// 				}
// 			}
// 			p = v[0] + ifrSx;
// 			n = v[1] + ifrSy;
// 			if (document.body
// 					&& (document.body.scrollTop || document.body.scrollLeft)) {
// 				S = document.body;
// 				s = p - S.scrollLeft;
// 				q = n - S.scrollTop
// 			} else {
// 				if (document.documentElement
// 						&& (document.documentElement.scrollTop || document.documentElement.scrollLeft)) {
// 					f = document.documentElement;
// 					s = p - f.scrollLeft;
// 					q = n - f.scrollTop
// 				} else {
// 					s = p;
// 					q = n
// 				}
// 			}
// 		} else {
// 			if (t.clientX && t.clientX != undefined) {
// 				S = document.body;
// 				if (S.clientLeft && S.clientTop) {
// 					s = t.clientX - S.clientLeft;
// 					q = t.clientY - S.clientTop
// 				} else {
// 					s = t.clientX;
// 					q = t.clientY
// 				}
// 			}
// 			if (document.body
// 					&& (document.body.scrollTop || document.body.scrollLeft)) {
// 				p = document.body.scrollLeft + (s < 0 ? 0 : s);
// 				n = document.body.scrollTop + (q < 0 ? 0 : q)
// 			} else {
// 				if (document.documentElement
// 						&& (document.documentElement.scrollTop || document.documentElement.scrollLeft)) {
// 					f = document.documentElement;
// 					if (f.scrollLeft != undefined) {
// 						p = f.scrollLeft + (s < 0 ? 0 : s)
// 					}
// 					if (f.scrollTop != undefined) {
// 						n = f.scrollTop + (q < 0 ? 0 : q)
// 					}
// 				} else {
// 					p = (s < 0 ? 0 : s);
// 					n = (q < 0 ? 0 : q)
// 				}
// 			}
// 			if (t.pageX) {
// 				p = t.pageX
// 			}
// 			if (t.pageY) {
// 				n = t.pageY
// 			}
// 		}
// 	} catch (Q) {
// 	}
// 	if (H == "" || typeof H == "undefined") {
// 		return
// 	}
// 	if (A.indexOf("1") != -1) {
// 		r = 0
// 	} else {
// 		if (g.href) {
// 			z = g.nodeName.toLowerCase();
// 			B = g.href.toLowerCase();
// 			if ((g.target && g.target != "_self" && g.target != "_top" && g.target != "_parent")
// 					|| (B.indexOf("javascript:") != -1)
// 					|| (g.getAttribute("href", 2) && g.getAttribute("href", 2)
// 							.charAt(0) == "#")
// 					|| (B.indexOf("#") != -1 && (B.substr(0, B.indexOf("#")) == document.URL))
// 					|| z.toLowerCase() == "img"
// 					|| C
// 					&& window.location.host.indexOf(a) == -1) {
// 				r = 0
// 			} else {
// 				r = 1
// 			}
// 		} else {
// 			r = 0
// 		}
// 	}
// 	if (g.href && g.href.indexOf(l + "//" + ccsrv) == 0) {
// 		j = g.href
// 	} else {
// 		j = l + "//" + ccsrv + "/" + nclkModule + "?a=" + H + "&r=" + D + "&i="
// 				+ u;
// 		j += "&bw=" + L + "&px=" + p + "&py=" + n + "&sx=" + s + "&sy=" + q
// 				+ "&m=" + r;
// 		if (G == 0) {
// 			j += "&nsc=" + nsc
// 		} else {
// 			if (G == 1) {
// 				j += "&ssc=" + g_ssc + "&q=" + encodeURIComponent(g_query)
// 						+ "&s=" + g_sid + "&p=" + g_pid
// 			}
// 		}
// 		if (P) {
// 			j += "&g=" + encodeURIComponent(P)
// 		}
// 		if (B && B.indexOf(l + "//" + ccsrv) != 0 && z.toLowerCase() != "img") {
// 			var N = g.href;
// 			if (g.outerHTML && !window.XMLHttpRequest) {
// 				N = (/\shref=\"([^\"]+)\"/i.test(g.outerHTML) && RegExp.$1)
// 						.replace(/\\/g, "\\\\").replace(/%([A-Z0-9]{2})/ig,
// 								"\\$1");
// 				(d = document.createElement("div")).innerHTML = N;
// 				N = d.innerText.replace(/\\([A-Z0-9]{2})/gi, "%$1").replace(
// 						/\\\\/g, "\\")
// 			}
// 			B = N.toLowerCase();
// 			if (B.indexOf("http:") == 0 || B.indexOf("https:") == 0
// 					|| B.indexOf("javascript:") == 0) {
// 				j += "&u=" + encodeURIComponent(N)
// 			} else {
// 				w = nclk.absPath(N);
// 				j += "&u=" + encodeURIComponent(w)
// 			}
// 		} else {
// 			if (g.href) {
// 				if (g.href.length > 0) {
// 					j += "&u=" + encodeURIComponent(g.href)
// 				} else {
// 					j += "&u=about%3Ablank"
// 				}
// 			} else {
// 				j += "&u=about%3Ablank"
// 			}
// 		}
// 	}
// 	if (r == 1) {
// 		O = g.innerHTML;
// 		g.href = j;
// 		if (g.innerHTML != O) {
// 			g.innerHTML = O
// 		}
// 	} else {
// 		if (document.images) {
// 			var K = new Date().getTime();
// 			j += "&time=" + K;
// 			if (k && !g.href) {
// 				var R = c = new Date();
// 				while ((R.getTime() - c.getTime()) < 100) {
// 					R = new Date()
// 				}
// 				var M = new Image();
// 				nclkImg.push(M);
// 				M.src = j
// 			} else {
// 				var M = new Image();
// 				nclkImg.push(M);
// 				M.src = j
// 			}
// 		}
// 	}
// 	return true
// };
//
// function nclks(name, obj, event) {
//     if (name == "") {
//         return;
//     }
//     try {
//         clickcr(obj,name,'','',event);
//     } catch(e) {
//     }
// }
// function nclks_clsnm(id, className, name, elseName, obj, event) {
//     nclks_if(className == $(id).className, name, elseName, obj, event);
// }
// function nclks_chk(id, name, elseName, obj, event) {
//     nclks_if($(id).checked, name, elseName, obj, event);
// }
// function nclks_if(success, name, elseName, obj, event) {
//     try {
//         if (success) {
//             nclks(name, obj, event);
//         } else {
//             nclks(elseName, obj, event);
//         }
//     } catch(e) {
//     }
// }
//
// /**
//  * lcslog.js  v 0.4.13
//  * Last Updated: 2011-04-06
//  * Author : Chin Mi Ae, Lee Dae Beom
//  * Copyright 2009 NHN Corp. All rights Reserved.
//  * NHN PROPRIETARY/CONFIDENTIAL. Use is subject to license terms.
//  *
//  * This code includes some part of the
//  * "Flash Player Detection Kit Revision 1.5" by Michael Williams
//  * & Copyright 2005-2007 Adobe Macromedia Softward.LLC. All rights reserved.
//  */
//
//
// var lcs_isie = (navigator.appName == "Microsoft Internet Explorer");
// var lcs_isns = (navigator.appName == "Netscape" );
// var lcs_isopera = (navigator.appVersion.indexOf("Opera") >=  0 );
// var lcs_ismac = (navigator.userAgent.indexOf("MAC")>=0);
//
// var lcs_add = {};
// var lcs_bc = {};
//
// var lcs_ver = "v0.4.13";
// var lcs_cnt = 0;
//
// function lcs_do( etc ) {
// 	// TODO : check lcs server name!!
// 	if (!lcs_SerName) { var lcs_SerName = "lcs.naver.com"; }
//
// 	var rs = "";
// 	var index;
// 	var doc = document;
// 	var wlt = window.location;
//
// 	try {
// 		var lcs_Addr = (wlt.protocol ? wlt.protocol : "http:")+"//" + lcs_SerName + "/m?";
// 	} catch(e){ return; }
//
// 	try {
// 		rs = lcs_Addr + "u=" + encodeURIComponent(wlt.href)
// 			+ "&e=" + (doc.referrer ? encodeURIComponent(doc.referrer) : "");
// 	} catch(e) {
// 	}
//
// 	try {
//
// 	if (typeof lcs_add.i == 'undefined' )
// 		lcs_add.i = "";
//
// 	for( var index in lcs_add)
// 	{
// 		if( typeof lcs_add[index] != 'function' )
// 			rs += "&" + index + "=" + encodeURIComponent(lcs_add[index]);
// 	}
//
// 	for( var index in etc )
// 	{
// 		if ( (index.length >= 3 && (typeof etc[index] != 'function')) || index == 'qy')
// 		{
// 			rs += "&" + index + "=" + encodeURIComponent(etc[index]);
// 		}
// 	}
//
//
// 	if(lcs_cnt < 1)
// 	{
// 		lcs_getBrowserCapa();
// 	}
//
// 	for( var index in lcs_bc )
// 	{
// 		if( typeof lcs_bc[index] != 'function' )
// 			rs += "&" + index + "=" + encodeURIComponent(lcs_bc[index]);
// 	}
//
// 	if(lcs_cnt > 0 )
// 	{
// 		var timeStr = (new Date).getTime();
// 		rs += "&ts=" + timeStr;
// 	}
// 	rs += "&EOU";
//
// 	if (doc.images) {
// 		var obj = (new Image());
// 		obj.src = rs;
// 		obj.onload = function() { obj.onload = null; return; }
// 	} else {
// 		doc.write( '<im' + 'g sr' + 'c="' + rs + '" width="1" height="1" border="0" />');
// 	}
// 	lcs_cnt++;
//
// 	} catch(e) {
// 		return;
// 	}
// }
//
// function lcs_do_gdid( gdid , etc) {
//
// 	try {
// 		if (gdid) {
// 			lcs_add["i"] = gdid;
//
// 			if (etc){
// 				lcs_do(etc);
// 			} else {
// 				lcs_do();
// 			}
//
// 		}
// 	} catch (e) {
// 	}
// }
//
// function lcs_getBrowserCapa() {
// 	lcs_getOS();
//
// 	lcs_getlanguage();
//
// 	lcs_getScreen();
//
// 	lcs_getWindowSize();
//
// 	lcs_getColorDepth();
//
// 	lcs_getJavaEnabled();
//
// 	lcs_getJavascriptVer();
//
// 	lcs_getCookieEnabled();
//
// 	lcs_getSwfVer();
//
// 	lcs_getSLVersion();
//
// 	lcs_getConnectType();
//
// 	lcs_getPlugIn();
//
// }
//
// function lcs_getOS() {
// 	var lcs_os = "";
// 	try {
// 		(navigator.platform ? lcs_os = navigator.platform : "");
// 	} catch (e) {
// 	}
// 	lcs_bc["os"] = lcs_os;
// }
//
// function lcs_getlanguage() {
// 	var lcs_ln = "";
// 	try {
// 		(navigator.userLanguage? lcs_ln = navigator.userLanguage : (navigator.language)? lcs_ln = navigator.language : "");
// 	} catch (e) {
// 	}
//
// 	lcs_bc["ln"] = lcs_ln;
// }
//
// function lcs_getScreen() {
// 	var lcs_sr = "";
// 	try {
// 		if ( window.screen && screen.width && screen.height)
// 		{
// 			lcs_sr = screen.width + 'x'+ screen.height;
// 		}
// 		else if ( window.java || self.java )
// 		{
// 			var sr = java.awt.Toolkit.getDefaultToolkit().getScreenSize();
// 			lcs_sr = sr.width + 'x' + sr.height;
//
// 		}
// 	} catch(e) {
// 		lcs_sr = "";
// 	}
//
// 	lcs_bc["sr"] = lcs_sr;
// }
//
//
// function lcs_getWindowSize() {
// 	var doc = document;
//
// 	lcs_bc["bw"] = '';
// 	lcs_bc["bh"] = '';
// 	try {
// 		lcs_bc["bw"] = doc.documentElement.clientWidth ? doc.documentElement.clientWidth : doc.body.clientWidth;
// 		lcs_bc["bh"] = doc.documentElement.clientHeight ? doc.documentElement.clientHeight : doc.body.clientHeight;
// 	}
// 	catch(e) {
// 	}
// }
//
// function lcs_getColorDepth(){
// 	lcs_bc["c"] = "";
// 	try {
// 		if (window.screen) {
// 			lcs_bc["c"] = screen.colorDepth ? screen.colorDepth : screen.pixelDepth;
// 		}
// 		else if (window.java || self.java ) {
// 			var c = java.awt.Toolkit.getDefaultToolkit().getColorModel().getPixelSize();
// 			lcs_bc["c"] = c;
// 		}
// 	} catch (e) {
// 		lcs_bc["c"] = "";
// 	}
// }
//
// function lcs_getJavaEnabled() {
// 	lcs_bc["j"] = "";
// 	try {
// 		lcs_bc["j"]= navigator.javaEnabled() ? "Y":"N";
// 	} catch (e) {}
//
// }
//
// function lcs_getCookieEnabled() {
// 	lcs_bc["k"] = "";
// 	try {
// 		lcs_bc["k"]= navigator.cookieEnabled ? "Y":"N";
// 	} catch (e) {
// 	}
//
// }
//
// function lcs_getConnectType() {
// 	var bd = document.body;
// 	var lcs_ct = "";
// 	try {
// 		if ( lcs_isie && !lcs_ismac && bd ) {
// 			var obj = bd.addBehavior("#default#clientCaps");
// 			lcs_ct = bd.connectionType;
// 			bd.removeBehavior(obj);
// 		}
// 	} catch(e) {
// 	}
//
// 	lcs_bc["ct"] = lcs_ct;
// }
//
//
// function lcs_getJavascriptVer() {
// 	var j = "1.0";
// 	try {
// 		if(String && String.prototype) {
// 			j = "1.1";
// 			if(j.search)
// 			{
// 				j = "1.2";
// 				var dt = new Date, no = 0;
// 				if ( dt.getUTCDate)
// 				{
// 					j = "1.3";
// 					var napp = navigator.appVersion;
// 					var i, ie = napp.indexOf('MSIE');
// 					if (ie > 0 )
// 					{
// 						var apv =  parseInt(i = napp.substring(ie+5));
// 						if (apv > 3) { n_apv = parseFloat(i); }
// 					}
// 					if(lcs_isie && lcs_ismac && apv >= 5)
// 					{
// 						j = "1.4";
// 					}
// 					if(no.toFixed)
// 					{
// 						j = "1.5";
// 						var a = new Array;
// 						if (a.every)
// 						{
// 							j = "1.6";
// 							i = 0;
// 							var obj = new Object;
// 							var test = function(obj) { var i = 0; try {	i = new Iterator(obj)} catch(e) {} return i};
// 							i = test(obj);
// 							if(i && i.next) j = "1.7";
//
// 							if(a.reduce) j = "1.8";
//
// 						}
//
// 					}
// 				}
// 			}
// 		}
// 	} catch (e) {}
// 	lcs_bc["jv"] = j;
// }
//
// function lcs_getSwfVer(){
// 	var flashVer = '';
// 	var isWin = false;
// 	var na = navigator;
//
// 	try {
// 		var pg = na.plugins;
//
// 		isWin = (na.appVersion.toLowerCase().indexOf("win") != -1) ? true : false;
//
// 		if (pg != null && pg.length > 0) {
// 			if (pg["Shockwave Flash 2.0"] || pg["Shockwave Flash"]) {
// 				var swVer2 = pg["Shockwave Flash 2.0"] ? " 2.0" : "";
// 				var flashDescription = pg["Shockwave Flash" + swVer2].description;
// 				var descArray = flashDescription.split(" ");
// 				var tempArrayMajor = descArray[2].split(".");
// 				var versionMajor = tempArrayMajor[0];
// 				var versionMinor = tempArrayMajor[1];
// 				flashVer = parseInt(versionMajor,10) + "." + parseInt(versionMinor, 10);
// 			}
// 		}
// 		else if (na.userAgent.toLowerCase().indexOf("webtv/2.6") != -1) flashVer = "4.0";
// 		else if (na.userAgent.toLowerCase().indexOf("webtv/2.5") != -1) flashVer = "3.0";
// 		else if (na.userAgent.toLowerCase().indexOf("webtv") != -1) flashVer = "2.0";
// 		else if ( lcs_isie && isWin && !lcs_isopera ) {
// 		    var version = '';
// 		    var axo;
//
// 		    try {
//        			axo = new ActiveXObject("ShockwaveFlash.ShockwaveFlash.7");
//    		     	version = axo.GetVariable("$version");
// 		    } catch (e) {}
//
// 		    if (!version)
// 		    {
// 		        try {
//        		    	axo = new ActiveXObject("ShockwaveFlash.ShockwaveFlash.6");
//            		 	version = "WIN 6,0,21,0";
// 	            	axo.AllowScriptAccess = "always";
//             		version = axo.GetVariable("$version");
//         			} catch (e) {}
//     		}
//
// 			if (!version)
// 			{
// 				try {
// 					axo = new ActiveXObject("ShockwaveFlash.ShockwaveFlash.3");
// 					version = "WIN 3,0,18,0";
// 					version = axo.GetVariable("$version");
// 				} catch (e) {}
// 			}
//
// 			if (!version)
// 			{
// 				try {
// 					axo = new ActiveXObject("ShockwaveFlash.ShockwaveFlash");
// 					version = "WIN 2,0,0,11";
// 				} catch (e) {}
// 			}
//
// 			if (version.indexOf(',') > 0 ) {
// 				version = version.replace( /%20/,'');
// 				version = version.replace( /[a-zA-Z]*[^0-9]/,'');
// 				version = version.replace( /,/g,'.');
// 			}
// 			flashVer = version;
// 		}
// 	} catch (e) {}
//
// 	lcs_bc["fv"] = flashVer;
// }
//
// function lcs_getSLVersion() {
// 	var lcs_sl = "";
// 	var doc = document;
// 	var bd = doc.body;
// 	try {
// 		var pg = navigator.plugins;
// 		if (pg && pg.length > 0 )
// 		{
// 			lcs_sl = pg["Silverlight Plug-In"].description || pg["WPFe Plug-In"].description;
// 			if (lcs_sl == '1.0.30226.2') lcs_sl = '2.0.30226.2';
// 		}
// 		else
// 		{
// 			var wrap, obj;
// 			if (typeof ActiveXObject != 'undefined') {
// 				try { obj = new ActiveXObject('AgControl.AgControl');
// 				} catch(e) {}
// 			} else {
// 				wrap = doc.createElement('div');
// 				wrap.innerHTML = '<object type="application/x-silverlight" style="position:absolute;" />';
// 				bd.insertBefore(wrap, bd.firstChild);
// 				obj = wrap.firstChild;
// 			}
//
// 			if (/\bopera\b/i.test(navigator.userAgent))
// 				for (var start = new Date().getTime(); typeof obj.isVersionSupported == 'undefined' && (new Date().getTime() - start < 1000); );
//
// 			if (typeof obj.isVersionSupported != 'undefined') {
//
// 				for (var major = 0; major < 9; major++) {
//
// 					for (var minor = 0; minor <= 9; minor++) {
// 						var v = major + '.' + minor;
// 						if (obj.isVersionSupported(v)) {
// 							lcs_sl = v;
// 						}
// 						else break;
//
// 					}
//
// 				}
//
// 			}
//
// 			if (obj) obj = null;
// 			if (wrap) bd.removeChild(wrap);
// 		}
//
// 		if ( lcs_sl.indexOf('.') > 0 ) {
// 			var verArray = lcs_sl.split('.');
// 			lcs_sl = verArray[0] + '.' + verArray[1];
// 		}
// 	} catch(e) { }
//
// 	lcs_bc["sl"] =  lcs_sl;
// }
//
//
// function lcs_getPlugIn() {
// 	var plArr = {};
// 	var lcs_p = "";
//
// 	var na = navigator;
// 	var pg = na.plugins;
//    	if (pg && pg.length > 0)
// 	{
// 		try {
// 			var piArr = pg;
// 			for (var i = 0; i < piArr.length; i++)
// 			{
// 				plArr[piArr[i].name] = '';
// 			}
// 		} catch (e) { }
//
// 	} else {
// 			if (lcs_bc['fv'] != '' )
// 				plArr["Shockwave Flash"] = '';
//
// 			if (lcs_bc['sl'] != '' )
// 				plArr["Silverlight"] = '';
// 	   	try {
// 			if (new ActiveXObject("SWCtl.SWCtl")) { plArr["Shockwave Director"] = '';}
//        	} catch (e) { }
//
// 	    try {
// 			if (new ActiveXObject("rmocx.RealPlayer G2 Control")
// 				|| new ActiveXObject("RealPlayer.RealPlayer(tm) ActiveX Control (32-bit)")
// 				|| new ActiveXObject("RealVideo.RealVideo(tm) ActiveX Control (32-bit)")) {
// 				plArr["RealPlayer"] = '';
// 			}
//         } catch (e) {
//         }
//
// 		try
// 		{
// 			var index = na.userAgent.indexOf('MSIE');
// 			if (index != -1)
// 			{
// 				var ie_ver = parseFloat(na.userAgent.substring(index + 4 + 1));
// 				if (ie_ver < 7 ){
// 					if (new ActiveXObject("QuickTime.QuickTime")) {
// 						plArr["QuickTime"] = '';
// 					}
//
// 					if (new ActiveXObject("MediaPlayer.MediaPlayer.1")) {
// 						plArr["Windows Media"] = '';
// 					} else {
// 						var obj_item = doc.getElementsByTagName("object");
// 						for(var i=0; i <  obj_item.length ; i++ ) {
// 							if(obj_item[i].classid) {
// 								var clsid = obj_item[i].classid.toUpperCase();
//  								if ( clsid == "CLSID:6BF52A52-394A-11D3-B153-00C04F79FAA6"
// 											|| clsid == "CLSID:22D6F312-B0F6-11D0-94AB-0080C74C7E95" ) {
// 									if (new ActiveXObject("MediaPlayer.MediaPlayer.1")) {
// 										plArr["Windows Media"] = '';
// 									}
// 								}
//
// 							}
//
// 						}
// 					}
// 				}
// 			}
// 		} catch (e) { }
// 	}
//
// 	for( var index in plArr ) {
// 		if( typeof plArr[index] != 'function' )
// 		lcs_p += index + ';';
// 	}
//
// 	lcs_bc["p"] = lcs_p.length ? lcs_p.substr(0, lcs_p.length-1) : lcs_p;
// }


// Some addition
function get_encpw(sessionkey, evalue, nvalue, id, pw){
    var rsa = new RSAKey();
    rsa.setPublic(evalue, nvalue);
    return rsa.encrypt(getLenChar(sessionkey) + sessionkey
			+ getLenChar(id) + id
			+ getLenChar(pw) + pw);
}
