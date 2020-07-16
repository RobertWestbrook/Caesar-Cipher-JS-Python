function rot13(str) {
    return str.replace(/[A-Za-z]/g, function (L) {
    if (L.charCodeAt(0) < 97) {
        return String.fromCharCode((L.charCodeAt(0) % 26) + 65)
    }else if (L.charCodeAt(0) > 65){
       return String.fromCharCode((L.charCodeAt(0) % 26) + 97)
    }
    });
}


//Understanding the Modulo:
//This code takes the str and filters through it with regexp to pull out alpha and
//then it checks the ascii character code to decide with the if statement what to
//do with the charachter based on whether the character is lower case or upper.
//Once it decides, the code then returns each character and replaces the original
//using String.fromCharCode() function passing the argument L.charCodeAt(0). This
//argument is simply getting the current index/letter and then it turns it into a ascii
//code. Before that code is passed as an int to the .fromCharCode() function,
//it takes the modulo % 26 of that letter's CharCode, adds the base ascii number of the
//uppercase or lower case codes, before returning. The Modulo is basicallly dividing the
//expressed number into the value to the left of it and returning its remainder. Once we 
//get that remainder it is then what the base number from the section of ascii is being 
//added to get the desired charCode before returning it to the .fromCharCode()function.
//So, if "A" = 65 then % 26 of "A" == 13. Take 13 + 65 to equal your new character code
//"N" = 78. If the code registers a lower case the previous modulo statement remains the
//same but the base number added will change to 97 which is = "a" in ascii.