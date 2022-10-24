/* 
  Recursive Factorial
  Input: integer
  Output: integer, product of ints from 1 up to given integer
  
  If less than zero, treat as zero.
  Bonus: If not integer, truncate (remove decimals).
  
  Experts tell us 0! is 1.
  
  rFact(3) = 6 (1*2*3)
  rFact(6.8) = 720 (1*2*3*4*5*6)
*/

const num1 = 3;
const expected1 = 6;
// Explanation: 1*2*3 = 6

const num2 = 6.8;
const expected2 = 720;
// Explanation: 1*2*3*4*5*6 = 720

const num3 = 0;
const expected3 = 1;

/**
 * Recursively multiples 1 to the given int.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} n The int to factorial. Treat negatives as zero and
 *    floor decimals.
 * @returns {number} The result of !n.
 */
function factorial(num, i=1) {
        // edge cases (negative, decimals)
        num = Math.floor(num)
        // base case
        if (i > num){
            return 1
        }
        
        // recursive call
        let sum = factorial(num, i+1) * i;
        // console.log(`return: ${sum}`);
        return sum
}
// console.log(factorial(num1));
// console.log(factorial(num2));
// console.log(factorial(num3));
/*****************************************************************************/


/* 
  Return the fibonacci number at the nth position, recursively.
  
  Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
  The next number is found by adding up the two numbers before it,
  starting with 0 and 1 as the first two numbers of the sequence.
*/

const two_num1 = 0;
const two_expected1 = 0;

const two_num2 = 1;
const two_expected2 = 1;

const two_num3 = 2;
const two_expected3 = 1;

const two_num4 = 3;
const two_expected4 = 2;

const two_num5 = 4;
const two_expected5 = 3;

const two_num6 = 8;
const two_expected6 = 21;

/**
 * Recursively finds the nth number in the fibonacci sequence.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} num The position of the desired number in the fibonacci sequence.
 * @returns {number} The fibonacci number at the given position.
 */
function fibonacci(num) {
    // edge cases (negative, decimals)
    // base case
    if ( num < 2 ){
        return num
    }
    // recursive call
    else {
        return ((fibonacci(num-1)) + (fibonacci(num-2)));
    }
}

console.log(fibonacci(8));
// console.log(fibonacci(two_num1));
// console.log(fibonacci(two_num2));
// console.log(fibonacci(two_num3));
// console.log(fibonacci(two_num4));
// console.log(fibonacci(two_num5));
// console.log(fibonacci(two_num6));

function fibonacci(num, memo={0:0, 1:1}) {
    // edge cases (negative, decimals)
    // base case

    if ( num < 2 ){
        return num
    }
    if (memo[num] !== undefined){
        return memo[num]
    }
    // recursive call
    memo[num] = fibonacci(num-1, memo) + fibonacci(num-2, memo)
    return memo[num]
}

console.log(fibonacci(8));
// console.log(fibonacci(two_num1));
// console.log(fibonacci(two_num2));
// console.log(fibonacci(two_num3));
// console.log(fibonacci(two_num4));
// console.log(fibonacci(two_num5));
// console.log(fibonacci(two_num6));