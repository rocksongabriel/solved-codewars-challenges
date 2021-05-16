function solution(number) {
    if (number > 0) {
        multiplesOf3Array = [];
        multiplesOf5Array = [];

        for (num in range(number)) {
            if (num % 3 === 0) {
                multiplesOf3Array.push(Number(num));
            } else if (num % 5 === 0) {
                multiplesOf5Array.push(Number(num));
            }
        }
        unionArray = [...new Set([...multiplesOf3Array, ...multiplesOf5Array])];
        sum = unionArray.reduce((total, num) => total + num, 0);

        return sum;
    } else {
        return 0;
    }
}

// function to get range from 1 to number - 1
range = (n) => {
    r = [...Array(n).keys()];
    delete r[0]
    return r;
}