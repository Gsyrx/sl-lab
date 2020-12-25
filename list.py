a = [ "Physics", "Mathematics", "Chemistry", "Biology" ]

print("\nSet of subjects in the list:" , a[1:3])

# indexing from the back side -1,-2,-3,...
print("\nNegative index :- " , a[-3])

# Replaces subject at index 2
a[2] = "English"
print("\nNew values in the list:" , a)

del a[2]
print("\nNew values in the list:",a)

#insert value at particular index
a.insert(1,"Social studies")
print("\nUpdated values in the list:",a)

#reverse values
a.reverse() 
print("\nReversed values in the list:",a)

#sorted values
a.sort() 
print("\nSorted values in the list:",a)
print("\n")

