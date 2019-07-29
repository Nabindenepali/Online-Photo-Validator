def is_grey(img):
    print(img.size)
    w, h, channel = img.shape
    print(w)
    print(h)
    for i in range(w):
        for j in range(h):
            r, g, b = img[i][j]
            print("r",r-g)
            print("g",g-b)
            print("b",b-r)
            # if r != g != b:
            #     return False
    return True