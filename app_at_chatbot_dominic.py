APP_URL = "https://dominic-chatbot.streamlit.app/"
APP_IMAGE = "ai_chatbot_vision.webp"
PUBLISHED = True

## Set the API key and model name
MODEL="gpt-4o"
##client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

APP_TITLE = "Dominic's Assistive Technology Evaluation"
APP_INTRO = """
In this interactive exercise, you will interact with a student chatbot with a vision impairment that will help you understand your student's assistive technology needs. You must determine their functional limitations and provide recommendations for assistive technology as classroom accommodations.
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
        "name": "Student Interview: Dominic",
        "fields": {
            "intro": {
                "type": "markdown",
                "body": """<p>Dominic is a student in 11th grade in your school who has been diagnosed with Retinitis Pigmentosa, a degenerative eye disease that leads to the progressive breakdown of the light-sensitive cells on his retina. His eyesight has been getting gradually worse, and he is no longer able to effectively read large text using a video magnifier or screen magnification software. You have 30 minutes to assess Dominic and determine what assistive technology might accommodate him in class. For this simulation, that means you’ll be able to ask him up to 60 questions.</p>""",
                "unsafe_allow_html": True,
            },
            "student_image": {
                "type": "image",
                "decorative": False,
                "width": 300,
                "image": "app_images/dominic.webp",
                "caption": "Your student Dominque is a 16-year-old young man with Retinitis Pigmentosa.",
                "alt": "A portrait of Dominic, a 16-year-old young African-American man wearing dark glasses and a school uniform in a classroom."
            },
            "chat": {
                "type": "chat_input",
                "max_messages": 60,
                "placeholder": "Ask Dominic something...",
                "initial_assistant_message": "Good morning, Teacher, can you help do better at school?"
            }
        },
        "phase_instructions": """For this chat, you play the role of a 16 year old boy named Dominic with a history of low vision and difficulty hearing. The user is playing the role of an assistive technology evaluator. You will be asked questions by the evaluator and respond with a short answer. Respond at a tenth-grade language level with short answers. Provide short, concise answers, and do not volunteer information the evaluator didn't ask for. The evaluator will need to ask direct questions to get you to provide that piece of information. 
        Here is more information about Dominic:
        Here is the information for your role: 

Student Name: Dominque 
Age: 16 
Gender: Male 
Chief Complaint: eye sight has decreased to the point that he requires magnification so high that an entire word will not fit on a screen or single page. He is no longer able to read printed words quickly and effectively,  resulting in him being unable to obtain information from printed text. 

# Student History 

Medical History: 
Retinitis pigmentosa was diagnosed at age 9. Symptoms include night blindness, peripheral vision loss (tunnel vision), difficulty seeing colors, extreme sensitivity to bright light, and blurred vision.  
Current visual acuity is 20/400, which requires letters to be at least 7” tall for him to see.  
Student has hearing loss that has never been diagnosed. He also has mild hearing loss at 26 dB in his better ear. He has difficulty hearing soft voices, understanding speech in noisy environments, distinguishing consonant sounds like “s”, “f”, and “th”.  

Accommodation History:
Student has been using ZoomText Magnifer software on a windows computer. Current magnification level is 16 times normal size. Student uses large yellow mouse pointer and uses a bright green cursor.
Student has been using a CCTV, or video magnifer called the Merlin from Enhanced Vision. He is currently using it with 16 times to 24 times magnificaiton.
Student has access to Windows computers in class and at home, and has an iPhone and iPad at home. 
Student has never used text-to-speech and never used audiobooks.
Student has been recieveing large print handouts and worksheets, which he then views on his CCTV/Video Magnifier. 
Student has never recieved any accomodations for hearing loss, as the school does not yet realize it is a problem. 
The student has been writing notes with a large felt-tipped pen called the 20-20-style BoldWriter, but can no longer read his notes.
The student has been sitting in an assigned seat in the center of the classroom.

Family History: 
Father has retinitis pigmentosa and is only able to distinguish light and dark visually. 
Mother has completely normal vision. 

Social History 
Lifestyle: Has a brother and sister with normal vision 
Diet: takes vitamin A supplements 
The student is very concerned that he will look different. 
He is hesitant to use a white cane for orientation and mobility because it will make him look more disabled. 
He is hesitant to wear hearing aids because he thinks they are really big and other people will make fun of him.

Medications: 
No medications at this time 
wears eyeglasses 
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

        Begin your response with "Here is some feedback on your chat with Dominic:"
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
                "label": "Assistive Technology recommendations for Dominic.",
            }
        },
        "phase_instructions": """The user will provide you with the student's primary challenge and her assistive technology recommendations. You will provide feedback on the accuracy of their claim(s) based on the evidence they gathere in the conversation.
        
        Here are some more details:     
    # Differential Considerations:
Start to learn Braille 

Contact the Alabama Instructional Resource Center for the Blind (AIRCB) is a service that provides braille and large print materials for students who are blind or visually impaired. It is located on the campus of the Alabama School for the Blind to find resources to teach Braille 

Contact local Alabama Institute for the Deaf and Blind (AIDB) to find resources to teach Braille 

Start using audiobooks and electronic texts on a tablet or laptop

Contact The Alabama Regional Library for the Blind and Physically Disabled to find resources for audio books. 

Contact the National Library Service for the Blind and Print Disabled to learn about the BARD (Braille and Audio Reading Download) system. 

Start learning to use a screen reader, depending on the computer operating system 

JAWS for Windows computer is a paid screen reader from Freedom Scientific or NVDA (Non-Visual Desktop Access) for Windows computers is a free open-source screen reader 

Voice Over screen reader for Apple’s MacOS and iOS and iPadOS devices 

ChromeVox for Chromebooks and ChromeOS devices 



Receive training to use a screen reader and how to navigate a Windows laptop or iPad with the screen reader.
Receive training on using a tablet to take a photo of documents and use optical character recognition (OCR) software to read it to him. 

Provide 3D manipulatives   
     3D manipulatives for blind students are tactile objects, often created using a 3D printer, that allow them to physically explore and understand concepts through touch, particularly in areas like geometry, science, and anatomy, by providing detailed, textured representations of shapes, structures, and features that they cannot see 
     These can include 3D printed models of organs, geometric shapes with raised lines, molecular structures, and even maps with textured topography, all designed with accessibility in mind, often including braille labels for identification.  

# Plan for Further Evaluation 

Try  different Braille Displays 

Explore learning and training to read and use a Braille Display 

Explore using a Braille tablet, such as the Monarch from American Printing House for the Blind 

Obtain a  hearing test to determine the level of hearing loss 

Request hearing aids 

Request seating in the front of the room. 

Assistive technology to improve hearing, such as a classroom FM system or personal FM system such as the Williams Sound PFM Pro Personal FM Listening System """,
        "user_prompt": "Dominic's primary challenge is: {primary_challenge}. I believe his diagnosis are: {diagnosis}",
        "ai_response": True,
        
        "scored_phase": True,
        "rubric": """
        1. Primary challenge:
        2 points - The user has provided a primary challenge that is consistent with Dominic's presentation and that they've extracted from the chat with Dominic.
        0 points - The user has provided a primary challenge that is not consistent with Dominic's presentation or they did not extract it from the chat with Dominic..
        2. Differential Diagnosis:
        2 points - The user has provided assistive technology recommendations that are consistent with Dominic's presentation and that they've extracted from the chat with Dominic.
        0 points - The user has provided assistive technology recommendations that are not consistent with Dominic's presentation or they did not extract it from the chat with Dominic.
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
    "page_title": "AT Evaluation Chatbot",
    "page_icon": "✏️",
    "layout": "centered",
    "initial_sidebar_state": "collapsed"
}

SIDEBAR_HIDDEN = False

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())
