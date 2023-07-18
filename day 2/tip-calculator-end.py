bill = float(input("Masukan jumlah tagihan: "))
split = int(input("Masukan jumlah orang: "))
tip = int(input("Masukan persentase tip (10%, 20%, 50%): "))


total_with_bill = tip /100  * bill +bill


total = round((total_with_bill / split ),2)
print("Total tagihan per orang: ", total)

