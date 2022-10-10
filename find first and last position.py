class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        self.nums = nums  #initializing globally
        self.target = target  #initializing globally
        first = self.binarySearch(True) #to perform bs on left side
        last = self.binarySearch(False) #to perform bs on right side
        return [first, last]    #it will give the first and last poistion
        
    def binarySearch(self,leftFlag):    #binary search function
        low = 0 #setting my low pointer to 0
        high = len(self.nums)-1 #setting my high pointer to last index on the list
        index = -1  #setting index to -1

        while low <= high:  #iterating through the loops
            mid = low+(high-low)//2 #to avoid integer overflow we are using this method to find mid

            if self.nums[mid] == self.target:   #if the element in mid is equal to the target then change index to mid
                index = mid

                if leftFlag:    #if left flag is true we are changing high pointer to mid -1 considering that left side of the binary search is done
                    high = mid-1    
                else:           #if left flag is false, we are changing to mid+1
                    low = mid+1 

            elif self.nums[mid] < self.target:  #else if the element in the mid is less than the target change low to mid+1
                low = mid+1
            else:
                high = mid-1    #else the element is greater than the target change high to mid-1
                
                    
                    
        return index    #returning index
        
        
       
   
        