#!python3
"""
Billy is inviting people to his party.  He is accepting requests
from his friends, but only wants to send 1 invitation out per
person. He decides to store names in a list, and only add the
ones that are not already there.  Can you help a brother out?

Your program should keep asking the user to enter in a name 
(first and last).  If the name is not on the list, add it,
otherwise say "That name is already on the list".

if the user enters in a blank line, then stop the input.
Sort the list of names (it will be sorted by first name)
and print out all of the names on the list.  Also print out
the number of names on the list so he knows how many 
invitations to send.

This program will require you to incorporate everything we
have learned so far.
"""

partylist = ["Matthew Turner","Marcus Cone","Sebastiaan Ter Keurs", "Landon Roberts", "Kieran Stuyt", "Emmett Rossler"]

for i in partylist:
    x = input("enter in a name")
    x = str(x)
   
    if x in partylist:
        print("that name is on the list")
        break
    
    else:
        print("that name is not on the list")
        partylist.append(x)
        break
    

    
    
partylist.sort()  
y = len(partylist)
    

print(f"You are inviting {partylist} to the party meaning you have {y} guests coming to the party")