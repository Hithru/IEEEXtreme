# Problem Number: 733
# Problem Name: Flood Fill
# Difficulty: Easy
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        new_colored = image.copy()
        coordinate = (image[sr][sc],sr,sc,color)

        search_list = [coordinate]

        num_rows = len(image)
        num_colomns = len(image[0])

        added_list = [[False for i in range(num_colomns)] for j in range(num_rows)]

        added_list[sr][sc] = True
        while len(search_list) > 0 :
            print(search_list)
            element = search_list.pop(0)

            start_color = element[0]
            row = element[1]
            coloumn = element[2]

            new_colored[row][coloumn] = color

            if row+1 < num_rows and image[row+1][coloumn] == start_color and not added_list[row+1][coloumn]:
                search_list.append((image[row+1][coloumn],row+1,coloumn,color))
                added_list[row+1][coloumn] = True


            if row-1 >= 0 and image[row-1][coloumn] == start_color and not added_list[row-1][coloumn]:
                search_list.append((image[row-1][coloumn],row-1,coloumn,color))
                added_list[row-1][coloumn] = True

            if coloumn+1 < num_colomns and image[row][coloumn+1] == start_color and not added_list[row][coloumn+1]:
                search_list.append((image[row][coloumn+1],row,coloumn+1,color))
                added_list[row][coloumn+1] = True

            if coloumn-1 >= 0 and image[row][coloumn-1] == start_color and not added_list[row][coloumn-1]:
                search_list.append((image[row][coloumn-1],row,coloumn-1,color))
                added_list[row][coloumn-1] = True
        return new_colored