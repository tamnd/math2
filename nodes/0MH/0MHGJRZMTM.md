---
tag: 0MHGJRZMTM
kind: statement
role: lemma
name: Every sequence has a monotone subsequence
msc: [40A05]
uses: [0R8J3ZQMJS, 0KN22AAW5R]
sources:
  - url: https://en.wikipedia.org/wiki/Bolzano–Weierstrass_theorem
    locator: Proof
---

## Statement

Let $(a_n)$ be a real sequence.
Then $(a_n)$ has a [[subsequence|0R8J3ZQMJS]] that is [[monotone|0KN22AAW5R]].

## Remarks

The usual proof uses peaks. An index $n$ is a peak if $a_m \le a_n$ for all $m > n$.
If there are infinitely many peaks, the terms at the peaks form a decreasing subsequence.
If there are finitely many peaks, start after the last one. Each index then has a later index with a larger term, and this gives a strictly increasing subsequence.
With the [[monotone convergence theorem|0FM6N4R0VB]], the lemma gives the [[Bolzano–Weierstrass theorem|0KDJD249DT]].

## Explanations

### L1 human

Think of the terms as heights of hills seen from left to right.
Either infinitely many hills have no higher hill to their right, or from some point on you can always find a higher hill further right.
