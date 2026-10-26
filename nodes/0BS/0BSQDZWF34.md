---
tag: 0BSQDZWF34
kind: statement
role: theorem
name: Riemann's theorem on removable singularities
aliases: [riemann-removable-singularity-theorem]
msc: [30D30]
uses: [0TYB3HM9KE, 0P18JC72RE, 0DG0Z72CQD]
sources:
  - url: https://en.wikipedia.org/wiki/Removable_singularity
    locator: Riemann's theorem
---

## Statement

Let $c \in \mathbb{C}$, let $r > 0$, and let $f$ be [[holomorphic|0DG0Z72CQD]] on the punctured disc $0 < |z - c| < r$.
Assume that $f$ is bounded near $c$: there are $M \ge 0$ and $\delta \in (0, r)$ with $|f(z)| \le M$ for $0 < |z - c| < \delta$.
Then $c$ is a [[removable singularity|0P18JC72RE]] of $f$. Moreover, the limit $\lim_{z \to c} f(z)$ exists, and the extension of $f$ by this value at $c$ is holomorphic on $|z - c| < r$.

## Remarks

The following are equivalent: $c$ is removable; $f$ has a continuous extension to $c$; $f$ is bounded near $c$; $\lim_{z \to c} (z - c) f(z) = 0$.
Proof idea: $h(z) = (z - c)^2 f(z)$, with $h(c) = 0$, is complex differentiable at $c$ with $h'(c) = 0$. So $h(z) = \sum_{n \ge 2} a_n (z - c)^n$, and $f(z) = \sum_{n \ge 2} a_n (z - c)^{n-2}$.
For example, $\frac{\sin z}{z}$ is bounded near $0$, so $0$ is removable.

## Explanations

### L1 human

If a holomorphic function stays bounded near a single bad point, then the point is not really bad.
You can give the function a value there, and the function becomes holomorphic at that point.
