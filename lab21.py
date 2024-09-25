wordbank= ["indentation", "spaces"]

tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

wordbank.append(4)

#print(wordbank)

num= int(input("Pick a student number from 0 to 20!"))

#Get user as a string. Convert the string to an integer

#print(type(num))

student= tlgstudents[num]

print(f"{student} always uses {wordbank[2]} {wordbank[1]} to indent.")

#choice= int(input("Pick a student number!"))
#student_name= tlgstudents[choice]

#print(f"{student_name} always uses {tlgstudents.slice[22]} {wordbank.slice[2]} to indent.)


