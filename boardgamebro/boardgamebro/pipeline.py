"""Add custom pipeline code here"""

# For reddit and email-backend:
# we need get_and_validate_email in pipe.
# also for discord if user does not have email associated.

def bgb_sign_up_form(strategy, backend, request):
    # Send user to view with form
    # Form needs:
        # username
        # email
        # newsletter optin
        # privacy ok
        # tos ok
