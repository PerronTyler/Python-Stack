



/* 
  Given two arrays, interleave them into one new array.
  The arrays may be different lengths. The extra items should be added to the
  back of the new array.
*/

const arrA1 = [1, 2, 3];
const arrB1 = ["a", "b", "c"];
const expected1 = [1, "a", 2, "b", 3, "c"];

const arrA2 = [1, 3];
const arrB2 = [2, 4, 6, 8];
const expected2 = [1, 2, 3, 4, 6, 8];

const arrA3 = [1, 3, 5, 7];
const arrB3 = [2, 4];
const expected3 = [1, 2, 3, 4, 5, 7];

const arrA4 = [];
const arrB4 = [42, 0, 6];
const expected4 = [42, 0, 6];

/**
 * Interleaves two arrays into a new array. Interleaving means alternating
 * the items starting from the first array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<any>} arr1
 * @param {Array<any>} arr2
 * @returns {Array<any>} A new array of interleaved items.
 * have a count variable that will increment but start at 0
at each array[count] we will push the array index onto a new array
 */
function interleaveArrays(arr1, arr2) {
    let expected = []
    if (arr1.length > arr2.length) {
        for (let i = 0; i < arr1.length; i++) {
            if (arr1[i] != undefined) {
                expected.push(arr1[i]);
            }
            if (arr2[i] != undefined) {
                expected.push(arr2[i]);
            }
        }
        return expected;
    }
    else {
        for (let i = 0; i < arr2.length; i++) {
            if (arr1[i] != undefined) {
                expected.push(arr1[i]);
            }
            if (arr2[i] != undefined)  {
                expected.push(arr2[i]);
            }
        }
        return expected;
    }

}
console.log(interleaveArrays(arrA1, arrB1));
console.log(interleaveArrays(arrA2, arrB2));
console.log(interleaveArrays(arrA3, arrB3));
console.log(interleaveArrays(arrA4, arrB4));
/* 
  Array: Binary Search (non recursive)
  Given a sorted array and a value, return whether the array contains that value.
  Do not sequentially iterate the array. Instead, ‘divide and conquer’,
  taking advantage of the fact that the array is sorted .
  Bonus (alumni interview): 
    first complete it without the bonus, because they ask for additions
    after the initial algo is complete
    return how many times the given number occurs
*/

const two_nums1 = [1, 3, 5, 6];
const two_searchNum1 = 4;
const two_expected1 = false;

const two_nums2 = [4, 5, 6, 8, 12];
const two_searchNum2 = 5;
const two_expected2 = true;

const two_nums3 = [3, 4, 6, 8, 12];
const two_searchNum3 = 3;
const two_expected3 = true;

// bonus, how many times does the search num appear?
const two_nums4 = [2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9];
const two_searchNum4 = 2;
const two_expected4 = 4;

/**
 * Efficiently determines if the given num exists in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the given num exists in the given array.
 * divide the array in half
 * if number of array length is greater than 3
 * divide the array in half again
 * binary searth the sides of the split to find the number we are looking for
 */
 function binarySearch(sortedNums, searchNum) {
    let leftIndex = 0
    let rightIndex = sortedNums.length - 1
    let midIndex = Math.floor(sortedNums.length / 2)
  
    while (leftIndex <= rightIndex) {
      if (sortedNums[midIndex] > searchNum) {
        rightIndex = midIndex - 1
      } else if (sortedNums[midIndex] < searchNum) {
        leftIndex = midIndex + 1
      } else {
        return true
      }
  
      midIndex = Math.floor(rightIndex - leftIndex / 2)
    }
    return false
  }