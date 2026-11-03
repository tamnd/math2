---
tag: KV8VQMQHEM
kind: statement
role: theorem
name: Danskin's theorem
msc: [49J52, 90C47, 90C31]
uses: [0R6EWFKRCF, 06KWGHDN2J, 0ABK9V9Y64]
about: [06KWGHDN2J]
sources:
  - url: https://en.wikipedia.org/wiki/Danskin%27s_theorem
same_as:
  wikidata: Q5221089
  wikipedia: Danskin's theorem
---

## Statement

Let $Z \subseteq \R^m$ be a nonempty [[compact|0R6EWFKRCF]] set, and let $\varphi \colon \R^n \times Z \to \R$ be continuous.
Assume that for each $z \in Z$ the function $\varphi(\cdot, z)$ is differentiable, and that its [[gradient|0ABK9V9Y64]] $\nabla_x \varphi(x, z)$ is continuous on $\R^n \times Z$.
Let $f(x) = \max_{z \in Z} \varphi(x, z)$ and $Z_0(x) = \set{z \in Z : \varphi(x, z) = f(x)}$.
Then, for all $x, d \in \R^n$, $f$ has the [[directional derivative|06KWGHDN2J]]
$$f'(x; d) = \max_{z \in Z_0(x)} \nabla_x \varphi(x, z) \cdot d.$$
In particular, if $Z_0(x)$ has a single element $\bar z$, then $f$ is differentiable at $x$ with $\nabla f(x) = \nabla_x \varphi(x, \bar z)$.

## Remarks

The lower bound $f'(x; d) \ge \nabla_x \varphi(x, z) \cdot d$ for $z \in Z_0(x)$ comes from $f(x + td) \ge \varphi(x + td, z)$.
For the upper bound, take maximizers $z_t$ at $x + td$; by compactness they accumulate in $Z_0(x)$, and the mean value theorem with the continuity of $\nabla_x \varphi$ bounds the quotient.
If moreover each $\varphi(\cdot, z)$ is convex, then $f$ is convex and its subdifferential at $x$ is the convex hull of $\set{\nabla_x \varphi(x, z) : z \in Z_0(x)}$.

Example: $Z = [-1, 1]$ and $\varphi(x, z) = xz$ on $\R \times Z$, so $f(x) = \abs{x}$.
For $x \ne 0$ the maximizer is unique, $\bar z = \sgn x$, and $f'(x) = \sgn x$.
At $x = 0$, $Z_0(0) = [-1, 1]$ and $f'(0; d) = \max_{\abs{z} \le 1} z d = \abs{d}$, so $f$ is not differentiable there.

Compactness of $Z$ is needed for the maxima to exist and for the limit argument.

## Explanations

### L1 human

The maximum of a family of smooth functions is usually not smooth, like the absolute value, which is the maximum of $x$ and $-x$.
Danskin's theorem tells how fast the maximum changes in each direction.
One looks only at the functions that achieve the maximum and takes the fastest of their rates of change.

### L2 human

The theorem is the basic tool to differentiate value functions of the form $\max_z \varphi(x, z)$.
It is used for the dual function in Lagrangian duality, for adversarial training, and in minimax problems where one descends on $x$ using the gradient at a best response $z$.
It is a nonsmooth relative of the [[envelope theorem|WK7MKDWRFF]] of economics.
