---
tag: ZH0PMDJBWV
kind: definition
name: Held–Karp algorithm
msc: [90C27, 90C39, 68W40]
defines: GEPM2KPAD8
uses: [XJRHJX2241, R3FXF08WBH, 9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm
---

## Definition

Let $n \ge 2$, and let $d(i, j) \ge 0$ be the distance from city $i$ to city $j$, for distinct $i, j \in \set{1, \dots, n}$.
Let $S \subseteq \set{2, \dots, n}$ and $k \in S$.
Let $g(S, k)$ be the least length of a path from city $1$ to city $k$ through all cities of $S$.
The path must visit each city of $S$ once and no other city except city $1$.
The *Held–Karp algorithm* is the following [[algorithm|9DMSG5HAQX]] for the [[travelling salesman problem|XJRHJX2241]].

1. For each $k \in \set{2, \dots, n}$, set $g(\set{k}, k) = d(1, k)$.
2. For $s = 2, \dots, n - 1$, for each $S \subseteq \set{2, \dots, n}$ with $\abs{S} = s$ and each $k \in S$, set
$$g(S, k) = \min_{m \in S \setminus \set{k}} \big( g(S \setminus \set{k}, m) + d(m, k) \big).$$
3. Return $\min_{k \in \set{2, \dots, n}} \big( g(\set{2, \dots, n}, k) + d(k, 1) \big)$.

The returned number is the length of a shortest tour.
A shortest tour itself is recovered by storing, for each $(S, k)$, a city $m$ that attains the minimum.

## Remarks

Correctness: in a shortest path for $(S, k)$, the part before $k$ ends at some $m \in S \setminus \set{k}$ and is itself a shortest path for $(S \setminus \set{k}, m)$.
This is the principle of [[dynamic programming|R3FXF08WBH]].
There are at most $n 2^{n}$ pairs $(S, k)$, and each takes $O(n)$ steps, so the running time is $O(n^2 2^n)$ and the memory is $O(n 2^n)$.

Example: take $n = 4$ with $d(1,2) = 1$, $d(2,3) = 1$, $d(3,4) = 1$, $d(4,1) = 1$, $d(1,3) = 2$, $d(2,4) = 2$, all symmetric.
Then $g(\set{2,3,4}, 4) = 3$ by the path $1, 2, 3, 4$, and adding $d(4, 1) = 1$ gives a tour of length $4$.
Every tour uses $4$ edges of length at least $1$, so $4$ is optimal.

Non-example: the nearest neighbour rule, which always moves to the closest unvisited city, is not the Held–Karp algorithm.
It keeps only one partial path instead of a table over all subsets, and it can return a tour longer than the optimum.

The algorithm works also for asymmetric distances, where $d(i, j) \ne d(j, i)$ is allowed.
