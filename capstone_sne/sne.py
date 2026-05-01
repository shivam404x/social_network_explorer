# -------- SOCIAL NETWORK EXPLORER --------

from collections import defaultdict, deque

# -------- DATA STORE --------
users = {}  # yaha pe user ka data store hoga (Hashing use ho raha hai)
graph = defaultdict(list)  # yaha pe friendships store hongi (Adjacency List)


# -------- USER ADD KARNA --------
def add_user(name, interests):
    users[name] = {
        "name": name,
        "interests": interests
    }


# -------- FRIENDSHIP ADD KARNA --------
def add_friend(u, v):
    graph[u].append(v)  # u ka friend v
    graph[v].append(u)  # v ka friend u (undirected graph)


# -------- FRIENDSHIP REMOVE KARNA --------
def remove_friend(u, v):
    if v in graph[u]:
        graph[u].remove(v)
    if u in graph[v]:
        graph[v].remove(u)


# -------- PROFILE SHOW KARNA --------
def show_profile(name):
    print(f"\nUser: {name}")
    print("Interests:", ", ".join(users[name]["interests"]))
    print("Friends:", ", ".join(graph[name]))


# -------- BFS (SHORTEST PATH NIKALNA) --------
def bfs(start, end):
    visited = set()   # visited nodes track karne ke liye
    parent = {}       # path store karne ke liye
    queue = deque([start])  # queue BFS ke liye

    visited.add(start)

    while queue:
        curr = queue.popleft()

        if curr == end:
            break

        # neighbors explore kar saktea hai
        for nei in graph[curr]:
            if nei not in visited:
                visited.add(nei)
                parent[nei] = curr
                queue.append(nei)

    # -------- PATH BANANA --------
    path = []
    temp = end

    while temp != start:
        path.append(temp)
        temp = parent[temp]

    path.append(start)
    path.reverse()

    print("\nShortest Path:", " -> ".join(path))


# -------- DFS (DEPTH LIMITED SEARCH) --------
def dfs_util(node, visited, depth):
    if depth < 0:
        return

    visited.add(node)
    print(node, end=" ")

    # neighbors explore kar sktea hai depth ke hisaab se
    for nei in graph[node]:
        if nei not in visited:
            dfs_util(nei, visited, depth - 1)


def dfs(start, depth):
    visited = set()
    print(f"\nDFS upto depth {depth}: ", end="")
    dfs_util(start, visited, depth)
    print()


# -------- COMMON INTERESTS COUNT KARNA --------
def common_interests(a, b):
    # set use karke intersection nikal rahe hain
    return len(set(users[a]["interests"]) & set(users[b]["interests"]))


# -------- RECOMMENDATION SYSTEM --------
def recommend(user):
    rec = []

    # har user ke saath compare kar rahe hain
    for u in users:
        if u != user:
            score = common_interests(user, u)
            rec.append((u, score))

    # score ke basis pe sort (descending)
    rec.sort(key=lambda x: x[1], reverse=True)

    print("\nRecommendations:")
    for name, score in rec:
        print(f"{name} (score: {score})")


# -------- MAIN FUNCTION --------
def main():
    # -------- USERS ADD --------
    add_user("A", ["music", "coding"])
    add_user("B", ["coding", "sports"])
    add_user("C", ["music", "travel"])
    add_user("D", ["sports", "travel"])
    add_user("E", ["coding", "AI"])

    # -------- CONNECTIONS ADD --------
    add_friend("A", "B")
    add_friend("A", "C")
    add_friend("B", "D")
    add_friend("C", "E")

    # -------- PROFILE SHOW --------
    show_profile("A")
    show_profile("B")
    show_profile("C")

    # -------- BFS RUN --------
    bfs("A", "D")

    # -------- DFS RUN --------
    dfs("A", 2)
    dfs("A", 3)

    # -------- RECOMMENDATION --------
    recommend("A")

    # -------- FRIEND REMOVE --------
    remove_friend("A", "B")
    print("\nAfter removing A-B connection:")
    show_profile("A")


# -------- PROGRAM START --------
if __name__ == "__main__":
    main()