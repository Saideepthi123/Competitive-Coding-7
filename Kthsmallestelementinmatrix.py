import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # Approach-1 : maintaing max heap of size k and size is above k, pop them out and the first element of the max heap is our kth smallest element in our heap # tc : O(n*2logk), #sc : O(logk) -heap
        
        # Approach-2 since we know that out rows and cols both are sorterd and we need to find x where k-1 elements are less than x then x is our kth smallest element in the matrix) using binary search 
        # we know the first element in the matrix is the smallest element and the last element is the largerst element and the range of elements in our matrix lies between this range, 
        # lets perform binary serch on this range,find the mid value and lets see if there are k elements less than the mid value then we have the right partiotion 
        # but one more trick part the mid value might exist or not exist in our matrix so the kth smallest element is not the mid but the max value which is <mid or = mid in the matrix is our result 
        # tc - O(n2log(max-min)) the binary search will be performed from the small to max so its log (max-min), sc : O(1) better than heap 
        # trade of between heap and binary search space complexity of the binarysearch better than heap, whereas time complexity depening if k is small like 10 and max-mn be smg like 1000 then heap is better 

        # Approach -3 : optimizing the countlessthanmid function tc : O(nlogM), sc : O(1) best approach 
        
        start = matrix[0][0]
        end = matrix[-1][-1]
        
        while start < end : # tc O(logM) M is max-min value 
            mid = start + (end - start) // 2 # 1+15/2 = 8
            
            count, small, large  =  self.countlessthanmid(matrix,mid)
            
            if count == k:
                return small # the max element close to mid where there are k elements smaller than the number 
            elif count <k:
                # end = mid -1, we can do this, will work, but in the testcase 7 does not exist in the matrix we wil be dng extra calls instead we should have our large from the left which is 5( we can get this from the above function )
                # start = mid will work but same as above explanation we dont need to do extactly from the mid instead ww have to do the from the smallest element which is greater than mid which is 9  
                start = large
            else:
                end = small
                   
        return start 
    
    
    # def countlessthanmid(self, matrix, mid): # tc O(n2) iteratign all the elements in the matrix to validate if less or not 
    #     small = matrix[0][0]
    #     large = matrix[-1][-1]
    #     count = 0
        
    #     for i in range(len(matrix)):
    #         for j in range(len(matrix[0])):
    #             if matrix[i][j] <= mid:
    #                 count +=1
    #                 small = max(small, matrix[i][j]) # the largerst number which is smaller or equal to mid
    #             else :
    #                 large = min(large,matrix[i][j]) # the smallest number which is greater than mid
    #     return count, small, large 

    
    def countlessthanmid(self,matrix,mid): # tc : O(n) worst case we will be movign the all the cols or all the rows 
        # since the rows are sorted and also the cols are sorted if at
        # matrix[row][col] < mid i can definitely say all the elements in the above row of this col will be less than mid 
        # if its greater than ne point of traversing from left to rigth of this row because oif matrix[row][col] > mid the matrix[row][col+1] will alsobe > mid no point of traversing instead we should move one row above to find the result

        small = matrix[0][0]
        large = matrix[-1][-1]
        count = 0 
        row = len(matrix) -1  # start from the last row 
        col = 0 

        while row >= 0 and col <= len(matrix)-1:
            if matrix[row][col] <= mid :
                count += row +1 # +1 because matrxis is 0 indexed at row 2 we have totoal 3 elements 
                small = max(small,matrix[row][col])
                col +=1
                
            else :
                large = min(large,matrix[row][col])
                row -= 1 

        return count, small, large



        
        
        
                    
                    
        