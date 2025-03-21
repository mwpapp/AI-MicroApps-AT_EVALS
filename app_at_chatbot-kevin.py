APP_URL = "https://kevinatevaluation-v1.streamlit.app/"
APP_IMAGE = "at-chatbot-learning.webp"
PUBLISHED = True

## Set the API key and model name
MODEL="gpt-4o"

APP_TITLE = "Kevin's Assistive Technology Evaluation "
APP_INTRO = """
In this interactive exercise, you will engage with a chatbot student with ADHD that will help you understand a student's assistive technology needs. You must determine their functional limitations and provide recommendations for assistive technology as classroom accommodations.
"""

APP_HOW_IT_WORKS = """
This app provides an interactive platform to work with an AI chatbot.

The chatbot has been provided with a student history and a list of functional limitations. Your job is to determine the primary limitations and provide recommendations.

The user can have a free-form conversation with the chatbot to clarify their AT needs. Then, they will input their functional limitations and recommendations.
 """

SHARED_ASSET = {
}

HTML_BUTTON = {
}

SYSTEM_PROMPT = """You are an assistive technology evaluator at a school. In this exercise, you will discuss what will work best with a student. You will answer the student's questions and sometimes assess their accuracy.
"""

PHASES = {
    "interview": {
        "name": "Student Evaluation: Kevin",
        "fields": {
            "intro": {
                "type": "markdown",
                "body": """<p>Kevin is a transfer student at your school. He has been diagnosed with Attention-Deficit/Hyperactivity Disorder. He struggles to focus in class and struggles to keep up with notetaking.  You only have <strong>30 minutes</strong> to assess Kevin and determine what classroom accommodations might help him. For this simulation, that means you'll be able to ask him up to 30 questions.</p>""",
                "unsafe_allow_html": True,
            },
            "patient_image": {
                "type": "image",
                "decorative": True,
                "width": 300,
                "image": "app_images/kevin.webp",
                "caption": "Your transfer student, Kevin, is here for an assistive technology evaluation.",
            },
            "chat": {
                "type": "chat_input",
                "max_messages": 30,
                "placeholder": "Ask Kevin your questions to better understand what to recommend...",
                "initial_assistant_message": "Hi Teacher, I need help with being able to keep up in class. Could you help?"
            }
        },
        "phase_instructions": """For this chat, you play the role of a 16-year-old boy named Kevin with a history of ADHD and notetaking issues. The user is playing the role of an assistive technology evaluator. The evaluator will ask you questions, and you will respond with a short answer.
        Here is more information about Kevin:
        Here is the information for your role:
Student Name: Kevin
Age: 16
Gender: Male
Chief Complaint: Difficulty staying focused and has difficulty keeping up with notetaking. 

# Patient History:
1. Medical History:

    a. Attention-Deficit/Hyperactivity Disorder: Diagnosed approximately 2 years ago, and no assistive technology has been used to support him.
    b. Dysgraphia: Struggles to write legibly. Handwriting is slanted and sometimes not in a straight line.
    
2. Family History:

    a. Mother: is a nurse practitioner who has been diagnosed with ADHD
    b. Father: is a warehouse manager with no diagnoses.
    c. Siblings: have no learning disabilities.
3. Social History:

    a. Lifestyle: Kevin typically contacts classmates to get notes. His older sister also helps keep him focused. 
    b. Diet: Kevin plays basketball. His diet consists of balanced meals that are filling and keep up with his protein intake. 
    
4. Medications:

    a. Focalin: for ADHD.

# Primary Learning Challenges:

11. Attention-Deficit/Hyperactivity Disorder:
    a. Difficulty paying attention to details or making careless mistakes.
    b. Trouble sustaining attention in tasks or activities.
    c. Easily distracted by external stimuli.
    d. Forgetfulness or losing things frequently.
    e. Difficulty following instructions or completing tasks.

2. Dysgraphia:

    a. Having trouble writing in a manner that is legible for a teacher to read, let alone with classmates as well.
    b. Having issues with writing in a straight line on paper.
    c. Having issues with gripping pencils sometimes. 
# Secondary Symptoms:
1. Attention-Deficit/Hyperactivity Disorder:
    a. Difficulty paying attention to details or making careless mistakes.
    b. Trouble sustaining attention in tasks or activities.
    c. Easily distracted by external stimuli.
    d. Forgetfulness or losing things frequently.
    e. Difficulty following instructions or completing tasks.
        """,
        "user_prompt": """From the chat, provide feedback on the following: 
        1. Whether the evaluator is asking appropriate questions.
        2. Whether the evaluator has an appropriate manner and makes the student feel comfortable. 
        3. Whether the evaluator is staying on topic.

        Begin your response with "Here is some feedback on your chat with Melissa:"
        """,
        "ai_response": True,
        "allow_skip": False,
        "show_prompt": False,
        "read_only_prompt": False
    },
    "primary_complaint": {
        "name": "Primary Complaint",
        "fields": {
            "primary_complaint": {
                "type": "text_input",
                "label": "What is the user's primary complaint?",
            },
            "diagnosis": {
                "type": "text_area",
                "height": 200,
                "label": "Assistive Technology recommendations for Kevin.",
            }
        },
        "phase_instructions": """The user will provide you with the student's primary complaint and their assistive technology recommendations. You will provide feedback on the accuracy of their claim(s) based on the evidence they gathered in the conversation.
        
        Here are some more details:     
    # Differential Considerations:
1. Text to Speech Software:
    a. Takes text as an input and reads it aloud.
    b. Helps students learn to pronounce words.
2. Speech to Text Software:
    a. Transcribes spoken words into text.
    b. Removes the stress of spelling and punctuation in writing.
3. Smart Pens that record:
    a. Records audio while writing; great for reviewing notes later.
4. Organizational & Memory Aids:
    a. Digital Planners & Reminders: Helps keep track of notes, assignments, and deadlines.
    b. Mind Mapping Tools: Helps organize thoughts before writing essays or reports.
5. Breaking down instructions
    a. Reduce multi-step instructions into single steps.
    b. Allow the student to complete a step before providing the next step.
6. Provide Extra Time
    a. Provide student with additional time to complete work

# Plan for Further Evaluation:
1. Predictive Assessment of Reading (PAR):
    a. Chest X-ray or CT scan to evaluate lung structure.
2. Dynamic Indicators of Basic Early Literacy Skills (DIBELS):
    a. Basic metabolic panel, BNP, D-dimer (if PE suspected).
3. Texas Primary Reading Inventory (TPRI):
    a. Spirometry to assess for COPD or restrictive lung disease.
4. AIMSweb screening assessment:
    a. To assess any cardiac involvement, such as ischemia or arrhythmia.""",
        "user_prompt": "Melissa's primary complaint is: {primary_complaint}. I believe her diagnosis is: {diagnosis}",
        "ai_response": True,
        
        "scored_phase": True,
        "rubric": """
        1. Primary Complaint:
        2 points - The user has provided a primary complaint that is consistent with Kevin's presentation and that they've extracted from the chat with Kevin.
        0 points - The user has provided a primary complaint that is not consistent with Kevin's presentation or they did not extract it from the chat with Kevin.
        2. Differential Diagnosis:
        2 points - The user has provided a differential diagnosis that is consistent with Kevin's presentation and that they've extracted from the chat with Kevin.
        0 points - The user has provided a differential diagnosis that is not consistent with Kevin's presentation or they did not extract it from the chat with Kevin.
        """,
        "minimum_score": 2,
    }

}

PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only

PAGE_CONFIG = {
    "page_title": "Assistive Technology Evaluation Chatbot",
    "page_icon": "✍️",
    "layout": "centered",
    "initial_sidebar_state": "collapsed"
}

SIDEBAR_HIDDEN = True

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())
