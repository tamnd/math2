---
tag: PBZK2A09X4
kind: definition
name: Well-quasi-ordering
msc: [06A06, 06A07]
defines: NH25G6GC07
uses: [0VABYWJWH9, 0G9EKM0E15, 03HF498P1J]
sources:
  - url: https://en.wikipedia.org/wiki/Well-quasi-ordering
---

## Definition

Let $X$ be a set and let $\le$ be a [[preorder|0VABYWJWH9]] on $X$.
The preorder is a *well-quasi-ordering* when for every infinite [[sequence|0G9EKM0E15]] $x_1, x_2, x_3, \ldots$ of elements of $X$ there are indices $i < j$ with $x_i \le x_j$.

## Remarks

Example: every finite set with any preorder is well-quasi-ordered.
Check: an infinite sequence in a finite set has $x_i = x_j$ for some $i < j$, and then $x_i \le x_j$ by reflexivity.

Non-example: the positive integers ordered by divisibility are well-founded but not well-quasi-ordered.
The sequence of primes $2, 3, 5, 7, \ldots$ has no $i < j$ with $p_i \mid p_j$.

Equivalent form: every infinite sequence has an infinite subsequence $x_{i_1} \le x_{i_2} \le \cdots$ with $i_1 < i_2 < \cdots$.
Another equivalent form: the strict part of $\le$ is well-founded and every [[antichain|03HF498P1J]] is finite.
A sequence with no $i < j$ such that $x_i \le x_j$ is called bad, so a well-quasi-ordering is a preorder with no bad sequences.
The abbreviation wqo is common.
