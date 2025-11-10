class Students:
    discount_amt = 200

    def __init__(self, first_name, last_name, tution_fee):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = f"{first_name}.{last_name}@std.kyrenia.edu.tr"
        self.tution_fee = tution_fee

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def apply_discount(self):
        self.tution_fee = int(self.tution_fee) - self.discount_amt
        return self.tution_fee

    def __repr__(self):
        return f"Student('{self.first_name}', '{self.last_name}', {self.tution_fee})"
    
    def __str__(self):
        return f"{self.full_name()} - {self.email_address}"
    
    def __add__(self, other):
        return self.tution_fee + other.tution_fee


# Create student objects
k2020 = Students('Rae', 'Wale', 8000)
k2021 = Students('Cell', 'Zed', 9000)
k2022 = Students('Lee', 'Min', 10000)

# Example usage
total_tution_fee = sum([e.tution_fee for e in (k2020, k2021, k2022)])
print("Total Tuition Fee:", total_tution_fee)
