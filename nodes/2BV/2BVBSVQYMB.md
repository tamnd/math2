---
tag: 2BVBSVQYMB
kind: proof
name: Proof of the finite dimension theorem by row reduction
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
proves: 0WK0Y8RH1M
methods: [0NTF6DMVAP, 0J0XBKG64S]
uses: [JPW6KVS70A, 0VTQTPQGAV, 0EVHJFTG9Z, 05EGHEQZAW]
sources:
  - url: https://en.wikipedia.org/wiki/Dimension_theorem_for_vector_spaces
    locator: lead section
  - book: isbn:9780135367971
    locator: Section 2.3
---

## Proof

We turn a possible dependence relation into a homogeneous linear system, and then use that such a system with more unknowns than equations has a nonzero solution.
This proves part 1 of the theorem, and part 2 in the case where one of the two bases is finite.

First we show this claim: if $b_1, \dots, b_n$ span $V$, then every list of $m > n$ vectors of $V$ is dependent.

1. Let $c_1, \dots, c_m \in V$ with $m > n$. Since the $b_i$ span $V$, there are scalars $a_{ij} \in F$ with
$$c_j = \sum_{i=1}^{n} a_{ij} b_i \qquad (j = 1, \dots, m).$$
2. Let $A = (a_{ij})$. It is an $n \times m$ matrix, with more columns than rows.
3. By [[the theorem on homogeneous systems|JPW6KVS70A]], there is a vector $x = (x_1, \dots, x_m) \ne 0$ in $F^m$ with $Ax = 0$, that is, $\sum_{j=1}^{m} a_{ij} x_j = 0$ for each $i$.
4. By the distributive and associative laws of the [[definition of a vector space|05EGHEQZAW]], we may substitute and regroup:
$$\sum_{j=1}^{m} x_j c_j = \sum_{j=1}^{m} x_j \sum_{i=1}^{n} a_{ij} b_i = \sum_{i=1}^{n} \Bigl( \sum_{j=1}^{m} a_{ij} x_j \Bigr) b_i = 0.$$
5. Not all $x_j$ are $0$, so this is a nontrivial relation, and $c_1, \dots, c_m$ are [[dependent|0EVHJFTG9Z]].

Now let $B = (b_1, \dots, b_n)$ be a finite basis and let $C = (c_i)_{i \in I}$ be any basis of $V$.

6. Suppose that $I$ has more than $n$ elements. Then $n + 1$ distinct members of $C$ are dependent by the claim, since $B$ spans $V$. But a subfamily of the independent family $C$ is independent, which is a contradiction.
7. So $I$ is finite, with some number $m \le n$ of elements.
8. The basis $C$ spans $V$, and the basis $B$ is an independent list of $n$ vectors. By the claim with the roles of $B$ and $C$ exchanged, $n \le m$.
9. Steps 7 and 8 give $m = n$.

## Idea

Each of the $m$ vectors is described by its $n$ coefficients in the spanning list, and these columns form an $n \times m$ matrix.
A relation among the vectors is the same as a solution of the homogeneous system with this matrix.
When $m > n$, row reduction leaves at least one free column, so a nonzero solution exists, and the vectors are dependent.
For example, the vectors $(1, 2)$, $(3, 1)$ and $(1, 1)$ in $\mathbb{R}^2$ give a $2 \times 3$ system, and one solution is $x = (2, 1, -5)$, since $2(1, 2) + (3, 1) - 5(1, 1) = (0, 0)$.

## Variants

The [[proof by the exchange lemma|WXB40PTZNV]] reaches the claim without matrices, by trading vectors one at a time, and it also gives the replacement form.
Both proofs use division in the field: the exchange proof divides by a coefficient, and row reduction divides by pivots.
