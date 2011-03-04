twenty_nuggets = 0
nine_nuggets = 0
six_nuggets = 0

for total_nuggets in range(50, 56):
	twenty_nuggets = 0
	while twenty_nuggets <= total_nuggets:
		nine_nuggets = 0
		while twenty_nuggets + nine_nuggets <= total_nuggets:
			six_nuggets = 0
			while twenty_nuggets + nine_nuggets + six_nuggets <= total_nuggets:
				if twenty_nuggets + nine_nuggets + six_nuggets == total_nuggets:
					print(str(total_nuggets) + " can be optained with:")
					print(str(twenty_nuggets) + " from twenty nuggets.")
					print(str(nine_nuggets) + " from nine nuggets.")
					print(str(six_nuggets) + " from six nuggets.")
					print()
				six_nuggets += 6
			nine_nuggets += 9
		twenty_nuggets += 20
