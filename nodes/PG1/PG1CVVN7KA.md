---
tag: PG1CVVN7KA
kind: statement
role: theorem
name: Bruhat decomposition of a Lie group
msc: ["22E46", "22E15"]
uses: [XJS07AJ50Y, 4YDR9Q36DS, Z2FEBW5MQM, T91E86D0RH]
about: [XJS07AJ50Y, Z2FEBW5MQM]
sources:
  - url: https://en.wikipedia.org/wiki/Bruhat_decomposition
---

## Statement

Let $G$ be a connected [[semisimple Lie group|XJS07AJ50Y]] with finite center, with an [[Iwasawa decomposition|4YDR9Q36DS]] $G = KAN$ and Lie algebra $\mathfrak{a}$ of $A$.
Let $M = Z_K(\mathfrak{a})$ and $M' = N_K(\mathfrak{a})$ be the centralizer and the normalizer of $\mathfrak{a}$ in $K$, and let $W = M'/M$ be the restricted [[Weyl group|YT1ZJ2S4EE]].
Let $P = MAN$ be the minimal [[parabolic subgroup|Z2FEBW5MQM]].
For $w \in W$, the double coset $P \tilde w P$ does not depend on the representative $\tilde w \in M'$ of $w$, and it is written $PwP$.
Then $G$ is the disjoint union
$$G = \bigsqcup_{w \in W} PwP.$$

## Remarks

The coset $P \tilde w P$ does not depend on $\tilde w$ because two representatives differ by an element of $M \subseteq P$.
A standard proof follows the algebraic case, with the minimal parabolic subgroup in place of a Borel subgroup.
Disjointness uses that $W$ acts simply transitively on the positive systems of restricted roots.

Example: $G = \mathrm{SL}_2(\R)$, where $P$ is the group of upper triangular matrices and $W = \set{1, s}$ with $s$ represented by $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.
A matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ lies in $P$ when $c = 0$ and in $PsP$ when $c \ne 0$.
So $\mathrm{SL}_2(\R) = P \sqcup PsP$.

The [[Bruhat decomposition for reductive algebraic groups|T91E86D0RH]] over an algebraically closed field is the analogue with a Borel subgroup in place of $P$.
For a real group, $W$ is the Weyl group of the restricted root system, which can be smaller than the Weyl group of the complexified group.

## Explanations

### L1 human

The group is cut into finitely many pieces, one for each element of a finite group $W$.
Each piece is a set of the form $PwP$, where $P$ is the minimal parabolic subgroup.
For $2 \times 2$ real matrices of determinant $1$, there are two pieces: the upper triangular matrices, and all the others.

### L2 human

Passing to the flag manifold $G/P$, the decomposition says that $P$ has finitely many orbits on $G/P$, one for each $w \in W$.
The orbit of the longest element of $W$ is open and dense, and its complement has lower dimension.
This open orbit is used to realize principal series representations on functions on $N^- = \theta(N)$.
