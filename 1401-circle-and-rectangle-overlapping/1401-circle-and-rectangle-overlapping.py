class Solution:
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        # Closest x-coordinate in the rectangle to the circle center
        x = max(x1, min(xCenter, x2))

        # Closest y-coordinate in the rectangle to the circle center
        y = max(y1, min(yCenter, y2))

        # Squared distance from circle center to closest rectangle point
        dx = x - xCenter
        dy = y - yCenter

        return dx * dx + dy * dy <= radius * radius