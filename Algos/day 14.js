/* 
  Array: Mode
  
  Create a function that, given an array of ints,
  returns the int that occurs most frequently in the array.
  What if there are multiple items that occur the same number of time?
    - return all of them (in an array)
    - what if all items occur the same number of times?
      - return empty array
*/

const nums1 = [];
const expected1 = [];

const nums2 = [1];
const expected2 = [1];

const nums3 = [5, 1, 4];
const expected3 = [];

const nums4 = [5, 1, 4, 1];
const expected4 = [1];

const nums5 = [5, 1, 4, 1, 5];
const expected5 = [5, 1];
//  - order doesn't matter

/**
 * Finds the mode or all modes if there are more than one. The mode is the
 *    value which occurs the most times in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums Test
 * @returns {Array<number>} Mode or modes in any order.
 */
function mode(nums) {
    let mode = {}
    let modeCount = 0;
    let modeList = []
    for (let i=0; i<nums.length; i++) {
        if (mode[nums[i]]) {
            mode[nums[i]] += 1
        }
        else {
            mode[nums[i]] = 1
        }
    }
    for (key in mode) {
        if (mode[key] > modeCount) {
            modeList = [parseInt(key)]
            modeCount = mode[key]
        }
        else if (mode[key] == modeCount){
            modeList.push(parseInt(key))
        }
    }
    if (modeList.length == nums.length && modeList.length != 1) {
        return []
    }
    else {
        return modeList
    }
}

function mode(nums) {

    if (nums.length === 1) return [nums[0]]
    
    var modes = []
    var freq = {}
    var maxFreq = 0
    let allSameFreq = true

    for (let num of nums){
        // ternary operator
        // 3 parts: condition ? if condition is true : if condition is false

        freq.hasOwnProperty(num) ? freq[num]++ : freq[num] = 1

        if (freq[num] > maxFreq) maxFreq = freq[num]
    }

    // console.log(freq, maxFreq);

    for (var key in freq) {
        if (freq[key] === maxFreq) modes.push(parseInt(key))
        
        else allSameFreq = false;
    }
    return allSameFreq ? [] : modes
}