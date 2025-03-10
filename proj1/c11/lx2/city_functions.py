def get_formatted_city(city,country,population=0):
	formatted_name = city+", "+country+" - population " + str(population)
	return formatted_name.title()