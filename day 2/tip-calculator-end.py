jumlah_tagihan = float(input("Masukan jumlah tagihan: "))
split_bill = int(input("Masukan jumlah orang: "))
tip_percentage = int(input("Masukan persentase tip (10%, 20%, 50%): "))

if tip_percentage == 10:
    tip = 0.1
elif tip_percentage == 20:
    tip = 0.2
elif tip_percentage == 50:
    tip = 0.5
else:
    print("Persentase tip yang valid adalah 10%, 20%, atau 50%.")
    exit()

total = jumlah_tagihan / split_bill * (1 + tip)
print("Total tagihan per orang: ", total)

