'''
The chess board is an 8x8 board, with columns lettered from a to h,
and rows numbered from 1 to 8.

The knight is the trickiest chess piece, giving pause to even the 
most experienced players. Unlike other chess pieces, the knight 
moves along 8 fixed vectors:

[
  (1, 2),
  (2, 1),
  (1, -2),
  (2, -1),
  (-1, 2),
  (-2, 1),
  (-1, -2),
  (-2, -1)
]

Given a 2 squares on a chess board (a and b),
return the lowest number of moves a knight takes from a to b.

Example 1:
  Input: (b1, b3)
  Output: 2

Example 2:
  Input: (d4, f6)
  Output: 4

Example 3:
  Input: (a1, h8)
  Output: 6

Constraints:
  number of moves will range from 1 to 6
'''






'''

pseudocode:
translate input to coordinates.
subtract starting and ending coordinates to determine vector of translation.
find combination of vector movements that sum to vector of translation.

'''

dictOfColumns = {
  'a':1,
  'b':2,
  'c':3,
  'd':4,
  'e':5,
  'f':6,
  'g':7,
  'h':8
}
knight_moves = [
  (1, 2),
  (2, 1),
  (1, -2),
  (2, -1),
  (-1, 2),
  (-2, 1),
  (-1, -2),
  (-2, -1)
]


class Solution():
  def translationVector(self, a_and_b: tuple):
    start = a_and_b[0]
    end = a_and_b[1]
    if start[0] in dictOfColumns.keys():
      start = [dictOfColumns[start[0]], int(start[1])]
    else:
      return print('invalid input')
    if end[0] in dictOfColumns.keys():
      end = [dictOfColumns[end[0]], int(end[1])]
    else:
      return print('invalid input')
    translation_vector = [end[0]-start[0], end[1]-start[1]]
    return translation_vector
  def countKnightMoves(self):
    return

solution = Solution()
print(solution.translationVector(('a1', 'd3')))
