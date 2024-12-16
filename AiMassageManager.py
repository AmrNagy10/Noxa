from main import vars
import google.generativeai as genai
from langchain_ollama import OllamaLLM


class Ai:
    def __init__(self, message):
        GEMINI_API_KEY = vars("GEMINI_API_KEY")
        genai.configure(api_key=GEMINI_API_KEY)
        self.message = message
        self.model = OllamaLLM(model="llama3")
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
        )
        self.chat_session = model.start_chat(history=[])

    def Ai(self):
        quary = "Without and never add any additional word. Rewrite the brackets ({input}) into one of the following forms: \
        [YouTubeSearch, keyword] or \
        [Goto, folder name] or \
        [Getfrom, file name, folder name] or \
        [Site, URL] or \
        [translate, text, ISO 639-1 code for the language] or \
        [Ask, Message] or \
        [exit] or\
        [lock] based on its meaning."
        try:
            response = self.chat_session.send_message(
                quary.format(input=self.message)
            ).text
            inner_text = response[1:-2]
            result = inner_text.split(", ")
            if len(result) > 3:
                text = ", ".join(result[1:-1])
                result[1] = text
                del result[2]
            return result
        except:
            resulte = self.model.invoke(
                input=f"Without and never add any additional word. rewrite the brackets ({self.message}) into one of the following forms: [YouTubeSearch, key word] or [Goto, folder name] or [Getfrom, file name, folder name] \
                or [Site, URL] or [translate, text, ISO 639-1 code for the language] or [Lock: in capital case, lock: in lower case] or [close, exit] based on its meaning."
            ).splitlines()
            for line in range(len(resulte)):
                if resulte[line].startswith("[") and resulte[line].endswith("]"):
                    print(eval(str(resulte[line])))
                    break

    def speakwithai(self):
        try:
            response = self.chat_session.send_message(self.message)
            return response.text

        except:
            resulte = self.model.invoke(input=self.message)
            return resulte
