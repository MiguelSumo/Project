#Miguel Sumo 3/27/23
#Fully Functional Code
#Only problem is remove code deletes too much

#This function is for adding to items in the cart
def ADD(list1,item,item_print):
	x=0
	while x==0:
		more_items=input("What item would you like to add? Type EXIT to be done:")
		if more_items=="EXIT":
			break
		#Shirt
		elif more_items=="shirt":
			list1.append("shirt")
			item_print.s_colors()
			shirt_color=input("What color would you like?:")
			item_print.s_sizes()
			shirt_size=input("What size would you like?:")
			if shirt_size=="S":
				item["shirt"]["quantity"]=item["shirt"]["quantity"]-1
			elif shirt_size=="M":
				item["shirt"]["quantity"]=item["shirt"]["quantity"]-1
			elif shirt_size=="L":
				item["shirt"]["quantity"]=item["shirt"]["quantity"]-1
			else:
				print("error")
			if more_items!="EXIT":
				receipt[len(list1)]={"item":more_items,"color":shirt_color,"size":shirt_size} #Code for adding to receipt dictionanry
		#Jeans
		elif more_items=="jeans":
			list1.append("jeans")
			item_print.j_colors()
			jeans_color=input("What color would you like?:")
			item_print.j_sizes()
			jeans_size=input("What size would you like?:")
			if jeans_size=="28":
				item["jeans"]["quantity"]=item["jeans"]["quantity"]-1
			elif jeans_size=="30":
				item["jeans"]["quantity"]=item["jeans"]["quantity"]-1
			elif jeans_size=="32":
				item["jeans"]["quantity"]=item["jeans"]["quantity"]-1
			elif jeans_size=="34":
				item["jeans"]["quantity"]=item["jeans"]["quantity"]-1
			else:
				print("error")
			if more_items!="EXIT":
				receipt[len(list1)]={"item":more_items,"color":jeans_color,"size":jeans_size} #Code for adding to receipt dictionanry
		#Shoes		
		elif more_items=="shoes":
			list1.append("shoes")
			item_print.o_colors()
			shoes_color=input("What color would you like?:")
			item_print.o_sizes()
			shoes_size=input("What size would you like?:")
			if shoes_size=="8":
				item["shoes"]["quantity"]=item["shoes"]["quantity"]-1
			elif shoes_size=="9":
				item["shoes"]["quantity"]=item["shoes"]["quantity"]-1
			elif shoes_size=="9.5":
				item["shoes"]["quantity"]=item["shoes"]["quantity"]-1
			elif shoes_size=="10":
				item["shoes"]["quantity"]=item["shoes"]["quantity"]-1
			elif shoes_size=="11":
				item["shoes"]["quantity"]=item["shoes"]["quantity"]-1
			elif shoes_size=="12":
				item["shoes"]["quantity"]=item["shoes"]["quantity"]-1
			else:
				print("error")
			if more_items!="EXIT":
				receipt[len(list1)]={"item":more_items,"color":shoes_color,"size":shoes_size} #Code for adding to receipt dictionanry
		#Hoodie
		elif more_items=="hoodie":
			list1.append("hoodie")
			item_print.h_colors()
			hoodie_color=input("What color would you like?:")
			item_print.h_sizes()
			hoodie_size=input("What size would you like?:")
			if hoodie_size=="S":
				item["hoodie"]["quantity"]=item["hoodie"]["quantity"]-1
			elif hoodie_size=="M":
				item["hoodie"]["quantity"]=item["hoodie"]["quantity"]-1
			elif hoodie_size=="L":
				item["hoodie"]["quantity"]=item["hoodie"]["quantity"]-1
			elif hoodie_size=="XL":
				item["hoodie"]["quantity"]=item["hoodie"]["quantity"]-1
			else:
				print("error")
			if more_items!="EXIT":
				receipt[len(list1)]={"item":more_items,"color":hoodie_color,"size":hoodie_size} #Code for adding to receipt dictionanry
		#Shorts
		elif more_items=="shorts":
			list1.append("shorts")
			item_print.r_colors()
			shorts_color=input("What color would you like?:")
			item_print.r_sizes()
			shorts_size=input("What size would you like?:")
			if shorts_size=="S":
				item["shorts"]["quantity"]=item["shorts"]["quantity"]-1
			elif shorts_size=="M":
				item["shorts"]["quantity"]=item["shorts"]["quantity"]-1
			elif shorts_size=="9.5":
				item["shorts"]["quantity"]=item["shorts"]["quantity"]-1
			elif shorts_size=="L":
				item["shorts"]["quantity"]=item["shorts"]["quantity"]-1
			elif shorts_size=="XL":
				item["shorts"]["quantity"]=item["shorts"]["quantity"]-1
			elif shorts_size=="XXL":
				item["shorts"]["quantity"]=item["shorts"]["quantity"]-1
			else:
				print("error")
			if more_items!="EXIT":
				receipt[len(list1)]={"item":more_items,"color":shorts_color,"size":shorts_size} #Code for adding to receipt dictionanry
		else:
			print("Error, please try again or type exit")
	return(list1)
#Code to reset the cart cost in loop #Very important or will get false cart cost
def reset_cart(num1):
	num1=0
	return num1
#This function is for removing items in the cart and receipt dictionary
def REMOVE(list1,item):
	x=0
	while x==0:
		remove_item=input("What # item would you like to remove? Type EXIT to be done:")
		if remove_item=="EXIT":
			break
	
		if receipt[int(remove_item)]["item"]=="shirt":
			list1.remove("shirt")
			item["shirt"]["quantity"]=item["shirt"]["quantity"]+1
		if receipt[int(remove_item)]["item"]=="hoodie":
			list1.remove("hoodie")
			item["hoodie"]["quantity"]=item["hoodie"]["quantity"]+1		
		if receipt[int(remove_item)]["item"]=="jeans":
			list1.remove("jeans")
			item["jeans"]["quantity"]=item["jeans"]["quantity"]+1				
		if receipt[int(remove_item)]["item"]=="shorts":
			list1.remove("hoodie")
			item["shorts"]["quantity"]=item["shorts"]["quantity"]+1
		if receipt[int(remove_item)]["item"]=="shoes":
			list1.remove("shoes")
			item["shoes"]["quantity"]=item["shoes"]["quantity"]+1						
		receipt[int(remove_item)]="removed item"

	return(cart_item)
#Dictionary for Logins
passwords = {
    "Miguel222": "password1",
    "Aboubacar345":"password2",
    "Lado111": "password3",
    "Arbab222": "password4",
}

#Member Discount function
def member_discount(num1):
	total=num1-(num1*.10)
	return total

codes=("rollMAVS","5%OFF", "A+Project") 
#Defining Dictionary for items

item = {
    "shirt": {"price": 20.99, "size": ["S", "M", "L"], "color": ["red", "blue", "green"], "quantity": 100},
    "hoodie":{"price": 39.99, "size": ["S", "M", "L", "XL"], "color": ["black", "gray", "navy"], "quantity": 50},
    "jeans": {"price": 49.99, "size": ["28", "30", "32", "34"], "color": ["blue", "black"], "quantity": 75},
    "shoes": {"price": 89.99, "size": ["8", "9", "9.5", "10", "11", "12"], "color": ["blue", "black"], "quantity": 49},
    "shorts":{ "price": 19.99, "size": ["S", "M", "L", "XL", "XXL"], "color": ["blue", "black", "red", "yellow"], "quantity": 120},
}
#Dictionary to make receipts
receipt={}
#Multi-level Class to display the costs 
class shirts:
	def s_display(self):
		print("Shirt:$20.99")
	def s_sizes(self):
		print("Sizes are S, M, and L")
	def s_colors(self):
		print("Colors are red, blue, and green")
class hoodie(shirts):
	def h_display(self):
		print("Hoodie:$39.99")
	def h_sizes(self):
		print("Sizes are S, M, L, and XL")
	def h_colors(self):
		print("Colors are black, gray, and navy")
class jeans(hoodie):
	def j_display(self):
		print("Jeans:$49.99")
	def j_sizes(self):
		print("Sizes are 28', 30', 32', and 34'")
	def j_colors(self):
		print("Colors are blue and black")
class shoes(jeans):
	def o_display(self):
		print("Shoes:$89.99")
	def o_sizes(self):
		print("Sizes are 8', 9', 9.5', 10', 11', and 12'")
	def o_colors(self):
		print("Colors are blue and black")	
class shorts(shoes):
	def r_display(self):
		print("Shorts:$19.99")
	def r_sizes(self):
		print("Sizes are S, M, L, XL, and XXL")
	def r_colors(self):
		print("Colors are blue, red, yellow, and black")			
item_print=shorts()		
#function to display all the items
def all_items(object1):		
	object1.s_display()
	object1.h_display()
	object1.j_display()
	object1.o_display()
	object1.r_display()
all_items(item_print)


#Getting User Input for items
cart_item=[]
store=0
while store==0:
	for x in range(1,1000):
		item_input=input("What item are you purchasing or type exit?:")
		if item_input=="exit":
			break
		#SHIRT
		elif item_input=="shirt":
			cart_item.append("shirt")
			item_print.s_colors()
			shirt_color=input("What color would you like?:")
			item_print.s_sizes()
			shirt_size=input("What size would you like?:")
			if shirt_size=="S":
				item["shirt"]["quantity"]=item["shirt"]["quantity"]-1
			elif shirt_size=="M":
				item["shirt"]["quantity"]=item["shirt"]["quantity"]-1
			elif shirt_size=="L":
				item["shirt"]["quantity"]=item["shirt"]["quantity"]-1
			else:
				print("error")
			receipt[x]={"item":item_input,"color":shirt_color,"size":shirt_size}
		#HOODIE
		elif item_input=="hoodie":
			cart_item.append("hoodie")
			item_print.h_colors()
			hoodie_color=input("What color would you like?:")
			item_print.h_sizes()
			hoodie_size=input("What size would you like?:")
			if hoodie_size=="S":
				item["hoodie"]["quantity"]=item["hoodie"]["quantity"]-1
			elif hoodie_size=="M":
				item["hoodie"]["quantity"]=item["hoodie"]["quantity"]-1
			elif hoodie_size=="L":
				item["hoodie"]["quantity"]=item["hoodie"]["quantity"]-1
			elif hoodie_size=="XL":
				item["hoodie"]["quantity"]=item["hoodie"]["quantity"]-1
			else:
				print("error")
			receipt[x]={"item":item_input,"color":hoodie_color,"size":hoodie_size}
		#JEANS
		elif item_input=="jeans":
			cart_item.append("jeans")
			item_print.j_colors()
			jeans_color=input("What color would you like?:")
			item_print.j_sizes()
			jeans_size=input("What size would you like?:")
			if jeans_size=="28":
				item["jeans"]["quantity"]=item["jeans"]["quantity"]-1
			elif jeans_size=="30":
				item["jeans"]["quantity"]=item["jeans"]["quantity"]-1
			elif jeans_size=="32":
				item["jeans"]["quantity"]=item["jeans"]["quantity"]-1
			elif jeans_size=="34":
				item["jeans"]["quantity"]=item["jeans"]["quantity"]-1
			else:
				print("error")
			receipt[x]={"item":item_input,"color":jeans_color,"size":jeans_size}
		#SHOES
		elif item_input=="shoes":
			cart_item.append("shoes")
			item_print.o_colors()
			shoes_color=input("What color would you like?:")
			item_print.o_sizes()
			shoes_size=input("What size would you like?:")
			if shoes_size=="8":
				item["shoes"]["quantity"]=item["shoes"]["quantity"]-1
			elif shoes_size=="9":
				item["shoes"]["quantity"]=item["shoes"]["quantity"]-1
			elif shoes_size=="9.5":
				item["shoes"]["quantity"]=item["shoes"]["quantity"]-1
			elif shoes_size=="10":
				item["shoes"]["quantity"]=item["shoes"]["quantity"]-1
			elif shoes_size=="11":
				item["shoes"]["quantity"]=item["shoes"]["quantity"]-1
			elif shoes_size=="12":
				item["shoes"]["quantity"]=item["shoes"]["quantity"]-1
			else:
				print("error")
			receipt[x]={"item":item_input,"color":shoes_color,"size":shoes_size}
	#SHORTS	
		elif item_input=="shorts":
			cart_item.append("shorts")
			item_print.r_colors()
			shorts_color=input("What color would you like?:")
			item_print.r_sizes()
			shorts_size=input("What size would you like?:")
			if shorts_size=="S":
				item["shorts"]["quantity"]=item["shorts"]["quantity"]-1
			elif shorts_size=="M":
				item["shorts"]["quantity"]=item["shorts"]["quantity"]-1
			elif shorts_size=="9.5":
				item["shorts"]["quantity"]=item["shorts"]["quantity"]-1
			elif shorts_size=="L":
				item["shorts"]["quantity"]=item["shorts"]["quantity"]-1
			elif shorts_size=="XL":
				item["shorts"]["quantity"]=item["shorts"]["quantity"]-1
			elif shorts_size=="XXL":
				item["shorts"]["quantity"]=item["shorts"]["quantity"]-1
			else:
				print("error")
			receipt[x]={"item":item_input,"color":shorts_color,"size":shorts_size}		
		else:
			print("Error, please try again or type exit")
	if item_input=="exit":
		break
#Calling Member Discount Function
#Login in point

member_input=input("Are you a member? YES or NO:")
if member_input=="YES":
	member_login=0
	while member_login==0:
		ask_username=input("What is your username?:")
		ask_password=input("What is your password?:")
		if ask_username in passwords:
			if ask_password== passwords[ask_username]:
				member_input=="YES"
				print("Login Successful")
				break
			else:
				print("Error Password Incorrect")
				member_quit=input("Would you like to try again? Y or N:")
				if member_quit=="N":
					break
				else:
					continue
		else:
			print("Error Username not found")
			member_quit=input("Would you like to try again? Y or N:")
			if member_quit=="N":
				break
			else:
				continue	
elif member_input=="NO":
	non_member=input("Would you like to become a member for 10% off this purchase? YES or NO:")
	if non_member=="NO":
		member_input="NO"
	if non_member=="YES":
		q=0
		while q==0:
			ask_username=input("What would you like your username to be?:")
			if ask_username in passwords:
				print("Username already taken. Try again")
			elif ask_username not in passwords:
				ask_password=input("What would you lik your password to be?:")
				passwords.update({ask_username:ask_password})
				print("Account Created Successfully")
				member_input="YES"
				break

			
#Confirming Cart
cart_cost=0
cart_confirmation=0
while cart_confirmation==0:
	for x in range(len(cart_item)):
		cart_cost+=float(item[str(cart_item[x])]["price"])
	if member_input=="YES":
		cart_cost=member_discount(cart_cost)
	print("These are the items in your cart")
	for x in range(1,len(cart_item)+1):
		if receipt[x]!="removed item":
			print(str(x)+".",receipt[x]["color"],receipt[x]["size"],receipt[x]["item"])
		if receipt[x]=="removed item":
			print(str(x)+". removed item")
			continue
	print("For $",round(float(cart_cost),2))
	cart_answer=input("Does the cart look correct? YES or NO:")
	if cart_answer=="YES":
		ask_code=input("Do you have a discount code? Y or N:")
		if ask_code=="Y":
			p=0
			while p==0:
				discount_code=input("Discount Code:")
				if discount_code in codes:
					cart_cost= cart_cost-(cart_cost*.05)
					print("Discount Added Successfully")
					break
				elif discount_code not in codes:
					ask_again=input("Error code not found, Would you like to try again? Y or N:")
					if ask_again=="Y":
						continue
					if ask_again=="N":
						break		
		elif ask_code=="N":
			break
		else:
			print("Try again")

		f=open("receipt_store.txt","w")
		f.write("This is your receipt from the Clothes Outlet")
		f.write("\n")
		
		for m in range(1,len(cart_item)+1):
			if receipt[m]!="removed item":
				f.write(str(m))
				f.write(". ")
				f.write(str(receipt[m]))
				f.write("\n")
			if receipt[m]=="removed item":
				f.write(str(m))
				f.write(". ")
				f.write("removed item")
				f.write("\n")
				continue
		f.write("Order Costs:$")
		cart_cost=(round(float(cart_cost),2))
		f.write(str(cart_cost))
		print("Receipt Created Successfully")
		break
	elif cart_answer=="NO":
		all_items(item_print)
		question_answer=input("Would you like to ADD or REMOVE items?:")
		if question_answer=="ADD":
			ADD(cart_item,item,item_print)
			cart_cost=reset_cart(cart_cost)
		elif question_answer=="REMOVE":
			REMOVE(cart_item,item)
			cart_cost=reset_cart(cart_cost)
		else:
			print("Error, Try again")
			cart_cost=reset_cart(cart_cost)		
	else:
		print("Error, Try again")
		cart_cost=reset_cart(cart_cost)
