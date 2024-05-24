def main():
    file = input()
    #ext = file[-4] + file[-3] + file[-2] + file[-1]
    flag = False
    ext = ""
    for char in file:
        if char == '.':
            flag = True
        if flag == True:
            ext += char
    print("File name:", end = " ")
    match ext:
        case ".gif":
            print("image/gif")
        case ".jpg":
            print("image/jpeg")
        case ".jpeg":
            print("image/jpeg")
        case ".png":
            print("image/png")
        case ".pdf":
            print("application/pdf")
        case ".txt":
            print("text/plain")
        case ".zip":
            print("application/zip")
        case _:
            print("application/octet-stream")

main()
