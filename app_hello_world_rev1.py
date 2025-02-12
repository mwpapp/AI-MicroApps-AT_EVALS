PHASES = {
    "phase1": {
        "name": "What is your name?",
        "fields": {
                "name": {
                "type": "text_input",
                "label": "What is your first name?",
            },
            "disability": {
            	"type": "text_input",
            	"label": "What is your disability?"
            }
        },
        "user_prompt": "My name is {name} and I have {disability}. Write a sonnet about me and my activity.",
    },
}

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())
