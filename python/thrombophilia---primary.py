# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"43GE100","system":"readv2"},{"code":"D30A.00","system":"readv2"},{"code":"D30A000","system":"readv2"},{"code":"105875.0","system":"med"},{"code":"107447.0","system":"med"},{"code":"12177.0","system":"med"},{"code":"23134.0","system":"med"},{"code":"25971.0","system":"med"},{"code":"26102.0","system":"med"},{"code":"30873.0","system":"med"},{"code":"32933.0","system":"med"},{"code":"44146.0","system":"med"},{"code":"7516.0","system":"med"},{"code":"8479.0","system":"med"},{"code":"8674.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('thrombophilia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["thrombophilia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["thrombophilia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["thrombophilia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
