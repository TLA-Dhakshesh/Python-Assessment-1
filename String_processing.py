def longest(words):
    m=0
    w=[]
    for j in words:
        if m<len(j):
            m=len(j)
    for j in words:
        if m==len(j):
            w.append(j)
    return w
def palindrome(words):
    l1=[]
    for j in words:
        if j.lower()==j.lower()[::-1] and len(j)>1:
            l1.append(j)
    return l1
input_text = open("sentences.txt","r")
Output=[]
for i in input_text:
    words=i.split()
    count=len(words)
    long=longest(words)
    pal=palindrome(words)
    if pal:
        pal = ', '.join(pal)
    else:
        pal= "None"
    final = (
        f"Sentence: {i.strip()}\n"
        f"Word Count: {count}\n"
        f"Longest Word: {', '.join(long)}\n"
        f"Palindromes: {pal}\n"
    )
    Output.append(final)
Output_text=open("sentence_analysis.txt","w")
Output_text.write('\n'.join(Output))
