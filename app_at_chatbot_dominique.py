APP_URL = "https://Dominiquechatbot-v1.streamlit.app/"
APP_IMAGE = "clinical_chatbot_general.webp"
PUBLISHED = True

## Set the API key and model name
MODEL="gpt-4o-mini"
##client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

APP_TITLE = "Assistive Technology Evaluation Chatbot"
APP_INTRO = """
In this interactive exercise, you will interact with a student chatbot that will help you understand your student's assistive technology needs. You must determine their functional limitations and provide recommendations for assistive technology as classroom accomodations.
"""

APP_HOW_IT_WORKS = """
This app provides a structured way to interact with an AI-powered student chatbot.

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
        "name": "Student Interview: Dominique",
        "fields": {
            "intro": {
                "type": "markdown",
                "body": """<p>Dominique is a student in 11th grade in your school who has been diagnosed with Retinitis Pigmentosa, a degenerative eye disease that leads to the progressive breakdown of the light-sensitive cells on his retina. His eyesight has been getting gradually worse, and he is no longer able to effectively read large text using a video magnifier or screen magnification software. You have 30 minutes to assess Dominique and determine what assistive technology might accommodate him in class. For this simulation, that means you’ll be able to ask him up to 30 questions.</p>""",
                "unsafe_allow_html": True,
            },
            "student_image": {
                "type": "image",
                "decorative": True,
                "width": 300,
                "image": "app_images/dominque.webp",
                "caption": "Your student Dominque is a 16-year-old young man with Retinitis Pigmentosa.",
            },
            "chat": {
                "type": "chat_input",
                "max_messages": 30,
                "placeholder": "Ask Dominique something...",
                "initial_assistant_message": "Good morning, Teacher, can you help do better at school?"
            }
        },
        "phase_instructions": """For this chat, you play the role of a 12 year old girl named Dominique with a history of reading difficulties and understanding oral instructions. The user is playing the role of an assistive technology evaluator. You will be asked questions by the evaluator and respond with a short answer. Respond at a fifth-grade language level.
        Here is more information about Dominique:
        Here is the information for your role: 

Student Name: Dominque 
Age: 16 
Gender: Male 
Chief Complaint: eye sight has decreased to the point that he requires magnification so high that an entire word will not fit on a screen or single page. He is no longer able to read printed words quickly and effectively,  resulting in him being unable to obtain information from printed text. 

# Student History 

Medical History: 
Retinitis pigmentosa diagnosed at age 9. Symptoms include night blindness, peripheral vision loss (tunnel vision), difficulty seeing colors, extreme sensitivity to bright light, and blurred vision.  
Current visual acuity is 20/400, which requires letters to be at least 7” tall for him to see.  
He also has mild hearing loss at 26 dB in his better ear. He has difficulty hearing soft voices, understanding speech in noisy environments, distinguishing consonant sounds like “s”, “f”, and “th”.  

Family History: 
Father has retinitis pigmentosa and is only able to distinguish light and dark visually. 
Mother has completely normal vision. 

Social History 
Lifestyle: Has a brother and sister with normal vision 
Diet: takes vitamin A supplements 

Medications: 
No medications at this time 
No eye glasses 
No hearing aids 

# Primary Learning Challenges:  

No longer able to read 
Can not read printed text unless each letter is at least 7” tall 
When using a screen magnifier, can not fit a long word entirely on the screen 
When using a video magnifier or CCTV, cannot fit a long word entirely on the screen 
Does not know Braille 
Has never had Orientation and Mobility training with a white cane. 
Has difficulty understanding teachers and peers in loud environments and distinguishing some consonant sounds. 
        """,
        "user_prompt": """From the chat, provide feedback on the following: 
        1. Whether the evaluator is asking appropriate questions.
        2. Whether the evaluator has an appropriate manner and makes the student feel comfortable. 
        3. Whether the evaluator is staying on topic.

        Begin your response with "Here is some feedback on your chat with Dominique:"
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
                "label": "Assistive Technology recommendations for Dominique.",
            }
        },
        "phase_instructions": """The user will provide you with the student's primary challenge and her assistive technology recommendations. You will provide feedback on the accuracy of their claim(s) based on the evidence they gathere in the conversation.
        
        Here are some more details:     
    # Differential Considerations:
Start to learn Braille 

Contact the Alabama Instructional Resource Center for the Blind (AIRCB) is a service that provides braille and large print materials for students who are blind or visually impaired. It is located on the campus of the Alabama School for the Blind to find resources to teach Braille 

Contact local Alabama Institute for the Deaf and Blind (AIDB) to find resources to teach Braille 

Start using audiobooks and electronic texts 

Contact The Alabama Regional Library for the Blind and Physically Disabled to find resources for audio books. 

Contact National Library Service for the Blind and Print Disabled to learn about the BARD (Braille and Audio Reading Download) system 

Start learning to use a screen reader, depending on the computer operating system 

JAWS for Windows computer is a paid screen reader from Freedom Scientific 

NVDA (Non-Visual Desktop Access) for Windows computer is a free open-source screen reader 

Voice Over screen reader for Apple’s MacOS and iOS and iPadOS devices 

ChromeVox for Chromebooks and ChromeOS devices 

Provide 3D manipulatives   

3D manipulatives for blind students are tactile objects, often created using a 3D printer, that allow them to physically explore and understand concepts through touch, particularly in areas like geometry, science, and anatomy, by providing detailed, textured representations of shapes, structures, and features that they cannot see 

These can include 3D printed models of organs, geometric shapes with raised lines, molecular structures, and even maps with textured topography, all designed with accessibility in mind, often including braille labels for identification.  

# Plan for Further Evaluation 

Braille Displays 

Explore learning to read and use a Braille Display 

Explore using a Braille tablet, such as the Monarch from American Printing House for the Blind 

Obtain a  hearing test to determine level of hearing loss 

Request hearing aids 

Assistive technology to improve hearing """,
        "user_prompt": "Diminique's primary challenge is: {primary_challenge}. I believe his diagnosis are: {diagnosis}",
        "ai_response": True,
        
        "scored_phase": True,
        "rubric": """
        1. Primary challenge:
        2 points - The user has provided a primary challenge that is consistent with Diminique's presentation and that they've extracted from the chat with Dominique.
        0 points - The user has provided a primary challenge that is not consistent with Dominique's presentation or they did not extract it from the chat with Dominique..
        2. Differential Diagnosis:
        2 points - The user has provided a differential diagnosis that is consistent with Dominique's presentation and that they've extracted from the chat with Dominique.
        0 points - The user has provided a differential diagnosis that is not consistent with Dominique's presentation or they did not extract it from the chat with Dominique.
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
    "page_icon": "✏️",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = False

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())
