def cek_gejala_jika_fakta(fakta, gejala):
    return gejala in fakta

def cek_gejala_jika_fakta_berdasarkan_rule(fakta, rule):
    status = []
    hasil = None
    for r in rule[0:len(rule)-1]:
        si = cek_gejala_jika_fakta(fakta, r)
        status.append(si)

        if si:
            hasil = rule[len(rule)-1]

    if False in status:
        return False
    return hasil


def cek_keberadaan_data_pada_rule_berdasarkan_gejala(gejala, rules):
    for rule in rules:
        if gejala == rule[len(rule)-1] :
            return rule
        else:
            continue
    return False


def cari_index_rule(gejala, rules):
    for i in range(len(rules)):
        if gejala == rules[i][len(rules[i])-1] :
            return i
        else:
            continue
    return -1

def cari_gejala_yang_tidak_fakta(rule, fakta):
    gejala = []
    for i in rule[0:len(rule)-1]:
        if i not in fakta:
            gejala.append(i)
            
    return gejala


def cari_gejala_yang_fakta(rule, fakta):
    gejala = []
    for i in rule[0:len(rule)-1]:
        if i in fakta:
            gejala.append(i)
            
    return gejala

def cek_gejala_jika_sudah_ada_di_stack(stack, gejala):
    status = False
    for i in stack:
        if i == gejala:
            status = True
            
    return status

def cek_gejala_jika_fakta_berdasarkan_rules(fakta, rules, penyakits):
    fakta_baru = fakta[1:]
    stack = []
    stack.append(fakta[0])
    
    while(len(stack) != 0):
        rule = cek_keberadaan_data_pada_rule_berdasarkan_gejala(stack[len(stack)-1], rules)
        if rule != False:
            data = cari_gejala_yang_tidak_fakta(rule, fakta_baru)
            print('DATA : ' + str(data))
            if len(data) == 0:
                fakta_baru.append(stack[len(stack)-1])
                stack.remove(stack[len(stack)-1])
                
            stack.extend(cari_gejala_yang_tidak_fakta(rule, fakta_baru))
            print('FAKTA : ' + str(fakta_baru))
            print('STACK : ' + str(stack) + '\n')

def cek_jika_penyakit_ada_di_fakta_baru(penyakits, fakta):
    for penyakit in penyakits:
        if penyakit in fakta:
            return True
    return False

def cek_gejala_jika_fakta_berdasarkan_rule2(fakta, rule, rule_item):
    status = False
    
    for r in rule[0:len(rule)-1]:
        if rule_item in fakta:
            status = True
        else:
            status = False
            
    return status

            
def print_keberadaan_gejala_pada_fakta(fakta, rule):
    for i in range(len(rule)-1):
        if cek_gejala_jika_fakta_berdasarkan_rule2(fakta, rule, rule[i]):
            print('\t' + rule[i] + ' : FAKTA')
        else:
            print('\t' + rule[i] + ' : TIDAK FAKTA')

def cari_then_pada_rule(rule, fakta):
    gejala = []
    for i in rule[0:len(rule)-1]:
        if i not in fakta:
            gejala.append(i)
            
    return gejala

def cari_index_terakhir_dari_gejala(stack, gejala):
    count = stack.count(gejala)

    index = -1

    if count > 1:
        for i in range(len(stack)):
            if stack[i] != gejala:
                continue
            index = i
            

    return index
            


def print_cek_gejala_jika_fakta_berdasarkan_rules(fakta, rules, penyakits):
    fakta_baru = fakta[1:]
    stack = []
    stack.append(fakta[0])

    print("1.\tMasukkan " + fakta[0] + " ke dalam Stack\n")
    print("\tStack : " + str(stack) + '\n\n')

    masuk_fakta = False
    fakta_yang_masuk = []
    faktanya = False

    index = 2
    while(len(stack) != 0):

        
        gejala = stack[len(stack)-1]
        index_rule = cari_index_rule(gejala, rules) + 1
        print(str(index) +'.\t' + str(gejala) + ' ada di rule ' + str(index_rule) + '\n')
        rule = cek_keberadaan_data_pada_rule_berdasarkan_gejala(stack[len(stack)-1], rules)

        print('\tFAKTA\t: ' + str(str(fakta_baru)) + '\n')
        print('\tRULE\t: ' + str(index_rule) + '\n')
        #print(rule)
        if rule != False:
            data = cari_gejala_yang_tidak_fakta(rule, fakta_baru)

            gejala_yang_tidak_fakta = cari_gejala_yang_tidak_fakta(rule, fakta_baru)
            stack.extend(gejala_yang_tidak_fakta)
            
            if len(data) == 0:
                fakta_baru.append(stack[len(stack)-1])
                masuk_fakta = True
                fakta_yang_masuk.append(stack[len(stack)-1])
                
                faktanya = stack[len(stack)-1]
                stack.pop()

            jika = rule[0:len(rule)-1]
            maka = rule[len(rule)-1]

            print('\tIF ' + str(jika) + ' THEN ' + maka + '\n')
            print('\t\tTIDAK FAKTA\t: ' + str(gejala_yang_tidak_fakta) + '\n')


            fakta_gejala = cari_gejala_yang_fakta(rule, fakta_baru)
            print('\t\tFAKTA\t\t: ' + str(fakta_gejala) + '\n')

            if len(gejala_yang_tidak_fakta) > 0:
                print('\t' + str(gejala_yang_tidak_fakta) + ' MASUK STACK\n')

            if masuk_fakta:
                print('\tFAKTA YANG MASUK\t: ' + str(faktanya) + '\n')
                print('\t' + str(faktanya) + ' KELUAR DARI STACK\n')
                
            print('\tSTACK : ' + str(stack) + '\n\n')

            index += 1


def print_cek_gejala_jika_fakta_berdasarkan_rules_kesimpulan(fakta, rules, penyakits):
    fakta_baru = fakta[1:]
    stack = []
    stack.append(fakta[0])

    print('\tRULE YANG JALAN\t:\n\n')

    fakta_yang_masuk = []

    rule_jalan = []

    fakta_lain = []

    stack_lain = []

    index = 1
    while(len(stack) != 0):
        gejala = stack[len(stack)-1]
        index_rule = cari_index_rule(gejala, rules) + 1
        
        rule = cek_keberadaan_data_pada_rule_berdasarkan_gejala(stack[len(stack)-1], rules)

        print(str(index) +'.\tRULE '+ str(index_rule) + ' : \n')

        print('\t\tSTACK\t: ' + str(stack) + '\n\n')

        print('\t\tFAKTA BARU\t: ' + str(fakta_yang_masuk) + '\n')

        if rule != False:
            data = cari_gejala_yang_tidak_fakta(rule, fakta_baru)
            if len(data) == 0:
                fakta_baru.append(stack[len(stack)-1])
                masuk_fakta = True
                fakta_yang_masuk.append(stack[len(stack)-1])
                fakta_lain.append(stack[len(stack)-1])
                rule_jalan.append('RULE ' + str(index_rule))
                stack.remove(stack[len(stack)-1])
                
            gejala_yang_tidak_fakta = cari_gejala_yang_tidak_fakta(rule, fakta_baru)
            stack.extend(gejala_yang_tidak_fakta)
            stack_lain.append(gejala_yang_tidak_fakta)

        index += 1

    print('\n+----------------------------------------------------------------+')

    print('|\tRULE YANG JALAN\t\tFAKTA BARU\t\tSTACK\t |')

    print('+----------------------------------------------------------------+\n')
    e = 1
    for i, j, k in zip(rule_jalan, fakta_lain, stack_lain):
        print('\t' + str(e) + '. ' + str(i) + '\t\t' + str(j) + '\t\t\t' + str(k) +'\n')
        e += 1


def buat_rule(rules):
    index = 1
    for rule in rules:
        print('R' + str(index) + '.\tIF ' + str(rule[0:len(rule)-1]) + ' THEN ' + rule[len(rule)-1] + '\n')
        index += 1

def cari_akibat_rule(rules):
    akibat = []
    for rule in rules:
        akibat.append(rule[len(rule)-1])

    return akibat

def cari_sebab_rule_yang_bukan_akibat(rules):
    sebab = []
    for rule in rules:
        for g in rule[0:len(rule)-1]:
            if g not in cari_akibat_rule(rules) and g not in sebab:
                sebab.append(g)
                
    return sebab
            

def buat_pertanyaan(rules, fakta):
    index = 1

    print(str(index) + '.\tAPAKAH SAKIT YANG ANDA RASAKAN ADALAH PENYAKIT ' + fakta[0] + ' ?\n')
    for i in cari_sebab_rule_yang_bukan_akibat(rules):
        print(str(index) + '.\tAPAKAH ANDA MENGALAMI ' + i + ' PADA TUBUH ANDA ?\n')
        index += 1

def demo_1():
    rules2 = [
	["G1", "G2", "G3", "P1"],
	["G4", "G2"],
	["G5", "G6", "G4"],
	["G1", "G5", "G6"],
	["G1", "G7", "P2"],
	["G1", "G4", "G2", "P3"]
    ]
    fact2 = ["P1", "G1", "G3", "G5"]
    penyakit2 = ["P1", "P2", "P3"]
    cek_gejala_jika_fakta_berdasarkan_rules(fact2, rules2, penyakit2)
    

def demo_2():
    rules2 = [
	["G1", "G2", "G3", "P1"],
	["G4", "G2"],
	["G5", "G6", "G4"],
	["G1", "G5", "G6"],
	["G1", "G7", "P2"],
	["G1", "G4", "G2", "P3"]
    ]
    fact2 = ["P1", "G1", "G3", "G5"]
    penyakit2 = ["P1", "P2", "P3"]

    print('\n+----------------------------------------------------------------+')
    print('|                               RULE                             |')
    print('+----------------------------------------------------------------+\n')

    buat_rule(rules2)

    print('\n+----------------------------------------------------------------+')
    print('|                       DAFTAR PERTANYAAN                        |')
    print('+----------------------------------------------------------------+\n')
    
    buat_pertanyaan(rules2, fact2)

    print('\n+----------------------------------------------------------------+')
    print('|                    PROSES BACKWARD CHAINING                    |')
    print('+----------------------------------------------------------------+\n')
    
    print_cek_gejala_jika_fakta_berdasarkan_rules(fact2, rules2, penyakit2)

    print('\n+----------------------------------------------------------------+')
    print('|               KESIMPULAN PROSES BACKWARD CHAINING              |')
    print('+----------------------------------------------------------------+\n')

    print_cek_gejala_jika_fakta_berdasarkan_rules_kesimpulan(fact2, rules2, penyakit2)



def demo_3():
    penyakit2 = ["P1", "P2", "P3"]
    fact2 = ["P2", "G1", "G4", "G5", "G6", "G8", "G14", "G15", "G17", "G22"]
    rules2 = [
	["G19", "G16", "G18", "P1"],
	["G17", "G13", "G16"],
	["G14", "G13"],
	["G5", "G13", "G1", "G18"],
	["G20", "P2"],
	["G10", "G9", "G16", "G22", "G4", "G23", "G15", "G20"],
	["G8", "G10"],
	["G6", "G1", "G9"],
	["G5", "G14", "G6", "G23"],
        ["G12", "G2", "G18", "G21", "G24", "P3"],
        ["G16", "G18", "G7", "G11", "G12"],
        ["G9", "G3", "G2"],
        ["G16", "G24"]
    ]

    print(cek_gejala_jika_fakta_berdasarkan_rules(fact2, rules2, penyakit2))

def demo_4():
    penyakit2 = ["P1", "P2", "P3"]
    fact2 = ["P2", "G1", "G4", "G5", "G6", "G8", "G14", "G15", "G17", "G22"]
    rules2 = [
	["G19", "G16", "G18", "P1"],
	["G17", "G13", "G16"],
	["G14", "G13"],
	["G5", "G13", "G1", "G18"],
	["G20", "P2"],
	["G10", "G9", "G16", "G22", "G4", "G23", "G15", "G20"],
	["G8", "G10"],
	["G6", "G1", "G9"],
	["G5", "G14", "G6", "G23"],
        ["G12", "G2", "G18", "G21", "G24", "P3"],
        ["G16", "G18", "G7", "G11", "G12"],
        ["G9", "G3", "G2"],
        ["G16", "G24"]
    ]

    print('\n+----------------------------------------------------------------+')
    print('|                               RULE                             |')
    print('+----------------------------------------------------------------+\n')

    buat_rule(rules2)

    print('\n+----------------------------------------------------------------+')
    print('|                       DAFTAR PERTANYAAN                        |')
    print('+----------------------------------------------------------------+\n')
    
    buat_pertanyaan(rules2, fact2)

    print('\n+----------------------------------------------------------------+')
    print('|                    PROSES BACKWARD CHAINING                    |')
    print('+----------------------------------------------------------------+\n')
    
    print_cek_gejala_jika_fakta_berdasarkan_rules(fact2, rules2, penyakit2)

    print('\n+----------------------------------------------------------------+')
    print('|               KESIMPULAN PROSES BACKWARD CHAINING              |')
    print('+----------------------------------------------------------------+\n')

    print_cek_gejala_jika_fakta_berdasarkan_rules_kesimpulan(fact2, rules2, penyakit2)



def demo_5():
    penyakit2 = ["P1", "P2"]
    fact2 = ["P2", "G2", "G8", "G5", "G11", "G3", "G13", "G4"]
    rules2 = [
	["G1", "G7", "G6", "G9", "P1"],
	["G2", "G4", "G3", "G1"],
	["G1", "G5", "G7"],
	["G7", "G8", "G6"],
	["G6", "G10", "G9"],
	["G14", "G10"],
        ["G6", "G12", "G16", "G15", "P2"],
        ["G6", "G7", "G2", "G12"],
        ["G15", "G14", "G16"],
        ["G12", "G13", "G15"],
        ["G11", "G14"]
    ]

    print('\n+----------------------------------------------------------------+')
    print('|                               RULE                             |')
    print('+----------------------------------------------------------------+\n')

    buat_rule(rules2)

    print('\n+----------------------------------------------------------------+')
    print('|                       DAFTAR PERTANYAAN                        |')
    print('+----------------------------------------------------------------+\n')
    
    buat_pertanyaan(rules2, fact2)

    print('\n+----------------------------------------------------------------+')
    print('|                    PROSES BACKWARD CHAINING                    |')
    print('+----------------------------------------------------------------+\n')
    
    print_cek_gejala_jika_fakta_berdasarkan_rules(fact2, rules2, penyakit2)

    print('\n+----------------------------------------------------------------+')
    print('|               KESIMPULAN PROSES BACKWARD CHAINING              |')
    print('+----------------------------------------------------------------+\n')

    print_cek_gejala_jika_fakta_berdasarkan_rules_kesimpulan(fact2, rules2, penyakit2)



if __name__ == '__main__':
    demo_5()