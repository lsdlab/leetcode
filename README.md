# leetcode

![Language](https://img.shields.io/badge/language-Python-blue.svg) ![License](https://img.shields.io/badge/license-MIT-blue.svg)

My LeetCode practices

## 2016/8/15
1. No.349 Intersection of two arrays 1
    * Tags: Binary Search/Hash Table/Two Pointers/Sort
    * 题意：两个数组计算交集 nums1 [1, 2, 2, 1] ^ nums2 [2, 2] => [2]。
    * 要求：结果不能重复、无需顺序。
    * 思路：set()，集合，无需。先给 nums1 去重，再遍历 nums2，`for i in nums1_set` 获得结果。

2. No.350 Intersection of two arrays 2
    * Tags: Binary Search/Hash Table/Two Pointers/Sort
    * 题意：两个数组计算交集，交集一次及以上，交集结果要体现次数，一个元素交集两次; 交集结果中要出现这个元素两次 [1, 2, 2, 1] ^ [2, 2] => [2, 2]。
    * 要求：结果要体现次数、无需顺序。
    * 思路：先计算长度小的数组每个元素出现次数，nums1 短，nums2 长。遍历长的数组，2 中的元素在 1 中，个数 > 0，加入结果，计数 -1。
    * 优化：1. 数组已经排好顺序，如何优化？2. 如果 nums1 长度小于 nums2，如何优化？3. nums2 存在磁盘上，如法全部加载到内存中，如何优化？
    * 2、3 点已经优化。

## LICENSE
MIT


