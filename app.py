from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data Persistence: Global list of dictionaries
# Initial seed data
medications = [
    {
        'id': 1,
        'name': 'Lisinopril',
        'dosage': '10mg',
        'stock': 30,
        'threshold': 10
    },
    {
        'id': 2,
        'name': 'Metformin',
        'dosage': '500mg',
        'stock': 4,
        'threshold': 10
    }
]

# Helper to generate new IDs
def get_next_id():
    if not medications:
        return 1
    return max(med['id'] for med in medications) + 1

@app.route('/')
def index():
    return render_template('index.html', medications=medications)

@app.route('/add_medication', methods=['POST'])
def add_medication():
    name = request.form.get('name')
    dosage = request.form.get('dosage')
    try:
        stock = int(request.form.get('stock'))
        threshold = int(request.form.get('threshold', 5))
    except (ValueError, TypeError):
        # Default to 0 if invalid
        stock = 0
        threshold = 5

    new_med = {
        'id': get_next_id(),
        'name': name,
        'dosage': dosage,
        'stock': stock,
        'threshold': threshold
    }
    medications.append(new_med)
    return redirect(url_for('index'))

@app.route('/update_stock/<int:med_id>', methods=['POST'])
def update_stock(med_id):
    try:
        change_amount = int(request.form.get('change_amount'))
    except (ValueError, TypeError):
        return redirect(url_for('index'))

    for med in medications:
        if med['id'] == med_id:
            med['stock'] += change_amount
            # Prevent negative stock
            if med['stock'] < 0:
                med['stock'] = 0
            break
    return redirect(url_for('index'))

@app.route('/delete_medication/<int:med_id>', methods=['POST'])
def delete_medication(med_id):
    global medications
    medications = [med for med in medications if med['id'] != med_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
