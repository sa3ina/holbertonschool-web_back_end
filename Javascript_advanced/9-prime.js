function countPrimeNumbers() {
    let count = 0;
    let startTime = performance.now();

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

    let endTime = performance.now();
    let timeUsed = endTime - startTime;

    console.log(`Execution time of printing countPrimeNumbers was ${timeUsed} milliseconds.`);
    return count;
}

countPrimeNumbers();