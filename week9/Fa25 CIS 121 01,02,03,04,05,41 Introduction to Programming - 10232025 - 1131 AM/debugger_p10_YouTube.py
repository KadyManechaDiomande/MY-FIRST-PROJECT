def like_or_dislike(events):
	state = "nothing"  #change like to nothing
	
	for event in events:  #no range
		if event == state:   #  != should be ==
			state = "nothing"
		else:
			state = event
	
	return state

print(like_or_dislike(["like"]))