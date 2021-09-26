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

let Question = function (hobby) {
	switch (hobby) {
		case "car":
			return function (name) {
				console.log(name, "do you have a car");
			};
		case "book":
			return function (name) {
				console.log(name, "what is a favourite book ?");
			};
		case "software":
			return function (name, type) {
				console.log(name, "are you interested in python ?", type);
			};
		default:
			return function (name) {
				console.log(name, "how are you?");
			};
	}
};

var carQuestion = Question("software");

carQuestion("cinar", "zort");
