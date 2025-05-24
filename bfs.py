from collections import deque

def main():
	graph = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
	numRows, numCols = len(graph), len(graph[0])
	q, seen = deque([]), set()
	directions = ((1, 0), (-1, 0), (0, 1), (0, -1)) # down, up, right, left

	def bfs(i, j):
		# BFS traversal of graph of dimensions n * m, where |V| = # of vertices and |E| = # of edges
		# Time Complexity: O(|V|+ |E|) = O(n*m + n*m) = O(n*m) (n*m # of vertices and # of edges)
		# Space Complexity: O(n*m) = max size of seen set (upper bound SC)
		q.append((i, j))
		while q:
			r, c = q.popleft()
			if (r, c) not in seen:
				print((graph[r][c])) # process cell here (e.g. print)
				for d in directions:
					if 0 <= r+d[0] < numRows and 0 <= c+d[1] < numCols: # if in bounds, then only append the new direction
						q.append((r+d[0], c+d[1]))
				seen.add((r, c))

	
	bfs(0, 0)
	# Note: if impassable walls/blocks in the graph, or the graph is not fully connected, or every cell has to be traversed just due to the nature
	# of the (LeetCode) question, run a double nested for loop on the graph, and call bfs with each (i, j).

	print("Nodes traversed:", seen)
	print("Num nodes traversed:", len(seen))

if __name__ == "__main__":
	main()
