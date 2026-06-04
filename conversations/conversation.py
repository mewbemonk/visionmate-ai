from speech_to_text.listen import listen
from memory.context import get_context
from agents.questions_agent import questions
from text_to_speech.pyttsx import voice
from agents.search_agent import search_agent







while True:

    question = listen()

    if not question.strip():
        continue

    print("Questions: ", question)

    if question.lower().strip() == 'exit':
        voice("Thank You")
        break

    answer = questions(
        get_context(),
        question
    )

    if answer == "SEARCH_REQUIRED":

        answer = search_agent(
            get_context(),
            question
        )

    print("answers: ", answer)

    voice(answer)