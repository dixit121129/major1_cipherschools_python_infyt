#!/usr/bin/env python
# coding: utf-8

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# 
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 
# You can return the answer in any order.
# 
#  
# 
# Example 1:
# 
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
# 
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
# 
# Input: nums = [3,3], target = 6
# Output: [0,1]
#  
# 
# Constraints:
# 
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

# In[3]:


def twoSum(nums, target):
        lst=[]
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                #print(nums[y],"H")
                if nums[x]+nums[y]==target:
                    #print(x,y,nums[y])
                    lst.extend([x,y])
        lst=list(set(lst))
        return lst

print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))


# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# 
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
# 
# Example
# records = [["chi", 20.0], ["beta", 50], ["alpha", 50]]
# The ordered list of scores is [20.0, 50.0] , so the second lowest score is 50.0 . There are two students with that score: ["beta", "alpha"] . Ordered alphabetically, the names are printed as:
# 
# alpha
# beta
# 
# Input Format
# 
# The first line contains an integer, N , the number of students.
# The 2N subsequent lines describe each student over 2 lines.
# - The first line contains a student's name.
# - The second line contains their grade.
# 
# Constraints
# 
# 1. 2 <= N <= 5
# 2. There will always be one or more students having the second lowest grade.
# 
# Output Format
# 
# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.
# 
# Sample Input 0
# 
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# 
# Sample Output 0
# 
# Berry
# Harry
# 
# Explanation 0
# 
# There are 5 students in this class whose names and grades are assembled to build the following list:
# 
# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# 
# The lowest grade of  37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

# In[2]:


N = int(input())

students = []
for i in range(2*N):
    students.append(input().split())
grades = {}
for j in range(0, len(students), 2):
    grades[students[j][0]] = float(students[j + 1][0])
result = []
num_to_match = sorted(set(grades.values()))[1]
for pupil in grades.keys():
    if grades[pupil] == num_to_match:
        result.append(pupil)
for k in sorted(result):
    print( k)


# In[ ]:




