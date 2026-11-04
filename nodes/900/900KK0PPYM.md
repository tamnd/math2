---
tag: 900KK0PPYM
kind: proof
name: Proof of Cayley's formula by Prüfer sequences
msc: [05C30]
proves: 0M2SSGSYPE
uses: [0MJ0JS72DZ, 09PV9JSY6E, 0H8Q4MANBD, 0FFAYNMAJZ, 0XNN9Z8E5A, 07CT9RDY7Q, 09VZBHB33V, 0JDE56HWQ8, 0T0F6CCS9W, 08QQH9F7G0, 0GV2573FP4]
sources:
  - url: https://sites.lafayette.edu/bloomjs/files/2016/03/Cayleys-formula.pdf
---

## Proof

We show that the [[Prüfer sequence|09PV9JSY6E]] is a bijection, by induction on the number of vertices. For the induction we allow any finite set of integers as vertex set.

1. For a finite set $S \subseteq \Z$ with $\abs{S} = n \ge 2$, let $\mathcal{T}_S$ be the set of [[trees|0MJ0JS72DZ]] with vertex set $S$. Let $\mathcal{W}_S = S^{n-2}$ be the set of sequences of length $n - 2$ with entries in $S$.
2. Lemma A: if $T$ is a tree with at least two vertices and $\ell$ is a leaf, then $T - \ell$ is a tree. Here $T - \ell$ removes $\ell$ and its edge.
3. Proof of Lemma A. A cycle of $T - \ell$ would be a [[cycle|07CT9RDY7Q]] of $T$, so $T - \ell$ is [[acyclic|0XNN9Z8E5A]]. It has the vertex adjacent to $\ell$.
4. Let $x, y \ne \ell$. By [[every walk contains a path|09VZBHB33V]], $T$ has a [[path|0JDE56HWQ8]] from $x$ to $y$. An inner vertex of a path has two distinct neighbours on it, so $\ell$ is not on this path.
5. So the path lies in $T - \ell$, and $T - \ell$ is [[connected|0FFAYNMAJZ]]. This proves Lemma A.
6. Define $\pi(T) \in \mathcal{W}_S$ for $T \in \mathcal{T}_S$ by recursion on $n$. If $n = 2$, let $\pi(T)$ be the empty sequence.
7. If $n \ge 3$, let $\ell$ be the smallest leaf of $T$, which exists by the [[leaf lemma|0H8Q4MANBD]], and let $a$ be its neighbour. Let $\pi(T) = (a, \pi(T - \ell))$, using Lemma A.
8. Unwinding the recursion gives exactly the process that defines the Prüfer sequence. So for $S = \set{1, \dots, n}$, $\pi(T)$ is the Prüfer sequence of $T$.
9. Lemma B: each vertex $x$ of $T \in \mathcal{T}_S$ appears exactly $\deg(x) - 1$ times in $\pi(T)$. We prove it by induction on $n$.
10. If $n = 2$, $T$ has one edge, both vertices have [[degree|0T0F6CCS9W]] $1$, and $\pi(T)$ is empty.
11. Let $n \ge 3$, with $\ell, a$ as in step 7 and $T' = T - \ell$. The vertex $\ell$ has degree $1$, and it does not appear in $\pi(T)$, since $a \ne \ell$ and $\ell$ is not a vertex of $T'$.
12. The vertex $a$ appears $1 + (\deg_{T'}(a) - 1) = \deg_T(a) - 1$ times, by the induction hypothesis. Every other vertex $x$ has $\deg_{T'}(x) = \deg_T(x)$, and appears $\deg_T(x) - 1$ times.
13. Consequence of Lemma B: every vertex of $T$ has degree at least $1$, since $T$ is connected with $n \ge 2$ vertices. So the leaves of $T$ are exactly the elements of $S$ that do not appear in $\pi(T)$.
14. Claim: for every $S$ with $\abs{S} = n \ge 2$, the map $\pi : \mathcal{T}_S \to \mathcal{W}_S$ is a bijection. We argue by induction on $n$.
15. If $n = 2$, say $S = \set{a, b}$, the only tree on $S$ has the single edge $ab$, because the graph with no edge is not connected. And $\mathcal{W}_S$ has only the empty sequence.
16. Let $\abs{S} = n + 1 \ge 3$, and assume the claim for all sets of size $n$. Let $w = (w_1, \dots, w_{n-1}) \in \mathcal{W}_S$.
17. The sequence $w$ has at most $n - 1$ distinct entries, and $S$ has $n + 1$ elements. Let $\ell$ be the smallest element of $S$ that does not appear in $w$.
18. Let $S' = S \setminus \set{\ell}$ and $w' = (w_2, \dots, w_{n-1})$. Then $w' \in \mathcal{W}_{S'}$. By the induction hypothesis, there is exactly one $T' \in \mathcal{T}_{S'}$ with $\pi(T') = w'$.
19. Existence. Let $T$ be $T'$ with the new vertex $\ell$ and the new edge $\ell w_1$; note $w_1 \in S'$. Then $T$ is connected, since $T'$ is connected and $\ell$ is joined to $w_1$.
20. A cycle in $T$ through $\ell$ would give $\ell$ two distinct neighbours, but $\ell$ has degree $1$. A cycle avoiding $\ell$ would lie in $T'$. So $T$ is acyclic, and $T \in \mathcal{T}_S$.
21. The vertex $w_1$ has degree at least $2$ in $T$: one edge in $T'$ by step 13, and the edge to $\ell$. So $w_1$ is not a leaf of $T$.
22. Let $x \ne \ell, w_1$ be a leaf of $T$. Then $x$ is a leaf of $T'$, so $x$ does not appear in $w'$ by step 13. Also $x \ne w_1$, so $x$ does not appear in $w$.
23. By the choice of $\ell$ in step 17, $x > \ell$. So $\ell$ is the smallest leaf of $T$, with neighbour $w_1$, and $T - \ell = T'$.
24. By step 7, $\pi(T) = (w_1, \pi(T')) = (w_1, w') = w$.
25. Uniqueness. Let $Q \in \mathcal{T}_S$ with $\pi(Q) = w$. By step 13, the leaves of $Q$ are the elements of $S$ not in $w$. The smallest of them is $\ell$.
26. By step 7, the neighbour of $\ell$ in $Q$ is $w_1$, and $\pi(Q - \ell) = w'$. By Lemma A, $Q - \ell \in \mathcal{T}_{S'}$. By step 18, $Q - \ell = T'$.
27. So the edges of $Q$ are those of $T'$ together with $\ell w_1$. These are the edges of $T$, so $Q = T$. This proves the claim.
28. Take $S = \set{1, \dots, n}$. By the [[number of functions between finite sets|08QQH9F7G0]], $\abs{\mathcal{W}_S} = n^{n-2}$.
29. By the claim and the [[bijection principle|0GV2573FP4]], the number of trees with vertex set $\set{1, \dots, n}$ is $n^{n-2}$.

## Idea

Prüfer's code removes the smallest leaf again and again, and it writes down the neighbour of each removed leaf. A vertex is written $\deg - 1$ times, so the leaves are exactly the labels that never appear.
This lets us read off the first removed leaf from the code alone. Hence the code can be decoded step by step, and the tree can be rebuilt in exactly one way.
