kalimat = "Adik mengantar ibu membeli buah di pasar"
kata = kalimat.split(" ")

for kt in kata:
    if kt == 'mengantar' or kt == 'membeli' :
        print('kata kerja')
    elif kt == 'Adik' or kt == 'ibu' or kt == 'buah' :
            print('kata benda')
    else:
        print('kata keterangan')