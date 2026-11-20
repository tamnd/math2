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

Let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]] of a vector space $V$ over a field $F$, and let $U$ be a $T$-[[invariant subspace|0ACX5QT8TE]].
The *restriction* of $T$ to $U$ is the map $T|_U \colon U \to U$, $u \mapsto T(u)$.
The *quotient operator* (or *induced map*) is $\bar T \colon V / U \to V / U$, $v + U \mapsto T(v) + U$, on the [[quotient space|0BR3FY5Q8M]].
Both are well defined exactly because $T(U) \subseteq U$.
In finite dimension, the matrix of $T$ in a basis adapted to $U$ is block upper triangular with diagonal blocks $T|_U$ and $\bar T$, and the characteristic polynomial of $T$ is the product of theirs.
These two smaller maps are the standard tools for proofs by induction on the dimension.

## Motivation

An invariant subspace $U$ cuts the problem of understanding $T$ into two smaller problems.
The first is how $T$ acts inside $U$, which is the restriction.
The second is how $T$ acts on what is left over when $U$ is ignored, which is the quotient operator.
In general $U$ has no invariant complement, so the second piece cannot live inside $V$, and the quotient space is its natural home.
Triangularization, the existence of a common eigenvector and many other results are proved by passing to $U$ and to $V / U$ and using induction.

## Notation

We write $T|_U$ or $T_U$ for the restriction, and $\bar T$, $T_{V/U}$ or $T/U$ for the quotient operator.
With the [[quotient map|0N4F5FMQZW]] $\pi \colon V \to V / U$, the quotient operator is the unique linear map with $\bar T \circ \pi = \pi \circ T$.
In Mathlib, the restriction is `LinearMap.restrict` and the quotient operator is `Submodule.mapQ`.

## Remarks

### Examples

- For the [[derivative on cubic polynomials|~6463dbd0]] and $U$ the polynomials of degree at most $1$, both $D|_U$ and $\bar D$ are nilpotent $2 \times 2$ blocks.
- For a [[3 × 3 block triangular matrix|~27c38ea6]], the restriction to the plane $z = 0$ and the quotient operator give the factors $(t - 3)(t + 1)$ and $t - 4$ of the characteristic polynomial.
- If $U = \ker T$, then $T|_U = 0$. If $U = V$, then $T|_U = T$ and $V / U = 0$.
- If $U = E_\lambda$ is an eigenspace, then $T|_U = \lambda \id_U$.

### Non-examples

- For a [[subspace that is not invariant|~cdde18e6]], the rule $v + U \mapsto T(v) + U$ gives different values on two representatives of one coset, so it defines no map.
- The map $u \mapsto T(u)$ for $u \in U$ is always defined as a map $U \to V$, but it is an endomorphism of $U$ only when $U$ is invariant.

### Basic properties

- Both maps are linear, and $\pi \circ T = \bar T \circ \pi$.
- In a basis of $V$ that extends a basis of $U$, the matrix of $T$ is $\begin{pmatrix} A & B \\ 0 & C \end{pmatrix}$ with $A$ the matrix of $T|_U$ and $C$ that of $\bar T$, and $p_T = p_{T|_U} \, p_{\bar T}$, by the [[block triangular form|~955c2a39]].
- So each eigenvalue of $T|_U$ or of $\bar T$ is an eigenvalue of $T$, and $\det T = \det(T|_U) \det \bar T$.
- For each polynomial $p$, $p(T)|_U = p(T|_U)$ and $\overline{p(T)} = p(\bar T)$. So the [[minimal polynomials|03NDVCSHSB]] of $T|_U$ and $\bar T$ divide that of $T$.
- If $T$ is [[diagonalizable|07SQCNV233]], then so is $T|_U$, by the [[minimal polynomial criterion|0MPAJRB23T]].

### History

Restrictions to invariant subspaces are as old as the reduction theory of matrices of Jordan and Frobenius.
The quotient operator became a standard tool with the abstract treatment of vector spaces and modules in the twentieth century.

### Common errors

- Thinking that the eigenvectors of $\bar T$ are eigenvectors of $T$. An eigenvector $v + U$ of $\bar T$ gives $T(v) - \lambda v \in U$, not $T(v) = \lambda v$.
- Identifying $V / U$ with a complement $W$ of $U$ and $\bar T$ with $T|_W$. When $W$ is not invariant, $T|_W$ is not an endomorphism of $W$.
- Forgetting that the lower left block is zero only in a basis that starts with a basis of $U$.

## Explanations

### L1 human

Suppose a map keeps a smaller room $U$ of a house inside itself.
Then we can watch the map inside the room only: this is the restriction.
We can also watch the map from far away, so that the whole room looks like a single point: this is the quotient operator.
For the plane $z = 0$ in space, the restriction sees only the floor, and the quotient sees only the height.
Together, the two views tell us all the eigenvalues of the map.

### L2 human

Let $A = \begin{pmatrix} 1 & 2 & 5 \\ 2 & 1 & 7 \\ 0 & 0 & 4 \end{pmatrix}$ and $U = \operatorname{span}(e_1, e_2)$.

1. $U$ is invariant, since the third entries of $A e_1$ and $A e_2$ are $0$.
2. The restriction has the matrix $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$, with characteristic polynomial $(t - 3)(t + 1)$.
3. The quotient $\R^3 / U$ has the basis $e_3 + U$, and $A e_3 + U = (5, 7, 4) + U = 4 e_3 + U$. So $\bar A = (4)$.
4. Hence $p_A(t) = (t - 3)(t + 1)(t - 4)$.

The typical use is in a proof by induction: apply the induction hypothesis to $T|_U$ and to $\bar T$, then combine.
The trap is in step 3: $e_3$ is not an eigenvector of $A$, although $e_3 + U$ is an eigenvector of $\bar A$.

### L3 human

The sequence $0 \to U \to V \to V / U \to 0$ is a short exact sequence of $F[x]$-modules, and $T|_U$ and $\bar T$ are the actions of $x$ on the sub and on the quotient.
The characteristic polynomial is multiplicative on short exact sequences, as the determinant and the trace are.
So the characteristic polynomial factors through the Grothendieck group of finite-dimensional $F[x]$-modules.
The same pattern appears for representations of groups and Lie algebras, where composition series reduce problems to irreducible pieces, as in [[Lie's theorem|11K6SVNXMH]].
