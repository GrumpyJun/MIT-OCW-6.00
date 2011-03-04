total_nuggets = 0
twenty_nuggets = 0
nine_nuggets = 0
six_nuggets = 0
bought = 0
cannot_buy = ()

while len(cannot_buy) < 6 and total_nuggets < 1000:
	total_nuggets += 1
	twenty_nuggets = 0
	bought = 0
	while twenty_nuggets <= total_nuggets:
		nine_nuggets = 0
		while twenty_nuggets + nine_nuggets <= total_nuggets:
			six_nuggets = 0
			while twenty_nuggets + nine_nuggets + six_nuggets <= total_nuggets:
				if twenty_nuggets + nine_nuggets + six_nuggets == total_nuggets:
					bought = 1
				six_nuggets += 6
			nine_nuggets += 9
		twenty_nuggets += 20
	if bought == 0:
		cannot_buy = cannot_buy + (total_nuggets,)
	else:
		cannot_buy = ()

print("The six consecutive values that cannot be bought are:")
print(cannot_buy)
