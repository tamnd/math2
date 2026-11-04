---
tag: 5EDHH0MCVE
kind: proof
name: Proof of Ore's theorem
msc: [05C45]
proves: 0NACHJYPKW
uses: [0JD5C82QMB, 0T0F6CCS9W, 090WPKFABX, 0HKXNG2RS1, 07CT9RDY7Q, 0JDE56HWQ8, 03WKB2H474]
methods: [0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Ore's_theorem
    locator: Proof
---

## Proof

We argue by contradiction, with an edge-maximal counterexample.

1. Let $G$ be a finite simple [[graph|0JD5C82QMB]] with vertex set $V$ and $n = \abs{V} \ge 3$. Suppose that $\deg(u) + \deg(v) \ge n$ for all distinct nonadjacent $u, v$.
2. Suppose, for a contradiction, that $G$ is not [[Hamiltonian|090WPKFABX]].
3. Consider the graphs $H$ on the vertex set $V$ that contain every edge of $G$ and are not Hamiltonian. Choose one with the largest number of edges. Such an $H$ exists, because $G$ is one of these graphs and there are finitely many graphs on $V$.
4. Each vertex has at least the same [[degree|0T0F6CCS9W]] in $H$ as in $G$, because $H$ contains all edges of $G$.
5. The graph $H$ is not the [[complete graph|03WKB2H474]] on $V$. Indeed, for $n \ge 3$ the complete graph has the [[Hamiltonian cycle|0HKXNG2RS1]] that visits the vertices in any order.
6. So $H$ has two distinct nonadjacent vertices $u$ and $v$. They are also nonadjacent in $G$, so by Steps 1 and 4, $\deg_H(u) + \deg_H(v) \ge n$.
7. By the choice of $H$ in Step 3, the graph $H + uv$ is Hamiltonian. Its Hamiltonian cycle uses the edge $uv$, since otherwise it would be a Hamiltonian cycle of $H$.
8. Remove the edge $uv$ from this [[cycle|07CT9RDY7Q]]. What remains is a [[path|0JDE56HWQ8]] $w_1, w_2, \dots, w_n$ in $H$ that contains every vertex, with $w_1 = u$ and $w_n = v$.
9. Let $A = \set{i \in \set{1, \dots, n-1} : u w_{i+1} \text{ is an edge of } H}$. The neighbours of $u$ lie among $w_2, \dots, w_n$, so $\abs{A} = \deg_H(u)$.
10. Let $B = \set{i \in \set{1, \dots, n-1} : w_i v \text{ is an edge of } H}$. The neighbours of $v$ lie among $w_1, \dots, w_{n-1}$, so $\abs{B} = \deg_H(v)$.
11. The sets $A$ and $B$ lie in $\set{1, \dots, n-1}$, which has $n - 1$ elements. So $\abs{A \cup B} \le n - 1$. By Step 6, $\abs{A \cap B} = \abs{A} + \abs{B} - \abs{A \cup B} \ge n - (n-1) = 1$. Let $i \in A \cap B$.
12. Since $u$ and $v$ are not adjacent, $1 \notin B$ and $n - 1 \notin A$. Hence $2 \le i \le n-2$.
13. Consider the closed walk $w_1, w_2, \dots, w_i, w_n, w_{n-1}, \dots, w_{i+1}, w_1$. Its edges are path edges, the edge $w_i w_n$ (as $i \in B$) and the edge $w_{i+1} w_1$ (as $i \in A$).
14. This closed walk visits each of the $n \ge 3$ vertices exactly once before it returns to $w_1$. So it is a Hamiltonian cycle of $H$.
15. This contradicts the choice of $H$ as a non-Hamiltonian graph. Hence $G$ is Hamiltonian.

## Idea

Add edges until one more edge would create a Hamiltonian cycle. Then two nonadjacent vertices $u, v$ are the ends of a Hamiltonian path. Their large degree sum forces a "crossing" pair of edges $u w_{i+1}$ and $w_i v$, and these two edges turn the path into a cycle.
