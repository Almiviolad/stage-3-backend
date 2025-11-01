import asyncio
from ai_core import generate_questions_from_note # Import your function

def main():
    """
    This is an async "wrapper" that allows us to use the 'await'
    keyword to properly call our AI function.
    """
    print("Testing AI core... Please wait.")
    
    # This is the test note you provided
    test_note = "Michael is a great guy that wants to becime a programmer, his name is Aloh Michael, a nigerian and loves to cide thoughhe is an intrivert"
    
    # We call your function using 'await'
    # This tells Python to "run the microwave and wait for the ding"
    quiz_data = generate_questions_from_note(test_note)
    
    # --- Check the results ---
    if quiz_data:
        print("\n✅ Success! AI returned quiz data:")
        print(json.dumps(quiz_data, indent=2)) # We need to import json
    else:
        print("\n❌ Failure. The function returned None.")
        print("   Check your GEMINI_API_KEY in .env and the AI's response.")

# --- This is the magic line ---
# It tells Python to get the asyncio manager and run our "main" function.
if __name__ == "__main__":
    import json # Add this import for pretty-printing
    main()
