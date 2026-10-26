---
tag: 01MPZXYVYF
kind: statement
role: theorem
name: Cauchy's integral theorem
aliases: [cauchy-goursat-theorem, cauchy-integral-theorem]
msc: ["30E20"]
uses: [0DG0Z72CQD, 00FWNP9TXY, 097KNJFJ7V]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%27s_integral_theorem
    locator: Formulation on simply connected regions
  - url: https://en.wikipedia.org/wiki/Cauchy%27s_integral_theorem
    locator: Statement
same_as:
  wikidata: Q834025
  wikipedia: Cauchy's integral theorem
---

## Statement

Let $U \subseteq \mathbb{C}$ be a simply connected open set: $U$ is connected, and each closed path in $U$ can be continuously deformed in $U$ to a constant path.
Let $f : U \to \mathbb{C}$ be [[holomorphic|0DG0Z72CQD]] on $U$.
Let $\gamma : [a, b] \to U$ be a closed path that is continuous and piecewise continuously differentiable.
Then the [[contour integral|00FWNP9TXY]] of $f$ along $\gamma$ is
$$\oint_\gamma f(z) \, dz = 0.$$

## Remarks

Open discs, open half-planes, $\mathbb{C}$ and each convex open set are simply connected. So the theorem holds on each of them.
A special case: if $f$ is holomorphic on an open set that contains the closed disc $|z - c| \le R$, then $\oint_{|z - c| = R} f(z) \, dz = 0$.
The hypothesis on $U$ is necessary. On $\mathbb{C} \setminus \{0\}$, the [[integral of 1/z|0SXZ68HV6F]] over the unit circle is $2 \pi i$.
It follows that the integral of $f$ along a path in $U$ depends only on the end points of the path.

## Explanations

### L1 human

The integral of a holomorphic function around a closed loop is zero, as long as the loop does not go around a hole of the domain.
It is like walking around a hill and coming back to the start: the total change of height is zero.
