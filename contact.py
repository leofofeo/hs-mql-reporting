class Contact():

    def __init__(self, first_name, last_name, email, became_mql_date):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.mql_date = became_mql_date
    
    def __str__(self):
        return f"""
        Email: {self.email}
        First name: {self.first_name}
        Last Name: {self.last_name}
        MQL date: {self.mql_date}
        """