// var use = {
// 	name: "Sadik Turan",
// };

// try {
// 	// console.log(myFunction());
// 	console.log(use.mail);
// 	if (!use.mail) {
// 		throw new TypeError("User has no email");
// 	}
// } catch (e) {
// 	console.log(e);
// } finally {
// 	console.log("finally block");
// }

// const arr = [1, 2, 3, 4, 5, 6, 7, 8];

// let even = arr.filter((a) => a % 2 == 0);

// ES5

// let list = {
// 	category: "phone",
// 	names: ["iphone 8", "samsung s8", "iphone 7"],
// 	call: function () {
// 		var self = this;
// 		this.names.map(function (name) {
// 			console.log(`${self.category} ${name}`);
// 		});
// 	},
// };

// ES6

// let list = {
// 	category: "phone",
// 	names: ["iphone 8", "samsung s8", "iphone 7"],
// 	call: function () {
// 		this.names.map((name) => {
// 			console.log(`${this.category} ${name}`);
// 		});
// 	},
// };

// list.call();

// ES5

// function Game() {
// 	this.live = 0;
// 	this.addLive = function () {
//         var self = this;
// 		this.OneUp = setInterval(function () {
// 			console.log(++self.live);
// 		}, 1000);
// 	};
// }

// ES6

// function Game() {
// 	this.live = 0;
// 	this.addLive = function () {
// 		this.OneUp = setInterval(() => {
// 			console.log(++this.live);
// 		}, 1200);
// 	};
// }

// let player = new Game();
// player.addLive();

// Spread Operator

// function getTotal(a, b, c) {
// 	return a + b + c;
// }

// console.log(getTotal(10, 20, 30));

// let numbers = [10, 20, 30];

// // ES5

// console.log(getTotal.apply(null, numbers));

// // ES6

// console.log(getTotal(...numbers));

//////

// let arr1 = ["two", "three"];
// let arr2 = ["one", "four", "five"];

// // arr1.push(...arr2);
// // arr1.unshift(...arr2);

// let arr3 = ["one", ...arr1, "four", "five"];

// // console.log(arr1);

// console.log(arr3);

// Rest Parameters

// ES5

// function sum() {
// 	let arr = Array.prototype.slice.call(arguments);
// 	console.log(arr);

// 	let result = 0;
// 	arr.forEach(function (item) {
// 		result += item;
// 	});
// 	return result;
// }

// console.log(sum(10, 20, 30));

// ES6

// function sum(...arr) {
// 	let result = 0;
// 	arr.forEach((item) => (result += item));
// 	return result;
// }

// console.log(sum(10, 20, 30));

// function isDriver(age, zort, ...years) {
// 	console.log(age);
// 	console.log(zort);
// 	console.log(years);
// years.forEach((year) => console.log(2021 - year >= 18));
// }

// isDriver(1990, 2000, 1993, 2005);

///////////////////////////////////////////////////

// Destructing

// destructing assigment

// var a, b, rest;
// [a, b] = [10, 20];

// console.log(a);
// console.log(b);

// [a, b, ...rest] = [10, 20, 30, 40, 50, 60];

// console.log(a);
// console.log(b);
// console.log(rest);

// ({ a, b } = { a: 10, b: 20 });
// console.log(a);
// console.log(b);

// ({ a, b, ...rest } = { a: 10, b: 20, c: 30, d: 40 });

// console.log(a);
// console.log(b);
// console.log(rest);

//////////////////////////////////////////////////////////

// const arrConfig = ["localhost", "8080", "900"];

// // ES5
// // var server = arrConfig[0];
// // var port = arrConfig[1];
// // var timeout = arrConfig[2];

// // ES6

// const [server, port, timeout] = arrConfig;

// console.log(server, port, timeout);

//////////////////////////////////////////////////////////////////

// Object destructing

// const objConfig = {
// 	server: "localhost",
// 	port: "8080",
// 	timeout: 800,
// };

// var server = objConfig.server;
// var port = objConfig.port;
// var timeout = objConfig.timeout;

// const { server, port, timeout } = objConfig;

// console.log(server, port, timeout);

// let { timeout: t } = objConfig;
// console.log(t);

// const { server, port, timeout = 900 } = objConfig;

// console.log(server, port, timeout);

// const days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];

// const [, , wed, , fri] = days;
// console.log(wed, fri);

///////////////////////////////

// var a = [1, 2, 3, 4, "zort", 5, 6, 7, 8, 9, 10];

// for (let box of a) {
// 	console.log(box);
// }

// let numbers = ["a", "b", "c"];

// let entries = numbers.entries();

///////////////////////////////////////////////////////////////

// Maps: key/value pairs (collectiob)

// let val;
// const numbers = new Map();
// numbers.set(1, "one");
// numbers.set("2", "two");
// numbers.set(3, "three");
// numbers.set("four", "four");

// val = numbers;
// val = numbers.get("1");
// val = numbers.get("2");
// val = numbers.size;
// val = numbers.has(1);
// val = numbers.delete("four");
// val = numbers.has("four");

// for (var [key, value] of numbers) {
// 	console.log(key, value);
// }

// for (var [key, value] of numbers.entries()) {
// 	console.log(key, value);
// }

// for (var key of numbers.keys()) {
// 	console.log(key);
// }
// for (var value of numbers.values()) {
// 	console.log(value);
// }

// numbers.forEach(function (key, value) {
// 	console.log(key, value);
// });

// var first = new Map([
// 	[1, "One"],
// 	[2, "two"],
// 	[3, "three"],
// ]);
// var second = new Map([
// 	[4, "Four"],
// 	[5, "Five"],
// ]);

// var merged = new Map([...first, ...second]);

// console.log(merged);

///////////////////////////////////////////////////////////

// Sets (Collection - Unique value)

// let val;

// var iki = 2;
// var mySet = new Set();
// mySet.add(1);
// mySet.add(2);
// mySet.add(4);
// mySet.add(iki);
// mySet.add("iki");
// mySet.add({ a: 1, b: 32 });

// var obj = { a: 1, b: 2 };

// mySet.add(obj);

// val = mySet.has(1);
// val = mySet.has(3);
// val = mySet.has(4);
// val = mySet.has(obj);

// mySet.delete(1);
// console.log(val);
// console.log(mySet);

// for (let item of mySet) {
// 	console.log(item);
// }

// for (item of mySet.values()) {
// 	console.log(item);
// }
// for (item of mySet.keys()) {
// 	console.log(item);
// }

// for (let [key, value] of mySet.entries()) {
// 	console.log(key, value);
// }

// console.log(Array.from(mySet));

// let mySet2 = new Set([1, 2, 3, 4]);
// // console.log(mySet2);

// // intersect

// var intersect = new Set([...mySet].filter((x) => mySet2.has(x)));

// console.log(intersect);
// // difference

// var differece = new Set([...mySet].filter((x) => !mySet2.has(x)));

// console.log(differece);

//////////////////////////////////////////////////////////////////////////////

// Classes

// ES5

// var PersonES5 = function (name, job, yearOfBirth) {
// 	this.name = name;
// 	this.job = job;
// 	this.yearOfBirth = yearOfBirth;
// };
// PersonES5.prototype.calculateAge = function () {
// 	return 2021 - this.yearOfBirth;
// };

// var yigit = new PersonES5("yigit", "student", 2010);

// // console.log(yigit.calculateAge());
// console.log(yigit);

// ES6

// class PersonES6 {
// 	constructor(name, job, yearOfBirth) {
// 		this.name = name;
// 		this.job = job;
// 		this.yearOfBirth = yearOfBirth;
// 	}
// 	calculateAge() {
// 		return 2021 - this.yearOfBirth;
// 	}
// 	static sayHi() {
// 		console.log("Hello there");
// 	}
// }

// let emel = new PersonES6("emel", "teacher", 1989);

// // console.log(emel.calculateAge());
// console.log(emel);

// PersonES6.sayHi();

// class Point {
// 	constructor(x, y) {
// 		this.x = x;
// 		this.y = y;
// 	}
// 	static distance(a, b) {
// 		const dx = a.x - b.x;
// 		const dy = a.y - b.y;

// 		return Math.hypot(dx, dy);
// 	}
// }

// const d1 = new Point(10, 10);
// const d2 = new Point(20, 20);

// console.log(Point.distance(d1, d2));

// Sub Classes

// ES5

// function PersonES5(firstName, lastName) {
// 	this.firstName = firstName;
// 	this.lastName = lastName;
// }
// PersonES5.prototype.sayHi = function () {
// 	return `Hello I'm ${this.firstName} ${this.lastName}`;
// };

// function CustomerES5(firstname, lastName, phone, username) {
// 	PersonES5.call(this, firstname, lastName);
// 	this.phone = phone;
// 	this.username = username;
// }

// CustomerES5.prototype = Object.create(PersonES5.prototype);

// var customer = new CustomerES5("sena", "turan", "12312312", "senaturan");
// console.log(customer.sayHi());
// console.log(customer);
// // ES6

// class PersonES6 {
// 	constructor(firstName, lastName) {
// 		this.firstName = firstName;
// 		this.lastName = lastName;
// 	}
// 	sayHi() {
// 		return `Hello I'm ${this.firstName} ${this.lastName}`;
// 	}
// }

// class CustomerES6 extends PersonES6 {
// 	constructor(firstName, lastName, phone, username) {
// 		super(firstName, lastName);
// 		this.phone = phone;
// 		this.username = username;
// 	}
// 	static getTotal() {
// 		return 1000;
// 	}
// }

// let customer1 = new CustomerES6("sena", "turan", "13412", "senaturan");
// console.log(customer1.sayHi());
// console.log(customer1);
// console.log(CustomerES6.getTotal());
