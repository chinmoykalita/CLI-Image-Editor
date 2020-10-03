from PIL import Image
import os

def cropImage(im, ima):
    print("To crop the image Please input the coordination")
    a = int(input("Left: "))
    b = int(input("Upper: "))
    c = int(input("Right: "))
    d = int(input("Lower: "))
    box = (a, b, c, d)
    print("Please wait....")
    region = im.crop(box)
    re = input("To show the image press 's'\nTo return press any key\n")
    if re == 's':
        region.show()
    else:
        return None    

def rotateImage(im, ima):
    print("To rotate the image Please enter the angle of rotation\n")
    a = int(input("Angle(degrees): "))
    im = im.rotate(a)
    print("Image rotated successfully\nTo show and save the image press 's'\nOtherwise press any key\n")
    b = input()
    if b == 's':
        im.show()
        ss = f"rotate{ima}"
        im.save(ss)
    else:
        return None    

def blackwhite(im, ima):
    print("\nPlease wait...")
    im = im.convert('1')
    print("To show and save the image press 's'\nTo return press any key")
    a = input()
    if a == 's':
        ss = f"blackwhite{ima}"
        im.save(ss)
        im.show()
    else:
        return None    

if __name__ == "__main__":
    print("-------------CLI Image Editor-------------\n---------------------------------------------\n---------------------------------------------\n---------------------------------------------\n---------------------------------------------\n")
    while True: 
        files = [f for f in os.listdir('.') if os.path.isfile(f) if f.endswith("jpg") or f.endswith("png") or f.endswith("jpeg")]
        print("\nPlease select which image to be edited\n")
        for f in range(len(files)):
            print(f"{f}: {files[f]}")
        i = input()
        try:
            ima = files[int(i)]
        except IndexError as e:
            print("Please enter valid file")
            continue
        except Exception as e:
            print("Please enter the index number")
            continue
        im = Image.open(ima)
        
        while True:

            print(f"\nWhat do you want to do with your image- {ima}?\n")

            print("To show the image press 's'\nTo crop the image press 'c'\nTo rotate the image press'r'\nTo greyscale the image press 'g'\nTo go back press 'b'\nTo exit press 'q")
            a = input()
            if a == 's':
                im.show()
            elif a == 'c':
                try:  
                    cropImage(im, ima)
                except Exception as e:
                    print("\nSomething went wrong\n")    
            elif a == 'r':
                try:
                    rotateImage(im, ima)
                except Exception as e:
                    print("\nSomething went wrong\n")     
            elif a == 'g':
                try:
                    blackwhite(im, ima)
                except Exception as e:
                    print("\nSomething went wrong\n")    
            elif a == 'b':
                break       
            elif a == 'q':
                exit()

            else:
                print("Please enter a valid option\n")            
        
