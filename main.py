
import csv

class Users(object):
    def __init__(self, file_path):
        
        # open file 
        # Read and parse the CSV file
        self.file_path = open(file_path, 'r')
        self.data = csv.reader(self.file_path)

    def first_name_all(self):
        first_name = []
        first = 0
        for row in self.data:
            if first != 0:
                first_name.append(row[1])
            first += 1
        return first_name

        # Users data parse

        # retrun first_name all list type
    def last_name_all(self):
        last_name = []
        last = 0
        for row1 in self.data:
            if last != 0:
                last_name.append(row1[2])
            last += 1
        return last_name
        # Users data parse

        # retrun last_name all list type
        
        

    def gender_male_count(self):
        gender_m_count = 0
        for row3 in self.data:
            if row3[4] == 'Male':
                gender_m_count += 1
        return gender_m_count
        
        # Users data parse

        # retrun gender mael count 
        
        
    def gender_female_count(self):
        gender_f_count = 0
        for row in self.data:
            if row[4] == 'Female':
                gender_f_count += 1
        return gender_f_count

        # Users data parse

        # retrun gender femael count 
       

    def get_all_domain_names(self):
        unique_domains = set()
        for row in self.data:
            if len(row) > 3 and '@' in row[3]:
                email = row[3]
                domain_full = email.split('@')[-1]
                domain = domain_full.split('.')[0]
                unique_domains.add(domain)
        return list(unique_domains)
        
        # Users data parse

        # Return all unique domain names from the data.

        # sample: username@gmail.com -> domen_name = 'gmail'



    def get_all_unique_jobs(self):
        unique_jobs = set()  
        for row in self.data:
            if len(row) > 5:
                job = row[5]
                unique_jobs.add(job)
        return list(unique_jobs)
        

        # Get all unique jobs from user data

        # Return answer
        
        

    def get_one_user(self, id: int):
        for row in self.data:
            if row[0] == str(id):
                return row
        return None

        # Return the user ID data equal to the id value.
    
f = Users("user_data.csv")

#print(f.first_name_all())
#print(f.last_name_all()) 
#print(f.gender_male_count())
#print(f.gender_female_count()) 
#print(f.get_all_domain_names())
#print(f.get_all_unique_jobs())
#print(f.get_one_user(10))