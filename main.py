def validate_user_input(user_input: str):
    if user_input=="":
        raise ValueError("No input provided")
