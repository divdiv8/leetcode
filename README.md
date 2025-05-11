mental model for solving problems
def searchRange(self, nums: List[int], target: int) -> List[int]:
        # checklist:
            # starting and ending positions of target
            # target may not exist in the array; return [-1, -1] in that case
            # nums may not have any elements; return [-1, -1] in that case
        
        # example:
            # nums = [1,2,3,5,5,5,8], target = 5
            # ans = [3, 5]
        
        # approach #1
            # do first pass binary search to find the first index. Whenever we find the index, 
            # update a `min_index` variable so that by the end of the binary search we will have
            # found the smallest index with value = target. If `min_index` is not updated, return [-1,-1]

            # do second pass binary search on the search space starting from [first_index+1,n-1]
            # this time use `max_index` variable to find the max_index with value = target
        
        # run through test case nums = [1,2,3,5,5,5,8], target = 5
            # binary search #1
                # lo = 0, hi = 6; mid = (6+0)//2 = 3
                # nums[mid] == 5   
                    # check if mid == 0 OR if mid - 1 != target
                    # if so, update min_index and break out of while loop
                    # otherwise, just update min_index
                
                # binary search #1 completed with `min_index` set to 3
                # res = [3]
            # binary search #2
                # lo = min_index + 1 = 4, hi = 6; mid = (6+4)//2 = 5
                # nums[5] = 5
                    # check if mid == n-1 OR if mid + 1 != target
                    # if so, update max_index and break out of while loop
                    # otherwise, just update max_index
                
                # binary search #2 completed with `max_index` set to 5
                # res = [3, 5]
        
        # run through test case nums = [1,2,2,3,3,5,5,5,5,8], target = 5; ans = [5,8]
        # binary search #1
                # lo = 0, hi = 9; mid = (9+0)//2 = 4
                # nums[4] == 3
                    # if nums[mid] == target
                        # check if mid == 0 OR if mid - 1 != target
                        # if so, update min_index and break out of while loop
                        # otherwise, just update min_index
                    # 3 < 5, so lo = mid+1 = 5, hi = 9; mid = (9+5)//2 = 7
                # nums[7] == 5
                    # if nums[mid] == target
                    # not the first occurrence of target; update min_index to 7; set hi to mid - 1
                # lo = 5, hi = 6; mid = (6+5)//2 = 5
                # nums[5] == 5
                    # if nums[mid] == target
                        # check if mid == 0 OR if mid - 1 != target
                        # mid - 1 != target, so update min_index and break out of while loop
                
                # binary search #1 completed with `min_index` set to 5
                # res = [5]
        # binary search #2 nums = [1,2,2,3,3,5,5,5,5,8]
            # lo = min_index + 1 = 6, hi = 9; mid = (9+6)//2 = 7
                # nums[7] = 7
                    # check if mid == n-1 OR if mid + 1 != target
                    # not true, so just update max_index to 7
                    # set lo to mid + 1
            # lo = 8, hi = 9; mid = (9+8)//2 = 8
                # nums[8] = 5
                    # check if mid == n-1 OR if mid + 1 != target
                    # true, so update max_index to 8 and break out of while loop
                
                # binary search #2 completed with `max_index` set to 8
                # res = [5, 8]

        # check if nums == 0
        n = len(nums)
        if n == 0:
            return [-1, -1]
        # first pass binary search
            # if mid is first index or if mid-1 is not target, we have found the first occurrence
                # update min_index, add to result, break out of while loop
            # otherwise only update min_index
            # if nums[mid] < target then search right
            # else search left
        min_index = float('inf')
        lo, hi = 0, n-1
        res = []
        while lo <= hi:
            mid = (lo+hi)//2

            if nums[mid] == target:
                if mid == 0 or nums[mid-1] != target:
                    min_index = mid
                    res.append(min_index)
                    break
                else:
                    min_index = min(min_index, mid)
            
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        # if min_index was not updated, return [-1,-1]
        if min_index == float('inf'):
            return [-1, -1]

        # second pass binary search
            # if mid is last index or if mid+1 is not target, we have found the last occurrence
                # update max_index, add to result, break out of while loop
            # otherwise only update max_index
            # if nums[mid] < target then search right
            # else search right
        lo, hi = min_index, n - 1
        max_index = float('-inf')
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                if mid == n-1 or nums[mid+1] != target:
                    max_index = mid
                    res.append(max_index)
                    break
                else:
                    max_index = max(max_index, mid)
                    lo = mid + 1
                    continue
            
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return res

        # Took ~23 mins to implement approach
            # Assumed code would work for the edge cases just because I ran through them in the initial stage
                # Should have run through the test case with an actual dry run after implementation
                    # That would have caught the bug with the while loop
                # Likely would have also caught the bug where search was incorrectly moving to the left after
                    # finding non-maximal target in second pass
                # Final bug where `lo` was set to min_index + 1 would've been caught with more thorough
                    # analysis of edge cases


        # mistakes 
        # 1. overlooked `while lo<hi` condition being incorrect
        # 2. overlooked edge case when target only occurs once. 
        # For the second binary search, I had `lo` set to `min_index + 1`
        # assuming that there would be multiple occurrences of target.
        # 3. The other bug was that in the second binary search for max_index,
        # when the most maximum index is not found, I was only updating `max_index`
        # and the search was moving to the left. This is incorrect when we
        # are trying to find the `max_index` -- it must be to the right.
        # We should only move to the left when nums[mid] > target        
