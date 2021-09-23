# Make a list that includes at least three people you
# would like to invite to dinner.

# Then use your list to print a message to each person,
# inviting them to dinner.

idol_guest_list = [
    "arnold schwarzenegger",
    "babe ruth",
    "sean connery"
]

invitation = f"Mr. {idol_guest_list[0].title()}, " \
             f"Mr. {idol_guest_list[1].title()}, and " \
             f"Mr. {idol_guest_list[2].title()}, " \
             f"I would like to invite you to dinner because " \
             f"\nyou are idols of mine and I have admired" \
             f"you and looked up to you sense I was a little " \
             f"boy."

print(invitation)

# You just heard that one of your guests can't make the
# dinner, so you need to send out a new set of
# invitations.You will have to think of someone else to
# invite.

# Start with your program from Exercise 3 - 4.
# Add a print() call at the end of your program stating
# the name of the guest who can not make it.

message = f"I am sorry to inform you but " \
          f"{idol_guest_list[1].title()} will not be able to " \
          f"make it for dinner."

print(message)

# Modify your list, replacing the name of the guest who
# can't make it with the name of the new person you
# are inviting.

idol_guest_list[1] = "keanu reeves"

print(idol_guest_list)

# Print a second set of invitation messages,
# one for each person who is still in your list.

invitation1 = f"Mr. {idol_guest_list[0].title()}, I would " \
              f"like to invite you to dinner because " \
              f"\nyou have been an idol of mine and I have " \
              f"admired you and looked up to you sense I " \
              f"was a little boy."
invitation2 = f"Mr. {idol_guest_list[1].title()}, I would " \
              f"like to invite you to dinner because " \
              f"\nyou have been an idol of mine and I have " \
              f"admired you and looked up to you sense I " \
              f"was a little boy."
invitation3 = f"Mr. {idol_guest_list[2].title()}, I would " \
              f"like to invite you to dinner because " \
              f"\nyou have been an idol of mine and I have " \
              f"admired you and looked up to you sense I " \
              f"was a little boy."

print(invitation1)
print(invitation2)
print(invitation3)
