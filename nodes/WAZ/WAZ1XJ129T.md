---
tag: WAZ1XJ129T
kind: object
name: BPST instanton
msc: [81T13, 53C07, "58E15"]
instance_of: [YWBTGC7MFA]
uses: [FJVQH0VPN7, 0GE4DVQKR8, CZCWFPNS4N, NJ21PN5ZGJ, ZAJFW1S078, 1Y4WX4XQWJ]
sources:
  - url: https://en.wikipedia.org/wiki/BPST_instanton
same_as:
  wikidata: Q4836279
  wikipedia: BPST instanton
---

## Description

Identify $\R^4$ with the [[quaternions|0GE4DVQKR8]] $\mathbb{H}$, writing $x = x_0 + x_1 i + x_2 j + x_3 k$ and $\bar x$ for the conjugate.
Identify [[$SU(2)$|CZCWFPNS4N]] with the unit quaternions, so that its Lie algebra is the space $\operatorname{Im}\mathbb{H}$ of imaginary quaternions.
Fix a centre $a \in \mathbb{H}$ and a scale $\lambda > 0$.
The *BPST instanton* is the [[connection|NJ21PN5ZGJ]] on the trivial $SU(2)$-bundle over $\R^4$ given by the $\operatorname{Im}\mathbb{H}$-valued $1$-form
$$A = \operatorname{Im}\left( \frac{(\bar x - \bar a)\, dx}{\abs{x - a}^2 + \lambda^2} \right).$$
Its [[curvature|ZAJFW1S078]] is
$$F_A = dA + A \wedge A = \frac{\lambda^2 \, d\bar x \wedge dx}{\left(\abs{x - a}^2 + \lambda^2\right)^2}.$$

## Remarks

Check that it is an [[instanton|FJVQH0VPN7]]: expanding in coordinates, the $i$-component of $d\bar x \wedge dx$ is $2(dx_0 \wedge dx_1 - dx_2 \wedge dx_3)$, and the $j$- and $k$-components are $2(dx_0 \wedge dx_2 - dx_3 \wedge dx_1)$ and $2(dx_0 \wedge dx_3 - dx_1 \wedge dx_2)$.
Each of these $2$-forms is anti-self-dual for the [[Hodge star|1Y4WX4XQWJ]] of the orientation $dx_0 \wedge dx_1 \wedge dx_2 \wedge dx_3$, since $\star(dx_0 \wedge dx_1) = dx_2 \wedge dx_3$ and so on.
So $\star F_A = -F_A$.

The curvature decays like $\abs{x}^{-4}$, so the Yang–Mills action $\int_{\R^4} \abs{F_A}^2$ is finite.
By conformal invariance the connection extends to a bundle over the sphere $S^4$, and the instanton number of that bundle has absolute value $1$.
Up to gauge transformations, the parameters $(a, \lambda) \in \R^4 \times (0, \infty)$ describe all anti-self-dual connections of instanton number $1$ for this orientation.
The [[moduli space|VP5PW8VSHZ]] of these connections over $S^4$ is an open $5$-dimensional ball.
The scale $\lambda$ measures the size of the region where the curvature is concentrated; as $\lambda \to 0$ the curvature concentrates at the point $a$.

Belavin, Polyakov, Schwartz and Tyupkin found this solution in 1975, and the name is formed from their initials.
In quantum field theory it describes tunnelling between vacua of $SU(2)$ Yang–Mills theory in Euclidean time.

## Explanations

### L1 human

The BPST instanton is the simplest twisted solution of the Yang–Mills equations in four-dimensional Euclidean space.
Its field strength forms a lump around one point, of a size that one may choose freely, and dies away quickly far from it.
Writing points of space as quaternions makes the formula as short as a fraction.
The lump cannot be smoothed away, because it carries one unit of a topological charge, much as a loop around a hole cannot be shrunk.
