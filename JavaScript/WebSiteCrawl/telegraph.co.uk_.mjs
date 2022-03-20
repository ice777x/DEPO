import fetch from "node-fetch";
import cheerio from "cheerio";

let url = "https://www.telegraph.co.uk/news/";

const response = await fetch(url);
const body = await response.text();
const $ = cheerio.load(body);
const base = "https://www.telegraph.co.uk";
const list_li = $("section.article-list").children("ul");
var li_s = list_li
	.find("li")
	.map(function (i, el) {
		if ($(this).find("a.e-byline__link").attr("href") === undefined) {
			var auth = null;
		} else {
			var auth = base + $(this).find("a.e-byline__link").attr("href");
		}
		return {
			title: $(this).find("span.list-headline__text").text().trim("\n"),
			link: base + $(this).find("a.list-headline__link").attr("href"),
			author: $(this).find("a.e-byline__link").text().trim().replace("\n", " ") || null,
			author_link: auth,
		};
	})
	.toArray();

const authot_parser = async (data) => {
	if (data.author_link === null) {
		return data;
	} else {
		const auth_response = await fetch(data.author_link);
		const auth_body = await auth_response.text();
		const $auth = cheerio.load(auth_body);
		const auth_article_list = $("section.article-list").children("ul");
		let author_li = auth_article_list
			.find("li")
			.map(function (i, el) {
				return {
					title: $auth(this).find("a.list-headline__link").text().trim("\n") || null,
					articleLink: base + $auth(this).find("a.list-headline__link").attr("href") || null,
					articleSpot: $auth(this).find("p.e-standfirst").text().trim() || null,
				};
			})
			.toArray();
		return {
			title: data.title,
			link: data.link,
			author: {
				name: data.author,
				link: data.author_link,
				articles: author_li,
			},
		};
	}
};

for (let i of li_s) {
	let aut = authot_parser(i);
	aut.then((result) => {
		console.log(result);
	});
}
