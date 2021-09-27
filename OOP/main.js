// var p = new Promise(function (resolve, reject) {
// 	if (true) {
// 		resolve("success");
// 	} else {
// 		reject("Fail");
// 	}
// });

// p.then(function (data) {
// 	console.log(data);
// }).catch(function (err) {
// 	console.log(err);
// });

// new Promise(function (resolve, reject) {
// 	setTimeout(() => {
// 		resolve(5);
// 	}, 1000);
// })
// 	.then(function (data) {
// 		console.log(data);
// 		return data ** 2;
// 	})
// 	.then(function (number) {
// 		console.log(number);
// 		return number ** 2;
// 	})
// 	.then(function (number) {
// 		console.log(number);
// 	});

const isMomHappy = true;

const willGetNewPhone = new Promise((resolve, reject) => {
	if (isMomHappy) {
		const phone = {
			name: "iphone 8",
			price: 4000,
			color: "silver",
		};
		resolve(phone);
	} else {
		const error = new Error("ZOoooooooort");
		reject(error);
	}
});

const showToFriends = function (phone) {
	const message = "He friends this is my new phone " + phone.name;
	return Promise.resolve(message);
};

const askMom = function () {
	willGetNewPhone
		.then(showToFriends) // bundan sonra yakaliyoruz
		.then((message) => console.log(message))
		.catch((err) => {
			console.log(err);
		});
};
askMom();
