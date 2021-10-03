import fetch from "node-fetch";
import cheerio from "cheerio";
import PromptSync from "prompt-sync";

const prompt = PromptSync();
var query = prompt("zort ?");
console.log(query);
const main = async () => {
	const response = await fetch("https://www.gsmarena.com/res.php3?sSearch=" + query);
	const body = await response.text();
	const $ = cheerio.load(body);
	const onDiv = $("div.makers");
	return onDiv
		.find("li")
		.map(function (i, el) {
			return "https://www.gsmarena.com/" + $(this).find("a").attr("href");
		})
		.toArray();
};

const parser_ph = async (link) => {
	let info_ph = new Array();
	for (let i of link) {
		const resss = await fetch(i);
		const body_2 = await resss.text();
		const $2 = cheerio.load(body_2);
		const name = $2("h1.specs-phone-name-title").text();
		const helper_1 = $2("ul.specs-spotlight-features");
		const infos = $2("li.specs-brief");
		var info_e = infos
			.find("span")
			.map(function (i, el) {
				return $2(this).text() || null;
			})
			.toArray();

		var topl = helper_1
			.find("li.accented")
			.map(function (i, el) {
				return ($2(this).find("span").text() + " " + $2(this).find("div").text()).trim() || null;
			})
			.toArray();
		topl.unshift(info_e);
		topl.unshift(name);
		info_ph.push(topl);
	}
	return info_ph;
};

let zort = main();

zort.then(function (result) {
	parser_ph(result).then((result) => {
		for (let i of result) {
			for (let x of i) {
				if (i.indexOf(x) == 1) {
					for (let y of x) {
						console.log(y);
					}
				} else {
					console.log(x);
				}
			}
			console.log("\n");
		}
	});
});
