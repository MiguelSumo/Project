#This function is for adding to items in the cart
def ADD(list1):
	print("the items are shirt for $20.00,pants for $60.00, and shoes for $120.00")
	x=0
	while x==0:
		more_items=input("What items would you like to add? Type EXIT to be done:")
		if more_items=="EXIT":
			break
		elif more_items=="shirt":
			list1.append("shirt")
		elif more_items=="pants":
			list1.append("pants")
		elif more_items=="shoes":
			list1.append("shoes")
		else:
			print("Error, please try again or type exit")
	return(list1)
	
#This function is for removing items in the cart	
def REMOVE(cart_item):
	x=0
	while x==0:
		remove_item=input("What item would you like to remove? Type EXIT to be done:")
		if remove_item=="EXIT":
			break
		elif remove_item=="shirt":
			cart_item.remove("shirt")
		elif remove_item=="pants":
			cart_item.remove("pants")
		elif remove_item=="shoes":
			cart_item.remove("shoes")
		else:
			print("Error, please try again or type exit")
	return(cart_item)
	
#Dictionary for Logins
Logins={"Miguel_Sumo":"12345678"}

#Member Discount function
def member_discount(num1):
	total=num1-(num1*.10)
	return total
	
#Defining Dictionary for items
item={"shirt":"20","pants":"60","shoes":"120"}

#Getting User Input for items
print("the items are shirt for $20.00,pants for $60.00, and shoes for $120.00")
cart_item=[]
store=0
while store==0:
	item_input=input("What item are you purchasing or type exit?:")
	if item_input=="exit":
		break
	elif item_input=="shirt":
		cart_item.append("shirt")
	elif item_input=="pants":
		cart_item.append("pants")
	elif item_input=="shoes":
		cart_item.append("shoes")
	else:
		print("Error, please try again or type exit")
#Calling Member Discount Function
member_input=input("Are you a member? YES or NO:")
	#Sign in for yes
	#Ask to sign up for no
	
#Confirming Cart
cart_cost=0
cart_confirmation=0
while cart_confirmation==0:
	for x in range(len(cart_item)):
		cart_cost+=float(item[cart_item[x]])
	if member_input=="YES":
		cart_cost=member_discount(cart_cost)
	print("These are the items in your cart")
	for x in range(len(cart_item)):
		print(cart_item[x])
	print("For $",float(cart_cost))
	cart_answer=input("Does the cart look correct? YES or NO:")
	if cart_answer=="YES":
		break#Write Receipt#
	elif cart_answer=="NO":
		question_answer=input("Would you like to ADD or REMOVE items?:")
		if question_answer=="ADD":
			ADD(cart_item)
			cart_cost=0
		elif question_answer=="REMOVE":
			REMOVE(cart_item)
			cart_cost=0

