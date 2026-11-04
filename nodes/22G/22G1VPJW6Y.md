---
tag: 22G1VPJW6Y
kind: proof
name: Proof of the Erdős–Szekeres theorem by the pigeonhole principle
msc: [05A05]
proves: 0SNJM8HSD3
uses: [0HGVCWQGY3, 0VPK4X73Q0]
sources:
  - url: https://en.wikipedia.org/wiki/Erdős–Szekeres_theorem
    locator: Proofs, Pigeonhole principle
---

## Proof

We argue by contradiction, with the [[pigeonhole principle|0HGVCWQGY3]].

1. Let $r, s \ge 1$ be integers, let $N = (r - 1)(s - 1) + 1$, and let $a_1, \dots, a_N$ be distinct real numbers.
2. A subsequence of length $m$ is given by indices $i_1 < i_2 < \dots < i_m$. It is increasing if $a_{i_1} < \dots < a_{i_m}$, and decreasing if $a_{i_1} > \dots > a_{i_m}$. It ends at $a_{i_m}$.
3. For each index $i$, let $x_i$ be the largest length of an increasing subsequence that ends at $a_i$. Let $y_i$ be the largest length of a decreasing subsequence that ends at $a_i$.
4. These maxima exist, because lengths are at most $N$. Also $x_i \ge 1$ and $y_i \ge 1$, because the single term $a_i$ is both increasing and decreasing.
5. Let $i < j$. We claim that $(x_i, y_i) \ne (x_j, y_j)$. Since the terms are distinct, either $a_i < a_j$ or $a_i > a_j$.
6. If $a_i < a_j$, take an increasing subsequence of length $x_i$ that ends at $a_i$. Appending $a_j$ gives an increasing subsequence of length $x_i + 1$ that ends at $a_j$. So $x_j \ge x_i + 1$.
7. If $a_i > a_j$, the same argument with a decreasing subsequence gives $y_j \ge y_i + 1$.
8. In both cases the pairs differ. So the map $g : i \mapsto (x_i, y_i)$ on $\set{1, \dots, N}$ is injective.
9. Suppose, for a contradiction, that there is no increasing subsequence of length $r$ and no decreasing subsequence of length $s$.
10. Then $x_i \le r - 1$ for all $i$. Otherwise an increasing subsequence of length $x_i \ge r$ exists, and its last $r$ terms form one of length $r$.
11. In the same way, $y_i \le s - 1$ for all $i$.
12. By steps 4, 10 and 11, $g$ maps $\set{1, \dots, N}$ into $P = \set{1, \dots, r - 1} \times \set{1, \dots, s - 1}$.
13. By the [[rule of product|0VPK4X73Q0]], $|P| = (r - 1)(s - 1) < N$.
14. By the pigeonhole principle, $g$ is not injective. This contradicts step 8.
15. Hence the sequence has an increasing subsequence of length $r$ or a decreasing subsequence of length $s$.

## Idea

Label each term by the lengths of the longest increasing and decreasing runs that end there. A later term always improves one of the two labels, so all labels differ. If both kinds of subsequence were short, there would be too few labels for $N$ terms.
