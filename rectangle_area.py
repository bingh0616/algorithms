# problem description: https://leetcode.com/problems/rectangle-area/
class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        area_first = (C-A) * (D-B)
        area_second = (G-E) * (H-F)
        area = area_first + area_second
        if (B>=H or F>=D) or (E>=C or A>=G):
            return area
        else:
            left_x, left_y, right_x, right_y = max(A, E), max(B, F), min(C, G), min(H, D)
            area -= (right_x-left_x) * (right_y-left_y)
        return area
