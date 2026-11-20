---
tag: ~cfd666bd
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

This proof gives part 1 of the statement, and part 2 when one basis is finite.
First we show: if $b_1, \dots, b_n$ span $V$, then each family of $m > n$ vectors of $V$ is dependent.

1. Let $c_1, \dots, c_m \in V$ with $m > n$. Since the $b_i$ span $V$, write $c_j = \sum_{i=1}^n a_{ij} b_i$ with $a_{ij} \in F$.
2. Let $A = (a_{ij})$, an $n \times m$ matrix with more columns than rows.
3. By [[the theorem on homogeneous systems|JPW6KVS70A]], there is $x = (x_1, \dots, x_m) \ne 0$ with $Ax = 0$, that is, $\sum_{j=1}^m a_{ij} x_j = 0$ for each $i$.
4. By the axioms of the [[definition|05EGHEQZAW]], $\sum_{j=1}^m x_j c_j = \sum_{j=1}^m x_j \sum_{i=1}^n a_{ij} b_i = \sum_{i=1}^n \Big( \sum_{j=1}^m a_{ij} x_j \Big) b_i = 0$.
5. Not all $x_j$ are $0$, so $c_1, \dots, c_m$ are [[dependent|0EVHJFTG9Z]].

Now let $B = (b_1, \dots, b_n)$ be a basis and let $C = (c_i)_{i \in I}$ be another basis.

6. If $I$ had more than $n$ elements, then $n + 1$ distinct members of $C$ would be dependent, by steps 1 to 5. A subfamily of an independent family is independent, so this is a contradiction.
7. So $I$ is finite, with $m$ elements, and $m \le n$.
8. The basis $C$ spans $V$, and $B$ is independent. By steps 1 to 5 with the roles exchanged, $n \le m$.
9. So $m = n$.

## Idea

Coordinates of $m$ vectors in a spanning list of $n$ vectors form an $n \times m$ matrix.
For $m > n$, the matrix has a free column, and a nonzero solution of the homogeneous system gives a dependence relation.
