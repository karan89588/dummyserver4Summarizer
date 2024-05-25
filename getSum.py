from extractiveSum import generateExtractiveSummary


def generateSummary(text):
    res = generateExtractiveSummary(text, "sum")
    return res


if __name__ == "__main__":

    text = """Google LLC (/ˈɡuːɡəl/ ⓘ GOO-ghəl) is an American multinational
	  technology company focusing on artificial intelligence,[9] online advertising,
	    search engine technology, cloud computing, computer software, quantum 
		computing, e-commerce, and consumer electronics. It has been referred
		to as "the most powerful company in the world"[10] and as one of the
		  world's most valuable brands due to its market dominance, data collection,
		    and technological advantages in the field of artificial intelligence.[11][12][13]
			  Google's parent company Alphabet Inc. is one of the five Big Tech companies,
			    alongside Amazon, Apple, Meta, and Microsoft."""
    print(generateSummary(text))
