import os

from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai import errors


# .env ფაილიდან გარემოს ცვლადების წაკითხვა
load_dotenv()


SYSTEM_INSTRUCTION = (
    "შენ ხარ მოკლე, მეგობრული და გასაგები ასისტენტი. "
    "მომხმარებელს უპასუხე ქართულ ენაზე, მარტივად და თავაზიანად."
)


MODEL_NAME = "gemini-3.6-flash"

MINIMUM_TURNS = 4


def get_api_key():

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY ვერ მოიძებნა. "
            "შექმენი .env ფაილი და ჩაწერე:\n"
            "GEMINI_API_KEY=შენი_api_key"
        )

    return api_key


def safe_token_value(usage_metadata, field_name):

    if usage_metadata is None:
        return 0

    value = getattr(usage_metadata, field_name, None)
    return value if value is not None else 0


def print_usage_statistics(total_usage):

    print("\n" + "=" * 50)
    print("გამოყენებული ტოკენების სტატისტიკა")
    print("=" * 50)

    print(f"Prompt tokens:     {total_usage['prompt']}")
    print(f"Candidate tokens:  {total_usage['candidates']}")
    print(f"Thoughts tokens:   {total_usage['thoughts']}")
    print(f"Total tokens:      {total_usage['total']}")


def run_chatbot():
    try:
        api_key = get_api_key()
        client = genai.Client(api_key=api_key)

    except ValueError as error:
        print("\nკონფიგურაციის შეცდომა:")
        print(error)
        return

    # აქ ინახება მთელი საუბრის ისტორია.
    history = []

    # აქ დავაგროვებთ ყველა API გამოძახების token-ებს.
    total_usage = {
        "prompt": 0,
        "candidates": 0,
        "thoughts": 0,
        "total": 0,
    }

    completed_turns = 0

    print("=" * 60)
    print("Gemini ჩატბოტი")
    print("=" * 60)
    print("ჩატის დასასრულებლად ჩაწერე: exit")
    print(f"საჭიროა მინიმუმ {MINIMUM_TURNS} ეტაპიანი საუბარი.\n")

    while True:
        user_message = input("შენ: ").strip()

        if not user_message:
            print("გთხოვ, ცარიელი შეტყობინება არ გაგზავნო.\n")
            continue

        if user_message.lower() in {"exit", "quit", "გასვლა"}:
            if completed_turns < MINIMUM_TURNS:
                remaining = MINIMUM_TURNS - completed_turns

                print(
                    f"\nჯერ საჭიროა კიდევ {remaining} შეტყობინება, "
                    f"რადგან დავალება მინიმუმ {MINIMUM_TURNS}-ეტაპიან "
                    "საუბარს მოითხოვს.\n"
                )
                continue

            break

        # ახალი მომხმარებლის შეტყობინება ემატება ისტორიაში.
        history.append(
            types.UserContent(
                parts=[
                    types.Part.from_text(text=user_message)
                ]
            )
        )

        try:
            # ყოველ API გამოძახებაზე იგზავნება მთელი history.
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=history,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_INSTRUCTION,
                    temperature=0.7,
                ),
            )

            model_answer = response.text

            if not model_answer:
                model_answer = (
                    "მოდელმა ტექსტური პასუხი ვერ დააბრუნა."
                )

            print(f"\nGemini: {model_answer}\n")

            # მოდელის პასუხიც ემატება ისტორიაში.
            history.append(
                types.ModelContent(
                    parts=[
                        types.Part.from_text(text=model_answer)
                    ]
                )
            )

            completed_turns += 1

            # მიმდინარე response-ის token-ების დამატება.
            usage = response.usage_metadata

            total_usage["prompt"] += safe_token_value(
                usage,
                "prompt_token_count",
            )

            total_usage["candidates"] += safe_token_value(
                usage,
                "candidates_token_count",
            )

            total_usage["thoughts"] += safe_token_value(
                usage,
                "thoughts_token_count",
            )

            total_usage["total"] += safe_token_value(
                usage,
                "total_token_count",
            )

        except errors.ClientError as error:
            print("\nGemini API-ის ClientError დაფიქსირდა.")
            print(f"Status code: {getattr(error, 'code', 'უცნობია')}")
            print(f"დეტალები: {error}")
            break

        except errors.ServerError as error:
            print("\nGemini სერვერის შეცდომა დაფიქსირდა.")
            print("სცადე პროგრამის ხელახლა გაშვება.")
            print(f"დეტალები: {error}")
            break

        except Exception as error:
            print("\nმოულოდნელი შეცდომა დაფიქსირდა.")
            print(f"შეცდომის ტიპი: {type(error).__name__}")
            print(f"დეტალები: {error}")
            break

    print("\nჩატი დასრულებულია.")
    print(f"შესრულებული ეტაპები: {completed_turns}")

    print_usage_statistics(total_usage)


if __name__ == "__main__":
    run_chatbot()
