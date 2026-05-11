let instructionTemplates = {};

window.addEventListener('DOMContentLoaded', async () => {
    // Initial fetch of templates
    try {
        const res = await fetch('/api/templates?t=' + new Date().getTime());
        if (res.ok) {
            instructionTemplates = await res.json();
            updateTemplate();
        }
    } catch (e) {
        console.error("Failed to load templates", e);
    }

    // Sidebar Navigation
    const navButtons = document.querySelectorAll('.nav-btn');
    const tabContents = document.querySelectorAll('.tab-content');
    const pageTitle = document.getElementById('page-title');
    const pageSubtitle = document.getElementById('page-subtitle');

    navButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const target = btn.dataset.tab;

            navButtons.forEach(b => b.classList.remove('active'));
            tabContents.forEach(c => c.classList.remove('active'));

            btn.classList.add('active');
            document.getElementById(target).classList.add('active');

            if (target === 'agent-tab') {
                pageTitle.textContent = 'Agent Instruction Generator';
                pageSubtitle.textContent = 'Create production-ready instructions for your AI voice agents.';
            } else {
                pageTitle.textContent = 'Knowledge Base Auditor';
                pageSubtitle.textContent = 'Score and reconstruct your KB for maximum accuracy.';
            }
        });
    });
});

// Update Template UI
document.querySelectorAll('input[name="instructionType"], input[name="callDirection"]').forEach(radio => {
    radio.addEventListener('change', () => {
        updateTemplate();
    });
});

function updateTemplate() {
    const activeType = document.querySelector('input[name="instructionType"]:checked').value;
    const activeDir = document.querySelector('input[name="callDirection"]:checked').value;
    
    if (instructionTemplates[activeType] && instructionTemplates[activeType][activeDir]) {
        document.getElementById('instructionTemplateText').value = instructionTemplates[activeType][activeDir].trim();
    }
}

// ==========================================
// KB EVALUATOR MODULE (Strictly KB Audit)
// ==========================================
const evalForm = document.getElementById('evalForm');
if (evalForm) {
    evalForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const inputKb = document.getElementById('inputKb').value;
        const submitBtn = document.getElementById('submitBtn');
        const resultSection = document.getElementById('resultSection');
        const loadingOverlay = document.getElementById('loadingOverlay');

        submitBtn.disabled = true;
        loadingOverlay.classList.remove('hidden');
        resultSection.classList.add('hidden');
        if(document.getElementById('qaFormSection')) document.getElementById('qaFormSection').classList.add('hidden');

        try {
            const response = await fetch('/api/evaluate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ input_kb: inputKb })
            });

            if (!response.ok) throw new Error('Evaluation failed');

            const data = await response.json();
            displayEvalResults(data.score, data.reasoning, data.improved_kb);

        } catch (error) {
            alert('Error: ' + error.message);
        } finally {
            submitBtn.disabled = false;
            document.getElementById('loadingOverlay').classList.add('hidden');
        }
    });
}

function displayEvalResults(score, reasoning, improved_kb) {
    const resultSection = document.getElementById('resultSection');
    const circle = document.querySelector('.circle');
    const percentageText = document.querySelector('.percentage');
    const reasoningText = document.getElementById('reasoningText');
    const inputKbField = document.getElementById('inputKb');

    resultSection.classList.remove('hidden');

    let color = '#ef4444'; 
    if (score >= 75) color = '#10b981';
    else if (score >= 50) color = '#f59e0b';

    circle.style.stroke = color;

    setTimeout(() => {
        circle.style.strokeDasharray = `${score}, 100`;
        animateValue(percentageText, 0, score, 1000);
    }, 100);

    reasoningText.textContent = reasoning;

    if (improved_kb) {
        inputKbField.value = improved_kb;
        inputKbField.style.borderColor = '#10b981';
    }

    if(document.getElementById('qaFormSection')) document.getElementById('qaFormSection').classList.remove('hidden');
}

// ==========================================
// AGENT GENERATOR MODULE (Strictly Generation)
// ==========================================
const generateForm = document.getElementById('generateForm');
if (generateForm) {
    generateForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const companyName = document.getElementById('companyName').value;
        const agentName = document.getElementById('agentName').value;
        const inputKb = document.getElementById('agentKbInput').value;
        const instructionTemplate = document.getElementById('instructionTemplateText').value;
        const extraInstructions = document.getElementById('extraInstructions').value;

        const generateBtn = document.getElementById('generateBtn');
        const btnText = generateBtn.querySelector('.btn-text');
        const loader = generateBtn.querySelector('.loader');

        const instructionsContainer = document.getElementById('instructionsContainer');
        const finalInstructions = document.getElementById('finalInstructions');
        const loadingOverlay = document.getElementById('loadingOverlay');

        generateBtn.disabled = true;
        loadingOverlay.classList.remove('hidden');
        instructionsContainer.classList.add('hidden');
        document.getElementById('downloadBtn').classList.add('hidden');

        try {
            const response = await fetch('/api/generate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    input_kb: inputKb,
                    company_name: companyName,
                    agent_name: agentName,
                    instruction_template: instructionTemplate,
                    extra_instructions: extraInstructions
                })
            });

            if (!response.ok) throw new Error('Generation failed');

            const data = await response.json();

            instructionsContainer.classList.remove('hidden');
            finalInstructions.textContent = data.final_instructions;
            document.getElementById('downloadBtn').classList.remove('hidden');

            document.getElementById('auditorScore').textContent = data.auditor_score;
            document.getElementById('auditorReasoning').textContent = data.auditor_reasoning;
            
            const refinedStatus = document.getElementById('refinedStatus');
            if (data.was_refined) {
                refinedStatus.textContent = "⚠️ REFINED: Auto-corrected to meet standards.";
                refinedStatus.style.color = "#f59e0b";
            } else {
                refinedStatus.textContent = "✅ VERIFIED: Passed initial criteria.";
                refinedStatus.style.color = "#10b981";
            }

        } catch (error) {
            alert('Error: ' + error.message);
        } finally {
            generateBtn.disabled = false;
            document.getElementById('loadingOverlay').classList.add('hidden');
        }
    });
}

// Helper: Animate Score Value
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

// Download Handlers
const downloadBtn = document.getElementById('downloadBtn');
if (downloadBtn) {
    downloadBtn.addEventListener('click', () => {
        const content = document.getElementById('finalInstructions').textContent;
        downloadFile(content, 'agent_instructions.txt');
    });
}

const generateQaBtn = document.getElementById('generateQaBtn');
if (generateQaBtn) {
    generateQaBtn.addEventListener('click', async () => {
        const inputKb = document.getElementById('inputKb').value;
        const qaContainer = document.getElementById('qaContainer');
        const qaOutput = document.getElementById('qaOutput');
        const loadingOverlay = document.getElementById('loadingOverlay');

        generateQaBtn.disabled = true;
        loadingOverlay.classList.remove('hidden');
        qaContainer.classList.add('hidden');

        try {
            const response = await fetch('/api/generate_qa', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ input_kb: inputKb })
            });
            if (!response.ok) throw new Error('Q&A generation failed');
            const data = await response.json();
            qaOutput.textContent = JSON.stringify(data.qa_list, null, 4);
            document.getElementById('qaContainer').classList.remove('hidden');
        } catch (error) {
            alert(error.message);
        } finally {
            generateQaBtn.disabled = false;
            document.getElementById('loadingOverlay').classList.add('hidden');
        }
    });
}

const downloadQaBtn = document.getElementById('downloadQaBtn');
if (downloadQaBtn) {
    downloadQaBtn.addEventListener('click', () => {
        const content = document.getElementById('qaOutput').textContent;
        downloadFile(content, 'sample_qa.txt');
    });
}

function downloadFile(content, filename) {
    if (!content) return;
    const blob = new Blob([content], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}
