data=[45,67,89,34,55,77,92,88,37,49,60,73,81,95,100,42,58,66,79,45,86,73,97,89,92,68,100]
print("===DATASET ANALYZER===\n")
print("Dataset: ",data)
print("Total values in dataset: ",len(data))
print("Sum of all values in dataset: ",sum(data))
print("Average of all values in dataset: ",sum(data)/len(data) if len(data) > 0 else 0)
print("Minimum value in dataset: ",min(data))
print("Maximum value in dataset: ",max(data))
print("Sorted dataset: ",sorted(data))
print("Unique values in dataset: ",set(data))
found = input("You want to find any data in dataset? (yes/no): ")
if found.lower() == "yes":
    search=int(input("Enter a value to search in dataset: "))
    if search in data:
        print("Value found in dataset",data.count(search),"times")
    else:
        print("Value not found in dataset")
else:
    print("Thank you for using dataset analyzer")

