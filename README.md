# Placement Prediction App

This is a simple Streamlit web application that predicts whether a person will get placed based on their CGPA and IQ.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/abhiram-k-2223/ppm-app.git
   ```
2. Install the required libraries:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run new-rec.py
   ```

2. Input your CGPA and IQ using the number input fields.

3. Click the "Submit" button to see the prediction.

## Model

The model used in this application was trained separately and saved as a pickle file. You can find the code for training the model in [this repository](https://github.com/abhiram-k-2223/new-repo). The trained model (`model.pkl`) is loaded directly into the Streamlit app.
