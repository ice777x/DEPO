let Person = function (name) {
	this.name = name;
};
Person.prototype.introduce = function () {
	console.log(`Merhaba ${this.name}`);
};

let Teacher = function (name, branch) {
	Person.call(this, name);
	this.branch = branch;
};

Teacher.prototype = Object.create(Person.prototype);
Teacher.prototype.constructor = Teacher;
Teacher.prototype.teach = function () {
	console.log("I teacher " + this.branch);
};

let Student = function (name, numbers) {
	Person.call(this, name);
	this.numbers = numbers;
};

Student.prototype = Object.create(Person.prototype);
Student.prototype.constructor = Student;
Student.prototype.study = function () {
	console.log("My student number is " + this.numbers + " I've already studied hard");
};

let Headmaster = function (name, branch) {
	Teacher.call(this, name, branch);
};

Headmaster.prototype = Object.create(Teacher.prototype);
Headmaster.prototype.constructor = Headmaster;

Headmaster.prototype.shareTask = function () {
	console.log("Ive shared all work");
};

let p1 = new Person("zort");
p1.introduce();

let t1 = new Teacher("sadik", "math");
t1.introduce();
t1.teach();

let s1 = new Student("yigit", 100);
s1.introduce();
s1.study();

let h1 = new Headmaster("ahmet", "physics");
h1.introduce(); // Person
h1.teach(); // Teacher
h1.shareTask(); // Headmaster
