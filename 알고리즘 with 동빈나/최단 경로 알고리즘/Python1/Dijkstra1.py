# 다익스트라 간단 구현
import sys
input = sys.stdin.readline

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정  # e9면 0이 9개, 1e9 => 1 000 000 000 (10진)

n, m = map(int, input().split(()))  # 노드의 개수, 간선의 개수를 입력받기
start = int(input())  # 시작 노드 번호를 입력받기

graph = [[] for _ in range(n + 1)]  # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
visited = [False] * (n+1)  # 방문한 적이 있는지 체크하는 목적의 리스트
distance = [INF] * (n+1)  # 최단 거리 테이블을 모두 무한으로 초기화

# 모든 간선 정보를 입력받기
for _ in range(m):  
    a, b, c = map(int, input().split())  # a번 노드 ~ b번 노드, 비용: c인 경우
    graph[a].append((b, c))  # (인접 노드, 비용)으로 넣음


def get_smallest_node():  # 방문하지 않은 노드 중, 가장 최단 거리가 짧은 노드의 번호 반환
    min_value = INF
    index = 0  # 가장 최단 거리가 짧은 노드의 인덱스
    for i in range(1, n+1):  # 노드 번호가 1부터 시작한다고 가정(대부분)
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = 1

        return index


def dijkstra(start):
    # 시작 노드에 대해 초기화
    distance[start] = 0  # 거리 처리
    visited[start] = True  # 방문 처리
    for j in graph[start]:  # distance리스트에 graph에서 각 노드의 비용을 넣음 
        distance[j[0]] = j[1]  

    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True

        # 현재 노드(now)와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]

            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
