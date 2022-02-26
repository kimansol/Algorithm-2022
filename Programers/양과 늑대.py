# https://programmers.co.kr/learn/courses/30/lessons/92343
# 2022카카오/레벨3/양과늑대
# 2022.02.19  56분
from collections import deque
from copy import deepcopy
import sys
sys.setrecursionlimit(100000)

def back(possible, sheep, wolf, info, path):
    new_possibe = deepcopy(possible)
    global answer
    if len(new_possibe) == 0:
        answer = max(answer, sheep)
        return

    for i in range(len(new_possibe)):
        node = new_possibe.popleft()
        if info[node] == 0: # 양
            if path.get(node) != None: #더 갈곳이 있을떄
                for i in range(len(path[node])):
                    new_possibe.append(path[node][i])
                back(new_possibe,sheep+1,wolf,info,path)
                for i in range(len(path[node])):
                    new_possibe.pop()
            else:  #더 갈곳이 없을떄
                back(new_possibe, sheep + 1, wolf, info,path)
        elif info[node] == 1: #늑대
            if sheep > wolf+1: #더 갈곳이 있을 때
                if path.get(node) != None:
                    for i in range(len(path[node])):
                        new_possibe.append(path[node][i])
                    back(new_possibe,sheep,wolf+1,info,path)
                    for i in range(len(path[node])):
                        new_possibe.pop()
                else: #더 갈곳이 없을떄
                    back(new_possibe, sheep, wolf + 1, info, path)
        new_possibe.append(node)
        if new_possibe == possible:
            answer = max(answer, sheep)
            return


answer = 0
def solution(info, edges):
    sheep = 1
    wolf = 0

    # 모든 경로를 딕셔너리에 저장 {0: deque([1, 8]), 1: deque([2, 4]), 8: deque([7, 9]), 9: deque([10, 11]), 4: deque([3, 6]), 6: deque([5])}
    path = dict()
    for s, e in edges:
        if s in path.keys():
            path[s].append(e)
        else:
            path[s] = deque([e])
    print(f'모든 경로 {path}')
    print(f'노드 상태 {info}')

    # #갈 필요 없는 경로 제거
    cnt = 1
    while cnt != 0:
        # 제거한 노드가 없을 시
        cnt = 0
        # 자식이 없으면서(마지막 노드)이면서 자신이 늑대일 경우 정보를 3으로 변경
        for i in range(len(info)):
            if info[i] == 1 and path.get(i) == None:
                info[i] = 3
                cnt += 1
        # 모든 경로를 돌며 정보가 3인곳으로 가는 경로를 제거
        zero = []
        if cnt != 0:
            for i in path.keys():
                for _ in range(len(path[i])):
                    tmp = path[i].popleft()
                    if info[tmp] != 3:
                        path[i].append(tmp)
                if len(path[i]) == 0:
                    zero.append(i)
        # 자식이 없는 노드의 경우 path 사전에서 제거
        for i in zero:
            del path[i]

    print(f'제거한 경로 {path}')
    print(f'노드 상태 {info}')

    # 시작하고 갈수 있는 곳 path[0]을 possible 에 넣기 deque([1, 8])
    if len(path) == 0:
        return 1
    possible = deque()
    for i in range(len(path[0])):
        possible.append(path[0][i])

    back(possible, sheep, wolf, info, path)

    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1],
                   [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))