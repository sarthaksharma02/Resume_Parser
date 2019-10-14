from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from io import StringIO
from docx import Document
import re
import nltk 
import spacy

# This function will extract text from the pdf file
def extract_pdf(pdf_path):                     
	with open(pdf_path, 'rb') as fh:
		# iterate over all pages of PDF document
		for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
			# creating a resoure manager
			resource_manager = PDFResourceManager()
			
			# create a file handle
			fake_file_handle = StringIO()
			
			# creating a text converter object
			converter = TextConverter(
								resource_manager, 
								fake_file_handle, 
								codec='utf-8', 
								laparams=LAParams()
						)

			# creating a page interpreter
			page_interpreter = PDFPageInterpreter(
								resource_manager, 
								converter
							)

			# process_pagess current page
			page_interpreter.process_page(page)
			
			# extract text
			text = fake_file_handle.getvalue()
			yield text

			# close open handles
			converter.close()
			fake_file_handle.close()

text = ''
for page in extract_pdf('/home/stk/Downloads/Resumes/DevanshuJain.pdf'): 
	text +=  page

#print(text)

# This Function will extract text from the doc file
def extract_docx(pdf_path):
	document = Document(pdf_path)
	return "\n".join([para.text for para in document.paragraphs])
'''
text = extract_docx('/home/stk/Downloads/Resumes/Vishal.docx')
text = str(text)
'''

def city_finder(text_data):
	sentences = [nltk.sent_tokenize(text_data)]
	words = [nltk.word_tokenize(w) for w in sentences]
	tags = [nltk.pos_tag(p) for p in words]
	
	return tags

'''print("City: ",city_finder(text))''' 	


def extract_email(file_path):
	pattern = re.compile(r'\S*@\S*')
	matches = pattern.findall(text) # Gets all email addresses as a list
	email = matches
	return email

infoDict = {} 

def extract_phone(text):
	phone = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', text) 
	if phone:
		number = ''.join(phone[0]) 
		if len(number) > 10:
			return '' + number
		else:
			return number 


information=[]
inputString = ''
tokens = []
lines = []
sentences = []
'''def read_file(filename):
	extension = filename.split(".")[-1] #Here we split the given filename by detecting the '.' notation and take the last element of the list for comparing further
	# firstly checking the 'txt' extension    	
	if extension == "txt":
		f = open(fileName, 'r')
		string = f.read()
		f.close() 
		return string, extension
	# Now we check the 'pdf' extension
	elif extension == "pdf":	
		return extract_pdf(pdf_path)
	#Finally we check the 'docx' extension
	elif extension == "docx":
	try:
		return extract_docx(docx_path)
	except:
		return ''
	else:
	print('Unsupported Format')
'''

def preprocess_text(text_file):
			'''Information Extraction: Preprocess a document with the necessary POS tagging.
			Returns three lists, one with tokens, one with POS tagged lines, one with POS tagged sentences.
			Modules required: nltk'''

		# Try to get rid of special characters
			document = text.encode('ascii', 'ignore') 
			# Newlines are one element of structure in the data
			# Helps limit the context and breaks up the data as is intended in resumes - i.e., into points
			global lines, sentences, tokens
			lines = [el.strip() for el in text.split("\n") if len(el) > 0]  # Splitting on the basis of newlines 
			lines = [nltk.word_tokenize(el) for el in lines]    # Tokenize the individual lines
			lines = [nltk.pos_tag(el) for el in lines]  # Tag them
			# Below approach is slightly different because it splits sentences not just on the basis of newlines, but also full stops 
			# - (barring abbreviations etc.)
			# But it fails miserably at predicting names, so currently using it only for tokenization of the whole document
			sentences = nltk.sent_tokenize(text)    # Split/Tokenize into sentences (List of strings)
			sentences = [nltk.word_tokenize(sent) for sent in sentences]    # Split/Tokenize sentences into words (List of lists of strings)
			tokens = sentences
			sentences = [nltk.pos_tag(sent) for sent in sentences]    # Tag the tokens - list of lists of tuples - each tuple is (<word>, <tag>)
			 
			# Next 4 lines convert tokens from a list of list of strings to a list of strings; basically stitches them together
			dummy = []
			for el in tokens:
				dummy += el
			tokens = dummy

			# tokens - words extracted from the doc, lines - split only based on newlines (may have more than one sentence)
			# sentences - split on the basis of rules of grammar
			return sentences 

def preprocess_textl(text_file):
			'''Information Extraction: Preprocess a document with the necessary POS tagging.
			Returns three lists, one with tokens, one with POS tagged lines, one with POS tagged sentences.
			Modules required: nltk'''

		# Try to get rid of special characters
			document = text.encode('ascii', 'ignore') 
			# Newlines are one element of structure in the data
			# Helps limit the context and breaks up the data as is intended in resumes - i.e., into points
			global lines, sentences, tokens
			lines = [el.strip() for el in text.split("\n") if len(el) > 0]  # Splitting on the basis of newlines 
			lines = [nltk.word_tokenize(el) for el in lines]    # Tokenize the individual lines
			lines = [nltk.pos_tag(el) for el in lines]  # Tag them
			# Below approach is slightly different because it splits sentences not just on the basis of newlines, but also full stops 
			# - (barring abbreviations etc.)
			# But it fails miserably at predicting names, so currently using it only for tokenization of the whole document
			sentences = nltk.sent_tokenize(text)    # Split/Tokenize into sentences (List of strings)
			sentences = [nltk.word_tokenize(sent) for sent in sentences]    # Split/Tokenize sentences into words (List of lists of strings)
			tokens = sentences
			sentences = [nltk.pos_tag(sent) for sent in sentences]    # Tag the tokens - list of lists of tuples - each tuple is (<word>, <tag>)
			 
			# Next 4 lines convert tokens from a list of list of strings to a list of strings; basically stitches them together
			dummy = []
			for el in tokens:
				dummy += el
			tokens = dummy

			# tokens - words extracted from the doc, lines - split only based on newlines (may have more than one sentence)
			# sentences - split on the basis of rules of grammar
			return lines 

def preprocess_textt(text_file):
			'''Information Extraction: Preprocess a document with the necessary POS tagging.
			Returns three lists, one with tokens, one with POS tagged lines, one with POS tagged sentences.
			Modules required: nltk'''

		# Try to get rid of special characters
			document = text.encode('ascii', 'ignore') 
			# Newlines are one element of structure in the data
			# Helps limit the context and breaks up the data as is intended in resumes - i.e., into points
			global lines, sentences, tokens
			lines = [el.strip() for el in text.split("\n") if len(el) > 0]  # Splitting on the basis of newlines 
			lines = [nltk.word_tokenize(el) for el in lines]    # Tokenize the individual lines
			lines = [nltk.pos_tag(el) for el in lines]  # Tag them
			# Below approach is slightly different because it splits sentences not just on the basis of newlines, but also full stops 
			# - (barring abbreviations etc.)
			# But it fails miserably at predicting names, so currently using it only for tokenization of the whole document
			sentences = nltk.sent_tokenize(text)    # Split/Tokenize into sentences (List of strings)
			sentences = [nltk.word_tokenize(sent) for sent in sentences]    # Split/Tokenize sentences into words (List of lists of strings)
			tokens = sentences
			sentences = [nltk.pos_tag(sent) for sent in sentences]    # Tag the tokens - list of lists of tuples - each tuple is (<word>, <tag>)
			 
			# Next 4 lines convert tokens from a list of list of strings to a list of strings; basically stitches them together
			dummy = []
			for el in tokens:
				dummy += el
			tokens = dummy

			# tokens - words extracted from the doc, lines - split only based on newlines (may have more than one sentence)
			# sentences - split on the basis of rules of grammar
			return tokens 


def getName():
		
			'''Given an input string, returns possible matches for names. Uses regular expression based matching.
			Needs an input string, a dictionary where values are being stored, and an optional parameter for debugging.
			Modules required: clock from time, code.'''

		# Reads Indian Names from the file, reduce all to lower case for easy comparision [Name lists]
			indianNames = open("/home/stk/Documents/nlp_projects/Names.txt", "r").read().lower()
		# Lookup in a set is much faster
			indianNames = set(indianNames.split())    
			
			sentences = preprocess_text(text)
			lines = preprocess_textl(text)
			tokens = preprocess_text(text) 

			otherNameHits = []
			nameHits = []
			name = None

			try:
			# tokens, lines, sentences = self.preprocess(inputString)
				#tokens, lines, sentences = tokens, lines, sentences
			# Try a regex chunk parser
			# grammar = r'NAME: {<NN.*><NN.*>|<NN.*><NN.*><NN.*>}'
				grammar = r'NAME: {<NN.*><NN.*><NN.*>*}'
			# Noun phrase chunk is made out of two or three tags of type NN. (ie NN, NNP etc.) - typical of a name. {2,3} won't work, hence the syntax
			# Note the correction to the rule. Change has been made later.
				chunkParser = nltk.RegexpParser(grammar) 
				all_chunked_tokens = []
				for tagged_tokens in lines:
				# Creates a parse tree
					if len(tagged_tokens) == 0: continue # Prevent it from printing warnings
					chunked_tokens = chunkParser.parse(tagged_tokens)
					all_chunked_tokens.append(chunked_tokens)
					for subtree in chunked_tokens.subtrees():
					#  or subtree.label() == 'S' include in if condition if required
						if subtree.label() == 'NAME':
							for ind, leaf in enumerate(subtree.leaves()):
								if leaf[0].lower() in indianNames and 'NN' in leaf[1]:
								# Case insensitive matching, as indianNames have names in lowercase
								# Take only noun-tagged tokens
								# Surname is not in the name list, hence if match is achieved add all noun-type tokens
								# Pick upto 3 noun entities
									hit = " ".join([el[0] for el in subtree.leaves()[ind:ind+3]])
								# Check for the presence of commas, colons, digits - usually markers of non-named entities 
									if re.compile(r'[\d,:]').search(hit): continue
									nameHits.append(hit)
								# Need to iterate through rest of the leaves because of possible mis-matches
			# Going for the first name hit
				if len(nameHits) > 0:
					nameHits = [re.sub(r'[^a-zA-Z \-]', '', el).strip() for el in nameHits] 
					name = " ".join([el[0].upper()+el[1:].lower() for el in nameHits[0].split() if len(el)>0])
					otherNameHits = nameHits[1:]

			except Exception as e:
				#print(traceback.format_exc())
				print('Error')         

			infoDict['name'] = name
			infoDict['otherNameHits'] = otherNameHits

			if __debug__:
				#print("\n", pprint(infoDict), "\n")
				#code.interact(local=locals())
				return name
    		    	

#print(preprocess_text(text))

print('\nName : ')
print(getName()) 

print('\nEmail Address :')
print(extract_email(text))

print('\nPhone Number : \n', extract_phone(text)) 

'''

def getExperience(text_file):
    experience=[]
    sentence = nltk.sent_tokenize(text_file)
    word = [nltk.word_tokenize(t) for t in sentence]
    pos_tag = [nltk.pos_tag(i) for i in word] 
    chunked_token = [nltk.ne_chunk(p) for p in pos_tag]
    return word

print(getExperience(text))'''