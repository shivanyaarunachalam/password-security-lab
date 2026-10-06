const passwordInput = document.getElementById("password");
const analyzeButton = document.getElementById("analyzeButton");
const results = document.getElementById("results");

const lengthElement = document.getElementById("length");
const entropyElement = document.getElementById("entropy");
const strengthElement = document.getElementById("strength");

const sha256Element = document.getElementById("sha256");
const saltElement = document.getElementById("salt");
const saltedHashElement = document.getElementById("saltedHash");
const saltTwoElement = document.getElementById("saltTwo");
const saltedHashTwoElement = document.getElementById("saltedHashTwo");

analyzeButton.addEventListener("click", analyzePassword);


passwordInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        analyzePassword();
    }
});


async function analyzePassword() {
    const password = passwordInput.value;

    if (!password) {
        alert("Please enter a fictional password.");
        return;
    }

    analyzeButton.disabled = true;
    analyzeButton.textContent = "Analyzing...";

    try {
        const response = await fetch("/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                password: password
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Analysis failed.");
        }

        lengthElement.textContent = data.length;
        entropyElement.textContent = data.entropy;
        strengthElement.textContent = data.strength;

        sha256Element.textContent = data.sha256;
        saltElement.textContent = data.salt_one;
saltedHashElement.textContent = data.salted_hash_one;

saltTwoElement.textContent = data.salt_two;
saltedHashTwoElement.textContent = data.salted_hash_two;

        results.classList.remove("hidden");

    } catch (error) {
        alert(error.message);

    } finally {
        analyzeButton.disabled = false;
        analyzeButton.textContent = "Analyze";
    }
}