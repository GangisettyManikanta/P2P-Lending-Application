import anvil.email
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42

@anvil.server.callable
def product_details(product_id, product_name,product_discription, product_categories,processing_fee,  extension_fee, membership_type, interest_type, max_amount, min_amount, min_tenure, max_tenure, roi, foreclose_type, extension_allowed, emi_payment, discount_coupons):
  row = app_tables.product_details.add_row(product_id=product_id,
                                           product_name=product_name,
                                           product_discription = product_discription,
                                           product_categories = product_categories,
                                           processing_fee=processing_fee,   
                                           extension_fee=extension_fee,
                                           membership_type=membership_type,
                                           interest_type= interest_type,
                                           # late_fee = late_fee,
                                           max_amount = max_amount,
                                           min_amount=min_amount,
                                           # tenure = tenure,
                                           min_tenure = min_tenure,
                                           max_tenure = max_tenure,
                                           roi = roi,
                                           foreclose_type=foreclose_type,
                                           extension_allowed=extension_allowed,
                                           # lapsed_status=lapsed_status,
                                           emi_payment = emi_payment,
                                           discount_coupons = discount_coupons
                                          )



@anvil.server.callable
def manage_products(groups,category):
  row = app_tables.product_categories.add_row(product_group=groups,product_category=category)


@anvil.server.callable
def user_issues_bugreports(user_issues, specific_issue, user_discription, image, feedback_form, email_user,coustmer_id):
 row = app_tables.user_issues_bugreports.add_row(user_issues=user_issues,
                                                 user_discription=user_discription,
                                                 specific_issue=specific_issue,
                                                 image=image,
                                                 feedback_form=feedback_form,
                                                 email_user=email_user,
                                                 customer_id=coustmer_id)




# @anvil.server.callable
# def add_product_group_to_table(group_name):
#     # Add the group_name to the "product_group" data table
#     app_tables.product_group.add_row(name=group_name)