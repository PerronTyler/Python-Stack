I=1
V=5
X=10
L=50
C=100
D=500
M=1000


input1="III"
input2="LVIII"
input3="MCMXCIV"

function romanConvert(str){
    data = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000,
    }
    let sum = data[str[str.length-1]]
    for (let i = str.length-1; i > 0; i--){
        if (data[str[i-1]] >= data[str[i]]){
            sum += data[str[i-1]]
        }
        else {
            sum -= data[str[i-1]]
        }
    }
    return sum
}
console.log(romanConvert(input1));
console.log(romanConvert(input2));
console.log(romanConvert(input3));

// function romanConvert(str){
//     data = {
//         I: 1,
//         V: 5,
//         X: 10,
//         L: 50,
//         C: 100,
//         D: 500,
//         M: 1000,
//     }
//     let sum = 0
//     for (let i = 0; i < str.length; i++){
//         if (data[str[i]] == data[str[i+1]]){
//         sum += data[str[i]]
//         }
//         if (data[str[i]] < data[str[i+1]]){
//         sum -= data[str[i]]
//         }
//     return sum
//     }
// }