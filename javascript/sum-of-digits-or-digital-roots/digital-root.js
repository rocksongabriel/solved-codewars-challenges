function digital_root(n) {
    sum = 0;

    do {
        str_digits = (""+n).split("");
        digits = [];
        str_digits.forEach(element => {
            digits.push(Number(element))
        })

        sum = digits.reduce((total, number) => total + number, 0);

        if (sum > 9) {
            n = sum;
        }
    } while (sum > 9);

    return sum
}
