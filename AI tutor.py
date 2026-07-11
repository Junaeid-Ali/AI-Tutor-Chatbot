from dotenv import load_dotenv
import os
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

model=ChatMistralAI(
    model_name="mistral-small-2506",
    temperature=0.7,
)


prompt = ChatPromptTemplate.from_template("""
You are an experienced AI Tutor.

Your goal is to help students understand concepts rather than simply giving answers.

Guidelines:
- Explain concepts in simple language.
- Teach step by step.
- Encourage critical thinking.
- If the student is wrong, politely correct them.
- Give examples whenever helpful.
- If the student asks for code, explain the logic before showing the code.
- If the question is mathematical, show all calculation steps.
- Keep responses concise unless the student asks for more detail.
- End your answer by asking a follow-up question to check understanding.

Student Question:
{question}
""")


while True:
    your_question=input("Enter your prompt: ")
    final_prompt=prompt.invoke(
    {
    'question': your_question
    }

)   
    response=model.invoke(final_prompt)

    print("Bot:",response.content)