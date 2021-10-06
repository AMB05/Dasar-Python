#nested dict
dict = {'Nama': 'Birri',
        'NPM': 5181011076, 
        'prodi':
            {
                'kelas' : 2,
                'nilai' : 100,
            }
        
        }
print ("dict['Nama']  : ", dict['Nama'])
print ("dict['NPM']   : ", dict['NPM'])
print ("dict['kelas'] : ", dict['prodi']['kelas'])
print ("dict['nilai'] : ", dict['prodi']['nilai'])

print("")

#mengambil panjang nilai
print("panjang data : %d" %len(dict))
print("")