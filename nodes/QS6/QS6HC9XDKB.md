---
tag: QS6HC9XDKB
kind: proof
name: Proof that n independent or n spanning vectors in an n-dimensional space form a basis
msc: [15A03]
proves: 096V7H13H9
uses: [0VTQTPQGAV, 05G2G0P224, 0EVHJFTG9Z, 0BJKVF90Z6, 0HR573CHNM, 0EPTJA5QV4, 08ZDRN6H41]
sources:
  - url: https://en.wikipedia.org/wiki/Basis_(linear_algebra)
    locator: Properties
---

## Proof

Both parts compare the given family with a basis, using the [[Steinitz exchange lemma|08ZDRN6H41]].

1. Since $\dim V = n$, by the definition of [[dimension|05G2G0P224]] there is a [[basis|0VTQTPQGAV]] $c_1, \dots, c_n$ of $V$. It is [[linearly independent|0EVHJFTG9Z]] and it [[spans|0BJKVF90Z6]] $V$.
2. First assume that $v_1, \dots, v_n$ are linearly independent. Suppose that some $v \in V$ is outside $\operatorname{span}(v_1, \dots, v_n)$, the [[linear span|0HR573CHNM]].
3. Let $a_1 v_1 + \cdots + a_n v_n + a v = 0$ with coefficients in $F$. If $a \ne 0$, then $v = -a^{-1}(a_1 v_1 + \cdots + a_n v_n)$ lies in the span, a contradiction.
4. So $a = 0$, and then all $a_i = 0$ by independence. Thus $v_1, \dots, v_n, v$ are $n + 1$ linearly independent vectors.
5. By the Steinitz exchange lemma with the spanning family $c_1, \dots, c_n$, we get $n + 1 \le n$. This is false.
6. So $v_1, \dots, v_n$ span $V$. Being linearly independent, they form a basis of $V$.
7. Now assume that $v_1, \dots, v_n$ span $V$. Suppose that they are not linearly independent. Then $a_1 v_1 + \cdots + a_n v_n = 0$ for some $a_i \in F$ with some $a_j \ne 0$.
8. Then $v_j = -a_j^{-1} \sum_{i \ne j} a_i v_i$. So $v_j$ lies in the span $Y$ of the $n - 1$ vectors $v_i$ with $i \ne j$.
9. Each $v_i$ lies in $Y$, and $Y$ is a [[linear subspace|0EPTJA5QV4]]. So $Y$ contains every linear combination of $v_1, \dots, v_n$, and $Y = V$.
10. So the $n - 1$ vectors $v_i$ with $i \ne j$ span $V$. The Steinitz exchange lemma, applied to the independent family $c_1, \dots, c_n$, gives $n \le n - 1$. This is false.
11. So $v_1, \dots, v_n$ are linearly independent. Since they span $V$, they form a basis of $V$.

## Idea

The exchange lemma says that an independent family is never longer than a spanning family. An independent family of $n$ vectors that missed a vector could be made longer than the basis. A spanning family of $n$ dependent vectors could be made shorter than the basis. Both are impossible.
