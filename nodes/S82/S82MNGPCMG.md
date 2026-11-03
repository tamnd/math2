---
tag: S82MNGPCMG
kind: definition
name: Lovász extension
msc: [90C27, 90C25, 05B35]
defines: KTT5A73PK7
uses: [4WQA9XFA52, 00E0YZCERH, 0RCQZ36MME]
sources:
  - url: https://en.wikipedia.org/wiki/Submodular_set_function
---

## Definition

Let $E = \set{1, \dots, n}$, and let $f \colon 2^E \to \R$ be a function on the [[power set|00E0YZCERH]] with $f(\emptyset) = 0$.
For $x \in \R^n$, choose a permutation $\sigma$ of $E$ with $x_{\sigma(1)} \ge x_{\sigma(2)} \ge \cdots \ge x_{\sigma(n)}$.
Let $S_0 = \emptyset$ and $S_k = \set{\sigma(1), \dots, \sigma(k)}$ for $k = 1, \dots, n$.
The *Lovász extension* of $f$ is the function $\hat{f} \colon \R^n \to \R$ given by
$$\hat{f}(x) = \sum_{k=1}^{n} x_{\sigma(k)} \big( f(S_k) - f(S_{k-1}) \big).$$

## Remarks

The value does not depend on the choice of $\sigma$ when some coordinates are equal.
For $A \subseteq E$ with [[indicator vector|0RCQZ36MME]] $1_A$, the sum telescopes to $\hat{f}(1_A) = f(A)$, so $\hat{f}$ extends $f$.
For $x \ge 0$ there is the integral form $\hat{f}(x) = \int_0^\infty f(\set{i : x_i \ge t}) \, dt$.

Lovász's theorem: $\hat{f}$ is convex if and only if $f$ is [[submodular|4WQA9XFA52]].
In that case $\min_{A \subseteq E} f(A) = \min_{x \in [0, 1]^n} \hat{f}(x)$, and the minimum of $\hat f$ is attained at a vertex of the cube.

Example: let $n = 2$, $f(\set{1}) = f(\set{2}) = 1$ and $f(\set{1, 2}) = 0$, the cut function of one edge.
If $x_1 \ge x_2$, then $\hat{f}(x) = x_1 (1 - 0) + x_2 (0 - 1) = x_1 - x_2$.
By symmetry $\hat{f}(x) = \abs{x_1 - x_2}$, a convex function.

Non-example: for $f(\set{1}) = f(\set{2}) = 0$ and $f(\set{1, 2}) = 1$, which is not submodular, $\hat{f}(x) = \min(x_1, x_2)$.
This function is not convex, since $\hat f(1, 0) = \hat f(0, 1) = 0$ but $\hat f(1/2, 1/2) = 1/2$.
