---
tag: 2EPRMNK1G2
kind: example
name: List of simple Lie groups
msc: ["22E46", "22C05", "17B25"]
illustrates: [AM7YJP8AR6]
uses: [CZCWFPNS4N, JJSXXJQGEH, 5NNPBFQA02, YX5FFSCR8P, MKT1263M0A]
sources:
  - url: https://en.wikipedia.org/wiki/Simple_Lie_group
---

## Example

Every compact connected [[simple Lie group|AM7YJP8AR6]] is isomorphic to a quotient $\tilde{G}/C$.
Here $\tilde{G}$ is exactly one group of the following list, and $C$ is a subgroup of the centre of $\tilde{G}$.
Each $\tilde{G}$ is compact, connected and simply connected, and its centre is finite.

| Type | $\tilde{G}$ | Dimension | Centre |
|---|---|---|---|
| $A_n$, $n \ge 1$ | $SU(n+1)$ | $n(n+2)$ | $\Z/(n+1)$ |
| $B_n$, $n \ge 2$ | $\mathrm{Spin}(2n+1)$ | $n(2n+1)$ | $\Z/2$ |
| $C_n$, $n \ge 3$ | $\mathrm{Sp}(n)$ | $n(2n+1)$ | $\Z/2$ |
| $D_n$, $n \ge 4$ | $\mathrm{Spin}(2n)$ | $n(2n-1)$ | $\Z/4$ for $n$ odd, $\Z/2 \times \Z/2$ for $n$ even |
| $G_2$ | $G_2$ | $14$ | trivial |
| $F_4$ | $F_4$ | $52$ | trivial |
| $E_6$ | $E_6$ | $78$ | $\Z/3$ |
| $E_7$ | $E_7$ | $133$ | $\Z/2$ |
| $E_8$ | $E_8$ | $248$ | trivial |

Here $SU(n+1)$ is the [[special unitary group|CZCWFPNS4N]], $\mathrm{Spin}(m)$ is the [[spin group|JJSXXJQGEH]], and $\mathrm{Sp}(n)$ is the [[compact symplectic group|5NNPBFQA02]].
The groups [[G2|YX5FFSCR8P]] and [[E8|MKT1263M0A]] are the smallest and the largest exceptional groups.
The type is the type of the [[Dynkin diagram|CS73JZQS66]] of the Lie algebra, and $n$ is the rank.
Check of one row: $SU(n+1)$ has Lie algebra of trace-zero skew-Hermitian $(n+1) \times (n+1)$ matrices, of dimension $(n+1)^2 - 1 = n(n+2)$.

## Remarks

The bounds on $n$ avoid repetitions and non-simple cases: $\mathrm{Sp}(1) \cong \mathrm{Spin}(3) \cong SU(2)$, $\mathrm{Sp}(2) \cong \mathrm{Spin}(5)$, $\mathrm{Spin}(6) \cong SU(4)$, and $\mathrm{Spin}(4) \cong SU(2) \times SU(2)$ is not simple.
The first four rows are the classical families, and the last five are the exceptional groups.
For example, $SO(3) = SU(2)/\set{\pm I}$ is the quotient for $A_1$ with $C$ the whole centre.
The same list of types classifies the complex simple Lie algebras.
The noncompact simple Lie groups are classified through the real forms of these complex Lie algebras, a classification due to Élie Cartan.

## Explanations

### L1 human

There are only a few kinds of compact simple Lie groups.
Four infinite families come from matrices that preserve lengths over the real numbers, the complex numbers or the quaternions.
Besides them there are exactly five exceptional groups, of dimensions $14$, $52$, $78$, $133$ and $248$.
Every compact simple Lie group is one of these, possibly divided by a finite group of central elements.
