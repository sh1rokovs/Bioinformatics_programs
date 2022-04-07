import collections


def cycle_of_euler(startVert, graph):
    ansPath = [startVert]
    curr = startVert
    while True:
        curr = False
        for i in ansPath:
            if len(graph[i]) > 0:
                curr = i
        while True:
            nextVert = graph[curr].pop(0)
            if nextVert == startVert:
                break
            else:
                ansPath.append(nextVert)
                curr = nextVert
        curr = False
        for i in ansPath:
            if len(graph[i]) > 0:
                curr = i
        if curr:
            n = ansPath.index(curr)
            ansPath = ansPath[n:] + ansPath[:n]
        else:
            return ansPath


def nicePrint(list):
    a = [st[0] for st in list]
    a.pop()
    a.append(list[-1])
    print("".join(a))


def iteration_nucle(def_nucle):
    if 'A' in def_nucle[:1]:
        if 'A' in def_nucle[1:2]:
            if 'A' in def_nucle[2:3]:
                if 'A' in def_nucle[3:4]:
                    return def_nucle
        if 'C' in def_nucle[1:2]:
            if 'A' in def_nucle[2:3]:
                if 'A' in def_nucle[3:4]:
                    pass
        if 'T' in def_nucle[1:2]:
            if 'A' in def_nucle[2:3]:
                if 'A' in def_nucle[3:4]:
                    pass
        if 'G' in def_nucle[1:2]:
            if 'A' in def_nucle[2:3]:
                if 'A' in def_nucle[3:4]:
                    pass
    if 'C' in def_nucle[:1]:
        if 'A' in def_nucle[1:2]:
            if 'A' in def_nucle[2:3]:
                if 'A' in def_nucle[3:4]:
                    pass
    if 'T' in def_nucle[:1]:
        if 'A' in def_nucle[1:2]:
            if 'A' in def_nucle[2:3]:
                if 'A' in def_nucle[3:4]:
                    pass
    if 'G' in def_nucle[:1]:
        if 'A' in def_nucle[1:2]:
            if 'A' in def_nucle[2:3]:
                if 'A' in def_nucle[3:4]:
                    pass


def find_bonus(graph):
    helper = {item: [0, 0] for item in graph.keys()}
    for key, valuelist in graph.items():
        helper[key][0] = len(valuelist)
        for it in valuelist:
            if it in helper.keys():
                helper[it][1] += 1
            else:
                helper[it] = [0, 1]
    for key, value in helper.items():
        if value[0] > value[1]:  # исходящих больше
            to = key
        if value[0] < value[1]:  # входящих больше
            fr = key
    return (fr, to)


in_put = input()
lines = []
while True:
    try:
        in_put = input()
        lines.append(in_put)
    except EOFError:
        break
ans = collections.defaultdict(list)
for el in lines:
    ans[el[:-1]].append(el[1:])
brujgraph = ans
vert_bonus = find_bonus(brujgraph)
brujgraph[vert_bonus[0]].append(vert_bonus[1])
nicePrint(cycle_of_euler(vert_bonus[1], brujgraph))
iteration_nucle(lines)
