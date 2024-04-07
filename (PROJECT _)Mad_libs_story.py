def mad_libs():
    #Mad Libs Story Template
   story="once upon a time ,there was a {adjective} {noun} who {verb} {adverb}"    
 
 #ask user for word to fill the blank
adjective=input("enter an adjective")
noun=input("enter an noun") 
verb=input("enter an verb") 
adverb=input("enter an adverb")

#fill the blanks with user input
filled_story= story.format(adjective=adjective,noun=noun,verb=verb,adverb=adverb)    

#print the complete story
print("filled_story")

#run the method
mad_libs()