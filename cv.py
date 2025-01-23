import cv2

# Open a JPG file
image = cv2.imread('1.jfif')  # Replace 'example.jpg' with the path to your image file


x = 0
y = 100
xlim = len(image) - 1
ylim = len(image[0]) - 1




if image is None:
    print("Error: Could not open the image")
else:
    # Display the image
    cv2.imshow('JPG Image', image)
        # Create a named window to allow positioning
    window_name = 'JPG Image'
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    # Move the window to a specified location (x=100, y=100)
    cv2.moveWindow(window_name, 100, 100)

    q = False
    while True:
        # q = False
        while True:
            key = cv2.waitKey(0)
            if key == ord("b"):
                break
            if key == ord("q"):
                q = True
                break
        if q:
            break


        image[x][y] = [0, 255, 0]
        for i in range(5):
            image[x-i][y] = [255,0,0]
            image[x+i][y] = [0,0,255]
        x += 1
        y += 1

        """
        image data type
        0    y0 y1 y2 y3 y4 ...
        x0
        x1
        x2
        x3
        x4
        ...

        image[x][y][b,g,r]
        """

        cv2.imshow(window_name, image)

        if (x >= xlim or y >= ylim):
            break
    # Display the image
    # cv2.imshow(window_name, image)

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
