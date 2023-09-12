# # class MySet:
# def first_repeated_value(list):
#         # for i in range(0, len(list)):
#         #     for j in range(i + 1, len(list)):
#         #         if list[i] == list[j]:
#         #             return list[i]
                
#         # return None
#     #Create a set to keep track of the values we have seen.
#     number_set = set()

#     #Iterate over each element from the list
#     for i in range(0, len(list)):

#         #If we have already seen a value, we have found the duplicate
#         if list[i] in number_set:
#             return list[i]
        
#         #Otherwise,add the value to our set
#         number_set.add(list[i])

#     #Return None if we reach the end and no value has been duplicated
#     return None

# print(first_repeated_value([1,2,3,3,4,4]))

class MySet:

    def __init__(self, enumerable = []):
       self.dictionary = {}
       
       for value in enumerable:
           self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary

    def add(self, value):
        self.dictionary[value] = True #Add a value as a key on the Dictionary
        return self                   #Return the updated set
    
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self
    
    def size(self):
        return len(self.dictionary)
    
    def clear(self):
        self.dictionary.clear()