# 1-b 
# 2-b
# 3-c
# 4-a
# 5-c
# 6-a
# 7.1-c
# 7.2-b
# 8-a
# 9-a
# 10-d
# 11-b
# 12-b
# 13- Arrays нь элементүүдийг санах ойн байрлалд хадгалдаг
    #   Холбогдсон жагсаалтууд нь хадгалах бүтэц багатай бөгөөд элементүүд нь ихэвчлэн зэрэгцэн байрладаггүй учраас дараагийн элементийг заасан 
# 14- Стек нь жагсаалтын зөвхөн нэг талаас элементүүдийг оруулах, устгах боломжтой шугаман өгөгдлийн бүтэц юм.
    #   Стек нь жагсаалтын зөвхөн нэг талд нь элементүүдийг оруулах, устгах боломжтой шугаман өгөгдлийн бүтэц бөгөөд нэг буюу хэд хэдэн зангилааны хязгаарлагдмал багц
# 15-c
# 16-a
# 17-b
# 18-c
# 1. Greedy algorithm Minimum Coin
#   1-c
# 2. haffman 

# 3. bubble sort and insertion sort
# def bubble_sort(arr):
#     n = len(arr)

#     for i in range(n - 1):

#         swapped = False

#         for j in range(n - 1 - i):

#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True

#         if not swapped:
#             break
#     return arr


# arr = [64, 34, 25, 12, 22, 11, 90]
# sorted_arr = bubble_sort(arr)
# print("Sorted array:", sorted_arr)

# def insertion_sort(arr):

#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1


#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr


# arr = [12, 11, 13, 5, 6]
# sorted_arr = insertion_sort(arr)
# print("Sorted array:", sorted_arr)


# Bubble Sort benefits from the early exit condition but still remains slower for larger arrays.
# Insertion Sort with binary search makes fewer comparisons, making it faster, especially for larger datasets with some order or repetition.

# 4. algorithm 1-c
# 5. binary tree Search

# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# class BinarySearchTree:
#     def __init__(self):
#         self.root = None

#     def insert(self, value):
#         if not self.root:
#             self.root = TreeNode(value)
#         else:
#             self._insert_recursive(self.root, value)

#     def _insert_recursive(self, node, value):
#         if value < node.value:
#             if node.left is None:
#                 node.left = TreeNode(value)
#             else:
#                 self._insert_recursive(node.left, value) 
#         else:
#             if node.right is None:
#                 node.right = TreeNode(value) 
#             else:
#                 self._insert_recursive(node.right, value)  

#     def inorder_traversal(self, node):
#         if node is not None:
#             self.inorder_traversal(node.left)
#             print(node.value, end=' ')
#             self.inorder_traversal(node.right)

# bst = BinarySearchTree()
# values_to_insert = [7, 3, 9, 1, 5, 8, 10, 11, 0]

# for value in values_to_insert:
#     bst.insert(value)


# print("In-order traversal of the BST:")
# bst.inorder_traversal(bst.root)  

# 6. function 1-b