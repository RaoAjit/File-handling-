import os

def create_file(filename):
    try:
          with open(filename,'x') as f:
               print(f'your {filename} is created')
    except FileExistsError:
         print('file has alredy exist')
    except Exception as e:
         print('an error ocuured')


def view_allfile():
     files=os.listdir()
     if not files:
          print('no file found')
     else:
          for file in files:
               print(file)

def delete_file(filename):
    try:
         os.remove(filename)
    except FileNotFoundError:
         print('file not found')
    except Exception as e:
         print('an erroer occured')
          
         
def read_file(filename):
     try:
        with open(filename,'r') as f:
               content=f.read()
               print(f' content is {filename}:\n{content}')
     except FileNotFoundError:
           print('file dos nopt exist')
     except Exception as e:
           print('an errer occured')

def edit_file(filename):
     try:
          with open(filename,'a')as f:
               content=str(input('enter your data :'))
               f.write(content +'\n')
     except FileNotFoundError:
          print('file not found')
     except Exception as e:
          print('an error is ocuured')

def main():
     while True:
          print('1:createfiles,2:view_allfiles,3:deletefile,4:readfile,5:editfil')
          option=input('select a number:  ')
          if option=='1':
               filename=input("enter file name:  ")
               create_file(filename)
          elif option=='2':
                view_allfile()
          elif option=='3':
               filename=input("enter file name:  ")
               delete_file(filename)
          elif option =='4':
                filename=input("enter file name:  ")
                read_file(filename)
          elif option == '5':
               filename=input("enter file name:  ")
               edit_file(filename)
          elif option == '6':
               break
          else:
               print('enter in range')
               

if __name__=="__main__":
     main()
               
               
      
          
      
               
               
          
    
