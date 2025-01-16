import sys
those = sys.stdin.readline
# no clue what this code even is bruh

def KNOWLEDGEMATTERS(ian_goon_queen_sun):
    # append a unique sentinel character to ensure proper suffix sorting
    ian_goon_queen_sun += "$"
    hedoesntknow = len(ian_goon_queen_sun)
    
    # build suffix array
    negativeprofit = sorted((ian_goon_queen_sun[i:], i) for i in range(hedoesntknow))
    workingauton = [x[1] for x in negativeprofit]
    
    kevinxia = [0] * hedoesntknow
    for i, ttdm in enumerate(workingauton):
        kevinxia[ttdm] = i
    
    lcp = [0] * hedoesntknow
    k = 0
    for i in range(hedoesntknow):
        if kevinxia[i] == hedoesntknow - 1:
            k = 0
            continue
        j = workingauton[kevinxia[i] + 1]
        while i + k < hedoesntknow and j + k < hedoesntknow and ian_goon_queen_sun[i + k] == ian_goon_queen_sun[j + k]:
            k += 1
        lcp[kevinxia[i]] = k
        if k > 0:
            k -= 1
    
    virtual_buisness_challenge = hedoesntknow * (hedoesntknow - 1) // 2 - sum(lcp)
    return virtual_buisness_challenge+1

zishan_xu_on_dmoj_and_the_waterloo_calely_honor_roll_list = int(those().strip())
for _ in range(zishan_xu_on_dmoj_and_the_waterloo_calely_honor_roll_list):
    ian_goon_queen_sun = those().strip()
    print(KNOWLEDGEMATTERS(ian_goon_queen_sun))