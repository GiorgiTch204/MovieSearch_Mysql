const API_URL = "http://127.0.0.1:8000";

async function searchMovies() {

    const query =
        document.getElementById("queryInput").value.trim();

    if (!query) {
        alert("შეიყვანეთ საძიებო ტექსტი");
        return;
    }

    const loader =
        document.getElementById("loader");

    const resultsGrid =
        document.getElementById("resultsGrid");

    loader.classList.remove("hidden");

    resultsGrid.innerHTML = "";

    try {

        const response = await fetch(
            `${API_URL}/search?query=${encodeURIComponent(query)}&limit=10`
        );

        const data = await response.json();

        loader.classList.add("hidden");

        if (!data.results.length) {

            resultsGrid.innerHTML = `
                <div class="col-span-full text-center text-slate-400">
                    შედეგები ვერ მოიძებნა
                </div>
            `;

            return;
        }

        data.results.forEach(movie => {

            const similarity =
                (movie.score * 100).toFixed(2);

            const card = document.createElement("div");

            card.className =
                "movie-card bg-slate-900 border border-slate-800 rounded-2xl p-6";

            card.innerHTML = `
                <h3 class="text-xl font-semibold mb-3">
                    ${movie.title}
                </h3>

                <p class="text-slate-400 text-sm leading-6">
                    ${movie.overview}
                </p>

                <div class="mt-4 flex items-center justify-between">

                    <span class="text-xs text-slate-500">
                        Semantic Similarity
                    </span>

                    <span class="text-green-400 font-semibold">
                        ${similarity}%
                    </span>

                </div>
            `;

            resultsGrid.appendChild(card);

        });

    } catch (error) {

        loader.classList.add("hidden");

        console.error(error);

        resultsGrid.innerHTML = `
            <div class="col-span-full text-center text-red-400">
                Server Error
            </div>
        `;
    }
}

document
    .getElementById("queryInput")
    .addEventListener("keypress", function(event) {

        if (event.key === "Enter") {
            searchMovies();
        }
    });