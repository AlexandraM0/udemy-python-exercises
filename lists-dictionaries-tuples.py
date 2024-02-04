# 1. Create a list of names and print the second item.
names_list = ["Mab", "Asterin", "Maeve", "Elena", "Lyria", "Aelin", "Morrigan"]
print(names_list[1])

# 2. Create a list of sports and then replace the second item with another sport.
sports_list = ["Judo", "Karting", "Baseball", "Archery", "Polo"]
sports_list[1] = "Football"
print(sports_list)

# 3. Create a list containing numbers and delete the fifth number from the array.
numbers_list = [1,5,7,13,2,6,3,10,26,4,9]
print(numbers_list)
del numbers_list[4]
print(numbers_list)

# 4. Create two lists of numbers and merge them.
num1 = [1,3,5,7,9]
num2 = [0,2,4,6,8,10]
print(num1+num2)

# 5. Create a list of numbers and find the length, minimum, and maximum.
numbers_list = [1,5,7,13,2,6,3,10,26,4,9]
print("The length of the list is of",len(numbers_list), "numbers")
print("The min number of the list is: " + str(min(numbers_list)))
print("The max number of the list is: ", max(numbers_list))

# 6. Create a dictionary of students and scores and print out a student’s score.
students = {"Mab":7, "Asterin":10, "Maeve":4, "Elena":7, "Lyria":8, "Aelin":10, "Morrigan":9}
print(students) # to see all students
print(students["Aelin"])

# 7. Create a dictionary with the key being names and values being ages and then delete the second key/value pair.
students1 = {"Mab":17, "Asterin":19, "Maeve":16, "Elena":19, "Lyria":18, "Aelin":17, "Morrigan":18}
print(students1) # before
del students1["Asterin"]
print(students1) # after

# 8. Create a dictionary of names and ages and then print out all the keys and values
data = {"Mab":17, "Asterin":19, "Maeve":16, "Elena":19, "Lyria":18, "Aelin":17, "Morrigan":18}
print("The keys are:", data.keys)
print("The values are:", data.values)

# 9. Create a tuple of your favorite books
books = ("Shadowhunters", "Throne of glass", "ACOTAR", "The fourth wing", "Crescent city", "Harry Potter", "Six of crows")
print(books)

# 10. Create a tuple and print all the items from the first to third index.
books = ("Throne of glass", "ACOTAR", "The fourth wing", "Crescent city", "Harry Potter", "Six of crows")
print(books[0:2])