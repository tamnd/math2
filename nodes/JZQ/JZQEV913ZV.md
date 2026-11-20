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

We find a root of the characteristic polynomial.

1. Let $n = \dim V$. Since $V \ne 0$, $n \ge 1$. Fix a basis $B$ of $V$ and let $A = [T]_B$.
2. By the definition of the [[characteristic polynomial of $T$|0BZ81AJNWF]], $p_T(t) = p_A(t) = \det(t I_n - A)$.
3. By the theorem on the [[coefficients of the characteristic polynomial|0FRYPZ6D0X]], $p_A(t) = t^n - (\tr A)\, t^{n-1} + \cdots$. So $p_T$ has leading coefficient $1$ and [[degree|0DPF6WRZW6]] $n \ge 1$.
4. The field $F$ is [[algebraically closed|02SJG1HC32]], so $p_T$ has a [[root|00EHX6FWC0]] $\lambda \in F$. That is, $p_T(\lambda) = 0$.
5. By the theorem that [[eigenvalues are the roots of the characteristic polynomial|053QVHF6N7]], $\lambda$ is an [[eigenvalue|0ZND7NQ970]] of $T$.

## Idea

The characteristic polynomial of $T$ has degree $\dim V$, which is at least $1$.
Over an algebraically closed field such a polynomial has a root, and each root is an eigenvalue.

## Variants

- [[Axler's proof|6TPH8WGRJJ]] avoids determinants. It factors a polynomial that kills one vector.
- For $F = \C$, step 4 is the [[fundamental theorem of algebra|0JP0W07Y9A]].
