class studentHogwarts {
    constructor(privateScore=0, name=null) {
        this.privateScore = privateScore;
        this.name = name;
    }

    #changeScoreBy(point) {
        this.privateScore += point;
    }

    setName(newName) {
        this.name = newName;
    }

    rewardStudent() {
        return this.#changeScoreBy(1);
    }

    penalizeStudent() {
        return this.#changeScoreBy(-1);
    }

    getScore() {
        return `${this.name}: ${this.privateScore}`
    }

}

const harry = new studentHogwarts();
harry.setName("Harry");
harry.rewardStudent();
harry.rewardStudent();
harry.rewardStudent();
harry.rewardStudent();
console.log(harry.getScore());

const draco = new studentHogwarts();
draco.setName("Draco");
draco.rewardStudent();
draco.penalizeStudent();
draco.penalizeStudent();
draco.penalizeStudent();
console.log(draco.getScore());