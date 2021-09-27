// let val;

// let Multiply = function (a, b, c, callback) {
// 	let arr = [];
// 	for (let i = 0; i < 3; i++) {
// 		arr[i] = callback(arguments[i] ** 2);
// 	}
// 	return arr;
// };

// let addOne = function (a) {
// 	return a + 1;
// };

// val = Multiply(5, 10, 20, addOne);

// console.log(val);

/////////////////////////////////////////////////////

// (function () {
// 	var days = [1, 2, 3, 4, 5];
// })();

// (function () {
// 	var days = [1, 2, 3, 4, 5];
// })();

/////////////////////////////////////////////////////

// let Question = function (hobby) {
// 	switch (hobby) {
// 		case "car":
// 			return function (name) {
// 				console.log(name, "do you have a car");
// 			};
// 		case "book":
// 			return function (name) {
// 				console.log(name, "what is a favourite book ?");
// 			};
// 		case "software":
// 			return function (name, type) {
// 				console.log(name, "are you interested in python ?", type);
// 			};
// 		default:
// 			return function (name) {
// 				console.log(name, "how are you?");
// 			};
// 	}
// };

// var carQuestion = Question("software");

// carQuestion("cinar", "zort");

// const person = {
// 	firstName: "sadik",
// 	lastName: "turan",
// };
// Object.defineProperty(person, "fullName", {
// 	get function() {
// 		return `${this.firstName} ${this.lastName}`;
// 	},
// 	set function(value) {
// 		const parts = value.split(" ");
// 		this.firstName = parts[0];
// 		this.lastName = parts[1];
// 	},
// });

// Object.defineProperty(person, "age", {
// 	value: 50,
// 	writable: false,
// });

// var welcome = function (a, b) {
// 	console.log("Welcome " + this.name + ".Are  you interested in " + a + " and " + b);
// };

// var yigit = { name: "yigit" };
// var ada = { name: "ada" };

// welcome.call(yigit, "asp.net", "angular");
// welcome.call(ada, "asp.net", "angular");

// welcome.apply(yigit, ["asp.net", "angular"]);
// welcome.apply(ada, ["asp.net", "angular"]);

// welcomeYigit = welcome.bind(yigit);

// welcomeYigit();
// welcomeAda = welcome.bind(ada);

// welcomeAda();

/////////////// Demo : Numeric Range

// var num = {
// 	min: 0,
// 	max: 100,
// 	checkNumericRange: function (value) {
// 		if (typeof value !== "number") {
// 			return false;
// 		} else {
// 			return value >= this.min && value <= this.max;
// 		}
// 	},
// };
// console.log(num.checkNumericRange(20));

// var num1 = { min: 50, max: 60 };

// console.log(num.checkNumericRange.call(num1, 49));
// console.log(num.checkNumericRange.apply(num1, [52]));

// var checkNumber = num.checkNumericRange.bind(num1);

// console.log(checkNumber(56));
