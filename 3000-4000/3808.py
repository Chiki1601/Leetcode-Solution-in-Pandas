import pandas as pd

def find_emotionally_consistent_users(reactions: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    cnt = defaultdict(set)
    for i, r in enumerate(reactions["reaction"]):
        uid = reactions["user_id"][i]
        d[uid].append(r)
        cnt[uid].add(reactions["content_id"][i])
    ans = []
    for c in cnt:
        size = len(cnt[c])
        if size >= 5:
            #print(c)
            now = d[c]
            size = len(now)
            bars = []
            for n in now:
                ratio = 100 * (now.count(n) / size) + 0.005
                ratio = ratio / 100
                ratio = round(ratio, 2)
                #ratio = round(ratio)
                if ratio >= 0.6:
                    if [n, ratio] not in bars:
                        bars.append([n, ratio])
            if bars:
                print(c, bars)
                #ans.append([c, ])
                for b in bars:
                    ans.append([c, b[0], b[1]])
    #ans.sort(key=lambda x: )
    ans.sort(key=lambda x: (-x[-1], x[0]))
    res = pd.DataFrame()
    a, b, c = [], [], []
    for v in ans:
        a.append(v[0])
        b.append(v[1])
        c.append(v[2])
    res["user_id"] = a
    res["dominant_reaction"] = b
    res["reaction_ratio"] = c
    return res
    
