import random
def generate_email():
    templates = [
        {
            'subject': "Your account has been compromised!",
            'from': "security@banking-alerts.com",
            'body': """Dear customer,<br>
            We noticed suspicious activity. Please verify:<br>
            <a href='http://fake-login.com'>Verify Account</a>"""
        },
        {
            'subject': "You won a prize!",
            'from': "noreply@prizehub.com",
            'body': """Congrats! Claim your gift card now:<br>
            <a href='http://freegift.com'>Claim Prize</a>"""
        },
        {
            'subject': "Password Reset Required",
            'from': "admin@webmail.com",
            'body': """Your password has expired. Reset here:<br>
            <a href='http://reset.com'>Reset Password</a>"""
        }
    ]
    return random.choice(templates)
