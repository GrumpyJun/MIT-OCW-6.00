bestSoFar = 0     # variable that keeps track of largest number
                  # of McNuggets that cannot be bought in exact quantity
packages = (6,9,20)   # variable that contains package sizes

twenty_nuggets = 0
nine_nuggets = 0
six_nuggets = 0
bought = 0

for total_nuggets in range(1, 200):
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
		bestSoFar = total_nuggets

print("Give package sizes " + str(packages[0]) + ", " + str(packages[1]) + ", and " + str(packages[2]) + ", the largest number of McNuggets that cannot be bought in exact quantity is: " + str(bestSoFar) + ".")
