---
tag: Z46WD9W1ZS
kind: statement
role: theorem
name: A matrix ring over a field has no nontrivial two-sided ideals
msc: ["16S50", "16D25"]
topics: [Y1ESNQ2V52]
audience: ug2
about: [AB2MD5CD13, 62M0NC3E2T]
uses: [0CD87SFM2N, 4H93XF4RVH, 04C5ZBG1WT]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_ring
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Simple_ring
    locator: Examples
---

## Statement

A two-sided ideal of a matrix ring over a field that contains one nonzero matrix contains every matrix.
Exactly: let $F$ be a [[field|04C5ZBG1WT]], or more generally a division ring, and let $n \ge 1$.
Then the only [[two-sided ideals|0CD87SFM2N]] of $M_n(F)$ are $\{0\}$ and $M_n(F)$.
So $M_n(F)$ is a [[simple ring|62M0NC3E2T]].

## Remarks

### A small case by hand

Take $n = 2$, and let $J$ be a two-sided ideal of $M_2(F)$ that contains $A = \begin{pmatrix} 0 & 0 \\ 3 & 0 \end{pmatrix}$, where $3 \ne 0$ in $F$.
Multiplying on both sides by [[matrix units|4H93XF4RVH]] gives
$$E_{12} A E_{11} = \begin{pmatrix} 3 & 0 \\ 0 & 0 \end{pmatrix}, \qquad E_{22} A E_{12} = \begin{pmatrix} 0 & 0 \\ 0 & 3 \end{pmatrix},$$
and both products lie in $J$.
Their sum is $3I$, and $\tfrac{1}{3}I \cdot 3I = I$, so $I \in J$.
Then $B = BI \in J$ for every $B$, and $J$ is the whole ring.
The [[proof|WT1K215XK5]] does the same with any nonzero entry in any size.

### Why each hypothesis is needed

The division by a nonzero entry needs a field or a division ring.
Over $\mathbb{Z}$, the matrices with even entries form the set $M_n(2\mathbb{Z})$, a proper nonzero two-sided ideal of $M_n(\mathbb{Z})$, and $2$ has no inverse.
The ideal must also be two-sided.
In $M_2(F)$ the matrices whose second column is zero form a left ideal, since $B A$ has second column $B$ times the second column of $A$, which is zero.
This left ideal is neither $\{0\}$ nor $M_2(F)$.

### Consequences

Every ring homomorphism from $M_n(F)$ to another ring is either $0$ or injective, since its kernel is a two-sided ideal.
For $n \ge 2$ there is no ring homomorphism with $1 \mapsto 1$ from $M_n(F)$ to a nonzero commutative ring.
Its kernel would be a proper ideal, hence $\{0\}$, and then $M_n(F)$ would be isomorphic to a subring of a commutative ring, which it is not.
The matrices of [[trace|0XC1RDBY7A]] zero are closed under addition but do not form a two-sided ideal: $E_{12}$ has trace $0$, while $E_{21} E_{12} = E_{22}$ has trace $1$.

### Generalizations

For any ring $R$ with identity, the two-sided ideals of $M_n(R)$ are exactly the sets $M_n(I)$ for the two-sided ideals $I$ of $R$.
So $M_n(R)$ is simple [[whenever R is simple|J41Y7CCE6B]].
In the other direction, the Wedderburn-Artin theorem says that every simple ring with the descending chain condition on left ideals is isomorphic to some $M_n(D)$ with $D$ a division ring.

## Explanations

### L1 human

An ideal is a set of matrices that is closed under addition, and under multiplication by any matrix on the left or on the right.
The theorem says: over a field, if such a set contains one nonzero matrix, then it contains every matrix.
So the only ideals are the set with just the zero matrix and the set of all matrices.

### L2 human

The [[proof|WT1K215XK5]] uses the matrix units as tools.
Multiplying a nonzero matrix on the left and on the right by matrix units cuts out one nonzero entry and moves it to any position.
Dividing by that entry gives every matrix unit, and the diagonal matrix units add up to the identity.
The typical use is to show that a ring homomorphism out of $M_n(F)$ is injective as soon as it is not zero.
Watch out: the theorem is about two-sided ideals only, and $M_n(F)$ has many one-sided ideals for $n \ge 2$.

### L3 human

The left ideals of $M_n(F)$ are the sets $\{ A : \ker A \supseteq W \}$ for subspaces $W$ of $F^n$, so they correspond to the subspaces of $F^n$.
Every module over $M_n(F)$ is a direct sum of copies of the column space $F^n$, so $M_n(F)$ is semisimple with one simple module up to isomorphism.
For a general ring $R$, the correspondence $I \mapsto M_n(I)$ between the ideals of $R$ and of $M_n(R)$ is one case of the [[Morita equivalence|JEBXXWHW8M]] of $R$ and $M_n(R)$.
