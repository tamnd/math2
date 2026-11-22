---
tag: JZQEV913ZV
kind: proof
name: Proof of the existence of an eigenvalue over an algebraically closed field
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug2
proves: 08CJB2NQ92
methods: [0NTF6DMVAP]
uses: [0BZ81AJNWF, 0FRYPZ6D0X, 02SJG1HC32, 0DPF6WRZW6, 00EHX6FWC0, 053QVHF6N7, 0ZND7NQ970]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Eigenvalues and characteristic polynomial
  - book: isbn:9780134860244
---

## Proof

We show that the characteristic polynomial of $T$ has degree at least $1$, take a root of it, and read that root as an eigenvalue.

1. Let $n = \dim V$.
   Since $V \ne 0$, we have $n \ge 1$.
2. Fix a basis $B$ of $V$ and let $A = [T]_B$ be the matrix of $T$ in this basis.
   By the definition of the [[characteristic polynomial of a linear map|0BZ81AJNWF]],
$$p_T(t) = p_A(t) = \det(t I_n - A).$$
3. By the theorem on the [[coefficients of the characteristic polynomial|0FRYPZ6D0X]],
$$p_A(t) = t^n - (\operatorname{tr} A)\, t^{n-1} + \dots + (-1)^n \det A.$$
   So $p_T$ is monic of [[degree|0DPF6WRZW6]] $n \ge 1$, and in particular it is not constant.
4. The field $F$ is [[algebraically closed|02SJG1HC32]], so every nonconstant polynomial over $F$ has a [[root|00EHX6FWC0]] in $F$.
   So there is $\lambda \in F$ with $p_T(\lambda) = 0$.
5. By the theorem that [[eigenvalues are the roots of the characteristic polynomial|053QVHF6N7]], a root of $p_T$ in $F$ is an [[eigenvalue|0ZND7NQ970]] of $T$.
   So $\lambda$ is an eigenvalue of $T$, which proves the statement.

## Idea

The eigenvalues of $T$ are the roots of one polynomial, and that polynomial has degree $\dim V$.
Since $V$ is not zero, the degree is at least $1$.
Over an algebraically closed field, a polynomial of positive degree always has a root, and that root is the eigenvalue we want.
All the work is hidden in two earlier results: the degree of the characteristic polynomial and the link between its roots and the eigenvalues.

## Variants

[[Axler's proof|6TPH8WGRJJ]] avoids determinants.
It finds a nonzero polynomial that kills one vector, factors it into linear factors, and shows that one factor $T - rI$ has a nonzero kernel.
For $F = \mathbb{C}$, step 4 is the [[fundamental theorem of algebra|0JP0W07Y9A]], so the proof above is only as elementary as that theorem.
