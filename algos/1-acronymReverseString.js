// Use the acronym function below to return the acronyms, or capitalized first letters, of each word in a sentence

// Example: acronym("free all rodents that like evil kittens") would return the string "FARTLEK"
// NOTE: A Fartlek is a period of fast running intermixed with periods of slower running - you're welcome (:
// TIP: A string can be treated like an array of letters.  For example "car" could be used as ["c","a","r"]

function acronym(str) {
    arr = str.split("");
    let acronym = [];
    for (let i = 0; i < arr.length; i++) {
        if (i == 0 || arr[i-1] == " "){
            acronym.push(arr[i]);
        }
    }
    acronym = acronym.join('');
    return acronym.toUpperCase();
}

console.log(acronym("free all rodents that like evil kittens"));
// console.log(acronym("never obey older babies sarcastically"));



// Use the reverseString function below to take in a string and reverse the order of each character in that string

// Example: reverseString("creature") would return "erutaerc"
// Example: reverseString("really?") would return "?yllaer"
// Example: reverseString("yo banana boy") would return "yob ananab oy"
// Example: reverseString("borrow or rob") would return "bor ro worrob"  

// ** Don't use the built-in reverse() method! ** That is cheating (: and you don't want to cheat!

function reverseString(str) {
    let reversed = [];
    

    return reversed();
}

// console.log(reverseString("creature"))
// console.log(reverseString("really?"))
// console.log(reverseString("yo banana boy"))
// console.log(reverseString("borrow or rob"))