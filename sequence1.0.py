def again():
    again = input("\nต้องการทำต่อหรือไม่? (y/n): \n").lower()
    if again not in ['y','yes','ok','k']:
        print('\nขอบคุณที่ใช้งานครับบบบ :)')
        exit()

def tryagain():
        print('\ntry again\n')
        again()

while True:
    sq_type = input('\n(1) ลำดับเลขคณิตจำกัด\n(2) ลำดับเรขาคณิตจำกัด\ninput: ')

    if sq_type == '1':

        try:
            a1,a2,n = map(float,input('\nใส่ a1 (พจน์แรก) a2 (พจน์สอง/a1+d) n (จำนวนพจน์ที่จะหา >0) ตามลำดับ \nเช่น 1 10 20\ninput (a1,a2,n): ').split(' '))
            if n <= 0:
                tryagain()

            d = a2-a1
            a3 = a2 + d
            an = a1+(n-1)*d

            print(f'\nดังนั้นลำดับพจน์ที่ {int(n)} ของลำดับเลขคณิต a₁ = {a1}, a₂ = {a2}, a₃ = {a3}, ..., a{int(n)} = {an}\n')
            again()

        except ValueError:
            tryagain()

    elif sq_type == '2':

        try:
            a1,a2,n = map(float,input('\nใส่ a1 (พจน์แรก) a2 (พจน์สอง/a1*r) n (จำนวนพจน์ที่จะหา >0) ตามลำดับ \nเช่น 2 8 20\ninput (a1,a2,n): ').split(' '))
            if n <= 0 or a1 == 0:
                tryagain()

            r = a2/a1
            a3 = a2 * r
            an = a1*(r**(n-1))

            print(f'\nดังนั้นลำดับพจน์ที่ {int(n)} ของลำดับเรขาคณิต a₁ = {a1}, a₂ = {a2}, a₃ = {a3}, ..., a{int(n)} = {an:.5f}\n')
            again()

        except ValueError:
            tryagain()

    else:
        tryagain()