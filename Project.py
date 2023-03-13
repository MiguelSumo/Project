
#Dictionary for Logins
Logins={"Miguel_Sumo":"12345678"}



#Creating functions for discount
def member_discount(num1):
	total=num1-(num1*.10)
	return total
#Defining Dictionary for items
item={"shirt":"20","pants":"60","shoes":"120"}
#Getting User Input for item
print("the items are shirt,pants, and shoes")
cart_cost=0
cart_length=0
while cart_length<5:
	item_input=input("What item are you purchasing or type exit?:")
	if item_input=="exit":
		break
	elif item_input=="shirt":
		cart_cost+=int((item[(item_input)]))
		cart_length+=1
	elif item_input=="pants":
		cart_cost+=int((item[(item_input)]))
		cart_length+=1
	elif item_input=="shoes":
		cart_cost+=int((item[(item_input)]))
		cart_length+=1
	else:
		print("Error, please try again or type exit")
#Calling Functions
member_input=input("Are you a member? Yes or No:")
if member_input=="Yes":
	cart_cost=member_discount(cart_cost)

elif member_input=="No":
	cart_cost=valentines_discount(cart_cost)
#Output
print("Your price is going to be","$",float(cart_cost))

