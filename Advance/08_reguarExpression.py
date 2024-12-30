import re


pattern = r"[A-Z]+erkit"
text = '''Jochi (c. 1182 – c. 1225) 
was a prince in the Mongol Empire.
 For months before his birth, his 
 mother Börte had been a captive of 
 the Merkit tribe, one of whom 
 forcibly married and raped her. 
 Although there was thus doubt over 
 his parentage, Börte's husband 
 Genghis Khan considered Jochi his 
 son and treated him as such. Many
   Mongols, most prominently Börte's 
   next son Chagatai, disagreed; 
   these tensions eventually caused 
   Jochi's exclusion from the line of
     succession. After Genghis founded the Mongol Empire in 1206, he entrusted Jochi with nine thousand warriors and a large territory in the west of the Mongol heartland; Jochi campaigned extensively to extend Mongol power in the region. He also commanded an army during the invasion of the Khwarazmian Empire, but tensions arose between him and his family during the siege of Gurganj in 1221. They were still estranged when Jochi died of ill health. His descendants continued to rule his territories,
 which became known as the Golden 
 Horde. (Full article...) pattern = Derkit"
'''

# match = re.search(pattern,text)
# print(match)

matches = re.finditer(pattern,text)

for match in matches:
    # print(type(match))
    print(text[match.span()[0]:match.span()[1]])