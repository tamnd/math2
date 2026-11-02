---
tag: ZZYCV5EX9J
kind: example
name: Heisenberg group
msc: ["22E25", "20F18", "22E70"]
instance_of: [DK87YN458D]
uses: [0DZ93493VN, 0Q7MMQHC1P, 7JBRGCVJRB]
sources:
  - url: https://en.wikipedia.org/wiki/Heisenberg_group
same_as:
  wikidata: Q1601337
  wikipedia: Heisenberg group
---

## Example

The (real, three-dimensional) *Heisenberg group* $H$ is the group of real upper unitriangular $3 \times 3$ matrices
$$[a, b, c] = \begin{pmatrix} 1 & a & c \\ 0 & 1 & b \\ 0 & 0 & 1 \end{pmatrix}, \qquad a, b, c \in \R,$$
with matrix multiplication.
Multiplying out gives
$$[a, b, c]\,[a', b', c'] = [a + a', \ b + b', \ c + c' + a b'],$$
and $[a, b, c]^{-1} = [-a, -b, -c + ab]$.
So $H$ is $\R^3$ with a polynomial group law, a [[Lie group|7JBRGCVJRB]] of dimension $3$.

Check that $H$ is a [[nilpotent Lie group|DK87YN458D]].
The commutator of $g = [a, b, 0]$ and $g' = [a', b', 0]$ is $g g' g^{-1} g'^{-1} = [0, 0, ab' - a'b]$.
The [[centre|0DZ93493VN]] of $H$ is $Z = \set{[0, 0, c] : c \in \R}$, and all commutators lie in $Z$.
So the lower central series is $H \supset Z \supset \set{1}$, and $H$ is a [[nilpotent group|0Q7MMQHC1P]] of class $2$; it is not abelian.

## Remarks

$H$ is connected and simply connected, being homeomorphic to $\R^3$.
Its Lie algebra has a basis $X, Y, Z$ with $[X, Y] = Z$ and $[X, Z] = [Y, Z] = 0$.
This is the bracket relation of the position and momentum operators of quantum mechanics, up to a constant, which is the origin of the name.
More generally, for $n \ge 1$ the Heisenberg group $H_{2n+1}$ is $\R^n \times \R^n \times \R$ with the law $(x, y, c)(x', y', c') = (x + x', y + y', c + c' + x \cdot y')$, of dimension $2n + 1$.
The matrices $[a, b, c]$ with integer entries form a discrete subgroup $H(\Z)$, and the quotient $H / H(\Z)$ is compact.

## Explanations

### L1 human

The Heisenberg group is the simplest group that is almost, but not quite, commutative.
Two of its elements commute up to an extra shift in the third coordinate, and that shift itself commutes with everything.
In the matrix picture, multiplying two matrices adds the entries above the diagonal, except that the corner entry picks up an extra product $ab'$.
This small failure of commutativity is the algebraic shadow of the uncertainty principle in quantum mechanics.
