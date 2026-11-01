---
tag: KK0B7V8DCX
kind: statement
role: theorem
name: Kuratowski embedding
msc: ["54E35", 54C25, 46B25]
uses: [0VKD1TP7F3, 02HPP5VCZH, 06GZ956657, 06HE9J7DXF]
about: [0VKD1TP7F3, 06GZ956657]
sources:
  - url: https://en.wikipedia.org/wiki/Kuratowski_embedding
same_as:
  wikidata: Q3984015
  wikipedia: Kuratowski embedding
---

## Statement

Let $(X, d)$ be a nonempty [[metric space|0VKD1TP7F3]].
Let $\ell^\infty(X)$ be the [[Banach space|06GZ956657]] of bounded functions $X \to \R$ with the norm $\norm{f}_\infty = \sup_{y \in X} \abs{f(y)}$.
Fix a point $x_0 \in X$.
For $x \in X$, define $\Phi(x) \colon X \to \R$ by
$$\Phi(x)(y) = d(x, y) - d(x_0, y).$$
Then each $\Phi(x)$ lies in $\ell^\infty(X)$, and $\Phi \colon X \to \ell^\infty(X)$ is an [[isometry|02HPP5VCZH]] onto its image.
That is, $\norm{\Phi(x) - \Phi(x')}_\infty = d(x, x')$ for all $x, x' \in X$.

## Remarks

By the triangle inequality, $\abs{d(x, y) - d(x', y)} \le d(x, x')$ for every $y$.
With $x' = x_0$, this shows that $\Phi(x)$ is bounded by $d(x, x_0)$.
In general, it gives $\norm{\Phi(x) - \Phi(x')}_\infty \le d(x, x')$.
Taking $y = x'$ gives the value $d(x, x')$, so equality holds.

If $X$ is bounded, the simpler map $x \mapsto d(x, \cdot)$ already works.
If $X$ is [[separable|0Z2P41SVDP]], the same idea with a countable dense subset embeds $X$ isometrically in the sequence space $\ell^\infty$.

## Explanations

### L1 human

Every metric space, however abstract, can be placed inside a space of real functions without changing any distance.
Each point $x$ is recorded by the list of its distances to all other points.
This turns questions about metric spaces into questions about normed vector spaces.

### L2 human

Since $\ell^\infty(X)$ is complete, the closure of $\Phi(X)$ is a complete metric space containing $X$ densely.
This gives a quick construction of the [[completion of a metric space|06RW4RKWH7]].
The embedding also lets one take convex hulls and straight segments of points of $X$ inside a Banach space.
For compact $X$ and $Y$, it shows that the distance on the [[Gromov–Hausdorff space|ETRF2FHAEE]] can be computed inside the single space $Z = \ell^\infty$.
