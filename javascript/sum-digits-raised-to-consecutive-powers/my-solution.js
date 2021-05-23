// My solution of the problem


// function to generate range
let range = (start, stop, step=1) => Array(stop - step).fill(start).map((x, y) => x + y * step)

function sumDigPow(a, b) {
  numbers = range(a, b)
  for (number in numbers){
    if (number > 9) {
      digits = split_digit(number);
      console.log(digits)
    }
  }
}

sumDigPow(10, 12);

function split_digit(digit) {
  s_digits = (""+digit).split("");
  digits = []
  s_digits.forEach(element => {
    digits.push(Number(element));
  });
  return digits
}

console.log(split_digit(2343))

console.log(range(1, 10))

