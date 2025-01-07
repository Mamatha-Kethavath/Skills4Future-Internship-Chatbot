# Skills4Future-Internship-Chatbot
The Skills4Future Internship chatbot is a friendly assistant designed to support users with tasks, offering information, creative ideas, and technical help. It responds thoughtfully and accurately, ensuring natural, seamless interactions while adapting to users’ needs for a smooth experience every time.

Skills4Future Internship Chatbot 🤖🚀

The Skills4Future Internship Chatbot is designed to streamline the application process, provide detailed program insights, and assist applicants in determining their eligibility. Using advanced Natural Language Processing (NLP) techniques and machine learning models, this chatbot creates a user-friendly and interactive experience for aspiring interns.


🚀 Features
Eligibility Checker: Assesses whether users meet the program requirements by analyzing their input.
FAQ Matching: Employs advanced similarity models to provide accurate answers to frequently asked questions.
Interactive Interface: Built using Streamlit for a seamless and visually appealing experience.
Fallback Responses: Ensures users receive meaningful guidance for any unrecognized queries.
Application Assistance: Provides tips and resources to help users prepare successful applications.
Conversation Logging: Tracks interactions to improve performance and analyze trends.


🛠 Tools and Technologies
Programming Language: Python
NLP Libraries:
NLTK
Sentence Transformers
Scikit-learn (TF-IDF Vectorizer and Logistic Regression)
Frontend Framework: Streamlit
Machine Learning: Logistic Regression, BERT-based embeddings
Utilities:
csv for logging conversations
datetime for timestamps
os and json for file handling


🧠 Methodology
Data Preparation
Eligibility criteria and FAQ data stored in structured JSON format.
Customized dataset for common internship-related queries.
Model Development
TF-IDF vectorizer converts user inputs into numerical features.
Logistic Regression classifies user intents (e.g., eligibility, FAQ, general questions).
Sentence Transformers generate embeddings for accurate FAQ matching.
Response Mechanism
User intents or matched FAQs trigger context-specific responses.
Fallback mechanism ensures meaningful engagement for unrecognized inputs.
Interface and Deployment
Streamlit powers a visually engaging, interactive interface.
Logs interactions for evaluation and performance improvement.




Prerequisites
Python 3.8 or above
Required Python libraries:
nltk
streamlit
scikit-learn
sentence-transformers



Description of Key Files
nlp.py: Core logic, including intent classification, FAQ matching, and response generation.
intents.json: Dataset defining user intents, patterns, and corresponding responses.
requirements.txt: List of dependencies and libraries required for the chatbot.
chat_log.csv: Logs all user interactions and chatbot responses for analysis and refinement.
Week 3 Project PPT: A detailed presentation of the chatbot's methodology, tools, and findings.
assets/: Contains additional resources such as datasets and pre-trained models.



🤖 Try now:
Skills4Future Chatbot: [Insert Link Here]



📬 Contact
If you have any questions, feedback, or suggestions, feel free to reach out:
Author: Mamatha Kethavath
Email: mamatharathod89@gmail.com
GitHub: Mamatha-Kethavath
LinkedIn: Mamatha Kethavath
