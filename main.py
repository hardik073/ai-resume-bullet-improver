from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

def improve_resume_bullet(bullet):
    prompt = f"""
    Rewrite the following resume bullet to make it more impactful,
    professional, and achievement-oriented:

    {bullet}
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"user","content":prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()

def main():
    print("=== AI Resume Bullet Improver ===")
    user_input = input("Enter your resume bullet:\n> ")
    improved = improve_resume_bullet(user_input)

    print("\nImproved Version:")
    print(improved)

if __name__ == "__main__":
    main()