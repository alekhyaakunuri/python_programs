i=0
while(1):
    signal=input("enter  signal:")
    if(signal=='red'):
       print('stop')
       i=i+1
    elif(signal=='green'):
       print('go')
       i=i+1
    elif(signal=='orange'):
       print('wait')
       i=i+1
    else :
        print(i)
        break



  