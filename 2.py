def circle():
    number_of_T = int(input())  # Number of test cases
    for _ in range(number_of_T):
        valid_N = int(input())  # Number of points
        N_min_x = float('inf')  # Initialize N_min_x to a large number
        N_mx_x = float('-inf')  # Initialize N_mx_x to a small number
        N_min_y = float('inf')  # Initialize N_min_y to a large number
        N_mx_y = float('-inf')  # Initialize N_mx_y to a small number
        
        # Read the x and y coordinates
        for _ in range(valid_N):
            x, y = map(float, input().split())
            # Update min and max values as we read the coordinates
            N_min_x = min(N_min_x, x)
            N_mx_x = max(N_mx_x, x)
            N_min_y = min(N_min_y, y)
            N_mx_y = max(N_mx_y, y)
        
        # Calculate width and height
        width = N_mx_x - N_min_x
        height = N_mx_y - N_min_y
        
        # Calculate the area of the rectangle (bounding box)
        area = width * height
        print(area)

# Call the function
circle()
