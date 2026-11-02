---
tag: HZKFNZTHZS
kind: definition
name: Smooth dynamical system
msc: [37C05, 37C10]
defines: 116TPXR5FS
uses: [WBZHXGKNSJ, 0Z1Y7JHGBR, BBZP1R872N]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamical_system
---

## Definition

Let $M$ be a [[smooth manifold|WBZHXGKNSJ]] and let $r \ge 1$ be an integer or $\infty$.
A *smooth dynamical system of class $C^r$* on $M$ is one of the following.

1. Discrete time: a $C^r$ [[diffeomorphism|0Z1Y7JHGBR]] $f \colon M \to M$, with the action $n \mapsto f^n$ of $\Z$ on $M$.
2. Continuous time: a $C^r$ map $\varphi \colon \R \times M \to M$, written $\varphi_t(x) = \varphi(t, x)$, such that $\varphi_0 = \id_M$ and $\varphi_{s+t} = \varphi_s \circ \varphi_t$ for all $s, t \in \R$.

## Remarks

In case 2 each $\varphi_t$ is a $C^r$ diffeomorphism with inverse $\varphi_{-t}$, and $\varphi$ is called a $C^r$ flow.
It is the flow of the vector field $X(x) = \frac{d}{dt}\varphi_t(x)\big|_{t=0}$, which is of class $C^{r-1}$.
Conversely, on a compact manifold every $C^r$ vector field generates a complete $C^r$ flow.
Some authors also allow non-invertible $C^r$ maps $f \colon M \to M$ in case 1.
Example: on the circle $M = \R/\Z$, the rotation $f(x) = x + \alpha \bmod 1$ is a $C^\infty$ diffeomorphism, and $\varphi_t(x) = x + t \bmod 1$ is a $C^\infty$ flow.
Non-example: $f(x) = 2x \bmod 1$ on the circle is smooth but two-to-one, so it is not a diffeomorphism and fails case 1 in this definition.
