let playerName = "";
let score = 0;
let aktualniOtazka = 0;

const otazky = [
    {
        otazka: "Jaký příkaz slouží k zobrazení obsahu adresáře v Linuxu?",
        odpovedi: ["ls", "cd", "mkdir", "rm"],
        spravne: 0
    },

    {
        otazka: "Který uživatel má v Linuxu nejvyšší oprávnění?",
        odpovedi: ["admin", "guest", "root", "sudo"],
        spravne: 2
    },

    {
        otazka: "Jaký příkaz vytvoří nový adresář?",
        odpovedi: ["touch", "mkdir", "rmdir", "nano"],
        spravne: 1
    },
];


function startGame() {
    // vezmeme jmeno hrace a pokud neni -> eror
    playerName = document.getElementById("player-name").value;
    if (playerName.trim() === "") {
        alert("Prosím zadejte své jméno!");
        return;
    }
    // skryjeme uvodni obrazovku
    document.getElementById("pocatecni-obrazovka").style.display = "none";
    document.getElementById("quiz-screen").style.display = "block";

    // zobrazime prvni otazku
    showQuestion();
}

function showQuestion() {
    const aktualni_otazka = otazky[aktualniOtazka];
    const zobrazena_otazka = document.getElementById("otazka");
    const zobrazene_odpovedi = document.getElementById("odpovedi");

    // vymazeme predchozi odpovedi
    zobrazene_odpovedi.innerHTML = "";

    // zobrazime aktualni otazku
    zobrazena_otazka.innerText = aktualni_otazka.otazka;

    // zobrazime odpovedi
    aktualni_otazka.odpovedi.forEach((odpoved, index) => {
        const button = document.createElement("button");
        button.innerText = odpoved;
        button.classList.add("button-odpovedi");
        button.onclick = () => checkAnswer(index);
        zobrazene_odpovedi.appendChild(button);
    });
}

function checkAnswer(zvolenaOdpoved) {
    const aktualni_otazka = otazky[aktualniOtazka];

    // Pokud je odpověď správná
    if (zvolenaOdpoved === aktualni_otazka.spravne) {
        score += 1;
    }

    // Další otázka nebo výsledek
    aktualniOtazka++;

    if (aktualniOtazka < otazky.length) {
        showQuestion();
    } else {
        showResult();
    }
}

function showResult() {
    document.getElementById("quiz-screen").style.display = "none";
    document.getElementById("result-screen").style.display = "block";

    const vysledekText = `${playerName}, získal(a) jsi ${score} z ${otazky.length} bodů! 🎉`;
    document.getElementById("final-score").innerText = vysledekText;
}

