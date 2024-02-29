I would prefer the one using sets as it is an order n solution having only one for lool while the one using lists is order n squared.

It is also possible to use a dictionary as follows:

```
def two_sum_dict(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []
```
