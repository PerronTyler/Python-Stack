// access each element of the string

// * 
// Given in an alumni interview in 2021.
// String Encode
// You are given a string that may contain sequences of consecutive characters.
// Create a function to shorten a string by including the character,
// then the number of times it appears. 


// If final result is not shorter (such as "bb" => "b2" ),
// return the original string.
// */

const str1 = "aaaabbcdddaaa";
const expected1 = "a4b2c1d3a3";

var newStr1 = '' 
function loopString1(str){
    for (let i=0;i<str.length;i++){
        count = 1
        if (str[i] = str[i-1]);
        else (print((str[i])) count++);
    }
}
console.log(loopString1(str1))
const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbcc";
const expected4 = "bbcc";

/**
 * Encodes the given string such that duplicate characters appear once followed
 * by a number representing how many times the char occurs. Only encode strings
 * when the result yields a shorter length.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str The string to encode.
 * @returns {string} The given string encoded.
 * we need to run through each element of the string
 * pull the letter we are comparing
 * count each instance of the letter
 * return a new string with the letter and the count for each
 */
function encodeStr(str) {}

/*****************************************************************************/

/* 
  String Decode  
*/

const two_str1 = "a3b2c1d3";
const two_expected1 = "aaabbcddd";

const two_str2 = "a3b2c12d10";
const two_expected2 = "aaabbccccccccccccdddddddddd";

/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @returns {string} The given str decoded / expanded.
 * 
 * 
 */
function decodeStr(str) {}