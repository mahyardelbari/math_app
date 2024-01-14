var mathsteps = require('mathsteps');
var steps = mathsteps.solveEquation(process.argv[2]);
steps.forEach(step => {
    console.log("Before change: " + step.oldEquation.ascii());
    console.log("Change: " + step.changeType);
    console.log("After change: " + step.newEquation.ascii());
});