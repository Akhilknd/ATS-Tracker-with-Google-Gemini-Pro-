# ATS-Tracker-with-Google-Gemini-Pro
# ATS Resume Expert

ATS Resume Expert is a Streamlit web application that helps you evaluate and improve your resume by providing insights from expert HR evaluations, technical HR manager insights, and ATS (Applicant Tracking System) evaluations. This project uses Google Gemini API to generate content and provide detailed feedback based on job descriptions and uploaded resumes.

## Features

- **Expert HR Evaluation**: Provides a professional evaluation of your resume against the job description by an experienced HR professional.
- **Technical HR Manager Insight**: Offers insights from a technical HR manager, highlighting strengths, weaknesses, and areas of improvement.
- **ATS Scanner Evaluation**: Evaluates your resume using an ATS scanner, providing a percentage match with the job description and identifying missing keywords.
- **ATS Scanner Skill Highlighting and Resume Rewrite**: Analyzes your experience to suggest skills to highlight for a role transition and provides a revised version of your resume.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/shanmukhasrinivas15/main/ATS-Tracker-with-Google-Gemini-Pro-.git
    cd ATS Scanner
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up your environment variables:**
    - Create a `.env` file in the project root directory.
    - Add your Google API key to the `.env` file:
      ```env
      GOOGLE_API_KEY=your_google_api_key
      ```

5. **Run the Streamlit application:**
    ```sh
    streamlit run ats.py
    ```
## ATS Tracking System
![Screenshot 2024-07-19 at 4 11 37 PM](https://github.com/user-attachments/assets/d34edb03-7b96-4425-8529-4040f78e4a20)


## Usage

1. Open your web browser and go to the URL provided by Streamlit (typically `http://localhost:8501`).
2. Enter the job description in the text area provided.
3. Upload your resume in PDF format.
4. Click on one of the buttons to get the respective evaluation or insight:
   - **Expert HR Evaluation**


   - **Technical HR Manager Insight**


   - **ATS Scanner Evaluation**


   - **ATS Scanner Skill Highlighting and Resume Rewrite**



## Code Explanation

### Main Functions

- **gemini_response(input, pdf_content, prompt)**: Sends the job description, PDF content, and a specific prompt to the Google Gemini API and returns the generated response.
- **input_pdf_setup(uploaded_file)**: Converts the uploaded PDF resume to an image and prepares it for API input.

### Streamlit App

- Sets up the Streamlit interface with text areas, file uploaders, and buttons for different evaluations.
- Handles button clicks to process the uploaded resume and job description, then displays the generated responses.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
