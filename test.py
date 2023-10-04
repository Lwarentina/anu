saldo = 10
harga_apel = 2
input_apel = input('mau beli berapa apel? ')
print('anda akan membeli ' + input_apel + ' apel')
total = harga_apel * int(input_apel)
print('total harga : ' + str(total))
if total<=int(saldo):
    kembali = saldo - int(total)
    print('kembalian : ' + str(kembali))
elif total==saldo:
    print('uang pas')
else:
    print('saldo tidak cukup')
