from ._anvil_designer import borrower_foreclosure_requestTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class borrower_foreclosure_request(borrower_foreclosure_requestTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Fetch the current user during form initialization
        user = anvil.users.get_user()
        # Check if a user is logged in
        if user:
            # Fetch the userprofile record based on the current user's email
            user_profile = app_tables.user_profile.get(email_user=user['email'])
            # Check if the user profile record is found
            if user_profile:
                # Access the user ID from the userprofile record
                user_id = user_profile['customer_id']
                # Filter loan_details table based on the current user's ID
                try:
                    customer_loans = app_tables.loan_details.search(borrower_customer_id=user_id)
                    # Set the filtered data as the items for the repeating panel
                    self.repeating_panel_1.items = customer_loans
                except anvil.tables.TableError as e:
                    print(f"Error: {e}")
            else:
                # Handle the case when no user profile record is found
                print("User profile record not found for the current user.")
        else:
            # Handle the case when no user is logged in
            print("No user logged in")

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('bank_users.borrower_dashboard')
