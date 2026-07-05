def myList():
    nums = [10,20,30,40,50]
    Names = ['Navin', 'Awantika', 'Mona']
    Names_Num = ['Awantika', 47, 'Mona']
    mix = [nums, Names]  # nums and Names is one object
    mix2 = [nums + Names]

    print(nums)
    print(nums[-1])
    print(nums[2])
    print(nums[0:2])  # slicing
    print(nums[0:])
    print(Names)
    print(Names_Num)
    print(mix)
    print(len(mix))
    print(type(mix))
    print(mix[0])  # 1st list
    print(mix[1][2])  # 2nd list's 3rd element
    print(len(mix2))
    print(type(mix2))
    nums.append(33) # add element in the end
    nums.insert(1, 55)
    print(nums)
    nums.remove(55)
    print(nums)
    nums.pop() # you can give index value like 0,1,2,3
    print(nums)
    del nums[1:3]  # until 3rd index
    print(nums)
    nums.extend([11,99])
    print(nums)
    nums[0:2] = [22,88]
    print(nums)
    nums.reverse()
    print(nums)
    nums.sort()
    print(nums)

    minimum = min(nums) # python in built functions
    print(minimum)
    maximum = max(nums)
    print(maximum)
    minimumName = min(Names)   # derives based on alphabetical order
    print(minimumName)

myList()

# list are mutable therefore, we can change the values of list