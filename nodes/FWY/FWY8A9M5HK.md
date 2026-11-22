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

An eigenvalue never has more independent eigenvectors than the number of times it is a root of the characteristic polynomial, and it always has at least one.
Let $F$ be a field, let $V$ be a vector space over $F$ with $n = \dim V \ge 1$ finite, and let $T \colon V \to V$ be a linear map.
Let $\lambda \in F$ be an [[eigenvalue|0BQAA2BK3Q]] of $T$, and let $m$ be its [[algebraic multiplicity|0FY42N02DV]], its multiplicity as a root of the characteristic polynomial $p_T$.
Then the [[eigenspace|0G0RFPG8HR]] $E_\lambda = \ker(T - \lambda \operatorname{id}_V)$ satisfies
$$1 \le \dim E_\lambda \le m.$$
So the [[geometric multiplicity|099TWVJ909]] of $\lambda$ lies between $1$ and its algebraic multiplicity.
The same holds for an $n \times n$ matrix $A$ over $F$, with $E_\lambda = \ker(A - \lambda I)$.

## Remarks

### Three small cases

The theorem allows every value between the bounds, and small matrices show the cases.
For the [[3 by 3 matrix with 4 on the diagonal and 1 elsewhere|7XFGVVTZ2X]], the eigenvalue $3$ has $m = 2$, and $A - 3I$ has rank $1$, so $\dim E_3 = 2$: the upper bound is reached.
For the [[shear|HTAWRAC3QE]] $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, the eigenvalue $1$ has $m = 2$, and $A - I$ has rank $1$, so $\dim E_1 = 1$: the bound is strict.
For a simple eigenvalue, with $m = 1$, both bounds meet and $\dim E_\lambda = 1$.

### Why each hypothesis is needed

The scalar $\lambda$ must be an eigenvalue for the lower bound.
For a scalar that is not an eigenvalue, $E_\lambda = 0$ and $m = 0$, so the upper bound $0 \le 0$ still holds but $1 \le 0$ fails.

The space must be finite-dimensional, because $p_T$ and $m$ exist only then.
On the space of polynomials, the derivative $D$ has $\ker D$ equal to the constants, so $\dim E_0 = 1$, but there is no characteristic polynomial to compare with.

### What it gives you

The theorem turns diagonalization into a count.
If $p_T$ splits, the algebraic multiplicities add up to $n$, and the geometric ones add up to at most $n$.
So $T$ is [[diagonalizable|07SQCNV233]] if and only if $\dim E_\lambda = m(\lambda)$ for every eigenvalue.
Only the eigenvalues with $m \ge 2$ need a check, because a simple eigenvalue always has $\dim E_\lambda = 1 = m$.
In particular, an $n \times n$ matrix with $n$ distinct eigenvalues is diagonalizable.

### The converse

Every pair of numbers $1 \le g \le m$ occurs.
Take the block diagonal matrix with one Jordan block of size $m - g + 1$ for $\lambda$ and $g - 1$ blocks $(\lambda)$ of size $1$.
Its characteristic polynomial is $(t - \lambda)^m$, and each block gives exactly one independent eigenvector, so $\dim E_\lambda = g$.
For $m = 3$ and $g = 2$ this is $\begin{pmatrix} \lambda & 1 & 0 \\ 0 & \lambda & 0 \\ 0 & 0 & \lambda \end{pmatrix}$.

### Generalizations

The algebraic multiplicity is the dimension of the generalized eigenspace $\ker(T - \lambda \operatorname{id}_V)^n$, which contains $E_\lambda$; the [[decomposition into generalized eigenspaces|0Z3GDY89T5]] proves this.
That gives a second view of the upper bound, as the inclusion of a subspace in a larger one.

## History

The inequality is the core of the usual test for diagonalizability, and textbooks such as Friedberg, Insel and Spence prove it with a basis that starts with a basis of the eigenspace, as in the [[proof by an adapted basis|M60QTW5EBV]].

## Explanations

### L1 human

The algebraic multiplicity counts how many times $\lambda$ is a root of the characteristic polynomial.
The geometric multiplicity counts how many independent arrows the map stretches by $\lambda$.
The theorem says that the second number is at least $1$ and never more than the first.
For the shear of the plane, the root $1$ counts twice, but only one direction is stretched by $1$.

### L2 human

Here is a typical check, for the [[3 by 3 defective example|18XQY67HMS]]:
$$A = \begin{pmatrix} 1 & 1 & 0 \\ -1 & 3 & 0 \\ -1 & 1 & 1 \end{pmatrix}.$$
Expand $\det(tI - A)$ along the third column, whose only nonzero entry is $t - 1$:
$$p_A(t) = (t - 1)\big((t - 1)(t - 3) + 1\big) = (t - 1)(t^2 - 4t + 4) = (t - 1)(t - 2)^2.$$
So $m(2) = 2$ and $m(1) = 1$.
The matrix $A - 2I$ has the rows $(-1, 1, 0)$, $(-1, 1, 0)$ and $(-1, 1, -1)$, of rank $2$, so $\dim E_2 = 1$.
The matrix $A - I$ has the rows $(0, 1, 0)$, $(-1, 2, 0)$ and $(-1, 1, 0)$, of rank $2$, so $\dim E_1 = 1$.
Both bounds hold, $1 \le 1 \le 2$ and $1 \le 1 \le 1$, and $A$ is not diagonalizable, since $\dim E_2 < 2$.
Watch out: the theorem gives only an inequality, and equality is a special property that you must check.

### L3 human

In the [[Jordan normal form|085HQ5G5TE]], $\dim E_\lambda$ is the number of Jordan blocks for $\lambda$, and $m$ is their total size, so the inequality says that each block has size at least $1$.
In module language, $E_\lambda$ is the part of the $(x - \lambda)$-primary component killed by $x - \lambda$, and that part sits inside a component of dimension $m$.
The sub-areas on diagonalization and on canonical forms use the theorem in this form.
