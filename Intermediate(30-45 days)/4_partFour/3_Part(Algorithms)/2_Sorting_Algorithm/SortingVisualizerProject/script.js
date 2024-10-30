let array = [];

function generateArray() {
    array = Array.from({ length: 20 }, () => Math.floor(Math.random() * 100));
    displayArray();
}

function displayArray() {
    const arrayContainer = document.getElementById("array");
    arrayContainer.innerHTML = "";
    array.forEach(value => {
        const bar = document.createElement("div");
        bar.style.height = `${value}px`;
        bar.className = "bar";
        arrayContainer.appendChild(bar);
    });
}

async function bubbleSort() {
    const n = array.length;
    for (let i = 0; i < n; i++) {
        let swapped = false;
        for (let j = 0; j < n - i - 1; j++) {
            if (array[j] > array[j + 1]) {
                [array[j], array[j + 1]] = [array[j + 1], array[j]];
                swapped = true;
                displayArray();
                await new Promise(resolve => setTimeout(resolve, 100)); // Delay for visualization
            }
        }
        if (!swapped) break;
    }
}

async function selectionSort() {
    const n = array.length;
    for (let i = 0; i < n; i++) {
        let minIndex = i;
        for (let j = i + 1; j < n; j++) {
            if (array[j] < array[minIndex]) {
                minIndex = j;
            }
        }
        [array[i], array[minIndex]] = [array[minIndex], array[i]];
        displayArray();
        await new Promise(resolve => setTimeout(resolve, 100)); // Delay for visualization
    }
}

async function insertionSort() {
    const n = array.length;
    for (let i = 1; i < n; i++) {
        const key = array[i];
        let j = i - 1;
        while (j >= 0 && array[j] > key) {
            array[j + 1] = array[j];
            j--;
            displayArray();
            await new Promise(resolve => setTimeout(resolve, 100)); // Delay for visualization
        }
        array[j + 1] = key;
    }
    displayArray();
}
