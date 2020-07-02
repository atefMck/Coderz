window.onload = function() {
	console.log("working")
	var box = $('.box');

	TweenLite.from(box, 1, {autoAlpha:0, delay:1});
	atef()
}