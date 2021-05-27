function squareDigits(num){
    numbers = split_digit(num)
    squared_str = ""
    for (number of numbers) {
        squared_str += number*number;
    }

    return Number(squared_str);
}

function split_digit(digit) {
    s_digits = (""+digit).split("")
    digits = []
    s_digits.forEach(element => {
      digits.push(Number(element));
    });
    return digits
}

/*
1. split the number into digits
2. square each digit
3. concat the results

*/

console.log(squareDigits(9119));