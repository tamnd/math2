---
tag: QS6HC9XDKB
kind: proof
name: Proof that n independent or n spanning vectors in an n-dimensional space form a basis
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
proves: 096V7H13H9
methods: [0J0XBKG64S, 0WCP0PVET6]
uses: [0VTQTPQGAV, 05G2G0P224, 0EVHJFTG9Z, 0BJKVF90Z6, 0HR573CHNM, 0EPTJA5QV4, 08ZDRN6H41]
sources:
  - url: https://en.wikipedia.org/wiki/Basis_(linear_algebra)
    locator: Properties
---

## Proof

In each part we suppose that the other condition fails, and we produce a list that the [[Steinitz exchange lemma|08ZDRN6H41]] forbids.

1. Since $\dim V = n$, by the definition of [[dimension|05G2G0P224]] there is a [[basis|0VTQTPQGAV]] $c_1, \dots, c_n$ of $V$. It is [[linearly independent|0EVHJFTG9Z]], and it [[spans|0BJKVF90Z6]] $V$.
2. For part 1, let $v_1, \dots, v_n$ be independent, and suppose that some $v \in V$ lies outside their [[linear span|0HR573CHNM]].
3. Let $a_1 v_1 + \dots + a_n v_n + a v = 0$. If $a \ne 0$, then $v = -a^{-1}(a_1 v_1 + \dots + a_n v_n)$ lies in the span, which is false. So $a = 0$, and then all $a_i = 0$ by independence.
4. So $v_1, \dots, v_n, v$ is an independent list of $n + 1$ vectors. The Steinitz exchange lemma with the spanning list $c_1, \dots, c_n$ gives $n + 1 \le n$, which is false.
5. Hence $v_1, \dots, v_n$ span $V$. They are independent, so they form a basis of $V$.
6. For part 2, let $v_1, \dots, v_n$ span $V$, and suppose that they are dependent. Then $a_1 v_1 + \dots + a_n v_n = 0$ with some $a_j \ne 0$.
7. Solving for $v_j$ gives $v_j = -a_j^{-1} \sum_{i \ne j} a_i v_i$. So $v_j$ lies in the span $Y$ of the $n - 1$ vectors $v_i$ with $i \ne j$.
8. Every $v_i$ lies in $Y$, and $Y$ is a [[linear subspace|0EPTJA5QV4]], so $Y$ contains every combination of $v_1, \dots, v_n$. Hence $Y = V$.
9. So $n - 1$ vectors span $V$. The Steinitz exchange lemma with the independent list $c_1, \dots, c_n$ gives $n \le n - 1$, which is false.
10. Hence $v_1, \dots, v_n$ are independent. They span $V$, so they form a basis of $V$.

## Idea

The exchange lemma says that an independent list is never longer than a spanning list, and the basis $c_1, \dots, c_n$ is both.
If $n$ independent vectors missed a direction, adding that direction would give $n + 1$ independent vectors, longer than the spanning basis.
If $n$ spanning vectors were dependent, dropping a spare one would give $n - 1$ spanning vectors, shorter than the independent basis.
Both are impossible, so the list is a basis.

## Variants

Part 1 also follows from the [[extension theorem|0M4SXE5WW3]]: the independent list extends to a basis, which has $n$ vectors by the [[dimension theorem|0WK0Y8RH1M]], so nothing was added.
Part 2 follows in the same way from the theorem that [[every spanning set contains a basis|06MRNP4BNT]]: the basis inside the list has $n$ vectors, so nothing was removed.
In $F^n$ there is a matrix proof, with the $n$ vectors as the columns of a square matrix.
Independence means a pivot in every column, spanning means a pivot in every row, and for a square matrix both mean exactly $n$ pivots, as in the [[square matrix criterion|WFM1CX5PZT]].
