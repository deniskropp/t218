/**
    * OCS Simulation - Controller Architecture
    */

// --- DATA STORE ---
const Data = {
    agents: [
        { id: 'gptase', name: 'GPTASe', role: 'TAS Extractor', color: '#6c5ce7' },
        { id: 'putase', name: 'puTASe', role: 'TAS Purifier', color: '#a29bfe' },
        { id: 'lyra', name: 'Lyra', role: 'Prompt Engineer', color: '#fd79a8' },
        { id: 'fizz', name: 'Fizz La Metta', role: 'Coordinator', color: '#00b894' },
        { id: 'tutor', name: 'AI Tutor', role: 'Knowledge Transfer', color: '#fdcb6e' },
        { id: 'codein', name: 'Codein', role: 'Code Investigator', color: '#e17055' },
        { id: 'dima', name: 'Dima', role: 'Ethical Compliance', color: '#0984e3' },
        { id: 'ar00l', name: 'AR-00L', role: 'Visual Assets', color: '#6c5ce7' },
        { id: 'qllick', name: 'QllickBuzz', role: 'Operational Rules', color: '#fd79a8' },
        { id: 'weplan', name: 'WePlan', role: 'Strategic Plans', color: '#00b894' },
        { id: 'kick', name: 'Kick La Metta', role: 'NL Translation', color: '#fdcb6e' },
        { id: 'orchestrator', name: 'Orchestrator', role: 'Role Adaptation', color: '#e17055' },
        { id: 'monitor', name: 'SystemMonitor', role: 'Integrity', color: '#0984e3' }
    ],
    steps: [
        { number: 1, title: 'TAS Extraction', agent: 'GPTASe', description: 'Extracting raw Task Agnostic Steps from the high-level objective.', details: { input: '⫻data/obj:', output: '⫻data/tas:', process: 'Analyzing objective and breaking down into initial steps' } },
        { number: 2, title: 'TAS Purification', agent: 'puTASe', description: 'Refining and removing ambiguity from extracted steps.', details: { input: '⫻data/tas:', output: '⫻data/ptas:', process: 'Clarifying requirements and removing redundancies' } },
        { number: 3, title: 'Workflow Structuring', agent: 'Lyra', description: 'Creating optimized workflows from purified steps.', details: { input: '⫻data/ptas:', output: '⫻data/spec:', process: 'Designing efficient execution pathways' } },
        { number: 4, title: 'Cognitive Coordination', agent: 'Fizz La Metta', description: 'Aligning agent roles and responsibilities.', details: { input: '⫻data/spec:', output: '⫻cmd/exec:', process: 'Assigning tasks to appropriate agents' } },
        { number: 5, title: 'Knowledge Transfer', agent: 'AI Tutor', description: 'Providing domain-specific insights and context.', details: { input: '⫻query/clarify:', output: '⫻data/logic:', process: 'Answering domain questions and providing expertise' } },
        { number: 6, title: 'Code Context', agent: 'Codein', description: 'Analyzing implementation needs and providing code references.', details: { input: '⫻data/spec:', output: '⫻data/logic:', process: 'Identifying code requirements and patterns' } },
        { number: 7, title: 'Prompt Refinement', agent: 'Lyra', description: 'Optimizing prompts based on feedback loops.', details: { input: '⫻query/clarify:', output: '⫻data/spec:', process: 'Improving prompt quality and specificity' } },
        { number: 8, title: 'Protocol Establishment', agent: 'Fizz La Metta', description: 'Creating operational rules and protocols.', details: { input: '⫻data/spec:', output: '⫻cmd/mode:', process: 'Defining execution guidelines and constraints' } },
        { number: 9, title: 'System Monitoring', agent: 'Fizz La Metta', description: 'Tracking execution and collecting performance metrics.', details: { input: '⫻data/logic:', output: '⫻data/obj:', process: 'Monitoring system health and performance' } },
        { number: 10, title: 'Ethical Compliance', agent: 'Dima', description: 'Validating decisions against ethical guidelines.', details: { input: '⫻query/clarify:', output: '⫻cmd/halt:', process: 'Ensuring ethical standards are maintained' } },
        { number: 11, title: 'Visual Assets', agent: 'AR-00L', description: 'Creating visual prototypes and design elements.', details: { input: '⫻data/spec:', output: '⫻data/logic:', process: 'Designing UI/UX components and visuals' } },
        { number: 12, title: 'Operational Rules', agent: 'QllickBuzz', description: 'Refining rules for edge cases and exceptions.', details: { input: '⫻data/ptas:', output: '⫻cmd/mode:', process: 'Handling special cases and exceptions' } },
        { number: 13, title: 'Strategic Plans', agent: 'WePlan', description: 'Developing long-term roadmaps and strategies.', details: { input: '⫻data/obj:', output: '⫻data/spec:', process: 'Planning future development and growth' } },
        { number: 14, title: 'NL Translation', agent: 'Kick La Metta', description: 'Converting informal requests to formal tasks.', details: { input: '⫻data/obj:', output: '⫻data/ptas:', process: 'Formalizing natural language inputs' } },
        { number: 15, title: 'Dynamic Role Adaptation', agent: 'Orchestrator', description: 'Adjusting agent roles based on workload shifts.', details: { input: '⫻cmd/exec:', output: '⫻flow:', process: 'Optimizing resource allocation' } },
        { number: 16, title: 'Joint Decisions', agent: 'Dima', description: 'Resolving conflicts and reaching consensus.', details: { input: '⫻query/clarify:', output: '⫻cmd/halt:', process: 'Mediating disagreements and finding solutions' } },
        { number: 17, title: 'Integrity Monitoring', agent: 'SystemMonitor', description: 'Ensuring system security and data integrity.', details: { input: '⫻data/logic:', output: '⫻cmd/halt:', process: 'Detecting and preventing security issues' } },
        { number: 18, title: 'Tailored Plans', agent: 'WePlan', description: 'Customizing workflows based on user feedback.', details: { input: '⫻query/clarify:', output: '⫻data/spec:', process: 'Adapting to user preferences and requirements' } },
        { number: 19, title: 'Holistic Task Approach', agent: 'Orchestrator', description: 'Unifying cross-domain tasks and execution.', details: { input: '⫻data/obj:', output: '⫻flow:', process: 'Integrating multiple domains and systems' } },
        { number: 20, title: 'Review & Refinement', agent: 'All', description: 'Final review and iterative improvements.', details: { input: '⫻data/logic:', output: '⫻data/ptas:', process: 'Evaluating results and making final adjustments' } }
    ]
};

// --- CONTROLLERS ---

/**
    * Handles Theme switching and persistence
    */
const ThemeController = {
    init() {
        const toggle = document.getElementById('themeToggle');
        const savedTheme = localStorage.getItem('ocs-theme') || 'light';

        document.documentElement.setAttribute('data-theme', savedTheme);
        this.updateIcon(savedTheme, toggle);

        toggle.addEventListener('click', () => {
            const current = document.documentElement.getAttribute('data-theme');
            const next = current === 'dark' ? 'light' : 'dark';

            document.documentElement.setAttribute('data-theme', next);
            localStorage.setItem('ocs-theme', next);
            this.updateIcon(next, toggle);
        });
    },

    updateIcon(theme, btn) {
        btn.textContent = theme === 'dark' ? '☀️' : '🌓';
    }
};

/**
    * Handles DOM updates and Animations
    */
const UIController = {
    elements: {
        agentList: document.getElementById('agentList'),
        stepContainer: document.getElementById('stepContainer'),
        startBtn: document.getElementById('startBtn'),
        pauseBtn: document.getElementById('pauseBtn'),
        stepBtn: document.getElementById('stepBtn'),
        glitchBtn: document.getElementById('glitchBtn'),
        objectiveInput: document.getElementById('objectiveInput'),
        progressFill: document.getElementById('progressFill'),
        progressText: document.getElementById('progressText'),
        statusDot: document.getElementById('statusDot'),
        statusText: document.getElementById('statusText'),
        loadingOverlay: document.getElementById('loadingOverlay'),
        finalOutput: document.getElementById('finalOutput'),
        outputContent: document.getElementById('outputContent'),
        restartBtn: document.getElementById('restartBtn')
    },

    init() {
        this.renderAgents();
        this.renderSteps();
    },

    renderAgents() {
        this.elements.agentList.innerHTML = '';
        Data.agents.forEach(agent => {
            const el = document.createElement('div');
            el.className = 'agent-item';
            el.dataset.agentId = agent.id;
            el.innerHTML = `
                <div class="agent-avatar" style="background-color: ${agent.color}">${agent.name.substring(0, 2)}</div>
                <div>
                    <div class="agent-name">${agent.name}</div>
                    <div class="agent-role">${agent.role}</div>
                </div>
            `;
            this.elements.agentList.appendChild(el);
        });
    },

    renderSteps() {
        this.elements.stepContainer.innerHTML = '';
        Data.steps.forEach((step, index) => {
            const agent = Data.agents.find(a => a.name === step.agent) || Data.agents[0];
            const el = document.createElement('div');
            el.className = 'step-item';
            el.dataset.stepIndex = index;
            el.innerHTML = `
                <div class="step-header">
                    <div class="step-number">${step.number}</div>
                    <div class="step-title">${step.title}</div>
                    <div class="step-agent" style="background-color: ${agent.color}">${step.agent}</div>
                </div>
                <div class="step-description">${step.description}</div>
                <div class="step-details">
                    <div class="step-detail-item">
                        <span class="detail-label">Input:</span>
                        <span class="detail-value">${step.details.input}</span>
                    </div>
                    <div class="step-detail-item">
                        <span class="detail-label">Output:</span>
                        <span class="detail-value">${step.details.output}</span>
                    </div>
                </div>
            `;
            this.elements.stepContainer.appendChild(el);
        });
    },

    updateStep(currentStep, isComplete = false) {
        // Update active step
        const currentEl = document.querySelector(`.step-item[data-step-index="${currentStep}"]`);
        if (currentEl) {
            currentEl.classList.add('active');
            currentEl.classList.remove('completed');
            currentEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }

        // Update previous step
        if (currentStep > 0) {
            const prevEl = document.querySelector(`.step-item[data-step-index="${currentStep - 1}"]`);
            if (prevEl) {
                prevEl.classList.remove('active');
                prevEl.classList.add('completed');
            }
        }

        // Complete all if finished
        if (isComplete && currentStep === Data.steps.length - 1) {
            currentEl?.classList.remove('active');
            currentEl?.classList.add('completed');
        }
    },

    highlightAgent(agentName) {
        document.querySelectorAll('.agent-item').forEach(el => el.classList.remove('active'));
        if (!agentName) return;

        const agent = Data.agents.find(a => a.name === agentName);
        if (agent) {
            const el = document.querySelector(`.agent-item[data-agent-id="${agent.id}"]`);
            el?.classList.add('active');
        }
    },

    updateProgress(percent) {
        this.elements.progressFill.style.width = `${percent}%`;
        this.elements.progressText.textContent = `${Math.round(percent)}% Complete`;
    },

    setStatus(text, type = 'normal') {
        this.elements.statusText.textContent = text;
        this.elements.statusDot.className = 'status-dot'; // Reset

        if (type === 'active') {
            this.elements.statusDot.classList.add('active');
            this.elements.statusDot.style.backgroundColor = 'var(--success)';
        } else if (type === 'error') {
            this.elements.statusDot.style.backgroundColor = 'var(--danger)';
        } else if (type === 'paused') {
            this.elements.statusDot.style.backgroundColor = 'var(--warning)';
        } else {
            this.elements.statusDot.style.backgroundColor = 'var(--secondary)';
        }
    },

    toggleControls(state) {
        // state: 'idle', 'running', 'paused', 'completed'
        const { startBtn, pauseBtn, stepBtn, glitchBtn, objectiveInput } = this.elements;

        switch(state) {
            case 'idle':
                startBtn.disabled = false;
                pauseBtn.disabled = true;
                stepBtn.disabled = true;
                glitchBtn.disabled = true;
                objectiveInput.disabled = false;
                pauseBtn.innerHTML = '<span>❚❚</span> Pause';
                break;
            case 'running':
                startBtn.disabled = true;
                pauseBtn.disabled = false;
                stepBtn.disabled = true; // Auto-advance
                glitchBtn.disabled = false;
                objectiveInput.disabled = true;
                pauseBtn.innerHTML = '<span>❚❚</span> Pause';
                break;
            case 'paused':
                startBtn.disabled = true;
                pauseBtn.disabled = false;
                stepBtn.disabled = false; // Allow manual stepping
                glitchBtn.disabled = true;
                pauseBtn.innerHTML = '<span>▶</span> Resume';
                break;
            case 'completed':
                startBtn.disabled = true;
                pauseBtn.disabled = true;
                stepBtn.disabled = true;
                glitchBtn.disabled = true;
                break;
        }
    },

    showFinalOutput(objective) {
        this.elements.outputContent.innerHTML = `
            <strong>Transformation Objective:</strong> ${objective}<br><br>
            <strong>Status:</strong> ✓ Successfully completed all 20 transformation steps<br><br>
            <strong>Key Achievements:</strong><br>
            • Extracted and purified Task Agnostic Steps (TAS)<br>
            • Established optimized workflows and protocols<br>
            • Ensured ethical compliance and system integrity<br>
            • Output generated in high-fidelity ⫻flow format<br><br>
            <strong>Agents Involved:</strong> ${Data.agents.length} active agents<br>
        `;
        this.elements.finalOutput.classList.add('active');
    },

    resetUI() {
        this.elements.progressFill.style.width = '0%';
        this.elements.progressText.textContent = '0% Complete';
        this.elements.finalOutput.classList.remove('active');

        document.querySelectorAll('.step-item').forEach(el =>
            el.classList.remove('active', 'completed')
        );
        document.querySelectorAll('.agent-item').forEach(el =>
            el.classList.remove('active')
        );

        this.setStatus('Ready');
        this.toggleControls('idle');
    }
};

/**
    * Main Simulation Logic
    */
const Simulation = {
    state: {
        currentStep: 0,
        status: 'idle', // idle, running, paused, error, completed
        timer: null,
        glitchTimer: null
    },

    init() {
        ThemeController.init();
        UIController.init();
        this.setupListeners();
    },

    setupListeners() {
        UIController.elements.startBtn.addEventListener('click', () => this.start());
        UIController.elements.restartBtn.addEventListener('click', () => this.reset());
        UIController.elements.pauseBtn.addEventListener('click', () => this.togglePause());
        UIController.elements.stepBtn.addEventListener('click', () => this.nextStep());
        UIController.elements.glitchBtn.addEventListener('click', () => this.triggerGlitch());
    },

    start() {
        if (this.state.status !== 'idle') return;

        const objective = UIController.elements.objectiveInput.value.trim();
        if (!objective) {
            alert('Please enter a transformation objective');
            return;
        }

        this.state.status = 'running';
        UIController.elements.loadingOverlay.classList.add('active');
        UIController.setStatus('Initializing...', 'normal');

        // Reset internal state
        this.state.currentStep = 0;
        UIController.resetUI(); // Clear classes

        setTimeout(() => {
            UIController.elements.loadingOverlay.classList.remove('active');
            UIController.setStatus('Running', 'active');
            UIController.toggleControls('running');

            this.runLoop();
        }, 1500);
    },

    runLoop() {
        if (this.state.timer) clearInterval(this.state.timer);

        this.state.timer = setInterval(() => {
            if (this.state.status === 'running') {
                this.processStep();
            }
        }, 1500); // 1.5s per step
    },

    processStep() {
        if (this.state.currentStep >= Data.steps.length) {
            this.complete();
            return;
        }

        // Update UI for current step
        const step = Data.steps[this.state.currentStep];
        UIController.updateStep(this.state.currentStep);
        UIController.highlightAgent(step.agent);

        // Update Progress
        const progress = ((this.state.currentStep + 1) / Data.steps.length) * 100;
        UIController.updateProgress(progress);

        this.state.currentStep++;
    },

    togglePause() {
        if (this.state.status === 'running') {
            this.state.status = 'paused';
            UIController.setStatus('Paused', 'paused');
            UIController.toggleControls('paused');
        } else if (this.state.status === 'paused') {
            this.state.status = 'running';
            UIController.setStatus('Running', 'active');
            UIController.toggleControls('running');
        }
    },

    nextStep() {
        if (this.state.status === 'paused') {
            this.processStep();
        }
    },

    triggerGlitch() {
        if (this.state.status !== 'running') return;

        const prevStatus = this.state.status;
        this.state.status = 'error';

        // Pause execution
        if (this.state.timer) clearInterval(this.state.timer);

        // Visual feedback
        UIController.setStatus('⚠️ SYSTEM INTEGRITY ALERT', 'error');
        UIController.highlightAgent('SystemMonitor');

        // Auto-resolve after 2s
        setTimeout(() => {
            UIController.setStatus('Resolving...', 'paused');
            UIController.highlightAgent('Dima'); // Ethical compliance checking

            setTimeout(() => {
                this.state.status = 'running';
                UIController.setStatus('Running', 'active');
                this.runLoop(); // Resume
            }, 1000);
        }, 2000);
    },

    complete() {
        clearInterval(this.state.timer);
        this.state.status = 'completed';

        UIController.updateStep(this.state.currentStep, true); // Mark last as done
        UIController.setStatus('Transformation Complete', 'active');
        UIController.toggleControls('completed');
        UIController.showFinalOutput(UIController.elements.objectiveInput.value);
    },

    reset() {
        if (this.state.timer) clearInterval(this.state.timer);
        this.state.status = 'idle';
        this.state.currentStep = 0;

        UIController.resetUI();
    }
};

// Boot
window.addEventListener('load', () => Simulation.init());
