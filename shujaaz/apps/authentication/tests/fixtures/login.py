correct_login_details = {"password": "salma123", "email": "user1@quexl.com"}

correct_login_response = "You have successfully logged in"


def update_login_details(detail, value):
    """
    update login details
    """
    new_login = correct_login_details.copy()

    if value is None:
        new_login.pop(detail)
    else:
        new_login[detail] = value

    return new_login


invalid_login_password = update_login_details("password", "worngPass1")
invalid_login_email = update_login_details("email", "wrong@email.com")
blank_password_login = update_login_details("password", "")
blank_email_login = update_login_details("email", "")
missing_email_login = update_login_details("email", None)
missing_password_login = update_login_details("password", None)

invalid_login_email_response = {
    "response":{
        "non_field_errors":[
            "Either your email or password is not right. Double check "
                "them, or reset your password to log in. "
        ]}
}

blank_email_login_response = {
    "response":{"email":["This field may not be blank."]}
}

missing_email_login_response = {
    "message": "Login failed. Fix the error(s) below",
    "error": "This field may not be null.",
}

missing_password_login_response = {
    "message": "Login failed. Fix the error(s) below",
    "error": "This field may not be null.",
}

blank_password_login_response = {
    "response":{"password":["This field may not be blank."]}
}
