# Write a Person class with an instance variable, , and a constructor that takes an integer, , as a parameter. The constructor must assign  to  after confirming the argument passed as  is not negative; if a negative argument is passed as , the constructor should set  to  and print . In addition, you must write the following instance methods:

# yearPasses() should increases the  instance variable by .
# amIOld() should perform the following conditional actions:
# If initialAge < 0, print Age is not valid, setting age to 0
# If  self.age >= 13and self.age >= 13, print you are a teenager
# Otherwise, print you're old.


class Person:
    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge < 0:
            print 'Age is not valid, setting age to 0.'
            age = 0
        else:
            age = initialAge
        self.age = age

    def amIOld(self):
        # Do some computations in here and print out the correct statement to
        # the console
        if self.age < 13:
            print 'You are young.'
        elif self.age < 18:
            print 'You are a teenager.'
        else:
            print 'You are old.'

    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1
