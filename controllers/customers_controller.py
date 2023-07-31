from datetime import datetime

from config import Session
from views.customers_view import Customers_View
from models.customers_model import Customer

from permissions.permissions import Permissions

class Customers_Controller:
    
    def __init__(self, user):
        self.my_view = Customers_View()
        self.user = user
    
    def customers_menu(self):
        """_summary_
        Call custormers view to display all customers
        
        Returns:
            _type_: _value_
        """
        table_name = "Clients"
        
        
        session = Session()
        customers = session.query(Customer).all()
        
        choix = self.my_view.customers_view_list(table_name, customers)
        
        try:
            match choix[0]:
                case "1":
                    customer_id = self.my_view.customers_id_input()
                    self.customers_detail(customer_id)
                case "2":
                    self.customers_add()
                case "3":
                    customer_id = self.my_view.customers_id_input()
                    self.customers_update(customer_id)
                case "4":
                    customer_id = self.my_view.customers_id_input()
                    self.customers_delete(customer_id)
        except IndexError:
            return
    
    def customers_detail(self, customer_id):
        """_summary_
        Show customer details
        
        args:
            customer_id (int): customer id
        """
        session = Session()
        
        customer = session.query(Customer).filter(Customer.id == customer_id).first()
        
        self.my_view.customers_view_detail(customer)
        
    @Permissions.sales_required    
    def customers_add(self):
        """_summary_
        Call custormers view to add a customer
        
        Returns:
            _type_: _description_
        """
        session = Session()
        
        form = self.my_view.customers_view_add()
        
        create_customer = Customer(
            complet_name=form['complet_name'],
            email=form['email'],
            phone=form['phone'],
            company_name=form['company_name'],
            creation_date = datetime.now(),
            date_update=datetime.now(),
            sale_contact_id=form['sale_contact_id'],
        )
        
        session.add(create_customer)
        session.commit()
        
        self.my_view.customers_add_validate()
    
    @Permissions.sales_required
    def customers_update(self, customer_id):
        
        session = Session()
        
        customer = session.query(Customer).filter(Customer.id == customer_id).first()
        
        form = self.my_view.customers_view_update(customer)
        
        if form['complet_name'] != "":
            customer.complet_name = form['complet_name']
        if form['email'] != "":
            customer.email = form['email']
        if form['phone'] != "":
            customer.phone = form['phone']
        if form['company_name'] != "":
            customer.company_name = form['company_name']
        customer.date_update = datetime.now()
        if form['sale_contact_id'] != "":
            customer.sale_contact_id = form['sale_contact_id']
        
        session.commit()
        
        self.my_view.customers_update_validate()
    
    @Permissions.admin_required
    def customers_delete(self, customer_id):
        
        session = Session()
        
        customer = session.query(Customer).filter(Customer.id == customer_id).first()
        
        session.delete(customer)
        session.commit()
        
        self.my_view.customers_delete_validate()
