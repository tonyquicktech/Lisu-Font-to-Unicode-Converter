#Script by www.tonyquick.tech - Version 1.7
"""NOTE: English words inside of a Lisu document may also be converted to Lisu,
         so you'll need to make sure and do a thorough proofread on your converted
         document. Numbers and other characters should appear in the same place
         as your original document, and should carry over just fine. The Naxi inverted
         "Y" is not supported in this script (U+11FBx). This script should work
         with all documents encoded in the ls_ font families.
"""
mapping= {
    u'b': u'ꓐ',     # Lisu letter B
    u'p': u'ꓑ',     # Lisu letter P
    u'P': u'ꓒ',     # Lisu letter ꓒ
    u'd': u'ꓓ',     # Lisu letter ꓓ
    u't': u'ꓔ',     # Lisu letter ꓔ
    u'T': u'ꓕ',     # Lisu letter ꓕ
    u'g': u'ꓖ',     # Lisu letter ꓖ
    u'k': u'ꓗ',     # Lisu letter ꓗ
    u'K': u'ꓘ',     # Lisu letter ꓘ
    u'j': u'ꓙ',     # Lisu letter ꓙ
    u'c': u'ꓚ',     # Lisu letter ꓚ
    u'C': u'ꓛ',     # Lisu letter ꓛ
    u'z': u'ꓜ',     # Lisu letter ꓜ
    u'f': u'ꓝ',     # Lisu letter ꓝ
    u'F': u'ꓞ',     # Lisu letter ꓞ
    u'm': u'ꓟ',    # Lisu letter ꓟ
    u'n': u'ꓠ',   # Lisu letter ꓠ
    u'l': u'ꓡ',   # Lisu letter ꓡ
    u's': u'ꓢ',   # Lisu letter ꓢ
    u'r': u'ꓣ',   # Lisu letter ꓣ
    u'R': u'ꓤ',   # Lisu letter ꓤ
    u'V': u'ꓥ',   # Lisu letter ꓥ
    u'v': u'ꓦ',   # Lisu letter ꓦ
    u'h': u'ꓧ',   # Lisu letter ꓧ
    u'G': u'ꓨ',   # Lisu letter ꓨ
    u'J': u'ꓩ',   # Lisu letter ꓩ
    u'w': u'ꓪ',   # Lisu letter ꓪ
    u'x': u'ꓫ',   # Lisu letter ꓫ
    u'y': u'ꓬ',   # Lisu letter ꓬ
    u'B': u'ꓭ',   # Lisu letter ꓭ
    u'a': u'ꓮ',   # Lisu vowel ꓮ
    u'A': u'ꓯ',   # Lisu vowel ꓯ
    u'e': u'ꓰ',   # Lisu vowel ꓰ
    u'E': u'ꓱ',   # Lisu vowel ꓱ
    u'i': u'ꓲ',   # Lisu vowel ꓲ
    u'o': u'ꓳ',   # Lisu vowel ꓳ
    u'u': u'ꓴ',   # Lisu vowel ꓴ
    u'U': u'ꓵ',   # Lisu vowel ꓵ
    u'L': u'ꓶ',   # Lisu vowel ꓶ
    u'D': u'ꓷ',   # Lisu vowel ꓷ
    u'.': u'ꓸ',   # Lisu tone marker ꓸ
    u',': u'ꓹ',   # Lisu tone marker ꓹ
    u'H': u'ꓺ',   # Lisu tone marker ꓺ
    u'Y': u'ꓻ',   # Lisu tone marker ꓻ
    u';': u'ꓼ',   # Lisu tone marker ꓼ
    u':': u'ꓽ',   # Lisu tone marker :
    u'I': u'꓾',   # Lisu punctuation marker ꓾
    u'=': u'꓿',   # Lisu punctuation marker ꓿
    u'O': u'_',   # Lisu punctuation/tone marker _
    u'S': u'ꓸꓼ',   # Lisu punctuation/tone marker ꓸꓼ
    u'<': u'ꓸꓼ',   # Lisu punctuation/tone marker ꓸꓼ
    u'W': u'ꓹꓼ',   # Lisu punctuation/tone marker ꓹꓼ
    u'>': u'ꓸꓽ',   # Lisu punctuation/tone marker ꓸꓽ
    u'}': u'ꓸꓹꓽ',   # Lisu punctuation/tone marker ꓸꓹꓽ
    u'{': u'ꓸꓸꓼ',   # Lisu punctuation/tone marker ꓸꓸꓼ
    u'~': u'ꓸꓹꓼ',   # Lisu punctuation/tone marker ꓸꓹꓼ
    u'\\': u'ꓸꓸꓽ',   # Lisu punctuation/tone marker ꓸꓸꓽ
}

with open('lisutext.txt', 'rb') as fp: #change lisutext.txt to the name of your .txt file, or vice versa
    data= fp.read().decode('utf-8')
for char in mapping:
    data= data.replace(char, mapping[char])
with open('utf8data.txt', 'wb') as fp: #You can change the output file name if you want as well, keeping the .txt part
    fp.write(data.encode('utf-8'))
