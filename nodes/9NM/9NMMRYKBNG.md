---
tag: 9NMMRYKBNG
kind: definition
name: Proximal operator
msc: [90C25, 47H09, 49J53]
defines: E239APE78P
uses: [HM2HHE3J51, 07Q7CNM5WF, RN4G8SGP6P]
sources:
  - url: https://en.wikipedia.org/wiki/Proximal_operator
---

## Definition

Let $H$ be a real [[Hilbert space|HM2HHE3J51]] with norm $\norm{\cdot}$.
Let $f \colon H \to (-\infty, +\infty]$ be a [[convex|07Q7CNM5WF]], [[lower semicontinuous|RN4G8SGP6P]] function that is not identically $+\infty$.
The *proximal operator* of $f$ is the map $\operatorname{prox}_f \colon H \to H$ given by
$$\operatorname{prox}_f(v) = \operatorname*{arg\,min}_{x \in H} \left( f(x) + \tfrac12 \norm{x - v}^2 \right).$$

## Remarks

The minimizer exists and is unique, since the function being minimized is lower semicontinuous, strongly convex and tends to $+\infty$ as $\norm{x} \to \infty$.
Equivalently, $p = \operatorname{prox}_f(v)$ exactly when $v - p$ lies in the subdifferential $\partial f(p)$.
Example: let $C \subseteq H$ be nonempty, closed and convex, and let $f$ be $0$ on $C$ and $+\infty$ outside.
Then $f(x) + \tfrac12 \norm{x - v}^2$ is finite only on $C$, so $\operatorname{prox}_f(v)$ is the point of $C$ nearest to $v$, the projection of $v$ onto $C$.
Example: for $f(x) = \lambda \abs{x}$ on $\R$ with $\lambda > 0$, one finds $\operatorname{prox}_f(v) = \sgn(v) \max(\abs{v} - \lambda, 0)$, the soft thresholding map.
Non-example: let $f$ be $0$ on $\set{-1, 1}$ and $+\infty$ elsewhere on $\R$, so $f$ is not convex.
At $v = 0$ both $-1$ and $1$ minimize $f(x) + \tfrac12 x^2$, so no single proximal point is defined.
