has_account = True
email_verified = False
email = "g@example.com"
user_age = 17

can_login = has_account  and email_verified 
is_email_valid = "@" in email 
is_age_valid = user_age >= 18
can_login_final = has_account and email_verified and is_email_valid and is_age_valid

print("can_login :", can_login)
print("is_email_valid :",is_email_valid)
print("is_age_valid :",is_age_valid)
print("can_login_final :", can_login_final)
print("has_account is true?", has_account is True)


