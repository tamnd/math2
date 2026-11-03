---
tag: ZKFN197MBR
kind: statement
role: proposition
name: Jacobi identity
msc: [17B01, 16W99]
uses: [0B1261B5ED, T2HH02QC2M]
about: [T2HH02QC2M]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobi_identity
---

## Statement

Let $R$ be a [[ring|0B1261B5ED]], not necessarily commutative.
For $x, y \in R$ let $[x, y] = xy - yx$ be their [[commutator|T2HH02QC2M]].
Then for all $x, y, z \in R$,
$$[x, [y, z]] + [y, [z, x]] + [z, [x, y]] = 0.$$

## Remarks

The proof is a direct expansion.
The term $[x, [y, z]]$ equals $xyz - xzy - yzx + zyx$.
In the cyclic sum, each of the six products of $x, y, z$ appears once with each sign.
So the sum is $0$.
For example, in the ring of $2 \times 2$ matrices with $x = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, $y = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$ and $z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$, the three terms are $2z$, $-2z$ and $0$.
The associativity of $R$ is used in this expansion.
In the [[octonions|1HRMT3DSX2]], which are not associative, the commutator does not satisfy the Jacobi identity.
The identity is the second axiom of a [[Lie algebra|5JJYBJ6A8K]], so every associative algebra becomes a Lie algebra under the commutator.
An equivalent form, given anticommutativity, is $[x, [y, z]] = [ [x, y], z] + [y, [x, z]]$: the map $[x, \cdot]$ is a derivation of the bracket.

## Explanations

### L1 human

The Jacobi identity is a rule about brackets of three elements.
Bracket $x$ with $[y, z]$, then rotate the letters and add the three results: the total is zero.
For matrices with $[A, B] = AB - BA$ it always holds, as a short computation shows.
The cross product of vectors in space obeys the same rule.

### L2 human

The identity replaces associativity in the theory of [[Lie algebras|5JJYBJ6A8K]].
It says that the adjoint map $y \mapsto [x, y]$ is a derivation, and that $x \mapsto [x, \cdot]$ preserves brackets.
This is why every Lie algebra acts on itself by the adjoint representation.
The same identity holds for the Lie bracket of vector fields and for the Poisson bracket of functions.
