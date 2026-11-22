---
tag: NT7GFT7H6T
kind: example
name: A longest path gives a long cycle in a graph of minimum degree d
msc: ["00A35", "05C38"]
topics: [GB14W4SYPK]
audience: school
instance_of: [MD3MRG90W4]
uses: [MD3MRG90W4, 0ZFZ8ZG3EN, 03NAMV1DHJ, 0Z05VCBQ7Y]
sources:
  - url: https://en.wikipedia.org/wiki/Longest_path_problem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Degree_(graph_theory)
    locator: lead section
---

## Example

Let $G$ be a finite simple graph whose [[minimum degree|0ZFZ8ZG3EN]] is $d \ge 2$.
We show by the [[extremal principle|MD3MRG90W4]] that $G$ has a [[cycle|0Z05VCBQ7Y]] of length at least $d + 1$.

1. A [[path|03NAMV1DHJ]] in $G$ uses each vertex at most once, and $G$ is finite, so $G$ has only finitely many paths.
   So $G$ has a longest path $P = v_0 v_1 \cdots v_k$.
2. Every neighbor of $v_0$ lies on $P$.
   If a neighbor $w$ were off $P$, then $w v_0 v_1 \cdots v_k$ would be a longer path, against the choice of $P$.
3. The vertex $v_0$ has at least $d$ neighbors, and by step 2 they are among $v_1, \ldots, v_k$.
4. Let $v_j$ be the neighbor of $v_0$ with the largest index $j$.
   The $d$ or more neighbors have distinct indices in $\{1, \ldots, j\}$, so $j \ge d$.
5. The vertices $v_0, v_1, \ldots, v_j$ are distinct, consecutive ones are adjacent along $P$, and $v_j$ is adjacent to $v_0$.
   So $v_0 v_1 \cdots v_j v_0$ is a cycle.
6. This cycle has $j + 1 \ge d + 1$ vertices, so its length is at least $d + 1$.

## Remarks

The end of a longest path has all its neighbors on the path, and this one fact does the work.
Step 1 is the existence part of the extremal principle, and it uses that $G$ is finite.

The bound $d + 1$ is the best possible in general.
The complete graph $K_{d+1}$ has minimum degree $d$, and no cycle in it is longer than $d + 1$, because a cycle has at most as many vertices as the graph.
Other graphs can have much longer cycles.
The [[hypercube graph|VG7DWJBYB9]] of dimension $3$ has minimum degree $3$, so the example promises a cycle of length at least $4$, and in fact it has a cycle through all $8$ vertices.

Both hypotheses matter.
When $d = 1$ the claim fails: a single edge has minimum degree $1$ and no cycle.
When $G$ is infinite, step 1 fails: the path on all the integers, with $n$ joined to $n + 1$, has minimum degree $2$ and no cycle at all, because no longest path exists.

## Explanations

### L1 human

Walk through the graph along a path that is as long as possible, never visiting a vertex twice.
Look at the first vertex of this path.
All its neighbors must already be on the path, or you could step to a new neighbor first and get a longer path.
This vertex has at least $d$ neighbors, so the farthest one lies at least $d$ steps along the path.
Jumping back from that neighbor to the start closes a cycle with at least $d + 1$ vertices.

### L2 human

We follow the steps in the cube graph, with $d = 3$.
Label the vertices by the strings $000, 001, \ldots, 111$, and join two strings that differ in exactly one place.
One longest path visits all $8$ vertices:
$$P = 000,\ 001,\ 011,\ 010,\ 110,\ 111,\ 101,\ 100.$$
The neighbors of $v_0 = 000$ are $001 = v_1$, $010 = v_3$ and $100 = v_7$, all on $P$, as step 2 says.
The farthest one is $v_7$, so $j = 7 \ge 3$, and the cycle $v_0 v_1 \cdots v_7 v_0$ has length $8$.
Check: $100$ and $000$ differ in the first place only, so the closing edge exists.
The typical use is to start from a longest path and study its ends; the argument promised length $4$ and here delivered $8$.
