from ._anvil_designer import view_profileTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class view_profile(view_profileTemplate):
  def __init__(self, value_to_display, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    

    # Any code you write here will run before the form opens.
    self.data = tables.app_tables.product_details.search()
    
    self.id_list = []
    self.name_list = []
    self.categories_list = []
    self.profee_list = []
    self.extfee_list = []
    self.foreclose_list = []
    self.extension_list = []
    self.type_list = []
    self.int_type = []
    self.roi = []
    self.max_amount = []
    self.min_amount = []
    self.min_tenure_list = []
    self.max_tenure_list = []
    self.emi_payment = []
    self.dis_cou = []

    a = -1
    for i in self.data:
      a+=1
      self.id_list.append(i['product_id'])
      self.name_list.append(i['product_name'])
      self.categories_list.append(i['product_categories'])
      self.profee_list.append(i['processing_fee'])
      self.extfee_list.append(i['extension_fee'])
      self.foreclose_list.append(i['foreclose_type'])
      self.extension_list.append(i['extension_allowed'])
      self.type_list.append(i['membership_type'])
      self.int_type.append(i['interest_type'])
      self.roi.append(i['roi'])
      self.max_amount.append(i['max_amount'])
      self.min_amount.append(i['min_amount'])
      self.min_tenure_list.append(i['min_tenure'])
      self.max_tenure_list.append(i['max_tenure'])
      self.emi_payment.append(i['emi_payment'])
      self.dis_cou.append(i['discount_coupons'])

    if a == -1:
      alert("No Data Available Here!!")
    else:
      if value_to_display in self.id_list:
        b = self.id_list.index(value_to_display)
        self.label_1.text = value_to_display
        self.label_2.text = self.name_list[b]
        self.label_4.text = self.categories_list[b]
        self.label_5.text = self.profee_list[b]
        self.label_6.text = self.extfee_list[b]
        self.label_20.text = self.foreclose_list[b]
        self.label_22.text = self.extension_list[b]
        self.label_7.text = self.type_list[b]
        self.label_11.text = self.int_type[b]
        self.label_8.text = self.min_amount[b]
        self.label_9.text = self.max_amount[b]
        self.label_15.text = self.min_tenure_list[b]
        self.label_16.text = self.max_tenure_list[b]
        self.label_10.text = self.roi[b]
        self.label_18.text = self.emi_payment[b]
        self.label_12.text = self.dis_cou[b]

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_products.edit_form')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_products.update_form')
        
        
        
      