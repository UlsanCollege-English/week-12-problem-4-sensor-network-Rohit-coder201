import heapq

def prim_mst(graph, start):
    # If the graph has only one node → no edges, cost = 0
    if start not in graph or len(graph) == 1:
        return ([], 0)

    visited = set([start])
    mst_edges = []
    total_cost = 0

    # Min-heap of (weight, u, v)
    heap = []
    for neighbor, w in graph[start]:
        heapq.heappush(heap, (w, start, neighbor))

    while heap and len(visited) < len(graph):
        w, u, v = heapq.heappop(heap)

        # Ignore edges leading to already visited nodes
        if v in visited:
            continue

        # Add edge to MST
        visited.add(v)
        mst_edges.append((u, v, w))
        total_cost += w

        # Add edges from v → others
        for nxt, w2 in graph.get(v, []):
            if nxt not in visited:
                heapq.heappush(heap, (w2, v, nxt))

    return (mst_edges, total_cost)


if __name__ == "__main__":
    sample_graph = {
        "G1": [("G2", 4), ("G3", 2)],
        "G2": [("G1", 4), ("G3", 3)],
        "G3": [("G1", 2), ("G2", 3)],
    }
    edges, cost = prim_mst(sample_graph, "G1")
    print("Sample MST edges:", edges)
    print("Total cost:", cost)
