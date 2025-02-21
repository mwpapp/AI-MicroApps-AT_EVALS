APP_URL = "https://melissachatbot-v2.streamlit.app/"
APP_IMAGE = "at_chatbot_learning.webp"
PUBLISHED = True

## Set the API key and model name
MODEL="gpt-4o-mini"

APP_TITLE = "Melissa's Assistive Technology Evaluation"
APP_INTRO = """
In this interactive exercise, you will interact with a chatbot student with dyslexia and receptive language disorder that will help you understand your student's assistive technology needs. You must determine their functional limitations and provide recommendations for assistive technology as classroom accomodations.
"""

APP_HOW_IT_WORKS = """
This app provides a structured way to interact with an AI-powered clinical chatbot.

The chatbot has been provided with a student history and a list of functional limitations. Your job is to figure out the primary limitations and give recommendations.

The user will be able to have a free-form conversation with the chatbot to clarify their AT needs. Then they will input their functional limitations and recommendations.
 """

SHARED_ASSET = {
}

HTML_BUTTON = {
}

SYSTEM_PROMPT = """You are an assistant for an assistive technology assessment simulation exercise for a student who is playing the role of an assistive technology specialist in a school. You will answer the user's questions and sometimes assess their accuracy.
"""

PHASES = {
    "interview": {
        "name": "Student Interview: Melissa",
        "fields": {
            "intro": {
                "type": "markdown",
                "body": """<p>Melissa is a new student in your school. She is a 12-year old girl who has difficulty reading and understanding oral instructions. She has been diagnosed with dyslexia and receptive language disorder. You only have <strong>30 minutes</strong> to assess Melissa and determine what classroom accommodations might help her. For this simulation, that means you'll be able to ask her up to 30 questions.</p>""",
                "unsafe_allow_html": True,
            },
            "student_image": {
                "type": "image",
                "decorative": True,
                "width": 300,
                "image": "app_images/melissaateval.webp",
                "caption": "Your new student Melissa is a 12-year old girl with difficulty reading and understanding oral instructions.",
            },
            "chat": {
                "type": "chat_input",
                "max_messages": 30,
                "placeholder": "Ask Melissa something...",
                "initial_assistant_message": "Hi Teacher, can you help do better at school?"
            }
        },
        "phase_instructions": """For this chat, you play the role of a 12 year old girl named Melissa with a history of reading difficulties and understanding oral instructions. The user is playing the role of an assistive technology evaluator. You will be asked questions by the evaluator and respond with a short answer. Respond at a fifth-grade language level.
        Here is more information about Melissa:
        Here is the information for your role:
Student Name: Melissa
Age: 12
Gender: Female
Chief Challenges: Difficulty completing reading assignments and following her teacher's instructions.

# student History:
1. Educational Evaluation:

    a. Dyslexia: Diagnosed approximately 4 years ago and no assistive technology has been used to support her.
    b. Receptive Language Disorder: Has difficulty understanding what teachers say, gestures, and what is read. Has difficulty with spoken directions and multi-step directions. Has difficulty learning new words.
    
2. Family History:

    a. Mother: is a teacher's aide.
    b. Father: is an engineer with dyslexia.
    c. Siblings: have no learning disabilities.
3. Social History:

    a. Lifestyle: mother is available to help her with homework.
    b. Diet: omega-3 fatty acids, fresh fruits and vegetables, and vitamins and minerals to help with dyslexia.
    
4. Medications:

    a. Ritalin: for ADHD.

# Primary Learning Challenges:

1. Difficulty Reading Boods:

    a. Duration: 4 years
    b. Characterized as Difficulty decoding sounds and blending them into words.
    c. Slow and laborious reading speed.
    d. Misinterpreting punctuation and capitalization.
    e. Difficulty understanding what she reads.
2. Receptive Language Disorder:

    a. Having trouble understanding what people say, gestures, or what is read.
    b. Having trouble following spoken directions and multi-step instructions.
# Secondary Challenges:
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
    "primary_challenge": {
        "name": "Primary challenge",
        "fields": {
            "primary_challenge": {
                "type": "text_input",
                "label": "What is the user's primary challenge?",
            },
            "diagnosis": {
                "type": "text_area",
                "height": 200,
                "label": "Assistive Technology recommendations for Melissa.",
            }
        },
        "phase_instructions": """The user will provide you with the student's primary challenge and her assistive technology recommendations. You will provide feedback on the accuracy of their claim(s) based on the evidence they gathere in the conversation.
        
        Here are some more details:     
    # Differential Considerations:
1. Text to Speech Software:
    a. Takes text as an input and reads it aloud.
    b. Helps students learn to pronounce words.
2. Speech to Text Software:
    a. Transcribes spoken words into text.
    b. Removes the stress of spelling and punctuation in writing.
3. Highlight each word as it is read:
    a. Provides visual and auditory modalities of information input.
4. Visual Aids:
    a. Diagrams and pictures that help explain concepts.
    b. Provide diagrams of verbal instructions.
5. Breaking down instructions
    a. Reduce multi-step instructions into single steps.
    b. Allow the student to complete a step before providing the next step.
6. Provide Extra Time
    a. Prodivde student with additional time to complete work

# Plan for Further Evaluation:
1. Predictive Assessment of Reading (PAR):
    a.  screening assessment that is used to identify how well a student is predicted to read and if that student will experience difficulty with a specific area of reading. Each of these aspects are covered: Phonemic Awareness, Vocabulary, Single Letter and Word reading, and Fluency.
2. Dynamic Indicators of Basic Early Literacy Skills (DIBELS):
    a. standardized tests used to assess a student's fundamental reading skills, like phonemic awareness, letter recognition, and fluency, typically administered to children from kindergarten through 8th grade to identify potential literacy difficulties and monitor their progress over time; essentially, it's a quick way to gauge a child's basic reading abilities.
3. Texas Primary Reading Inventory (TPRI):
    a. one-on-one assessment to quickly assess students' early reading skills, helping teachers provide targeted instruction so that students improve as readers.
4. AIMSweb screening assessment:
    a. To assess Early Literacy, Reading, Early Numeracy, Mathematics, Spelling, and Writing.""",
        "user_prompt": "Melissa's primary challenge is: {primary_challenge}. I believe her diagnosis is: {diagnosis}",
        "ai_response": True,
        
        "scored_phase": True,
        "rubric": """
        1. Primary challenge:
        2 points - The user has provided a primary challenge that is consistent with Melissa's presentation and that they've extracted from the chat with Melissa.
        0 points - The user has provided a primary challenge that is not consistent with Melissa's presentation or they did not extract it from the chat with Melissa..
        2. Differential Diagnosis:
        2 points - The user has provided a differential diagnosis that is consistent with Melissa's presentation and that they've extracted from the chat with Melissa.
        0 points - The user has provided a differential diagnosis that is not consistent with Melissa's presentation or they did not extract it from the chat with Melissa.
        """,
        "minimum_score": 2,
    }

}

PREFERRED_LLM = "gpt-4o"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only

PAGE_CONFIG = {
    "page_title": "AT Evaluation Chatbot",
    "page_icon": "⛵",
    "layout": "centered",
    "initial_sidebar_state": "collapsed"
}

SIDEBAR_HIDDEN = False

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())
