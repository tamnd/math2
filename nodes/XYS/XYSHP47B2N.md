---
tag: XYSHP47B2N
kind: statement
role: theorem
name: Cauchy's stress theorem
msc: [74A10]
uses: [HXGCGHS070, KG2XWEMJ30, SBCV6VZG6D, 0NRYHJPQG2]
about: [KG2XWEMJ30]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy_stress_tensor
---

## Statement

Let a body occupy an open set $\Omega \subseteq \R^3$ at a fixed time, with mass density $\rho$, acceleration $a$ and body force per unit mass $b$.
Assume that $\rho a$ and $\rho b$ are bounded on $\Omega$.
Let $t \colon \Omega \times S^2 \to \R^3$ be a traction field of [[stress|HXGCGHS070]] that is continuous in $x$ for each unit vector $n$.
Suppose that the balance of linear momentum of [[Euler's laws of motion|SBCV6VZG6D]] holds for every part $P$ of the body with $\overline{P} \subset \Omega$.
With $n(x)$ the outward unit normal of $\partial P$, this means the following.
$$\int_{\partial P} t(x, n(x))\, dA + \int_P \rho b\, dV = \int_P \rho a\, dV.$$
Then:

1. $t(x, -n) = -t(x, n)$ for all $x$ and $n$;
2. for each $x \in \Omega$ there is a unique [[linear map|0NRYHJPQG2]] $\sigma(x)$, the [[Cauchy stress tensor|KG2XWEMJ30]], with $t(x, n) = \sigma(x)\, n$ for all unit vectors $n$;
3. if moreover $\sigma$ is $C^1$, $\rho$, $a$ and $b$ are continuous, and angular momentum is balanced for every such part, then each $\sigma(x)$ is symmetric.

## Remarks

For parts 1 and 2 one applies the balance law to small regions, where the volume terms are of higher order and drop out.
A thin flat box gives part 1.
A small tetrahedron with three faces on the coordinate planes gives $t(x, n) = \sum_j n_j\, t(x, e_j)$, which is part 2.
For part 3 one inserts $t = \sigma n$ into the balance of angular momentum and uses the divergence theorem and the local balance of linear momentum.
What remains is that the skew part of $\sigma$ vanishes.
For example, in a fluid at rest the theorem gives $\sigma = -p I$ once one knows that the traction is normal to every surface.
Without the balance of angular momentum, as in polar continua with couple stresses, $\sigma$ need not be symmetric.

## Explanations

### L1 human

The forces on cuts through a point in all directions are not independent.
Knowing them on three perpendicular cuts determines them on every cut, and the rule is linear.
This is why stress at a point is a $3 \times 3$ matrix.

### L2 human

The theorem turns Cauchy's postulate on tractions into the tensor $\sigma$ that appears in all field equations.
With it, the integral balance of linear momentum becomes the Cauchy momentum equation $\rho a = \operatorname{div} \sigma + \rho b$.
Symmetry of $\sigma$ means that at each point there are three perpendicular directions on which the stress is purely normal, the principal directions.
