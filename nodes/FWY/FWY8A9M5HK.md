---
tag: FWY8A9M5HK
kind: statement
role: theorem
name: Dimension of an eigenspace is at most the algebraic multiplicity
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug2
about: [099TWVJ909, 0FY42N02DV]
uses: [0ZND7NQ970, 0AYEPBQMAW, 0S7A0EMPF4, 06YSJVR356, 0BZ81AJNWF]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section4-2.xml#L797
    locator: src/section4-2.xml:797
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Eigenspaces, geometric multiplicity, and the eigenbasis
  - book: isbn:9780134860244
---

## Statement

Let $F$ be a field, let $V$ be a vector space over $F$ with $n = \dim V \ge 1$, and let $T \colon V \to V$ be a linear map.
Let $\lambda \in F$ be an [[eigenvalue|0BQAA2BK3Q]] of $T$, and let $m$ be its [[algebraic multiplicity|0FY42N02DV]], that is, its multiplicity as a root of the characteristic polynomial $p_T$.
Then the [[eigenspace|0G0RFPG8HR]] $E_\lambda$ satisfies
$$1 \leq \dim E_\lambda \leq m.$$
In words: the [[geometric multiplicity|099TWVJ909]] of an eigenvalue is at least $1$ and at most its algebraic multiplicity.
The same holds for an $n \times n$ matrix $A$ over $F$, with $E_\lambda = \ker(A - \lambda I)$.

## Remarks

### Why each hypothesis is needed

- $\lambda$ must be an eigenvalue for the lower bound. For a scalar that is not an eigenvalue, $E_\lambda = 0$ and $m = 0$.
- $V$ must be finite-dimensional, because $p_T$ and $m$ are defined only then.
- The upper bound can be strict: for the [[shear|~919ae3c7]], $\dim E_1 = 1 < 2 = m$.

### Consequences

- If $p_T$ splits, then $T$ is [[diagonalisable|07SQCNV233]] if and only if $\dim E_\lambda = m(\lambda)$ for every eigenvalue $\lambda$.
- A simple eigenvalue, with $m = 1$, has a one-dimensional eigenspace.
- So an $n \times n$ matrix with $n$ distinct eigenvalues has $n$ eigenspaces of dimension $1$ and is diagonalisable.

### Converse

Every pair $1 \le g \le m$ occurs: the block diagonal matrix with one Jordan block of size $m - g + 1$ for $\lambda$ and $g - 1$ blocks $(\lambda)$ of size $1$ has geometric multiplicity $g$ and algebraic multiplicity $m$.

### Generalizations

The algebraic multiplicity is the dimension of the [[generalised eigenspace|0Z3GDY89T5]], which contains $E_\lambda$.
This gives a second view of the upper bound.

## History

This inequality is part of the standard criterion for diagonalisability, found in linear algebra textbooks such as Friedberg, Insel and Spence.

## Explanations

### L1 human

The algebraic multiplicity counts how many times $\lambda$ is a root of the characteristic polynomial.
The geometric multiplicity counts how many independent eigenvectors belong to $\lambda$.
The second number is at least $1$ and never more than the first.
When it is smaller, the map cannot be diagonalised.

### L2 human

We check the theorem for $A = \begin{pmatrix} 1 & 1 & 0 \\ -1 & 3 & 0 \\ -1 & 1 & 1 \end{pmatrix}$, studied in the [[3 by 3 defective example|~5db5cf19]].

1. $p_A(t) = (t - 1)(t - 2)^2$, so $m(2) = 2$ and $m(1) = 1$.
2. $A - 2I$ has the rows $(-1, 1, 0)$, $(-1, 1, 0)$ and $(-1, 1, -1)$, of rank $2$. So $\dim E_2 = 1$.
3. $A - I$ has the rows $(0, 1, 0)$, $(-1, 2, 0)$ and $(-1, 1, 0)$, of rank $2$. So $\dim E_1 = 1$.
4. So $1 \le 1 \le 2$ and $1 \le 1 \le 1$, as the theorem says.

The typical use is the test for diagonalisability: only eigenvalues with $m \ge 2$ need a check.
A trap: the theorem does not say that $\dim E_\lambda = m$; equality is a special property.

### L3 human

In the [[Jordan normal form|085HQ5G5TE]], $\dim E_\lambda$ is the number of Jordan blocks for $\lambda$, and $m$ is their total size.
So the inequality says that each block has size at least $1$.
