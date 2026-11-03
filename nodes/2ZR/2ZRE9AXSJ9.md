---
tag: 2ZRE9AXSJ9
kind: proof
name: Proof that every sequence has a monotone subsequence, by peaks
msc: [40A05]
proves: 0MHGJRZMTM
uses: [0R8J3ZQMJS, 0KN22AAW5R, 01BX15HSRR]
sources:
  - url: https://en.wikipedia.org/wiki/Bolzano–Weierstrass_theorem
    locator: Proof
---

## Proof

We use peak indices and split into two cases.

1. Call an index $n \in \mathbb{N}$ a peak if $a_m \le a_n$ for all $m > n$.
2. Case 1: there are infinitely many peaks. Let $n_0$ be the smallest peak. For $k \ge 0$, let $n_{k+1}$ be the smallest peak with $n_{k+1} > n_k$.
3. These smallest elements exist by the [[well-ordering principle|01BX15HSRR]]. The sets involved are nonempty, because there are infinitely many peaks.
4. Then $n_0 < n_1 < n_2 < \cdots$, so $(a_{n_k})$ is a [[subsequence|0R8J3ZQMJS]].
5. For each $k$, the index $n_k$ is a peak and $n_{k+1} > n_k$. So $a_{n_{k+1}} \le a_{n_k}$.
6. So $(a_{n_k})$ is decreasing, hence [[monotone|0KN22AAW5R]].
7. Case 2: there are finitely many peaks. Let $n_0$ be a natural number larger than every peak. If there is no peak, let $n_0 = 0$.
8. Assume $n_k \ge n_0$ is defined. Then $n_k$ is not a peak, so there is $m > n_k$ with $a_m > a_{n_k}$. Let $n_{k+1}$ be the smallest such $m$, by the well-ordering principle.
9. Then $n_{k+1} > n_k \ge n_0$, so the recursion continues for all $k$.
10. We get $n_0 < n_1 < n_2 < \cdots$ and $a_{n_{k+1}} > a_{n_k}$ for all $k$.
11. So $(a_{n_k})$ is a strictly increasing subsequence, hence monotone.
12. In both cases, $(a_n)$ has a monotone subsequence.

## Idea

A peak is a term that no later term exceeds. If there are infinitely many peaks, they go down one after the other. If there are only finitely many, then past the last one each term is beaten by a later term. So we climb from term to term.
