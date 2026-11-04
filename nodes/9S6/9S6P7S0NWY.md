---
tag: 9S6P7S0NWY
kind: proof
name: Proof that a graph is bipartite iff it has no odd cycle
msc: [05C75]
proves: 01R1HPEK6S
uses: [07DVHJ8N0A, 07CT9RDY7Q, 0PD57PSHNR, 0VJZM0F9YM, 0J8XE7W68F, 01VVP10MWJ, 0WPZ5YPAGR, 0KMVFSHFGZ, 0HTGB13FE2]
sources:
  - url: https://en.wikipedia.org/wiki/Bipartite_graph
    locator: Characterization
---

## Proof

We prove the easy direction by alternation of sides, and the converse by colouring with the parity of the distance.

1. ($\Rightarrow$) Let $(A, B)$ be a bipartition of $G$, as in the definition of a [[bipartite|07DVHJ8N0A]] graph. Let $(w_0, \dots, w_k)$ be a [[cycle|07CT9RDY7Q]], and say $w_0 \in A$; the case $w_0 \in B$ is symmetric.
2. Each edge has one end in $A$ and one in $B$. By induction on $t$, $w_t \in A$ for even $t$ and $w_t \in B$ for odd $t$.
3. Since $w_k = w_0 \in A$, the length $k$ is even. So $G$ has no cycle of odd length.
4. ($\Leftarrow$) Lemma: if $G$ has a closed [[walk|0VJZM0F9YM]] of odd length, then $G$ has a cycle of odd length. We use [[strong induction|0KMVFSHFGZ]] on the length $k$.
5. Let $W = (w_0, \dots, w_k)$ with $w_k = w_0$ and $k$ odd. Since no vertex is adjacent to itself, $k \ne 1$. So $k \ge 3$.
6. Case 1: $w_1, \dots, w_k$ are pairwise distinct. The edges are $\set{w_{t-1}, w_t}$ with indices modulo $k$. Two of them, for $s \ne t$, could only agree if $w_{s-1} = w_t$ and $w_s = w_{t-1}$.
7. That would give $t \equiv s - 1$ and $s \equiv t - 1$ modulo $k$, so $k \mid 2$, which is false. So the edges are distinct, $W$ is a [[circuit|0PD57PSHNR]], and it is a cycle of odd length.
8. Case 2: $w_i = w_j$ for some $1 \le i < j \le k$. Then $W_1 = (w_i, w_{i+1}, \dots, w_j)$ is a closed walk of length $j - i$.
9. Also $W_2 = (w_j, w_{j+1}, \dots, w_k, w_1, \dots, w_i)$ is a closed walk of length $k - (j - i)$, using $w_k = w_0 \sim w_1$.
10. Both lengths are between $1$ and $k - 1$, and they add up to the odd number $k$. So one of them is odd, and the induction hypothesis gives an odd cycle. This proves the lemma.
11. Now assume that $G$ has no cycle of odd length. By the [[axiom of choice|0HTGB13FE2]], choose a vertex $r_C$ in each [[connected component|01VVP10MWJ]] $C$ of $G$. For finite $G$ no choice principle is needed.
12. For a vertex $v$ in the component $C$, the vertex $v$ is [[reachable|0J8XE7W68F]] from $r_C$. So the [[distance|0WPZ5YPAGR]] $\delta(v) = d(r_C, v)$ is a natural number.
13. Let $A = \set{v : \delta(v) \text{ even}}$ and $B = \set{v : \delta(v) \text{ odd}}$. They are disjoint, and their union is the vertex set.
14. Let $xy$ be an edge. Then $x$ and $y$ are reachable from each other, so they lie in the same component $C$. Let $r = r_C$.
15. Suppose $\delta(x)$ and $\delta(y)$ have the same parity. Take a walk $P$ from $r$ to $x$ of length $\delta(x)$, and a walk $Q$ from $r$ to $y$ of length $\delta(y)$.
16. Follow $P$ from $r$ to $x$, then the edge $xy$, then $Q$ backwards from $y$ to $r$. This is a closed walk of length $\delta(x) + 1 + \delta(y)$, which is odd.
17. By the lemma, $G$ has a cycle of odd length, a contradiction. So $\delta(x)$ and $\delta(y)$ have different parities.
18. Hence every edge has one end in $A$ and one end in $B$, and $G$ is bipartite.

## Idea

Along any walk the side changes at each step, so a closed walk in a bipartite graph has even length. Conversely, colour each vertex by the parity of its distance from a root. An edge inside one colour class would close an odd walk, and an odd closed walk always contains an odd cycle.
