---
tag: 5NNPBFQA02
kind: example
name: Compact symplectic group
msc: ["22E15", "22C05", "20G20"]
instance_of: [9TFC6ADC1C]
uses: [X12FS2JAP0, 0R9R0Y1HDK, 0GE4DVQKR8, E5P8AG6CK7]
sources:
  - url: https://en.wikipedia.org/wiki/Symplectic_group
    locator: Sp(n)
---

## Example

Let $n \ge 1$ and let $\mathbb{H}$ be the [[quaternions|0GE4DVQKR8]].
For a quaternionic matrix $A \in M_n(\mathbb{H})$, let $A^*$ be its quaternionic conjugate transpose.
The *compact symplectic group* is
$$\mathrm{Sp}(n) = \set{A \in M_n(\mathbb{H}) : A^* A = I_n},$$
the group of $\mathbb{H}$-linear maps of $\mathbb{H}^n$ that preserve the quaternionic inner product $\ip{x}{y} = \sum_k \bar{x}_k y_k$.
It is also called the quaternionic unitary group.

For $n = 1$, the condition reads $\bar{q} q = 1$, so $\mathrm{Sp}(1)$ is the group of unit quaternions, which is isomorphic to [[SU(2)|E5P8AG6CK7]].

Writing $\mathbb{H}^n = \C^{2n}$ turns $\mathrm{Sp}(n)$ into a group of complex $2n \times 2n$ matrices, and then
$$\mathrm{Sp}(n) = \mathrm{Sp}(2n, \C) \cap U(2n),$$
the intersection of the complex [[symplectic group|X12FS2JAP0]] with the [[unitary group|0R9R0Y1HDK]].
This is a closed and bounded subgroup of $GL_{2n}(\C)$, so $\mathrm{Sp}(n)$ is a [[compact Lie group|9TFC6ADC1C]].

## Remarks

$\mathrm{Sp}(n)$ is connected and simply connected, and its real dimension is $n(2n + 1)$.
Its Lie algebra is simple of type $C_n$.
It is a maximal compact subgroup of $\mathrm{Sp}(2n, \C)$.
The maximal compact subgroup of the real group $\mathrm{Sp}(2n, \R)$ is different: it is isomorphic to $U(n)$.
The notation $\mathrm{Sp}(n)$ for this group clashes with the notation $\mathrm{Sp}(2n)$ for the noncompact symplectic groups, and some authors write $\mathrm{Sp}(2n)$ or $USp(2n)$ for it.

## Explanations

### L1 human

The compact symplectic group plays for the quaternions the role that the orthogonal group plays for the real numbers and the unitary group plays for the complex numbers.
It collects the quaternionic matrices that keep the length of every vector.
For $n = 1$ it is the set of quaternions of length $1$, which is a $3$-sphere.
Together with the special orthogonal and special unitary groups it gives the infinite families of compact simple Lie groups.
