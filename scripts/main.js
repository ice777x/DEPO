let Person = function (name) {
	this.name = name;
};
Person.prototype.introduce = function () {
	console.log(`Merhaba ${this.name}`);
};

let zort = new Person("zort");
zort.introduce();
