'''
NAME
    Make_FakeAthleticClub.py


PURPOSE
    Loads neccessary  external  modules   and   classes,  and provides internal  class\n
    definitions for the  FakeAthleticClub  subclass, which inhereits from the FakeCompany\n  
    superclass.


FUNCTIONS
    #1 Imports Data Providers As Global Variables Named  fake  And  phony 
    
    #2 Imports the  FakeCompany  superclass

    #3 Defines The  FakeAthleticClub  subclass


DEPENDENCIES
    #1 initialize_fake_data_providers.py\n

    #2 Make_FakeCompany.py
'''


from Make_FakeCompany import FakeCompany, phony, fake



#  2) Defining The FakeAthleticClub Class
#####################################################################################################
class FakeAthleticClub( FakeCompany ):
    '''
    NAME
        FakeAthleticClub


    SYNOPSIS
        A  subclass  which  inherits  from the  FakeCompany  superclass.\n 
        Represents a company specializing in  Fitness and Nutition  services.    


    COMPONENTS
        #2.a) Overload Of The FakeCompany  Constructor
            i.  __init__()

        #2.b) Overload  Of The FakeCompany  MakeFakePayroll Method 
            i.  MakeFakePayroll()  


        #2.c A Method To Generate A Fake, Randomized "Members" Dictionary
            i.  MakeFakeMembers()  


    ATTRIBUTE PARAMETERS
        name           -   Defines the Fake Company's Name\n
                           DEFAULT VALUE:  random fake company name\n 

        category       -   Defines what type of Fake Company it is\n
                           DEFAULT VALUE:  random fake company type\n

        employee_size  -   Defines the number of records to be produced
                           for Payroll or Personnel oreiented reports\n
                           DEFAULT VALUE:  random  integer  between  10  and  160\n

        member_size    -   Defines the number of records to be produced
                           for Member or Service oreiented reports\n
                           DEFAULT VALUE:  random  integer  between  2  and  500\n

        city           -   Defines the  US City  where the Company is located\n
                           DEFAULT VALUE:  random  fake  or  existing  US City\n

        state          -   Defines the  2-letter US State Abbreviation  where the Company is 
                           located\n
                           DEFAULT VALUE:  random  existing   2-letter US State Abbreviation\n 
   
        zip_code       -   Defines the  US Zip Code  where the Company is located\n
                           DEFAULT VALUE:  random  fake  or  existing  US Zip Code\n

        departments    -   Defines the list of possible departments to which employees at this 
                           Company might belong\n
                           DEFAULT VALUE:  Management, Personal Training, Coaching Staff,\n 
                                           Sales and Merchandise,  and   Diet and Nutrition

    
    EXAMPLE OUTPUT
        Name: Pull Applications Fitness\n
        Category: Athletic Club\n
        Number of Employees: 25\n
        City:  New Andrewshire\n
        State: DC\n
        Zip Code: 20018\n
        Departments: [
            'Management',
            'Personal Training',
            'Coaching Staff',
            'Sales and Merchandise',
            'Diet and Nutrition'
        ]\n
        Payroll: dict_keys([
            'Employee ID',
             'First Name',
             'Last Name',
             'Date Of Birth',
             'Phone Number',
             'Address',
             'City',
             'State',
             'Zip Code',
             'Hire Date',
             'Salary',
             'Department'
        ])\n


    PARENT MODULE
        FakeCompany.py
    '''

    # 2.a) Overload Of The FakeCompany  Constructor  
    ############################################################################
    def __init__(                                                #
    self,                                                        # A Contrsuctor                 
    name   =  ' '.join(phony.Text().words(1)).title()+" Fitness",# whose params 
    category      =  "Athletic Club",                            # may all be                
    employee_size =  phony.Numeric().integer_number(10,160),     # optionally                   
    member_size   =  phony.Numeric().integer_number(2, 500),     # priovided,                      
    city          =  fake.city(),                                # with the   
    state         =  fake.state_abbr(),                          # exception of    
    zip_code      =  fake.zipcode(),                             # "departments",   
    departments   =  [                                           # which     
        "Management",                                            # initializes   
        "Personal Training",                                     # as a static  
        "Coaching Staff",                                        # list.  
        "Sales and Merchandise",                                 #  
        "Diet and Nutrition"                                     # 
    ]                                                            #
    ):                                                           #
        self.Name         =  name                                # Once the   
        self.Category     =  category                            # state
        self.EmployeeSize =  employee_size                       # param is 
        self.MemberSize   =  member_size                         # accessible, 
        self.City         =  city                                # clobber
        self.State        =  state                               # the zip_code
        self.ZipCode      =  fake.zipcode_in_state(state)        # param with an  
        self.Departments  =  departments                         # improvement.
    ############################################################################


    # 2.b) Overload  Of The  FakeCompany  MakeFakePayroll Method  
    ############################################################################
    def MakeFakePayroll(self):
        '''
        NAME
            MakeFakePayroll


        SYNOPSIS
            Creates a  dictionary of lists  consisting of randomly\n 
            generated  fake data,  specifically modeled to resemble a\n
            simplified Payroll for a company specializing in Fitness and\n 
            Nutrition Services.


        DESCRIPTION
            An  Overload  for the  FakeCompany.MakeFakePayroll() Method\n
            which modifies a  copy  of the  superclass method's\n
            resultant dictionary of lists  in a way that more closely\n 
            simulates a dataset that specifically ressembles an\n
            Athletic Club.\n 

            Once the  copy  of the  Payroll Dictionary  has been adapted to\n
            the specificity of the "Athletic Club" profile, the  copy\n
            is then returned as output, thereby replacing the\n
            the original end value of the  superclass's MakeFakePayroll() 
            Method.   


        PROCESS
            #2.b.i.1 
                Retrieve a copy of the  Fake Payroll Dictionary  produced by\n  
                the superclass's  MakeFakePayroll  Method  to simplify code\n
                refactoring efforts.      

            #2.b.i.2 
                Replace any  Payroll Attributes  which are inconsistent\n 
                with the  FakeAthleticClub's Profile  with  adjusted values. 
                 
            #2.b.i.2 
                Export the  Fake Payroll,  which is now a   dict of lists.    


        INPUTS
            None

        
        OUTPUT
            a  <dict>  whose  keys  correspond to the  Payroll's  Column Names\n
            amd whose  values  correspond to "rows" or "records" of  Employees
            

        PARENT:
            FakeCompany
        '''

        # 2.b.i.1)   Retrieve a copy of the  Fake Payroll Dictionary  produced by  
        #            the superclass's  MakeFakePayroll  Method  to simplify code
        #            refactoring efforts      
        #||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||#       
        FakeAthleticClubPayroll = FakeCompany(       # 
            name            =   self.Name,           # The FakeCompany 
            category        =   self.Category,       # (superclass)  
            employee_size   =   self.EmployeeSize,   # MakeFakePayroll Method 
            city            =   self.City,           # is invoked using  
            state           =   self.State,          # the  FakeAthleticClub 
            zip_code        =   self.ZipCode,        # (subclass) constructor 
            departments     =   self.Departments     # parameters
        ).MakeFakePayroll()                          #
        #||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||#
        
        # 2.b.i.2)   Replace any  Payroll Attributes  which are inconsistent 
        #            with the  FakeAthleticClub's Profile  with  adjusted values. 
        #||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||#
        FakeAthleticClubPayroll["Date Of Birth"] = [ # 
                                                     #  
            phony.Datetime().date(                   # Adjust the default range     
                1985,                                # of Employee Birth Dates    
                2000                                 # to simulate a younger  
            ).strftime('%m/%d/%Y')                   # demographic,  
                                                     # for each of the        
            for _ in range(self.EmployeeSize)        # 'EmployeeSize' many rows     
                                                     # 
        ]                                            #
                                                     #
        FakeAthleticClubPayroll["Salary"]       =  [ # Adjust the default range    
                                                     # of Employee Salaries   
            phony.Finance().price(50000, 75500)      # to simulate low income  
                                                     # levels, 
            for _ in range(self.EmployeeSize)        # for each of the       
                                                     # 'EmployeeSize' many rows    
        ]                                            # 
                                                     # 
        FakeAthleticClubPayroll['Employee ID']  = [  # Adjust the default range      
                                                     # of Employee ID Numbers    
            fake.iana_id()[:5]                       # to not exceed 5 digits 
                                                     # in length,   
            for _ in range(self.EmployeeSize)        # for each of the       
                                                     # 'EmployeeSize' many rows    
        ]                                            # 
        #||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||||#

        # 2.b.i.3)   Export the  Fake Payroll,  which is now a   dict of lists.     
        #|||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
        return FakeAthleticClubPayroll  # for use as input in a Pandas DataFrame
        #|||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
    ############################################################################


    # 2.c) A Method To Generate A Fake, Randomized "Members" Dictionary
    ############################################################################
    def MakeFakeMembers(self):
        '''
        NAME
            MakeFakeMembers


        SYNOPSIS
            Creates a  dictionary of lists  consisting of randomly\n 
            generated  fake data,  specifically modeled to resemble a\n
            collection of  "Member" Clients  belonging to a company\n 
            specializing in  Fitness  and  Nutrition  Services.


        DESCRIPTION
            Utililizes the  FakeAthleticClub.MakeFakePayroll() Method\n
            Overload,  which modifies a  copy  of the  supclass method's\n
            resultant dictionary of lists  in a way that more closely\n 
            simulates a dataset that specifically ressembles an Athletic Club. 

            Once the  copy  of the  Payroll Dictionary  has been adapted to\n
            the specificity of the "Athletic Club" profile, the  copy\n
            is then re-modified in a process where the FakeAthleticClub's\n
            adjusted attriubutes are filtered to simulate a data context\n
            resembling  Athletic Club Clients,  a.k.a. "Members",  rather\n
            than  Athletic Club Employees. 


        PROCESS
            #2.c.i.1 
                Retrieve a copy of the  Fake Payroll Dictionary  produced by\n  
                the superclass's  MakeFakePayroll  Method  to simplify code\n
                refactoring efforts.      

            #2.c.i.2 
                Filter out any  Coulumn Attributes which are not consistant\n
                with a  Athletic Company Members  Data Context.  
            
            #2.c.i.3)   
                Add  additional columns  to the  Member Data Context\n 
                representing  a  Member's  ID,  Membership Date,  and\n  
                Membership Plan.

            #2.c.i.4) 
                Export the  Fake Members,  which is now a   dict of lists.    


        INPUTS
            None

        
        OUTPUT
            a  <dict>  whose  keys  correspond to  Column Attribute Names\n
            amd whose  values  correspond to "rows" or "records" of  Members.
        '''

        # 2.c.i.1)   Retrieve a copy of the  Fake Payroll Dictionary  produced   
        #            by the superclass's  MakeFakePayroll  Method  to simplify 
        #            code refactoring efforts. 
        #||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||#
        FakeAthleticClubMembers = FakeCompany(           # The FakeCompany  
            name            =   self.Name,               # (superclass)  
            category        =   self.Category,           # MakeFakePayroll Method 
            employee_size   =   self.EmployeeSize,       # is invoked using  
            city            =   self.City,               # the  FakeAthleticClub 
            state           =   self.State,              # (subclass) constructor 
            zip_code        =   self.ZipCode,            # parameters
            departments     =   self.Departments         #
        ).MakeFakePayroll(                               # the has_custom_size  
            has_custom_size =   True,                    # switch indicates  
            custom_size     =   self.MemberSize          # the dict's length will 
        )                                                # match the  MemberSize
        #||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||#

        # 2.c.i.2)   Filter out any  Coulumn Attributes which are not consistant 
        #            with a  Athletic Company Members  Data Context. 
        #||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||#
        del FakeAthleticClubMembers['Salary']            # Club Members would 
        del FakeAthleticClubMembers['Department']        # not likely have a
        del FakeAthleticClubMembers['Hire Date']         # Salary, Department,
        del FakeAthleticClubMembers['Date Of Birth']     # Hire Date, Date Of
        del FakeAthleticClubMembers['Employee ID']       # Birth or Employee ID
        #||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||#

        # 2.c.i.3)   Add additional Columns Attributes to the Member Data Context 
        #            representing  a  Member's  ID,  Membership Date,  and  
        #            Membership Plan.
        #||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||#
        FakeAthleticClubMembers['Member ID']  =  [       # Add a  Member ID  
                                                         # column using  fake's
            fake.iana_id()[:4]                           # data method for      
                                                         # providing random id 
            for _ in range(self.MemberSize)              # numbers, limiting the 
                                                         # number of digits to 4,
        ]                                                # for each of the    
                                                         # 'MemberSize' many rows
                                                         #
        FakeAthleticClubMembers["Membership Date"] = [   # 
                                                         # Add a  Membership Date   
            phony.Datetime().date(                       # column using  phony's     
                2018,                                    # method for random fake    
                2022                                     # dates ranging between           
            ).strftime('%m/%d/%Y')                       # 2018 and the 'current      
                                                         # year', for each of the         
            for _ in range(self.MemberSize)            # 'MemberSize' many rows 
                                                         # 
        ]                                                #
        FakeAthleticClubMembers['Membership Plan'] =  [  # 
                                                         # Add a  Membership Plan   
            phony.Choice()([                             # column using  phony's    
                "Silver",                                # method selecting      
                "Gold",                                  # between random choices            
                "Platinum"                               # of Silver, Gold, and       
            ])                                           # Platinum  Membership,  
                                                         # for each of the  
            for _ in range(self.MemberSize)              # 'MemberSize' many rows
        ]                                                # 
        #||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||#

        # 2.c.i.4)   Export the  Fake Members,  which is now a   dict of lists.     
        #|||||||||||||||||||||#|||||||||||||||||||||||||||||||||||||||||||||||||#
        return FakeAthleticClubMembers  # for use as input in a Pandas DataFrame
        #|||||||||||||||||||||#|||||||||||||||||||||||||||||||||||||||||||||||||#
    #############################################################################
#####################################################################################################
