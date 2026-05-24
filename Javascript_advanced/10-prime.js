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


let startTime = performance.now();
let a = 0;

while (a < 100) {
    countPrimeNumbers();
    a++;
}

let endTime = performance.now();
let timeUsed = endTime - startTime;

console.log(`Execution time of calculating prime numbers 100 times was ${timeUsed} milliseconds.`);