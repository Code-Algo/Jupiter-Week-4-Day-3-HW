# Ex 1

word = ['this' , 'is', 'a', 'sentence', '.']

def reverse_strings(s):
    box = []
    delthis = ' '
    for char in s:
        if char.isalpha:
            box.append(char)
    return delthis.join(reversed(box))
reverse_strings(word)

def swap(alist,a,b,c,d,e):
    alist[a],alist[b],alist[c],alist[d],alist[e] = alist[e],alist[d],alist[c],alist[b],alist[a]
    return alist
print(words)
print(swap(word, 4,3,2,1,0))

reversed_word = list(reversed(word))

print(reversed_word)


word.reverse()
print(word)

# Ex 2

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

def dist_words(wrd):
    distinct = {}
    word = wrd.split()
    
    for i in word:
        if i in distinct:
            distinct[i]+=1
        else:
            distinct[i]=1
    
    return distinct
print(dist_words(a_text))


# Ex 3

nums_list = [10,23,45,70,11,15]
target = 70

def linear_search(alist, x):
    for num in range(len(alist)):
        if alist[num] == x:
            return num
    return -1
linear_search(nums_list, 70)