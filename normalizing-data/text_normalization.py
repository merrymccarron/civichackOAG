import re

def text_normalization(s):
	return re.sub(r'[\W_]+','',s.lower().strip())
	
if __name__ == "__main__":
	text_normalization(s)