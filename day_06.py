''' Day 6: Universal Orbit Map '''

INPUT = ['F4H)7LQ', 'TG2)G6N', 'Y6X)5MP', 'TK5)5KN', 'LLY)WKD', 'XL2)94R',
         'BTG)PQ1', 'DLS)LR5', 'X4H)C93', 'JK5)WB1', 'GRQ)9RF', 'YVJ)1SJ',
         'XPV)T62', 'N6B)735', 'ZBD)C78', 'XYT)LSN', 'TTW)JQY', 'MP6)68B',
         'BVT)VFN', 'YTZ)83Q', 'DP5)FCJ', '61Q)SYF', '7JG)D23', '5SF)QJS',
         '8BW)F52', '4DB)ZLT', 'F1F)QQL', '3XG)RYX', '54Z)SJ8', 'KDD)44C',
         'GGJ)7LV', 'DRC)P22', 'XD7)DXM', 'G9Y)VLV', '7XC)BV7', '265)Y7N',
         'JN4)8XM', 'RKX)ZDK', '556)H6B', 'WKD)YDF', 'Z3T)B4N', 'T83)ZMP',
         '3M2)5TN', '83Q)SX9', '9R9)X4H', 'ZV9)YHM', 'PG8)7WP', '23M)4N7',
         'SX9)QJR', 'V5J)VNL', 'XJP)M3V', 'YR3)DZX', '6VZ)HQ1', 'QQV)BCZ',
         'JC2)2FQ', 'JCS)SJC', '46V)H1F', 'F6M)17N', 'S7Q)7R8', 'HG7)HQC',
         'KGP)MD8', 'X3R)679', 'JWQ)ZNT', 'VNG)WHN', 'B11)YB9', 'FBM)BLX',
         '26Q)QTZ', '5MH)72G', 'DK8)BJJ', '8C2)TYH', 'CCF)1Y5', '5GF)X48',
         'MP2)LRM', 'GT5)1SZ', 'XJK)3ZF', 'WNX)CNN', 'JN4)ZWG', 'WK1)8DX',
         'KPN)3TW', 'GMC)ZBD', 'ZX5)9RD', 'CD4)NC7', 'H1F)4GC', 'VLV)DFW',
         '2F3)7P2', 'G6S)85X', '49H)K1P', 'WCQ)Y93', 'TF9)HL7', '2FQ)D4B',
         '992)7JG', 'JBH)VHV', '53N)WMR', 'M3V)43Q', 'C8B)MFX', 'D4C)PKS',
         '855)4HH', 'WWF)GGM', 'KKR)88M', 'COM)KHS', 'LDN)CRH', 'FRB)KYK',
         'FYC)R85', 'L28)WBT', 'CM7)LT9', '5WV)Y7S', 'DF6)Y12', 'JDQ)2KF',
         '8Y4)XF2', 'SP2)W7T', '7C3)H8S', 'BD8)51R', 'Q96)7WM', 'BCX)RG4',
         '1CW)8VH', 'CSW)K6P', 'JRR)KSF', 'T7W)QBT', '94R)XSK', 'QD9)ZDD',
         'LD8)HC7', 'K1P)698', 'K5H)MDY', 'ZWG)C8B', 'X48)Y9L', '6RH)654',
         'SRH)M15', '3ZF)LD4', 'T3W)1TS', 'C93)MYT', 'D8S)HM8', 'VQB)SYN',
         'XPX)W37', 'QLS)1F8', 'JXQ)H9F', 'ZLT)BMY', '758)9R9', 'WMR)GP1',
         '3ZQ)K1Q', 'F52)52M', 'Q4B)CM7', 'RPW)VYB', 'YYV)CTL', '7LV)53N',
         '3WL)KX6', 'QCG)4SX', 'NYK)HVJ', 'F7G)JLG', 'RZH)B14', 'PWD)963',
         'X5W)9MC', 'NJS)3TR', '1MQ)JBH', '36D)SY4', 'YDF)Y88', '8KX)6VZ',
         '215)TW9', 'S1V)5CN', 'BWH)LV7', '2XT)CGT', 'ZRK)TG2', 'MFB)L35',
         'MHT)M4C', 'NMY)KGP', '9RF)C5T', 'SKY)X5D', 'HJ6)Y9C', 'TGT)2ZQ',
         'YQQ)P89', 'Q4X)28M', '3V2)7Q5', 'P3V)756', 'L1V)M9L', 'VZT)P6S',
         'N6T)MP6', 'BHL)TLD', 'S6W)79Q', 'GB5)XD7', '6Z7)X5W', 'CFC)JS8',
         '2DJ)LZK', '4HH)CXG', 'K1Q)TTW', 'B5D)HLF', '8ZR)34Z', 'Q19)NV8',
         '28L)BHL', 'DVT)X8D', 'QGH)L5N', 'Q9J)X78', 'WM4)TSP', 'RG4)514',
         '4K6)M1M', 'W8Y)NZ2', 'ZRQ)VJM', 'VT8)B6X', 'RY1)JDQ', 'X8D)C1G',
         'G6N)MN1', '6XJ)NMP', 'ZMP)7G2', '1JD)XL5', 'M4C)G2F', 'Q3N)W7Z',
         'PWR)3NF', '2J3)215', 'F33)GK9', 'SDR)5XZ', '53N)TZT', 'QJS)72Q',
         'KWT)6Q6', 'SX9)771', '4DB)97W', 'DN1)VY9', 'ZH1)SCN', 'F52)GH4',
         'HS1)8N5', 'MYV)CXP', 'XC1)LD8', 'F5F)WCQ', '4ZC)P3V', 'LR5)XL2',
         '2H1)BMH', 'K52)858', 'NVX)85N', '5JW)XNL', '5RM)TF8', 'TW3)4T8',
         '3ZJ)KZZ', 'WXS)37V', '72T)RR4', 'ZZC)Q19', '3VM)ZL3', 'X2C)MFB',
         '91H)TJF', 'GJD)CDC', 'LSY)FLK', 'LRM)L4P', '65C)Z3P', '7JZ)2XT',
         'QJR)J4F', 'MKM)L46', 'S2S)3V9', 'MH9)PYK', 'ZBW)1TV', 'MDY)QXW',
         'DXV)VGW', 'NB1)34B', '9VS)YWD', 'GJL)2F3', '1BH)J4K', 'BLX)HY2',
         'HDN)TK5', 'Q96)JLD', 'DWV)MV8', 'BDF)NGQ', 'CFC)HKM', 'QG9)DK8',
         'TNH)1S9', 'WHN)HC9', 'WP3)VQB', 'QXW)SKN', 'QYZ)DG2', '6N9)NDH',
         'Q7X)F33', '6K1)YBK', 'WK9)SKY', 'L5Y)X7V', '1SZ)J2X', '8Y1)2J3',
         'WFK)MTK', 'YKR)YK5', 'VGW)YYV', 'PXQ)3WL', '21L)272', '1CR)2DJ',
         'SXV)J26', 'V41)2VS', 'SRW)5JS', '97W)K17', 'R7R)C5H', '9CC)P59',
         'KLR)DCD', 'SNQ)JB6', '43Q)JW5', 'KQ9)6XJ', 'W84)HSM', 'PYS)YQQ',
         '47W)2DG', 'NDR)PXQ', '7JT)WZX', '2N6)SZ8', '4T8)FV7', '9DX)BC1',
         'JS8)1CV', 'D4B)YMD', 'NJS)GY1', 'GV8)91D', 'SCM)818', 'L5N)GDV',
         'T62)47D', 'SQT)R4V', 'ZBT)9F3', 'LDB)NX7', 'WTF)1WN', 'BLX)FMW',
         'GZB)KLR', 'VJM)NPD', 'GGM)BFL', '52M)49P', 'C6Z)3JT', 'WDX)WNX',
         'C5T)2YY', 'QX9)96M', 'TLN)HQQ', 'BV7)51L', '7WM)5DB', 'ZKK)YVG',
         'SCN)MRM', '8QY)7KX', '8FS)MJG', '19S)WV9', 'QQV)KJY', '6Z5)FYC',
         'ZYL)RG5', 'QMR)PH6', '68B)7FD', '72Q)S1V', 'BCB)C4Q', 'NC7)9T8',
         '2XT)Q3N', '54D)CWD', 'TSP)X2C', 'HFY)LNL', 'HL7)54Z', '5KN)DZK',
         '93Q)3PH', 'MD8)Y7L', 'CT6)RPW', 'YSD)M25', 'ZWG)DVX', 'K95)Q8T',
         'C38)JH7', 'HNX)LSG', 'GZB)T82', 'WVJ)J8R', '3JP)8BW', 'TVN)B82',
         '524)CB6', 'CHZ)GZB', '1F3)YWK', 'CXG)98G', 'CR5)VNG', 'Q8T)DVT',
         'H6B)K5R', 'B49)6MZ', '4QF)9YT', '3YL)F1F', '2KF)N7M', '9MC)K4Z',
         'JLD)L9V', '3GR)FYS', 'VHH)D5D', 'NPD)L7P', 'PQ1)Z1K', '3S4)RBD',
         'YVG)2WN', 'YBK)RKX', 'HS6)KQ5', 'G3Z)91H', 'L5Q)LMN', 'M15)KQ9',
         'MZD)JSX', '3PH)T1M', '5Y2)1N7', 'NX5)YM5', 'VL4)69H', '2GS)1D6',
         '47T)LHW', 'FW3)4K6', 'XR4)9VK', 'MQ9)D4S', 'R2N)X6T', 'HM8)JTX',
         'GGR)892', 'TKL)QLS', 'B8Y)Q4P', '3KF)4VM', '8BS)9P2', 'SYN)2ZC',
         'KJZ)GGJ', 'CW3)R28', 'GQN)Y62', 'R9R)B5D', '6FJ)TF9', '8N4)JGY',
         'W66)W2D', 'T78)M11', 'RR4)G9Y', '5B8)3M2', 'C8Q)13M', '4HM)BCB',
         'FQV)N6B', 'LGN)DST', 'MX9)P4W', 'VT7)4T2', 'BMH)JJB', 'YZF)MP2',
         'B7D)HT4', 'H7R)X2F', '8X8)D4H', 'RG9)2VM', 'YB9)Q7X', 'TBY)FLL',
         'GP1)3BJ', 'HL9)HFT', 'KQ5)LJH', '5FQ)D4C', 'BJJ)MX9', 'L3B)45C',
         'TQN)32C', 'GH4)STG', '82M)HSH', 'N7M)PSD', '5V7)5TD', '223)36G',
         '4L5)ZYJ', '9VK)62Q', '1WN)CLG', '37Z)JXQ', 'PKS)H6C', 'CXL)1TD',
         '3YV)F6M', '63H)943', 'X42)ZGP', 'TLD)S3W', '96Y)2H1', '1DM)FC8',
         '6SR)QJP', '8F9)K95', '9T6)GQ6', 'SCZ)969', '3TR)3VX', 'X42)RDS',
         '13M)RZH', 'TV1)LDN', '5PV)XR4', 'TKK)8K2', 'KJZ)QLH', 'HC9)ZBT',
         'MKB)56X', 'KM9)GQ5', 'H9B)FKT', 'QJS)HM6', 'NV8)5JW', 'H2H)Z99',
         '56W)3S4', '586)82M', '7XK)3XG', '4T2)HTN', 'K52)4F6', 'NNT)JN6',
         'WB1)X42', 'LZK)SKD', 'XDN)TW3', 'P21)WFK', '7Y8)4DB', 'D5J)V5J',
         'WKD)F64', 'M1M)5F4', 'F33)BPZ', 'SPZ)SDC', '16V)J2B', '7X9)YZF',
         '7YX)95R', 'RG5)MJY', '2NM)QKC', 'BPZ)ZBW', 'VK6)G61', 'STG)46V',
         '39L)R1R', 'ZG9)4BB', 'HDN)9YR', '68W)3M1', '1M6)561', '5JZ)D1W',
         '3VX)JTH', 'SLY)HDN', 'ZDK)2NG', '5TD)54D', 'W37)9FG', '5JS)NB1',
         'DTY)KRB', '37V)9CM', 'F51)3ZJ', 'JKR)B8Y', 'D1W)WK9', 'KXF)DWV',
         'ZHB)7KY', 'VSM)B8P', '8BW)FW3', '2LT)5VB', '29W)1HY', '3VX)5V7',
         'WBT)6QN', 'KNS)SH6', 'WP1)4HM', 'CQW)3QW', 'PFB)43J', 'GBK)YC5',
         'LVW)5PV', 'VHK)VJH', '2TS)LDB', 'ZHF)PTT', 'VJH)MQ9', '3HY)VF4',
         '2Z7)X5C', '43P)FHB', 'Z75)X3G', 'LL7)76L', 'LHW)VF8', '1TV)8C2',
         '5VB)SPZ', 'Y62)HNG', 'HSM)VVR', '9SY)6N7', 'Z3P)CHB', 'J2B)SRH',
         'J26)YSB', '2KW)DBJ', '99Z)SCM', '7ZK)8NL', 'R7R)2GS', 'SH6)BGY',
         'VTH)N44', 'ML1)FF8', 'LH8)8Y1', 'F48)3VM', '7KX)7HX', 'VFN)PFB',
         'QJP)RJB', '4L5)48C', 'VVR)MCW', '8N4)NDR', '756)PWK', 'NDH)X3K',
         'NNT)H9B', 'L28)56W', 'RBD)W57', 'KXF)PSP', '2HJ)KJZ', '6KX)589',
         'FV7)NMY', 'QMC)2TS', '96Y)2HJ', 'HNG)WDX', '4BB)R2G', '51L)L28',
         'G5W)QTM', 'LD9)NMN', 'FRF)4JG', 'Z67)9GC', 'Q2T)L91', 'CXW)K5H',
         'YQN)VL4', 'K5R)QZ5', '17N)H3K', 'SDC)4J1', 'CLG)ZZF', 'C74)MH9',
         'TV6)39L', 'RP1)Y1Y', 'KHS)S4H', '827)DCX', 'DS9)5PG', '79Q)G5W',
         'V66)ZTL', 'ZTL)6X1', 'DZX)VT7', 'PW8)G3Z', 'F4K)PXM', 'GHW)FP9',
         '6XK)NNT', 'QKC)CDS', 'C78)K6F', '1HY)WJP', '3YL)HLN', 'Y7S)KLJ',
         'QTN)H6Y', 'WS5)XJP', '1D3)T7W', '5DB)6J3', 'CHB)WVV', '93Q)QX9',
         'CMQ)W8Y', 'DTQ)F1G', 'PRL)9HS', 'J2X)TJX', 'TDX)KT1', 'YZQ)G3K',
         'CM7)F7G', '3V9)9T6', 'W3X)BD8', 'NZ2)MHT', 'C48)D47', 'XL5)M1P',
         'F4H)1NP', 'NJK)3LX', '589)LG7', 'YSB)GBK', 'X5C)CRV', 'R5L)WXS',
         'HC7)Q4X', '514)GX8', 'Y7S)HG7', '9FG)SRW', 'Y12)M99', '45H)R5L',
         'NXV)2CK', '574)VHK', 'YNG)VTH', 'QYZ)ZYL', '32C)XHF', 'D41)W9K',
         'HLF)9PQ', 'W92)VZT', '47D)MLP', 'HY2)QMC', '7G2)SLY', 'DXV)MKB',
         '3BJ)HL9', 'W7T)PG8', '5TN)MQW', '9GC)KWT', 'X48)Y6X', '7P2)S8B',
         '5VX)GMC', 'DG2)5X8', 'QZ5)5MH', '6YF)FZ1', '44C)2HT', '7R8)L5Q',
         '7PM)6VD', 'YWK)R3B', 'J92)W8M', 'H6Y)QGH', 'H9F)5JZ', 'P6S)T77',
         '8K2)38J', 'D5D)4D7', 'FP9)QQV', 'GCS)H7R', 'DCC)9SN', '1TV)72T',
         '7FD)7CL', '6J3)QRL', 'MSF)64F', '3M7)CD4', '128)3KF', '855)TV6',
         '8NL)WM4', 'ZCY)C48', '9NN)D5J', 'QTM)W3N', 'QG9)1K4', '2KF)NWL',
         '8GL)VHH', '7LQ)7XK', 'YHM)ZG9', 'LGN)YKR', 'MYT)3MK', 'L96)YQN',
         'D4S)SRP', '1QP)G2S', 'WM4)MSQ', 'LTV)YCM', '2TT)6FJ', 'C17)8TF',
         '5C8)YZQ', 'WVV)JVR', 'P89)GJD', 'GGQ)8GL', 'PK7)F48', '5WR)MB5',
         'Y62)HT9', 'D41)QG9', 'DFW)LKM', 'BV3)96Y', '3SF)93Q', 'C78)7C3',
         'MFX)3M7', 'N44)1M8', 'WWF)NY2', '2WN)WK1', 'X5D)N6T', '96L)QL4',
         'J4K)J1X', 'G2S)S6W', 'GL3)S3K', '3WL)2Z7', 'RHQ)GJL', 'C1G)GYW',
         'CSW)VT8', 'ZKS)L3B', 'ZZN)YNG', '3LX)DGG', 'HLN)N48', 'F64)574',
         'ZGP)DXV', '1M8)ZH1', 'YM5)L5Y', 'GDV)NX5', 'MQW)1T3', '1KP)W84',
         'DG9)K2W', '6RH)BD7', 'FLK)CR5', 'FHB)7ZK', 'LD2)ZV5', 'XKR)JC2',
         'GDG)5WV', 'Y9C)PYS', 'L27)GGQ', 'GYW)HS1', '679)SXV', '2VS)8QY',
         '72G)XJK', 'RJB)8N4', '3MK)WWF', 'MTK)F2W', 'HTM)LGN', 'RXP)7JT',
         'X28)6Z7', 'GY1)Z8Y', 'MMX)WP3', '3ZJ)FRB', '735)2NM', '1D6)8X8',
         'TN9)4ZC', 'DPV)739', '7PS)XPX', 'PPJ)BXZ', 'JW5)M5D', 'ZDD)1JD',
         '1Y5)ZVQ', 'SJ8)45K', '3ZQ)RYQ', '43J)JK5', 'MFX)2TT', 'Z67)ZKS',
         'D2G)HK2', 'GX8)5RM', 'M11)GNK', 'W7T)NJK', '771)5VT', 'G2F)3R2',
         'Y1Y)D8S', 'C3G)S63', 'B5N)8Y4', 'BGY)KPN', 'GK9)6K1', 'Y7L)H2B',
         'CQL)DPV', 'F2K)TQC', '38J)LSY', 'YVR)GB5', 'M1Z)H2Q', 'FCJ)3YL',
         'P22)8KX', '1TS)F5F', 'QL4)W92', 'CG5)D41', 'MKY)WVJ', 'H2Q)1BM',
         'DCD)PDC', '3JT)47T', 'GQ6)RP1', 'Y93)GCS', 'NMP)76S', '3NF)YYM',
         'PHQ)4QF', 'DR8)JXJ', '64F)5B8', 'BFL)PHQ', '44S)8FS', '85N)5SF',
         'JLG)MSF', '3BJ)L96', 'DGG)GDG', 'CLM)TGT', 'J7L)TLW', 'HT4)7XC',
         'WMV)SNQ', 'KZ3)9CC', 'G6T)X81', 'HFT)4WW', 'VQB)HVR', 'GGM)JGV',
         'KX6)SCZ', '561)6N9', 'NDH)BVT', 'DFG)PRL', 'NP6)3ZQ', '1MQ)MKY',
         'X81)1BH', 'G55)HS6', '4ZX)CQW', '62Y)9L7', 'D6B)6XK', '2SH)63H',
         'K2W)3HF', 'QQL)N51', 'WZB)5YM', 'TJF)6RH', 'G11)348', '8YK)Y23',
         'KYK)W67', 'JGY)77D', 'HM5)HFY', 'VY5)DP5', 'QCL)67G', 'J7F)7X9',
         'LMK)68W', 'CXP)62Y', '311)6PB', 'JTX)SAN', 'P8Q)7HF', '1S9)FHL',
         '48J)QCJ', 'KH6)D91', '858)RB3', '95Z)C9W', 'VS1)9DX', 'Y12)21L',
         'CZB)TKK', 'Q4P)PXH', 'GBD)QCL', 'PXH)TQN', '4X3)KW8', 'RXP)XYT',
         '7VW)1CW', '5PG)LVW', 'KJY)QYZ', 'MRM)QL1', 'KN7)3HP', 'JB6)C3G',
         'H2H)7VW', '4F6)TKF', 'D23)9KH', 'B6X)1M6', 'KLJ)2N6', 'NMN)8ZR',
         'QTZ)SDR', 'C3G)43P', 'BRB)FKC', '9PQ)BR7', 'PDC)QCG', 'KRB)524',
         'Z5M)WP1', 'K17)5VG', 'XNL)NCT', '26V)C9X', '9YR)26Q', 'QLH)RPD',
         '5VT)FZQ', 'C9X)BR9', 'M5D)SVP', 'NY2)8PF', 'ZZC)YCZ', 'Y23)GDP',
         'LR5)855', '1CV)J7F', 'LV7)VS1', '783)CG5', 'ZSL)3WH', 'L91)1KP',
         'DVX)TYV', 'SDH)D6F', 'Y2T)WFB', '5K5)NSM', 'G61)ML1', 'HM6)Z5M',
         'M11)HTM', 'XSK)LMK', 'XJP)45H', 'L46)WS5', '45C)G1K', '1SJ)KNS',
         'BC1)HCS', 'DHH)26V', 'GV8)CHZ', '9F3)HVV', 'YCS)L27', 'BXZ)WZB',
         'VF8)NV7', '2ZC)75W', '9YT)LD2', 'QMC)TNH', 'BZ6)B11', 'HKM)ZKK',
         'CTL)WRS', 'MKK)697', 'TYV)GRQ', 'XS1)L79', '5G2)XSG', '1BM)44S',
         'X7V)TN9', 'NGQ)DN1', 'HT9)VMT', 'RB3)8BS', 'SKN)6QL', 'ZL3)NVX',
         'GDP)WTF', '2YY)KZ3', 'WDD)Q2R', 'TW9)ZCY', 'QTV)128', 'J27)HNX',
         '77D)GQN', '52R)YVJ', 'VY9)ZHB', 'JSX)HM5', 'MV8)KDD', 'Y88)BWH',
         '2DG)K52', 'ZVQ)3YV', 'PTT)BDF', '75W)ZZN', 'RYQ)Z5Z', 'G1K)VSM',
         'WRS)DFG', '34B)FLW', '95R)T4W', '6X1)DHH', 'FGP)FPK', 'L1V)RKS',
         '36G)5K5', 'Z8Y)6WR', '6Z2)D2G', 'X3G)TLN', '4N7)DRC', 'SKY)S2S',
         '2HT)DCC', 'X78)YRX', 'L7P)1DM', '2NG)BTG', '97R)1D3', 'KW8)5HN',
         'ZNT)WMF', 'Y2F)2Z1', 'FZQ)28L', 'WZX)Q9J', 'CQX)GBD', 'LKM)KS8',
         'QL4)CMQ', 'T77)J92', 'WMR)556', 'TYH)LTV', 'Z99)D6B', 'FKT)8F9',
         'JQY)QMR', '3WH)NXV', 'WMF)V41', 'GQ5)QTN', 'N5M)MKM', 'RGG)BV3',
         '7Q5)S4C', '7HX)R9R', 'FC8)FRL', 'MJY)F9D', '4D7)F2K', '348)DC2',
         'JVR)D1M', 'K6F)DL1', 'M99)YOU', '8PF)SYQ', 'L79)FQV', 'M9L)HJW',
         'FHL)NP6', 'J4F)7PS', 'XSK)TC3', 'KZZ)Z75', 'VHV)6YF', '6QN)52R',
         'BCZ)Z9K', '6Q6)5FQ', 'J6N)DS9', 'XF2)CCF', 'C9W)WFD', 'DCX)B49',
         'GNK)9SM', 'KW8)TDX', '3M1)LH8', 'KT1)3SF', 'YK5)16V', '9SM)2LT',
         'VF4)SDH', 'HSH)YCS', 'RKS)5G5', 'TDX)7JZ', '9CM)2CF', 'K9H)2KW',
         '3HD)RXP', 'CQL)FRF', '6N7)MMX', 'JB6)37Z', 'J2B)FTZ', '9RD)49H',
         '3HP)L1V', 'P4W)CZB', '1Y5)FYT', '2H1)ZRQ', 'JH7)6LF', 'DXM)RG9',
         'X6T)BZ6', '69H)GV8', 'XQ7)Z7R', '5NP)QD9', 'JTH)4L5', 'FTC)LLY',
         'LT9)PWD', '739)SP2', 'ZZF)DF6', '9V6)Q96', 'R28)4PR', 'C5H)GHW',
         '7HF)DTY', '49P)J27', '2LT)CFC', 'HQQ)JCS', 'F1G)NVG', 'JXJ)65C',
         'W7Z)B7D', 'Q8T)VK6', '83Q)CXW', '7XC)XQ7', 'S4H)KM9', '5TD)R7R',
         '45P)T83', 'TC3)ZX5', '8N5)61Q', 'HTN)JRK', 'W2D)NRH', 'CB6)9H4',
         'HVV)73D', 'B82)DR8', '9R9)GT5', 'X2F)GT4', 'D6F)XDN', 'DBJ)KH6',
         'Y7N)1F3', 'SY4)X28', 'N48)29W', '735)JN4', 'SJC)19S', 'M25)BP1',
         'HK2)5D4', '3R2)7PM', 'Z9K)YSD', 'YCM)W1F', 'JJB)KN7', '3TR)36D',
         '48C)RM5', 'L27)JV6', 'BD7)CLM', 'D47)ZWB', 'R3B)2CP', 'FMW)4ZX',
         'FPK)JRR', 'H6C)NMR', 'HJW)P8Q', '5G5)KKR', 'W84)ZSL', 'K95)CT6',
         'HQC)JRB', 'LSG)J7L', '5GF)KXF', 'R2G)95Z', '62Q)45P', 'Q2R)W66',
         '9F3)Q2T', '969)XPV', 'H8S)CM3', 'G2S)X3R', 'WS5)XC1', 'CDS)F4K',
         'TZT)W7W', '6LF)9SY', '5HN)992', 'HCS)M1Z', 'GK9)XKR', 'BMY)G6T',
         'RHQ)23M', 'PYK)TXD', 'VNL)6Z2', '7R6)QTV', 'HVJ)6Z5', 'S63)HJ6',
         'CWD)CQX', 'R4V)TV1', '4VM)8YK', 'W9K)J6N', '28M)586', 'TKF)P21',
         'PSD)758', '5MP)265', 'VYB)FBM', 'SKD)Z3T', '7KY)YR3', 'FYT)9VS',
         'PG8)47W', 'RDS)CHS', 'LJH)F4H', '8N9)MZD', 'F9D)3GR', '4GC)G7Y',
         '272)Z67', 'DZK)X54', 'NRH)ZHF', 'FF8)LD9', 'WVQ)R2N', 'JRK)DG9',
         '6WR)WVQ', 'J27)JDW', 'B14)WMV', 'W7W)QM9', 'D1M)C38', 'SRP)RHQ',
         'T1M)S7Q', 'RYX)Q4B', 'WJP)T78', '48C)BCX', '892)JKR', 'SZ8)48J',
         'DL1)4X3', 'JCS)G11', 'KS8)827', '1TD)65N', 'FLL)7YX', '65N)783',
         'CNN)5G2', '586)311', '4SX)8N9', '9KH)C8Q', 'JJB)CQL', 'YMQ)754',
         '5RC)7R6', 'ZWB)96L', 'XSG)3JP', 'T82)T8Z', 'ZYJ)K9H', 'WDD)G55',
         'YC5)9YL', '2CK)86G', 'JN6)3HD', 'MTK)GGR', 'KSF)3HY', '67G)6KX',
         'DST)KRK', 'VJH)F51', 'VMT)99Z', '4JG)DLS', 'TLW)WQB', 'PWK)PPJ',
         'YMD)ZV9', 'FRL)FXY', 'TF9)7Y8', 'R1R)M79', '98G)JWQ', '8XM)5GF',
         'TXD)MXZ', 'MSQ)9NN', '4PR)H2H', 'NVG)PH4', 'QL1)XMW', 'MB5)MYV',
         '5XZ)PK7', 'M79)3V2', 'PXM)1QP', '3HF)XS1', '4WW)B5N', '6MZ)N5M',
         'B5N)Y2F', 'TQC)FS9', '5YM)TMV', 'LMN)W3X', 'RBB)5NP', '9VS)CW3',
         '2ZQ)KXV', 'J7F)NYK', '2VM)6JV', '2TS)1MQ', 'NV7)CSW', '3JT)FGP',
         'T78)YVR', 'WV9)YMQ', '6JV)2SH', 'W57)Y2T', 'L9V)223', 'F2W)GL3',
         'HVR)RGG', 'PSP)VY5', '7WP)PWR', 'SYQ)9V6', '9YL)6SR', 'NX7)V66',
         'D4B)RBB', '1K4)TBY', 'X54)ZRK', 'CM3)6BV', '73D)5RC', 'D91)5C8',
         '6VD)FTC', 'VTH)C17', 'SVP)CXL', 'HQ1)TZ2', 'TMV)WDD', 'RM5)DTQ',
         'T8Z)PW8', 'R85)5WR', '7ZK)SQT', '5X8)DT1', 'FTZ)TKL', '45K)97R',
         'RPD)RY1', 'CGT)T3W', 'TNH)1CR', 'H2B)TVN', '5F4)5VX', 'MJG)YTZ',
         'J8R)LL7', '85X)C6Z', '6BV)BRB', 'YCZ)D3V', '56X)ZZC', '697)C74',
         'H8S)MKK', '9YL)G6S', 'FLW)NJS', 'DT1)5Y2']


class orbit_tree(object):
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        if self.parent is not None:
            self.depth = parent.depth + 1
        else:
            self.depth = 0
        self.children = list()

    def _increase_depth(self):
        self.depth = self.parent.depth + 1
        for child in self.children:
            child._increase_depth()

    def add_child(self, child):
        self.children.append(child)

    def add_parent(self, parent):
        self.parent = parent
        self.depth = parent.depth + 1
        for child in self.children:
            child._increase_depth()

    def count_childs(self):
        i = self.depth
        for child in self.children:
            i += child.count_childs()
        return i

    def find_root(self):
        if self.parent is None:
            return self
        else:
            return self.parent.find_root()


def orbit_map(input):
    orbit_nodes = dict()
    for orbit in input:
        planets = orbit.split(')')
        if set(planets).issubset(set(orbit_nodes.keys())):
            orbit_nodes[planets[1]].add_parent(orbit_nodes[planets[0]])
            orbit_nodes[planets[0]].add_child(orbit_nodes[planets[1]])
        else:
            if planets[0] in orbit_nodes.keys():
                node = orbit_tree(planets[1], orbit_nodes[planets[0]])
                orbit_nodes[planets[0]].add_child(node)
            else:
                pnode = orbit_tree(planets[0], None)
                if planets[1] in orbit_nodes.keys():
                    node = orbit_nodes[planets[1]]
                    node.add_parent(pnode)
                else:
                    node = orbit_tree(planets[1], pnode)
                orbit_nodes.update({planets[0]: pnode})
                orbit_nodes[planets[0]].add_child(node)
            orbit_nodes.update({planets[1]: node})
    return orbit_nodes


def object_distance(orbit_map, obj1, obj2):
    obj_parents = dict()
    for obj in [obj1, obj2]:
        obj_parents[obj] = list()
        current_object = orbit_map[obj]
        while current_object.parent is not None:
            obj_parents[obj].append(current_object.parent.name)
            current_object = current_object.parent

    dup_parents = set(obj_parents[obj1]).intersection(set(obj_parents[obj2]))
    return (len(obj_parents[obj1]) + len(obj_parents[obj2]) -
            2 * len(dup_parents))


orbits = orbit_map(INPUT)
print(orbits['COM'].count_childs())
print(object_distance(orbits, 'YOU', 'SAN'))
