---
tag: TN4GDFWGAR
kind: statement
role: theorem
name: Friendship theorem
msc: [05C75, 05C50]
uses: [0JD5C82QMB, 01T3TMGTTE, 0NZ8MDBN6Q]
about: [0JD5C82QMB]
sources:
  - url: https://en.wikipedia.org/wiki/Friendship_graph
---

## Statement

Let $G$ be a finite nonempty [[graph|0JD5C82QMB]] in which every two distinct vertices have exactly one common [[neighbour|01T3TMGTTE]].
Then $G$ has a vertex adjacent to all other vertices.
Consequently, for some integer $k \ge 0$, the graph $G$ consists of $k$ triangles that share one common vertex and are otherwise disjoint.

## Remarks

The second sentence follows from the first.
If $w$ is adjacent to all other vertices, each other vertex $u$ has exactly one common neighbour with $w$.
So the vertices other than $w$ fall into pairs of adjacent vertices.
For the first sentence, suppose that no vertex is adjacent to all others.
A counting argument shows that two non-adjacent vertices have the same degree, and from this that $G$ is $k$-regular for some $k$.
Then the [[adjacency matrix|0NZ8MDBN6Q]] $A$ satisfies $A^2 = (k - 1) I + J$, where $J$ is the all-ones matrix, so the eigenvalues of $A$ are $k$ and $\pm \sqrt{k - 1}$.
Since the trace of $A$ is $0$, the number $\sqrt{k - 1}$ must be rational, and the multiplicities force $k = 2$.
Then $G$ is a triangle, which has a vertex adjacent to all others, a contradiction.
The finiteness hypothesis is needed: there are infinite graphs in which every two vertices have exactly one common neighbour but no vertex is adjacent to all others.
Paul Erdős, Alfréd Rényi and Vera Sós proved the theorem in 1966.

## Explanations

### L1 human

Suppose that in a group of people, every two people have exactly one friend in common.
Then someone is friends with everybody else, a "politician".
Moreover, the rest of the group splits into pairs of friends, each pair together with the politician forming a triangle.

### L2 human

The usual proof is a short application of linear algebra to a combinatorial condition: the hypothesis says exactly that $A^2 = (\text{diagonal of degrees}) - I + J$.
It is a typical use of eigenvalues in [[spectral graph theory|5JESM2ZN48]], where integrality of eigenvalue multiplicities rules out most cases.
The graphs it describes, $k$ triangles glued at a vertex, are called friendship graphs or windmill graphs.
