function toggleMenu(btn) {
	const container = document.querySelector("#menu-wrapper");
	const expanded = container.getAttribute("aria-expanded") === "true";
	// Determine container (colored vs white)
	container.setAttribute("aria-expanded", (!expanded).toString());
	// Expand/collapse container
	btn.classList.toggle("bg-brand");
	container.style.gridTemplateRows = expanded ? "0fr" : "1fr";
}

function toggleFaq(btn) {
	const expanded = btn.getAttribute("aria-expanded") === "true";
	// Determine container (colored vs white)
	const card = btn.parentElement;
	const contentWrap = card.querySelector(".grid");

	// Toggle styles
	btn.setAttribute("aria-expanded", (!expanded).toString());
	const icon = btn.querySelector("svg");
	icon.classList.toggle("rotate-45");

	// Expand/collapse container
	contentWrap.style.gridTemplateRows = expanded ? "0fr" : "1fr";
}

const swiper = new Swiper(".marquee-swiper", {
	loop: true,
	centeredSlides: true,
	allowTouchMove: false,
	slidesPerView: "auto",
	spaceBetween: 25,
	speed: 8000,
	freeMode: {
		enabled: true,
		momentum: false,
	},
	autoplay: {
		delay: 0,
		disableOnInteraction: false,
		pauseOnMouseEnter: false,
	},
});

const contentArea = document.querySelector(".content-area");
const progressBar = document.querySelector("#scroll-progress");

contentArea.addEventListener("scroll", () => {
	const doc_height = contentArea.scrollHeight - contentArea.clientHeight;
	const progress = contentArea.scrollTop;
	const percentage = (progress / doc_height) * 100;

	progressBar.style.height = `${percentage}%`;
});
