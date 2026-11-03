---
tag: W0KBNZBCRR
kind: statement
role: theorem
name: Toyoda–Bruck theorem
msc: [20N05, 20N02]
uses: [VZHN6GA3TA, 082GHNPJ53, DSQ17TNW1C]
about: [VZHN6GA3TA]
sources:
  - url: https://en.wikipedia.org/wiki/Medial_magma
---

## Statement

Let $(Q, \cdot)$ be a [[quasigroup|ZJD31SPPFP]].
Then $(Q, \cdot)$ is [[medial|VZHN6GA3TA]], that is, $(x \cdot y) \cdot (u \cdot v) = (x \cdot u) \cdot (y \cdot v)$ for all $x, y, u, v \in Q$, if and only if there exist:

1. an [[abelian group|082GHNPJ53]] structure $(Q, +)$ on the same set;
2. two [[automorphisms|DSQ17TNW1C]] $\varphi$ and $\psi$ of $(Q, +)$ with $\varphi \circ \psi = \psi \circ \varphi$;
3. an element $c \in Q$;

such that $x \cdot y = \varphi(x) + \psi(y) + c$ for all $x, y \in Q$.

## Remarks

The converse direction is a direct computation.
With $x \cdot y = \varphi(x) + \psi(y) + c$, the product $(x \cdot y) \cdot (u \cdot v)$ equals $\varphi^2(x) + \varphi\psi(y) + \psi\varphi(u) + \psi^2(v) + \varphi(c) + \psi(c) + c$.
Swapping $y$ and $u$ gives the same value because $\varphi\psi = \psi\varphi$, and the operation is a quasigroup because $\varphi$ and $\psi$ are bijective.
For the main direction, one fixes an element of $Q$ and defines a new addition on $Q$ from the quasigroup operation by an isotopy.
Mediality forces this addition to be associative and commutative, and the quasigroup operation then becomes affine in each argument.

Example: on $\Z/5\Z$ the operation $x \cdot y = 2x + 3y$ is a medial quasigroup, with $\varphi(x) = 2x$, $\psi(y) = 3y$ and $c = 0$.
Example: on $\Z/3\Z$ the operation $x \cdot y = -x - y$ is a medial quasigroup, with $\varphi = \psi = -\id$ and $c = 0$.

The quasigroup hypothesis is needed.
The commutative semigroup $(\N, \cdot)$ is medial, but it is not of this form.
In an operation $\varphi(x) + \psi(y) + c$ each map $y \mapsto x \cdot y$ is a bijection, while in $(\N, \cdot)$ the map $y \mapsto 0 \cdot y$ is constant.

## Explanations

### L1 human

A quasigroup is a set with an operation whose "multiplication table" is a Latin square: every element appears exactly once in each row and each column.
The theorem says that such an operation obeys the medial law only when it comes from an abelian group in a simple way.
One twists each argument by a symmetry of the group, adds, and shifts by a constant.
So a single identity forces the whole structure to be essentially linear.

### L2 human

The theorem is the main structure result for medial quasigroups.
It reduces questions about medial quasigroups to questions about abelian groups with two commuting automorphisms.
It is also called the Bruck–Murdoch–Toyoda theorem.
If the medial quasigroup is moreover idempotent, so that $x \cdot x = x$, then putting $x = 0$ gives $c = 0$, and then $\varphi + \psi = \id$.
Such quasigroups are the affine combinations $x \cdot y = \varphi(x) + (\id - \varphi)(y)$, as in the midpoint operation $(x + y)/2$ on $\Q$.
