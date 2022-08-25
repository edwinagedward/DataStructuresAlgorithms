# // Naive
# function hasPairWithSum(arr, sum){
#   var len = arr.length;
#   for(var i =0; i<len-1; i++){
#      for(var j = i+1;j<len; j++){
#         if (arr[i] + arr[j] === sum)
#             return true;
#      }
#   }

#   return false;
# }

# // Better
# function hasPairWithSum2(arr, sum){
#   const mySet = new Set();
#   const len = arr.length;
#   for (let i = 0; i < len; i++){
#     if (mySet.has(arr[i])) {
#       return true;
#     }
#     mySet.add(sum - arr[i]);
#   }
#   return false;
# }

# hasPairWithSum2([6,4,3,2,1,7], 9)

# Naive solution
def hasPairWithSum(arr, sum):
    length = len(arr)
    for i in range(0, length-1):
      for j in range(i+1, length):
        if arr[i] + arr[j] == sum:
          return True
    return False


# Better solution
def hasPairWithSum2(arr, sum):
  length = len(arr)
  diff_set = set()
  for i in range(0, length):
    if arr[i] in diff_set:
      return True
    diff_set.add(sum-arr[i])
  return False

print(hasPairWithSum2([6,4,3,2,1,7], 9))

