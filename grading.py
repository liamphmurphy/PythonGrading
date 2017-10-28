def main():
	userGrade = Grading.getGrade()
	Grading.checkGrade(userGrade)

class Grading:
	def getGrade():
	
		print ("Please type in your score from 0-100.")
		''' Store user input as an integer '''
		userGrade = int(input())
		''' Would like to get rid of this if possible. Currently necessary to get input to checkGrade function. '''
		return userGrade
		
	def checkGrade(userGrade):
	
		if userGrade == int(100):
			print("Congrats, you got a perfect score! A+!!")
		elif 90 <= userGrade <= 99:
			print("Woohoo! You got an A!")
		elif 80 <= userGrade <= 89:
			print("Nice, you got a B!")
		elif 70 <= userGrade <= 79:
			print("You passed with a C!")
		elif 60 <= userGrade <= 69:
			print("You got a D... you may want to study more!")
		else:
			print("You got quite a low score, tutoring is a fantastic option!")
main()