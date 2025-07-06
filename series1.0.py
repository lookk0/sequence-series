def again():
    again = input("\nต้องการทำต่อหรือไม่? (y/n): \n").lower()
    if again not in ['y','yes','ok','k']:
        print('\nขอบคุณที่ใช้งานครับบบบ :)')
        exit()

def tryagain():
        print('\ntry again\n')
        again()

while True:
    sr_type = input('\n(1) อนุกรมเลขคณิตจำกัด\n(2) อนุกรมเราขาคณิตจำกัด\ninput: ')

    if sr_type == '1':

        try:
            a1,d,n = map(float,input('\nใส่ a1 (พจน์แรก) d (ผลต่างร่วม/a2-a1) n (จำนวนพจน์ที่จะหา >0) ตามลำดับ \nเช่น 1 10 20\ninput (a1,d,n): ').split(' '))
            if n <= 0:
                tryagain()

            a2 = a1+d
            a3 = a2 + d
            sn = (n/2)*(2*a1+(n-1)*d)

            print(f'\nดังนั้นผลรวม {int(n)} พจน์ของลำดับเลขคณิต a₁ = {a1}, a₂ = {a2}, a₃ = {a3}, ... , a{int(n)} = {sn}\n')
            again()

        except ValueError:
            tryagain()

    elif sr_type == '2':

        try:
            a1,r,n = map(float,input('\nใส่ a1 (พจน์แรก) r (อัตราส่วนร่วม|a2/a1) n (จำนวนพจน์ที่จะหา >0) ตามลำดับ \nเช่น 1 10 20\ninput (a1,r,n): ').split(' '))
            if n <= 0 or a1 == 0:
                tryagain()

            if r == 1:
                sn = a1*r
            else:
                sn = a1*((r**n)-1)/(r-1)

            a2 = a1 * r
            a3 = a2 * r
    
            print(f'\nดังนั้นผลรวม {int(n)} พจน์ของลำดับเรขาคณิต a₁ = {a1:.5f}, a₂ = {a2:.5f}, a₃ = {a3:.5f}, ... , a{int(n)} = {sn:.5f}\n')
            again()

        except ValueError:
            tryagain()

    else:
        tryagain()