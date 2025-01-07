# Import necessary libraries
import streamlit as st
import spacy

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Knowledge base for chatbot
knowledge_base = {
    

# Expanded greetings
    "hi": "Hello! How can I assist you today?",
    "hey": "Hey there! What can I help you with?",
    "hello": "Hi! Feel free to ask any questions about the Skills4Future Internship.",
    "how are you": "I'm just a chatbot, but I'm here and ready to help you!",
    "good morning": "Good morning! How can I assist you today?",
    "good afternoon": "Good afternoon! What would you like to know about the internship?",
    "good evening": "Good evening! Let me know how I can help you.",
    "what's up": "Not much! I'm here to answer your questions about the Skills4Future Internship. What's up with          you?",
    "yo": "Yo! What's on your mind? Ask me anything about the internship.",
    "howdy": "Howdy! How can I assist you today?",
    "hiya": "Hiya! What would you like to know about the Skills4Future Internship?",
    "sup": "Sup! Got any questions about the Skills4Future program?",
    "greetings": "Greetings! I'm here to provide information about the Skills4Future Internship.",
    "morning": "Morning! How can I help you today?",
    "evening": "Good evening! Feel free to ask any questions.",
    "hi there": "Hi there! What can I help you with?",
    "hello there": "Hello there! What would you like to know about the internship?",
    "how's it going": "It's going great, thanks! How can I assist you with the Skills4Future Internship?",
    "hey there": "Hey there! Feel free to ask me anything about the internship.",
    "what's good": "What's good? Let me know how I can assist you.",
    "aloha": "Aloha! How can I help you today?",
    "salutations": "Salutations! I'm ready to answer your questions about the internship.",
    "nice to meet you": "Nice to meet you too! Let me know how I can help.",
    "hey buddy": "Hey buddy! What's on your mind? Ask me anything about the internship.",
    # Chatbot questions
    "who are you": "I'm the Skills4Future Internship Chatbot, here to help you with information about the program.",
    "what is this chatbot": "I am a chatbot designed to provide information about the Skills4Future Internship program, including application details, eligibility, and more.",
    "what can you do": "I can answer questions about the Skills4Future internship, application process, deadlines, and more. Try asking me something!",
    "green skills": "Green skills are skills that contribute to preserving or restoring environmental quality...",
    "AI internship": "The AI internship at Skills4Future involves applying artificial intelligence to solve...",
    "eligibility": "To apply for the Skills4Future AI internship, you should have a basic understanding of AI concepts, programming skills (in Python or similar languages), and a keen interest in sustainability. A degree or coursework in computer science, environmental science, or related fields is an advantage.",
    "application process": "The application process involves submitting an online application through the Skills4Future platform. You must upload your CV, a cover letter, and relevant academic/professional documents. After screening, shortlisted candidates will be interviewed, either virtually or in person.",
    "deadline": "The application deadline for the current internship cycle is 31st December 2024. Ensure that your application is submitted before the deadline.",
    "history": "Skills4Future was founded in 2018 with the goal of providing AI and tech-related internships to students and young professionals. The internship program began in 2020, aiming to solve environmental problems through AI. Over 1000 interns have participated in the program across the world.",
    "past internships": "Past internships have been focused on developing AI applications for waste management, sustainable energy, and water conservation. Interns contributed to the development of machine learning models for predicting environmental impact, optimizing energy usage, and reducing carbon footprints.",
    "present internships": "Currently, the internships involve AI for sustainable energy management, using machine learning algorithms to optimize energy consumption, and analyzing large datasets related to environmental factors such as air quality and climate change.",
    "future internships": "Future internship opportunities will focus on advanced AI applications in renewable energy sources, climate change mitigation, smart agriculture, and environmental monitoring. Interns will be expected to work with cutting-edge AI technologies like deep learning and reinforcement learning.",
    "introduced by": "The Skills4Future Internship program was introduced by a group of leading AI and sustainability experts from the Skills4Future organization, which collaborates with tech companies, universities, and environmental NGOs to offer impactful internship experiences.",
    "discovered by": "The internship program was designed by the founding team of Skills4Future, which includes AI researchers, data scientists, and sustainability advocates. The idea was to bridge the gap between AI technology and real-world environmental challenges.",
    "members": "Skills4Future offers internships to students, professionals, and early-career researchers from diverse backgrounds. The members of the program are involved in AI research, data science, environmental policy, and sustainability efforts across the globe.",
    "percentage": "Approximately 85% of past interns have successfully transitioned to full-time roles in AI, environmental science, or related industries. Many have gone on to work with top tech companies or research organizations focused on sustainability.",
    "free or paid": "The Skills4Future Internship is a paid program. Interns receive stipends, which are based on the duration and complexity of their assigned projects. The stipend helps cover living expenses and encourages more participation from students worldwide.",
    "ratios": "The internship program has an excellent track record, with a 70% success rate of interns securing permanent roles in related fields after completing their program. Many interns also receive job offers from the organizations they worked with during their internship.",
    "channels": "To stay connected with Skills4Future, you can follow us on our YouTube channel 'Skills4FutureAI', join our Telegram group [Skills4Future](https://t.me/skills4future), or contact us through WhatsApp at [Skills4Future WhatsApp](https://wa.me/1234567890). These channels provide updates, resources, and direct communication with mentors.",
    "next internship start date": "The next internship program will start on 15th February 2024. We encourage early registration to ensure your spot in the program.",
    "process after registration": "After registration, you will undergo a screening process where your CV, academic background, and personal statements will be reviewed. Shortlisted candidates will be contacted for an interview. Upon successful selection, you will be assigned to a project and receive your internship details.",
    "steps to follow": "1. Register on the Skills4Future platform with your personal details. 2. Submit your CV, cover letter, and supporting documents. 3. Wait for the screening process. 4. Attend an interview (if selected). 5. Start your internship project after selection.",
    "whom to contact for other details": "If you need further assistance or have any questions, feel free to contact our support team at support@skills4future.org or call us at +1234567890. You can also contact us through our social media channels for quick responses.",
    "chatbot history": "I was created in 2023 to assist interns and applicants with information related to the Skills4Future program. I am designed to answer questions about the internship, provide details on the application process, and guide users through the different stages of registration.",
    "why choose skills4future": "Skills4Future offers an exceptional learning environment where interns work on meaningful projects that address real-world challenges. With mentorship from experts in AI and sustainability, you'll gain valuable experience that can shape your career in the tech industry. Plus, you’ll be contributing to important environmental causes.",
    "uses": "The Skills4Future Internship prepares you with skills in AI, machine learning, and sustainability practices. You'll work with experts to build AI models for solving environmental issues and gain hands-on experience that will be valuable in future roles in tech or environmental sectors.",
    "advantages": "Joining the Skills4Future internship allows you to gain practical experience in AI and sustainability, making you more competitive in the job market. You’ll also have the opportunity to network with industry professionals, gain mentorship, and work on impactful projects.",
    "headquarters": "Skills4Future is headquartered in Silicon Valley, California, with global partnerships in Europe, Asia, and Africa. The organization focuses on creating a bridge between AI technology and sustainability efforts worldwide.",
    "founders": "Skills4Future was founded by Dr. Sarah Lee, an AI expert, and John Smith, a sustainability advocate. They envisioned a platform where students and young professionals could apply their technical skills to solving critical environmental problems.",
    "company history": "Founded in 2018, Skills4Future has rapidly grown into a leading platform for AI-driven sustainability internships. With a global presence and partnerships with top tech companies, the organization aims to foster a generation of professionals who can drive environmental change using AI technology.",
    "about internship": "The Skills4Future internship focuses on using AI and machine learning to develop solutions for global environmental challenges. Interns work on projects involving sustainable energy, waste management, climate change solutions, and more, using cutting-edge technologies to build real-world solutions.",
    "chatbot questions": "You can ask me about the Skills4Future internship, the application process, eligibility, and deadlines. I can also answer questions about the chatbot's history, its purpose, and its creators. Ask me anything!",
    "application link": "You can apply for the Skills4Future Internship through our application portal: www.skills4future.org/apply.",
    "how can I apply": "To apply for the Skills4Future Internship, visit our website (www.skills4future.org), create an account, and fill out the application form with your details.",
    "fees for application": "There are no fees to apply for the Skills4Future Internship. It is free to apply.",
    "registration link": "You can register for the internship at: www.skills4future.org/register.",
    "website": "Visit our official website for more details: www.skills4future.org.",
    "website link": "Our website link is www.skills4future.org. It contains all information about the program.",
    "purpose of this internship": "The purpose of the Skills4Future internship is to train individuals in applying AI to solve pressing environmental issues, such as climate change, waste management, and energy optimization. It aims to create a workforce skilled in both technology and sustainability.",
    "how can i apply for this internship": "Users can apply through our official website at www.skills4future.org. Create an account, fill out the application form, and submit the required documents such as a CV and cover letter.",
    "ongoing internships topics": "Current internships focus on AI for sustainable energy management, climate change analysis, and waste management using data-driven approaches.",
    "past internships topics": "Previous projects included developing AI solutions for water conservation, predicting environmental impacts, and optimizing energy usage in urban settings.",
    "future internships topics": "Future programs will tackle advanced topics like AI for renewable energy optimization, climate change mitigation, and smart agriculture using deep learning and IoT.",
    "eligibility": "Applicants should have basic knowledge of AI, programming skills, and a passion for sustainability. Preferred backgrounds include computer science, environmental science, or related fields.",
    "application process": "Submit your application through our platform, including your CV and cover letter. Shortlisted candidates will undergo an interview, and selected interns will receive project details.",
    "application link": "Apply at www.skills4future.org/apply.",
    "ongoing projects": "Projects currently in progress include using machine learning for air quality prediction and developing AI models to reduce energy consumption in industries.",
    "company location": "Skills4Future is headquartered in Silicon Valley, California, with a global presence and partnerships in Europe, Asia, and Africa.",
    "explain about this internship": "The Skills4Future internship focuses on applying artificial intelligence to solve real-world environmental challenges. Interns work on projects such as sustainable energy management, waste reduction, climate change mitigation, and eco-friendly practices. Participants gain hands-on experience, mentorship from industry experts, and the opportunity to contribute to impactful solutions. The program is conducted online, making it accessible to participants worldwide.",
    "mail id": "You can contact us at support@skills4future.org for more information or queries related to the internship.",
    "where to get internship": "You can apply for the Skills4Future internship through our official website, www.skills4future.org. All internship details, including application forms, are available on the platform.",
    "offline or online": "The Skills4Future internship is an online program, allowing interns to participate remotely and collaborate virtually with team members and mentors.",
    "duration": "The duration of the Skills4Future internship typically lasts between 3 to 6 months, depending on the project and intern’s progress.",
    "limits": "There are limited spots available for each internship cycle. We encourage you to apply early to secure your place in the program.",
    "website": "Visit our official site for detailed information: www.skills4future.org.",
    "topics": "Interns will work on topics such as AI for sustainable energy, climate change mitigation, machine learning for waste management, data analysis for air quality, and more.",
    "who can apply": "Students, recent graduates, and early-career professionals with a background in AI, computer science, environmental science, or related fields can apply for the Skills4Future internship.",
}

# Function to process the user's query
def process_query(user_input):
    # Process the user's input with spaCy NLP model
    doc = nlp(user_input.lower())  # Lowercase for case insensitivity

    # Check if any of the keywords are in the user's input
    for key in knowledge_base:
        if key in user_input.lower():
            return knowledge_base[key]

    # Default response if no keyword matches
    return "Sorry, I couldn't find an answer to that. Can I help you with something else?"

# Streamlit app
def main():
    # Title and description
    st.title("Skills4Future Internship Chatbot")
    st.write("Welcome to the Skills4Future Internship Chatbot! Ask me anything about the program, application process, or topics.")

    # Input box for user query
    user_input = st.text_input("Type your question here:")
    
    if user_input:
        # Process the query and get the response
        response = process_query(user_input)
        
        # Display the response
        st.write("🤖:", response)

    # Add some example queries
    st.sidebar.title("Example Queries")
    st.sidebar.write("- What are green skills?")
    st.sidebar.write("- Tell me about the AI internship.")
    st.sidebar.write("- How can I apply?")
    st.sidebar.write("- What is the application deadline?")
    st.sidebar.write("- Who are the founders?")

# Run the Streamlit app
if __name__ == "__main__":
    main()