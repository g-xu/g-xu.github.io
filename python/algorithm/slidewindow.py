
# slide window template
# def slide_window(total, sub):
#     left = right = 0
#     while right < len(total):
#         item = total[right]
#         right += 1
#         #do something now

#         while window needs shrink:
#             item = total[left]
#             left += 1
#             # do something now



# def sub_contain(s, t):
#     for itm in t:
#         if s[itm] < t[itm]:
#             return 0
#     return 1
def min_substr(src, target):
    source = [s for s in src]
    tcount = dict(zip([k for k in set(target)], [0] * len(set(target))))
    scount = tcount.copy()
    for itm in list(target):
        tcount[itm] += 1
    
    left = right = 0
    min_left =  0
    min_width = len(src) + 1
    key_match = 0
    while right < len(src):
        cur = source[right]
        right += 1
        if cur in scount:
            scount[cur] += 1
            if scount[cur] == tcount[cur]:
                key_match += 1

        #while sub_contain(scount, tcount):
        while key_match == len(tcount):
            if right - left < min_width:
                min_width = right - left
                min_left = left
            cur = source[left]
            if cur in scount:
                if scount[cur] == tcount[cur]:
                    key_match -= 1
                scount[cur] -= 1
            left += 1

    print(min_left, min_width, ''.join(source[min_left:min_left+min_width]))

def check_include(s, t):
    source = [s for s in src]
    tcount = dict(zip([k for k in set(target)], [0] * len(set(target))))
    scount = tcount.copy()
    for itm in list(target):
        tcount[itm] += 1
    
    left = right = 0
    min_left =  0
    min_width = len(src) + 1
    key_match = 0
    while right < len(src):
        cur = source[right]
        right += 1
        if cur in scount:
            scount[cur] += 1
            if scount[cur] == tcount[cur]:
                key_match += 1

        #while sub_contain(scount, tcount):
        while right - left >= len(tcount):
            if key_match == len(tcount):
                return True
            cur = source[left]
            if cur in scount:
                if scount[cur] == tcount[cur]:
                    key_match -= 1
                scount[cur] -= 1
            left += 1

    return False

def longest_sub_wo_repeat(src):
    print('------')
    source = [s for s in src]
    window = {}
    
    left = right = 0
    total = 0
    while right < len(source):
        cur = source[right]
        right += 1
        if cur in window:
            window[cur] += 1
        else:
            window[cur] = 1

        while window[cur] > 1:
            curl = source[left]
            left += 1
            window[curl] -= 1
        
        if right - left > total:
            total = right - left
            print(left, total)
    
    return total


    return max_length            

    return False

if __name__ == '__main__':
    # min_substr('ADOBECODEBANC', 'ABC')
    # min_substr('ACDBOBECODEBANC', 'ABC')
    # min_substr('ADBOBPEFLSDFL', 'ABC')

    longest_sub_wo_repeat('abcabcbb')
    longest_sub_wo_repeat('bbbbbbb')
    longest_sub_wo_repeat('pwwkew')