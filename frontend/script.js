const API_URL = "https://multiple-disease-prediction-system-1-uwes.onrender.com";

function switchTab(event, tab) {
    // Buttons
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');

    // Forms
    document.querySelectorAll('.form-section').forEach(section => section.classList.remove('active'));
    document.getElementById(`${tab}-form`).classList.add('active');
}

async function predictDiabetes(event) {
    event.preventDefault();
    const resultBox = document.getElementById('diabetes-result');
    resultBox.style.display = 'none';

    const data = {
        Pregnancies: parseInt(document.getElementById('d-pregnancies').value),
        Glucose: parseFloat(document.getElementById('d-glucose').value),
        BloodPressure: parseFloat(document.getElementById('d-bp').value),
        SkinThickness: parseFloat(document.getElementById('d-skin').value),
        Insulin: parseFloat(document.getElementById('d-insulin').value),
        BMI: parseFloat(document.getElementById('d-bmi').value),
        DiabetesPedigreeFunction: parseFloat(document.getElementById('d-dpf').value),
        Age: parseInt(document.getElementById('d-age').value)
    };

    try {
        const response = await fetch(`${API_URL}/predict/diabetes`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        resultBox.textContent = `Result: ${result.prediction}`;
        resultBox.className = 'result-box ' + (result.prediction === 'Diabetic' ? 'danger' : 'success');
        resultBox.style.display = 'block';

    } catch (error) {
        console.error('Error:', error);
        resultBox.textContent = 'Error connecting to server. Is the backend running?';
        resultBox.className = 'result-box danger';
        resultBox.style.display = 'block';
    }
}

async function predictHeart(event) {
    event.preventDefault();
    const resultBox = document.getElementById('heart-result');
    resultBox.style.display = 'none';

    const data = {
        age: parseInt(document.getElementById('h-age').value),
        sex: parseInt(document.getElementById('h-sex').value),
        cp: parseInt(document.getElementById('h-cp').value),
        trestbps: parseFloat(document.getElementById('h-trestbps').value),
        chol: parseFloat(document.getElementById('h-chol').value),
        fbs: parseInt(document.getElementById('h-fbs').value),
        restecg: parseInt(document.getElementById('h-restecg').value),
        thalach: parseFloat(document.getElementById('h-thalach').value),
        exang: parseInt(document.getElementById('h-exang').value),
        oldpeak: parseFloat(document.getElementById('h-oldpeak').value),
        slope: parseInt(document.getElementById('h-slope').value),
        ca: parseInt(document.getElementById('h-ca').value),
        thal: parseInt(document.getElementById('h-thal').value)
    };

    try {
        const response = await fetch(`${API_URL}/predict/heart`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        resultBox.textContent = `Result: ${result.prediction}`;
        resultBox.className = 'result-box ' + (result.prediction === 'Heart Disease' ? 'danger' : 'success');
        resultBox.style.display = 'block';

    } catch (error) {
        console.error('Error:', error);
        resultBox.textContent = 'Error connecting to server. Is the backend running?';
        resultBox.className = 'result-box danger';
        resultBox.style.display = 'block';
    }
}
