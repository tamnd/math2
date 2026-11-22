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

We remove redundant vectors one at a time and use induction on the number of vectors.
This proof covers a finite spanning set $S$, and the [[proof by Zorn's lemma|KS6PP0BVSD]] covers the general case.
We prove, by induction on $n \ge 0$, that every spanning set of $V$ with $n$ elements contains a [[basis|0VTQTPQGAV]] of $V$.

1. Let $S$ be a spanning set of $V$ with $n$ elements. If $S$ is linearly independent, then $S$ is independent and [[spans|0BJKVF90Z6]] $V$, so $B = S$ is a basis.
2. This covers the case $n = 0$, because the empty set is linearly independent. So we may assume that $n \ge 1$ and that $S$ is linearly dependent.
3. List the elements of $S$ as $v_1, \dots, v_n$. By the [[linear dependence lemma|H75GS7QVPB]], there is an index $k$ with $v_k \in \operatorname{span}(v_1, \dots, v_{k-1})$.
4. By the same lemma, removing $v_k$ does not change the span. So $S' = S \setminus \{v_k\}$ has the same span as $S$, which is $V$.
5. The set $S'$ spans $V$ and has $n - 1$ elements. By the induction hypothesis, $S'$ contains a basis $B$ of $V$.
6. Then $B \subseteq S' \subseteq S$, so $S$ contains a basis of $V$, and the induction is complete.

## Idea

A dependent list always has a vector that the earlier vectors can build, and that vector is spare.
Throwing it away keeps the span, and the list gets shorter.
A finite list cannot get shorter forever, so after at most $\abs{S}$ removals what is left is independent and still spans, which is a basis.
Notice that the proof never chooses from infinitely many options, so it needs no form of the axiom of choice.

## Variants

In $F^m$, row reduction finds the same kind of basis in one pass.
Put the vectors of $S$ as the columns of a matrix and reduce it to echelon form.
The original columns in the pivot positions form a basis of the column space, as the [[pivot basis of the column space|11CSKXQNG3]] shows.
A third route starts from the other end: pick vectors of $S$ one at a time, keeping a vector only when it lies outside the span of those already kept.
The kept vectors stay independent by the dependence lemma, and when $S$ is used up they span $V$.
