---
tag: 0KN7EPH7Z0
kind: concept
name: Restriction and quotient operators
msc: ["15A04", "47A15"]
topics: [Z6S6PWMJPH]
audience: ug1
uses: [0ACX5QT8TE, 0BR3FY5Q8M, 0N4F5FMQZW]
sources:
  - url: https://en.wikipedia.org/wiki/Invariant_subspace
    locator: For a single operator
  - book: isbn:9783031410253
    locator: Chapter 5
  - book: isbn:9780135367971
    locator: Section 6.4
---

## Summary

An invariant subspace $U$ splits one linear map into two smaller ones: the map inside $U$, and the map on what is left once $U$ is ignored.
The second piece lives on the quotient space $V / U$, and together the two pieces carry all the eigenvalues of the original map.
Let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]] of a vector space $V$ over a field $F$, and let $U$ be a $T$-[[invariant subspace|0ACX5QT8TE]].
The *restriction* of $T$ to $U$ and the *quotient operator* on the [[quotient space|0BR3FY5Q8M]] are
$$T|_U \colon U \to U, \quad u \mapsto T(u), \qquad \bar T \colon V / U \to V / U, \quad v + U \mapsto T(v) + U.$$
The [[definition|0PFPWKBDTJ]] states both formally, and both make sense exactly because $T(U) \subseteq U$.
When $V$ has finite dimension, the [[block triangular form|ENVF51H5S3]] gives $p_T = p_{T|_U} \cdot p_{\bar T}$ for the characteristic polynomials.

## Motivation

Many theorems about a linear map are proved by induction on the dimension of $V$.
The induction needs two smaller maps to which the hypothesis can be applied, and an invariant subspace provides them.
The restriction is the obvious first piece.
The second piece is less obvious, because $U$ usually has no invariant complement inside $V$, so the rest of the map cannot be found as a map on a subspace.
The quotient space $V / U$ is the place where the rest of the map lives without any choice.

This pattern proves [[triangularization|0363JMQ42Y]]: find one eigenvector, pass to the quotient by its line, and repeat.
The same steps prove [[simultaneous triangularization|42PG67Q5YN]] of commuting maps over $\C$.
The pattern returns in the theory of group representations, where a representation with an invariant subspace is studied through its subrepresentation and its quotient.

## Notation

We write $T|_U$ or $T_U$ for the restriction, and $\bar T$, $T_{V/U}$ or $T/U$ for the quotient operator, which some books call the *induced map*.
With the [[quotient map|0N4F5FMQZW]] $\pi \colon V \to V / U$, the quotient operator is the unique linear map with $\bar T \circ \pi = \pi \circ T$.
In Mathlib, the restriction is `LinearMap.restrict` and the quotient operator is `Submodule.mapQ`.

## Remarks

### A worked example

Let $A = \begin{pmatrix} 1 & 2 & 5 \\ 2 & 1 & 7 \\ 0 & 0 & 4 \end{pmatrix}$ act on $\R^3$, and let $U = \operatorname{span}(e_1, e_2)$.
The plane $U$ is invariant, since $A e_1 = (1, 2, 0)$ and $A e_2 = (2, 1, 0)$ lie in it.
The restriction has the upper left block as its matrix, and its characteristic polynomial is
$$\det \begin{pmatrix} t - 1 & -2 \\ -2 & t - 1 \end{pmatrix} = (t - 1)^2 - 4 = (t - 3)(t + 1).$$
The quotient $\R^3 / U$ has the basis $e_3 + U$, and $A e_3 + U = (5, 7, 4) + U = 4 e_3 + U$, because $(5, 7, 0) \in U$.
So $\bar A$ is multiplication by $4$, and $p_A(t) = (t - 3)(t + 1)(t - 4)$ without any $3 \times 3$ determinant.
The [[full example|D59VWM8NX7]] also finds the eigenvectors.

### Why invariance is needed

The restriction needs $T(u) \in U$ to be a map from $U$ to $U$ at all.
The quotient operator needs more thought, because a coset $v + U$ has many representatives.
If $v + U = v' + U$, then $v - v' \in U$, so $T(v) - T(v') = T(v - v') \in U$, and the two representatives give the same coset $T(v) + U$.
That last step used $T(U) \subseteq U$.
For the map $T(x, y) = (x, x + y)$ and the line $U = \R e_1$, the representatives $0$ and $e_1$ of the same coset give the different cosets $U$ and $e_2 + U$, so the [[rule defines no map|B448MTVVJW]].

### The rules you can use

Both maps are linear, and $\pi \circ T = \bar T \circ \pi$ by the definition.
In a basis of $V$ that starts with a basis of $U$, the matrix of $T$ is $\begin{pmatrix} A & B \\ 0 & C \end{pmatrix}$, where $A$ is the matrix of $T|_U$ and $C$ is that of $\bar T$.
The determinant of a block triangular matrix is the product of the diagonal blocks, so $p_T = p_{T|_U}\, p_{\bar T}$ and $\det T = \det(T|_U) \det \bar T$.
Every eigenvalue of $T|_U$ or of $\bar T$ is therefore an eigenvalue of $T$.

Polynomials pass to both pieces: $p(T)|_U = p(T|_U)$ and $\overline{p(T)} = p(\bar T)$.
So $m_T(T|_U) = 0$ and $m_T(\bar T) = 0$, and the [[minimal polynomials|03NDVCSHSB]] of both pieces divide $m_T$.
With the [[minimal polynomial criterion|0MPAJRB23T]], this shows that the restriction and the quotient of a [[diagonalizable|07SQCNV233]] map are diagonalizable.

### Three small cases

If $U = \ker T$, then $T|_U = 0$.
If $U = V$, then $T|_U = T$ and $V / U$ is the zero space, whose characteristic polynomial is $1$.
If $U = E_\lambda$ is an eigenspace, then $T|_U = \lambda \id_U$.
For the [[derivative on cubic polynomials|7DGJWWZ8DW]] with $U$ the polynomials of degree at most $1$, the restriction has the matrix $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and the quotient has $\begin{pmatrix} 0 & 3 \\ 0 & 0 \end{pmatrix}$, so both pieces are nilpotent.

### Watch out

An eigenvector of $\bar T$ need not come from an eigenvector of $T$ in the same coset.
Take $T = \begin{pmatrix} 3 & 1 \\ 0 & 3 \end{pmatrix}$ and $U = \R e_1$.
The quotient sends $e_2 + U$ to $(1, 3) + U = 3 e_2 + U$, so $e_2 + U$ is an eigenvector of $\bar T$.
But the only eigenvectors of $T$ are the multiples of $e_1$, and none of them lies in the coset $e_2 + U$.
All that $\bar T(v + U) = \lambda (v + U)$ tells you is that $T(v) - \lambda v \in U$.

A second trap is to replace $V / U$ by a complement $W$ of $U$ and $\bar T$ by "$T$ on $W$".
When $W$ is not invariant, $T$ does not map $W$ to $W$.
The correct model of $\bar T$ on $W$ is "apply $T$, then project onto $W$ along $U$", because $w \mapsto w + U$ is an isomorphism from $W$ to $V / U$.

### Try it

First, for $A = \begin{pmatrix} 1 & 4 \\ 0 & 2 \end{pmatrix}$ and $U = \R e_1$, find the restriction and the quotient operator.
The restriction is multiplication by $1$, since $A e_1 = e_1$, and the quotient is multiplication by $2$, since $A e_2 = (4, 2) = 4 e_1 + 2 e_2$.

Second, show that $\bar T = 0$ exactly when $\operatorname{im} T \subseteq U$.
The condition $\bar T(v + U) = T(v) + U = U$ for all $v$ says that $T(v) \in U$ for all $v$.

## Explanations

### L1 human

Suppose a map keeps a smaller room $U$ of a house inside itself.
Then we can watch the map inside the room only, and this is the restriction.
We can also watch the map from far away, so that the whole room looks like a single point, and this is the quotient operator.
For the floor $z = 0$ of space, the restriction sees only the floor, and the quotient sees only the height.
Together, the two views tell us all the stretch factors of the map.

### L2 human

Here is a typical problem: find the characteristic polynomial and the eigenvalues of $T(x, y) = (x + 2y, 3y)$ on $\R^2$ by using the line $U = \R e_1$.
Since $T(e_1) = e_1$, the line is invariant and $T|_U = \id_U$, with characteristic polynomial $t - 1$.
The quotient $\R^2 / U$ has the basis $e_2 + U$, and
$$\bar T(e_2 + U) = (2, 3) + U = 3 e_2 + U,$$
because $(2, 0) \in U$.
So $\bar T$ is multiplication by $3$, and $p_T(t) = (t - 1)(t - 3)$.
The eigenvalue $3$ of $T$ has the eigenvector $(1, 1)$, since $T(1, 1) = (3, 3)$, and $(1, 1)$ lies in the coset $e_2 + U$.
This is the typical use: two small problems replace one large one, which is the engine of proofs by induction on the dimension.
Watch out: $e_2$ itself is not an eigenvector, since $T(e_2) = (2, 3)$.

### L3 human

The sequence $0 \to U \to V \to V / U \to 0$ is a short exact sequence of $F[x]$-modules, and $T|_U$ and $\bar T$ are the actions of $x$ on the submodule and on the quotient.
The characteristic polynomial is multiplicative on short exact sequences, as the determinant is, so along a composition series it is the product of the characteristic polynomials of the simple factors.
The same pattern appears for representations of groups and of Lie algebras, where problems are reduced to irreducible pieces, as in the proof of [[Lie's theorem|11K6SVNXMH]].
