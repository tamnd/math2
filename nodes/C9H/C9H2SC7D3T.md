---
tag: C9H2SC7D3T
kind: proof
name: Proof of the number of compositions by partial sums
msc: [05A17]
proves: 057H72B2MB
uses: [0J8ANSYKAC, 01VG2A0BHW, 0GV2573FP4, 0C5RDJE73X]
sources:
  - url: https://en.wikipedia.org/wiki/Composition_(combinatorics)
    locator: Number of compositions
---

## Proof

We give a bijection between [[compositions|0J8ANSYKAC]] of $n$ and subsets of $\set{1, \dots, n-1}$.

1. Let $n \ge 1$. Let $\mathcal{C}$ be the set of compositions of $n$, and let $\mathcal{S}$ be the set of subsets of $\set{1, \dots, n - 1}$.
2. Let $(a_1, \dots, a_k) \in \mathcal{C}$. Then $k \ge 1$, because the empty sequence has sum $0 \ne n$.
3. Put $s_i = a_1 + \dots + a_i$ for $0 \le i \le k$. Then $s_0 = 0$ and $s_k = n$.
4. Since each $a_i \ge 1$, we have $s_0 < s_1 < \dots < s_k$. Hence $\set{s_1, \dots, s_{k-1}}$ is a subset of $\set{1, \dots, n-1}$.
5. Define $\Phi(a_1, \dots, a_k) = \set{s_1, \dots, s_{k-1}} \in \mathcal{S}$.
6. Let $S \in \mathcal{S}$ have elements $t_1 < \dots < t_j$. Put $t_0 = 0$ and $t_{j+1} = n$, so $t_0 < t_1 < \dots < t_{j+1}$.
7. Define $\Psi(S) = (t_1 - t_0, t_2 - t_1, \dots, t_{j+1} - t_j)$. Its entries are positive integers, and they sum to $t_{j+1} - t_0 = n$. So $\Psi(S) \in \mathcal{C}$.
8. Let $(a_1, \dots, a_k) \in \mathcal{C}$. The elements of $\Phi(a_1, \dots, a_k)$ in increasing order are $s_1 < \dots < s_{k-1}$, by step 4.
9. So $\Psi(\Phi(a_1, \dots, a_k)) = (s_1 - s_0, \dots, s_k - s_{k-1}) = (a_1, \dots, a_k)$.
10. Let $S = \set{t_1 < \dots < t_j} \in \mathcal{S}$. The partial sums of $\Psi(S)$ are $t_1, \dots, t_{j+1}$, because the differences telescope.
11. So $\Phi(\Psi(S)) = \set{t_1, \dots, t_j} = S$.
12. Thus $\Phi$ and $\Psi$ are inverse maps, and $\Phi$ is a [[bijection|01VG2A0BHW]] from $\mathcal{C}$ to $\mathcal{S}$.
13. The set $\set{1, \dots, n-1}$ has $n - 1$ elements. By the [[number of subsets of a finite set|0C5RDJE73X]], $\abs{\mathcal{S}} = 2^{n-1}$.
14. By the [[bijection principle|0GV2573FP4]], $\abs{\mathcal{C}} = 2^{n-1}$.

## Idea

Write $n$ as a row of $n$ ones. A composition is the same as a choice of the places where we cut the row.
There are $n - 1$ gaps between the ones, and each gap is cut or not. The cut positions are exactly the partial sums $a_1 + \dots + a_i$ with $i < k$.
