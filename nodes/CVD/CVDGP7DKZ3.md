---
tag: CVDGP7DKZ3
kind: statement
role: theorem
name: Local existence of harmonic conjugates
msc: [31A05]
uses: [0DEB0JMN0W, 050F2FMTKF, 0NAHXR1FRH, 0T71SSYZ39, 02AC7JR6G6, 0QW64ARSHB]
about: [050F2FMTKF, 0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_conjugate
---

## Statement

Let $U \subseteq \C$ be an open set and let $u \colon U \to \R$ be a [[harmonic function|0DEB0JMN0W]].
Let $D = \set{z \in \C : \abs{z - a} < r}$ be an open disc with $D \subseteq U$.
Then there is a [[holomorphic function|0NAHXR1FRH]] $f \colon D \to \C$ with $\operatorname{Re} f = u$ on $D$.
Its imaginary part $v = \operatorname{Im} f$ is a [[harmonic conjugate|050F2FMTKF]] of $u$ on $D$, and it is unique up to an additive real constant.

## Remarks

Proof idea: write $z = x + iy$ and set $g = u_x - i u_y$.
The equation $u_{xx} + u_{yy} = 0$ and the symmetry $u_{xy} = u_{yx}$ are exactly the [[Cauchy–Riemann equations|0T71SSYZ39]] for $g$, so $g$ is holomorphic on $U$.
A holomorphic function on a disc [[has a primitive|02AC7JR6G6]] $F$, and $F' = g$ gives $\nabla(\operatorname{Re} F) = \nabla u$.
So $\operatorname{Re} F - u$ is a real constant $c$ on $D$, and $f = F - c$ works.
The same proof works on every [[simply connected domain|0QW64ARSHB]] in place of the disc.
The result is local: on $U = \C \setminus \set{0}$ the function $u(z) = \log\abs{z}$ is harmonic.
On each disc that avoids $0$ it has the conjugate $v = \arg z$ for a continuous branch of the argument.
It has no harmonic conjugate on all of $U$, because no continuous argument exists on a circle around $0$.

## Explanations

### L1 human

A harmonic function in the plane looks like the real part of a holomorphic function.
This theorem says that this is always true, at least on small discs.
So questions about harmonic functions in two variables can often be turned into questions about holomorphic functions, where many tools are available.

### L2 human

The theorem lets one transfer results from complex analysis to planar harmonic functions.
For example, the mean value property and the maximum principle for $u$ follow from those for a local holomorphic $f$ with $\operatorname{Re} f = u$.
Globally, a harmonic conjugate exists exactly when the period $\oint (-u_y \, dx + u_x \, dy)$ vanishes on each closed curve in $U$.
These periods are the obstruction on multiply connected domains, as the example $\log\abs{z}$ shows.
