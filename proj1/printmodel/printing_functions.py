def print_function(unprinteds,completed):
	while unprinteds:
		current = unprinteds.pop()
		print("current: " + current)

		completed.append(current)

	for complete in completed:
		print(complete)