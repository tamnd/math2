---
tag: GJKC4QQWAW
kind: proof
name: Proof that a finite spanning set contains a basis
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
proves: 06MRNP4BNT
methods: [0ASJVEFA9J, X5HG1RNWQX]
uses: [H75GS7QVPB, 0VTQTPQGAV, 0BJKVF90Z6]
sources:
  - book: isbn:9783031410253
    locator: Section 2B
---

## Proof

This proof covers a finite spanning set $S$; the general case is in the [[proof by Zorn's lemma|KS6PP0BVSD]].
We use induction on the number $n = \abs{S}$.

1. If $S$ is independent, then $S$ is independent and [[spans|0BJKVF90Z6]] $V$, so $B = S$ is a [[basis|0VTQTPQGAV]]. This covers $n = 0$, because the empty set is independent.
2. Suppose that $S$ is dependent, with $n \ge 1$. List $S$ as $v_1, \dots, v_n$.
3. By part 1 of the [[dependence lemma|H75GS7QVPB]], there is an index $k$ with $v_k \in \operatorname{span}(v_1, \dots, v_{k - 1})$.
4. By part 2 of the dependence lemma, $S' = S \setminus \set{v_k}$ has the same span as $S$, which is $V$.
5. The set $S'$ has $n - 1$ elements, and it spans $V$. By the induction hypothesis, $S'$ contains a basis $B$ of $V$.
6. Then $B \subseteq S' \subseteq S$, so $S$ contains a basis.

## Idea

Remove redundant vectors one at a time; the span stays the same, and the process stops after at most $\abs{S}$ steps.

## Variants

Row reduction gives the same basis directly: the pivot columns of the matrix with columns in $S$.
