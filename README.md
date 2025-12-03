# MedVault - Medication Inventory Tracker

MedVault is a simple, efficient web application designed to help you manage your personal medication inventory. Built with Flask and Tailwind CSS, it provides a clean interface to track your medications, monitor stock levels, and receive low-stock alerts.

## Features

- **Inventory Tracking**: Keep a digital record of all your medications, including names and dosages.
- **Stock Management**: Easily update stock levels with "Restock" and "Take" quick actions.
- **Low Stock Alerts**: Visual indicators highlight medications that have fallen below your specified threshold.
- **Responsive Design**: A modern, clean interface that works on desktop and mobile devices.

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, Tailwind CSS (via CDN)
- **Data Storage**: In-memory (Python list) for simplicity (Note: Data resets on server restart)

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/shrutimalik123/MedVault---Medication-Inventory-Tracker.git
    cd MedVault---Medication-Inventory-Tracker
    ```

2.  Install dependencies (if using a virtual environment, activate it first):
    ```bash
    pip install flask
    ```

### Running the Application

1.  Start the Flask server:
    ```bash
    python app.py
    ```

2.  Open your web browser and navigate to:
    ```
    http://127.0.0.1:5000
    ```

## Usage

1.  **Add Medication**: Use the form at the top of the page to enter the medication name, dosage, current stock, and a low-stock threshold.
2.  **Manage Stock**: Use the "+1 Restock" and "-1 Take" buttons on each medication card to adjust quantities.
3.  **Delete**: Remove medications you no longer need to track.
