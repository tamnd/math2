---
tag: XHC8SXGFXS
kind: definition
name: Moreau envelope
msc: [90C25, 49J52, 52A41]
defines: GSTG1NVYWW
uses: [HM2HHE3J51, 07Q7CNM5WF, RN4G8SGP6P, E239APE78P]
sources:
  - url: https://en.wikipedia.org/wiki/Moreau_envelope
---

## Definition

Let $H$ be a real [[Hilbert space|HM2HHE3J51]] with norm $\norm{\cdot}$.
Let $f \colon H \to (-\infty, +\infty]$ be [[convex|07Q7CNM5WF]], lower [[semicontinuous|RN4G8SGP6P]] and not identically $+\infty$, and let $\lambda > 0$.
The *Moreau envelope* of $f$ with parameter $\lambda$ is the function $M_{\lambda f} \colon H \to \R$ given by
$$M_{\lambda f}(x) = \inf_{y \in H} \left( f(y) + \frac{1}{2\lambda} \norm{x - y}^2 \right).$$

## Remarks

The infimum is attained at the single point $\operatorname{prox}_{\lambda f}(x)$, where $\operatorname{prox}$ is the [[proximal operator|E239APE78P]].
The envelope is convex, finite everywhere and satisfies $M_{\lambda f} \le f$.
It is Fréchet differentiable, with $\nabla M_{\lambda f}(x) = \frac{1}{\lambda}\big(x - \operatorname{prox}_{\lambda f}(x)\big)$, and this gradient is Lipschitz with constant $1/\lambda$.
It has the same infimum and the same minimizers as $f$, and $M_{\lambda f}(x) \to f(x)$ as $\lambda \to 0$ for every $x$.
Other notations are $e_\lambda f$ and $f_\lambda$; the operation is an infimal convolution of $f$ with $\frac{1}{2\lambda}\norm{\cdot}^2$.

Example: $H = \R$ and $f(y) = \abs{y}$.
The minimizer is $y = \sgn(x) \max(\abs{x} - \lambda, 0)$, which gives
$$M_{\lambda f}(x) = \begin{cases} x^2 / (2\lambda) & \text{if } \abs{x} \le \lambda, \\ \abs{x} - \lambda/2 & \text{if } \abs{x} > \lambda. \end{cases}$$
This is the Huber function, differentiable with derivative $\max(-1, \min(1, x/\lambda))$.

Non-example: $f(y) = -y^2$ on $\R$ is not convex, and with $\lambda = 1$ the expression $-y^2 + \frac12 (x - y)^2$ tends to $-\infty$ as $\abs{y} \to \infty$.
So the infimum is $-\infty$ and no real-valued envelope is defined.
