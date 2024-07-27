import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers.string import StrOutputParser
from operator import itemgetter
from chain import prompt_template

load_dotenv()


class Wrap:
    def __init__(self):
        llm = ChatGoogleGenerativeAI(
            model="gemini-pro", google_api_key=os.getenv("GOOGLE_API_KEY")
        )
        self.chain = (
            prompt_template
            # {
            #     "name": itemgetter("name"),
            #     "year": itemgetter("year"),
            #     "university": itemgetter("university"),
            #     "python": itemgetter("python"),
            #     "java": itemgetter("java"),
            #     "webdev": itemgetter("webdev"),
            #     "ml": itemgetter("ml"),
            #     "projectType": itemgetter("projectType"),
            #     "projectArea": itemgetter("projectArea"),
            #     "projectDescription": itemgetter("projectDescription"),
            # }
            | llm
            | StrOutputParser()
        )

    def generate_text(self, prompt):
        return self.chain.invoke(prompt)