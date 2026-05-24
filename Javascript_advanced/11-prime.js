function countPrimeNumbers() {
    let count = 0;

    for (let i = 2; i <= 100; i++) {
        let isPrime = true;

        for (let j = 2; j * j <= i; j++) {
            if (i % j === 0) {
                isPrime = false;
                break;
            }
        }

        if (isPrime) {
            count++;
        }
    }

    return count;
}

setTimeout(() => {
    let endTime = performance.now();
    console.log(`Execution time of calculating prime numbers 100 times was ${endTime - startTime} milliseconds.`);
}, 0);

let startTime = performance.now();
for (let i = 0; i < 100; i++) {
    countPrimeNumbers();
}
let endTime = performance.now();