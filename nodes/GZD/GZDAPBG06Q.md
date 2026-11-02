---
tag: GZDAPBG06Q
kind: definition
name: Inverse problem
msc: [35R30, 47A52, 65J22]
defines: PCMW7KN5P4
uses: [W09B9NZ9B5, 03J5RAKB30]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_problem
---

## Definition

Let $X$ and $Y$ be [[normed vector spaces|03J5RAKB30]], or more generally metric spaces, and let $F \colon X \to Y$ be a map, called the forward map.
The elements of $X$ are the unknown parameters, and the elements of $Y$ are the data.
The *inverse problem* for $F$ is: given $y \in Y$, find $x \in X$ with $F(x) = y$.
In practice only noisy data $y^\delta$ with $\norm{y^\delta - y} \le \delta$ are known, and one seeks approximations of $x$ that converge to it as $\delta \to 0$.

## Remarks

The inverse problem is [[well-posed|W09B9NZ9B5]] in the sense of Hadamard when $F$ is a bijection with continuous inverse; otherwise it is ill-posed.
Example: let $X = Y = C[0, 1]$ with the maximum norm and $(Fx)(t) = \int_0^t x(s) \, ds$.
The inverse problem is differentiation: $x = y'$ when $y = Fx$.
It is ill-posed, since $y_n(t) = n^{-1} \sin(n^2 t)$ satisfies $\norm{y_n} \le n^{-1} \to 0$ while $\norm{y_n'} = n \to \infty$.
Non-example: computing $y = Fx$ from a given $x$ is the forward problem, not an inverse problem; here it is stable, since $\norm{Fx} \le \norm{x}$.
Standard regularization methods replace $F^{-1}$ by a family of stable maps, such as Tikhonov regularization $x_\alpha = \operatorname{argmin}_x \left( \norm{Fx - y^\delta}^2 + \alpha \norm{x}^2 \right)$ in Hilbert spaces.
