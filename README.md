# AI Blog Generation Application Project
# AI Blog App

The **AI Blog App** is an innovative application that converts your videos into text and automatically saves the generated content as a blog post. This app simplifies the process of creating blog content from video media, making it accessible, efficient, and user-friendly.

## Features
- **Video-to-Text Conversion**: Transcribe videos into text using advanced AI-powered libraries.
- **Blog Post Generation**: Automatically format and save the transcribed text as a blog post.
- **Front-End Design**: A clean and modern user interface built with pure HTML and styled using Tailwind CSS.
- **Back-End Processing**: Powered by Python Django for efficient data handling and API integration.
- **Cloud Database Support**: Save and retrieve generated blog posts from an online database for easy access and management.

## Technologies Used
- **Assembly AI**: For accurate and efficient video-to-text transcription.
- **OpenAI**: To enhance text processing and improve content quality.
- **HTML and Tailwind CSS**: For building a responsive and visually appealing front end.
- **Python Django**: As the back-end framework for application logic and database management.
- **Online Database**: To store the generated blog posts securely and reliably.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd ai-blog-app
   ```

2. **Install Dependencies**
   Ensure you have Python installed. Then, install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup API Keys**
   - Log in to your [OpenAI account](https://openai.com/) and create an API key. Copy the key and add it to your project settings.
   - Similarly, log in to [Assembly AI](https://www.assemblyai.com/) and generate an API key. Add this key to your project settings.

   **Example:**
   Create a `.env` file in the project root and add:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ASSEMBLYAI_API_KEY=your_assemblyai_api_key
   ```

4. **Run the Application**
   Start the Django development server:
   ```bash
   python manage.py runserver
   ```

5. **Access the Application**
   Open your browser and navigate to `http://127.0.0.1:8000` to start using the AI Blog App.

## Notes
- You must set up your OpenAI and Assembly AI API keys before running the application.
- An online database is used to store blog posts. Ensure your database connection details are correctly configured in your Django settings file.
- Tailwind CSS is pre-configured for styling. You can customize it further as needed.

## Contribution Guidelines
We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- **OpenAI** for their powerful AI APIs.
- **Assembly AI** for seamless video-to-text transcription.
- The open-source community for providing tools and frameworks that made this project possible.

---
We hope you enjoy using the AI Blog App! Feel free to reach out with questions, feedback, or suggestions.

