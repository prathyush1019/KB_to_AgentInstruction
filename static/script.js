let instructionTemplates = {};

window.addEventListener('DOMContentLoaded', async () => {
    try {
        const res = await fetch('/api/templates?t=' + new Date().getTime());
        if (res.ok) {
            instructionTemplates = await res.json();
            const activeType = document.querySelector('input[name="instructionType"]:checked').value;
            if (instructionTemplates[activeType]) {
                document.getElementById('instructionTemplateText').value = instructionTemplates[activeType];
            }
        }

    } catch (e) {
        console.error("Failed to load templates", e);
    }
});

document.querySelectorAll('input[name="instructionType"]').forEach(radio => {
    radio.addEventListener('change', (e) => {
        const type = e.target.value;
        if (instructionTemplates[type]) {
            document.getElementById('instructionTemplateText').value = instructionTemplates[type];
        }
    });
});

document.getElementById('evalForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const inputKb = document.getElementById('inputKb').value;
    const submitBtn = document.getElementById('submitBtn');
    const btnText = submitBtn.querySelector('.btn-text');
    const loader = submitBtn.querySelector('.loader');
    const resultSection = document.getElementById('resultSection');

    // Reset UI
    submitBtn.disabled = true;
    btnText.classList.add('hidden');
    loader.classList.remove('hidden');
    resultSection.classList.add('hidden');
    document.getElementById('instructionFormSection').classList.add('hidden');
    document.getElementById('instructionsContainer').classList.add('hidden');
    if(document.getElementById('qaFormSection')) document.getElementById('qaFormSection').classList.add('hidden');
    if(document.getElementById('qaContainer')) document.getElementById('qaContainer').classList.add('hidden');

    try {
        const response = await fetch('/api/evaluate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                input_kb: inputKb
            })
        });

        if (!response.ok) {
            const errData = await response.json();
            throw new Error(errData.error || 'Something went wrong');
        }

        const data = await response.json();

        displayResults(data.score, data.reasoning, data.improved_kb);

    } catch (error) {
        alert('Error: ' + error.message);
    } finally {
        submitBtn.disabled = false;
        btnText.classList.remove('hidden');
        loader.classList.add('hidden');
    }
});

function displayResults(score, reasoning, improved_kb) {
    const resultSection = document.getElementById('resultSection');
    const circle = document.querySelector('.circle');
    const percentageText = document.querySelector('.percentage');
    const reasoningText = document.getElementById('reasoningText');
    const instructionFormSection = document.getElementById('instructionFormSection');
    const inputKbField = document.getElementById('inputKb');

    resultSection.classList.remove('hidden');

    // Set color based on score
    let color = '#ef4444'; // red
    if (score >= 75) color = '#10b981'; // green
    else if (score >= 50) color = '#f59e0b'; // yellow

    circle.style.stroke = color;

    // Animate circle
    setTimeout(() => {
        circle.style.strokeDasharray = `${score}, 100`;
        animateValue(percentageText, 0, score, 1000);
    }, 100);

    reasoningText.textContent = reasoning;

    if (improved_kb) {
        // AI reconstructed the KB because it was below standard
        inputKbField.value = improved_kb;
        inputKbField.style.borderColor = '#10b981';
        inputKbField.style.boxShadow = '0 0 0 2px rgba(16, 185, 129, 0.3)';
    } else {
        // Reset border if it was previously changed
        inputKbField.style.borderColor = '';
        inputKbField.style.boxShadow = '';
    }

    if (score >= 75) {
        instructionFormSection.classList.remove('hidden');
        if(document.getElementById('qaFormSection')) document.getElementById('qaFormSection').classList.remove('hidden');

        // Scroll down to the instruction form smoothly
        setTimeout(() => {
            instructionFormSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 100);

        // Populate initial template
        const activeType = document.querySelector('input[name="instructionType"]:checked').value;
        if (instructionTemplates[activeType] && !document.getElementById('instructionTemplateText').value) {
            document.getElementById('instructionTemplateText').value = instructionTemplates[activeType];
        }
    }
}

document.getElementById('generateForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const inputKb = document.getElementById('inputKb').value;
    const instructionTemplate = document.getElementById('instructionTemplateText').value;
    const extraInstructions = document.getElementById('extraInstructions').value;

    const generateBtn = document.getElementById('generateBtn');
    const btnText = generateBtn.querySelector('.btn-text');
    const loader = generateBtn.querySelector('.loader');

    const instructionsContainer = document.getElementById('instructionsContainer');
    const finalInstructions = document.getElementById('finalInstructions');

    generateBtn.disabled = true;
    btnText.classList.add('hidden');
    loader.classList.remove('hidden');
    instructionsContainer.classList.add('hidden');
    document.getElementById('downloadBtn').classList.add('hidden');

    try {
        const response = await fetch('/api/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                input_kb: inputKb,
                instruction_template: instructionTemplate,
                extra_instructions: extraInstructions
            })
        });

        if (!response.ok) {
            const errData = await response.json();
            throw new Error(errData.error || 'Something went wrong');
        }

        const data = await response.json();

        instructionsContainer.classList.remove('hidden');
        finalInstructions.textContent = data.final_instructions;
        document.getElementById('downloadBtn').classList.remove('hidden');

        document.getElementById('auditorScore').textContent = data.auditor_score;
        document.getElementById('auditorReasoning').textContent = data.auditor_reasoning;
        if (data.was_refined) {
            document.getElementById('refinedStatus').textContent = "⚠️ Initial generation failed criteria. Refiner Agent successfully reconstructed instructions.";
            document.getElementById('refinedStatus').style.color = "#f59e0b"; // yellow
        } else {
            document.getElementById('refinedStatus').textContent = "✅ Initial generation passed all criteria.";
            document.getElementById('refinedStatus').style.color = "#10b981"; // green
        }

        // Scroll down to the generated agent instructions code smoothly
        setTimeout(() => {
            instructionsContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 100);

    } catch (error) {
        alert('Error: ' + error.message);
    } finally {
        generateBtn.disabled = false;
        btnText.classList.remove('hidden');
        loader.classList.add('hidden');
    }
});

function animateValue(obj, start, end, duration) {
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        obj.innerHTML = Math.floor(progress * (end - start) + start) + '%';
        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    window.requestAnimationFrame(step);
}

document.getElementById('downloadBtn').addEventListener('click', () => {
    const finalInstructions = document.getElementById('finalInstructions').textContent;
    if (!finalInstructions) return;

    const blob = new Blob([finalInstructions], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'agent_instructions.txt';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
});

document.getElementById('generateQaBtn').addEventListener('click', async () => {
    const inputKb = document.getElementById('inputKb').value;
    const generateQaBtn = document.getElementById('generateQaBtn');
    const btnText = generateQaBtn.querySelector('.btn-text');
    const loader = generateQaBtn.querySelector('.loader');
    const qaContainer = document.getElementById('qaContainer');
    const qaOutput = document.getElementById('qaOutput');

    generateQaBtn.disabled = true;
    btnText.classList.add('hidden');
    loader.classList.remove('hidden');
    qaContainer.classList.add('hidden');

    try {
        const response = await fetch('/api/generate_qa', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ input_kb: inputKb })
        });

        if (!response.ok) {
            const errData = await response.json();
            throw new Error(errData.error || 'Something went wrong');
        }

        const data = await response.json();
        
        const jsonStr = JSON.stringify(data.qa_list, null, 4);
        qaOutput.textContent = jsonStr;
        qaContainer.classList.remove('hidden');

    } catch (error) {
        alert('Error: ' + error.message);
    } finally {
        generateQaBtn.disabled = false;
        btnText.classList.remove('hidden');
        loader.classList.add('hidden');
    }
});

document.getElementById('downloadQaBtn').addEventListener('click', () => {
    const qaText = document.getElementById('qaOutput').textContent;
    if (!qaText) return;

    const blob = new Blob([qaText], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'sample_qa.txt';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
});
