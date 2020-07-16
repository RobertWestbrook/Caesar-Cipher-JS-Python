function rot13(str) {
    return str.replace(/[A-Za-z]/g, function (L) {
    if (L.charCodeAt(0) < 97) {
        return String.fromCharCode((L.charCodeAt(0) % 26) + 65)
    }else if (L.charCodeAt(0) > 65){
       return String.fromCharCode((L.charCodeAt(0) % 26) + 97)
    }
    });
}


//Understnding the Code:
//line 2 returns the string with a regex replace parameter that 
//replaces any of the target characters with the result of the arrow
//function =>
//Line 3: calls the String.fromCharCode to take the character output from the
//parameter and turns translates it into letter.
//The Parameter L.charCodeAt(0) % 26) + 65