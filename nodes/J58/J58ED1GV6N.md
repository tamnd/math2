---
tag: J58ED1GV6N
kind: example
name: SL(2,C)
msc: ["22E10", "22E46", "20G20"]
instance_of: [7JBRGCVJRB]
uses: [0V9PMN0RBH, 0J78KBPFZB, 0SG74WBFA2, E5P8AG6CK7, 0P17NGQQMQ]
sources:
  - url: https://en.wikipedia.org/wiki/Special_linear_group
---

## Example

The group $SL(2, \C)$ is the [[special linear group|0V9PMN0RBH]] of complex $2 \times 2$ matrices with determinant $1$:
$$SL(2, \C) = \set{\begin{pmatrix} a & b \\ c & d \end{pmatrix} : a, b, c, d \in \C, \ ad - bc = 1}.$$
It is cut out of $M_2(\C) = \C^4$ by the single polynomial equation $ad - bc = 1$, whose differential is nonzero at every solution.
So it is a complex [[Lie group|7JBRGCVJRB]] of complex dimension $3$, that is, of real dimension $6$.

It acts on the [[Riemann sphere|0J78KBPFZB]] $\C \cup \set{\infty}$ by [[Möbius transformations|0SG74WBFA2]] $z \mapsto (az + b)/(cz + d)$.
Check: the matrix $g$ acts as the identity map exactly when $(az + b)/(cz + d) = z$ for all $z$, which forces $b = c = 0$ and $a = d$, and then $ad = 1$ gives $g = \pm I$.
So the group of Möbius transformations is $PSL(2, \C) = SL(2, \C)/\set{\pm I}$.

## Remarks

Every $g \in SL(2, \C)$ has a unique polar decomposition $g = u p$ with $u \in$ [[SU(2)|E5P8AG6CK7]] and $p$ a positive definite [[Hermitian matrix|0P17NGQQMQ]] of determinant $1$.
These $p$ form a space homeomorphic to $\R^3$, so $SL(2, \C)$ is homeomorphic to $S^3 \times \R^3$.
Hence it is connected and simply connected, and $SU(2)$ is a maximal compact subgroup.
Its Lie algebra $\mathfrak{sl}(2, \C)$ is the complex simple Lie algebra of type $A_1$.
$SL(2, \C)$ acts on the Hermitian $2 \times 2$ matrices by $X \mapsto g X g^*$, preserving $\det X$, which is a quadratic form of signature $(1, 3)$.
This gives a double cover of the identity component of the Lorentz group, so $SL(2, \C)$ is the spin group $\mathrm{Spin}(1, 3)$.

## Explanations

### L1 human

$SL(2, \C)$ is the complex version of the group of $2 \times 2$ matrices with determinant $1$.
Each of its elements moves the points of the extended complex plane by a fractional linear map, and two matrices $g$ and $-g$ give the same map.
These maps send circles to circles, and they are exactly the orientation-preserving conformal symmetries of the sphere.
In physics the same group describes how spinors change under the rotations and boosts of special relativity.
