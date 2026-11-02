---
tag: KZ3YVM10SP
kind: definition
name: Peetre K-functional
msc: [46B70, 41A25, 41A65]
defines: CAE0X7G9R5
uses: [VX1R6FN6PS, 06GZ956657, 04KFTA34C5]
sources:
  - url: https://en.wikipedia.org/wiki/Interpolation_space
---

## Definition

Let $(X_0, X_1)$ be a compatible couple of [[Banach spaces|06GZ956657]].
So both are continuously embedded in a common Hausdorff topological vector space, and the sum $X_0 + X_1$ is defined.
For $x \in X_0 + X_1$ and $t > 0$, the *Peetre K-functional* is the [[infimum|04KFTA34C5]]
$$K(t, x) = K(t, x; X_0, X_1) = \inf \set{ \norm{x_0}_{X_0} + t \norm{x_1}_{X_1} : x = x_0 + x_1, \ x_0 \in X_0, \ x_1 \in X_1 }.$$

## Remarks

Example: take $X_0 = X_1 = \R$ with the absolute value.
For a split $x = x_0 + x_1$ the cost is $\abs{x_0} + t \abs{x_1} \ge \min(1, t) (\abs{x_0} + \abs{x_1}) \ge \min(1, t) \abs{x}$, and putting all of $x$ in the cheaper space attains this, so $K(t, x) = \min(1, t) \abs{x}$.

Non-example: the K-functional is only defined on $X_0 + X_1$.
For $X_0 = X_1 = \ell^1$ inside the space of all sequences, the sequence $(1, 1, 1, \dots)$ has no split at all, so $K(t, \cdot)$ is not defined there.

For each $x$, the function $t \mapsto K(t, x)$ is nondecreasing and concave, and $K(1, x)$ is the norm of $x$ in $X_0 + X_1$.
For $0 < \theta < 1$ and $1 \le q \le \infty$, the real [[interpolation space|VX1R6FN6PS]] $(X_0, X_1)_{\theta, q}$ consists of the $x$ for which $t \mapsto t^{-\theta} K(t, x)$ lies in $L^q((0, \infty), dt / t)$.
In approximation theory one takes $X_0 = L^p[a, b]$ and $X_1$ the Sobolev space $W^{k, p}[a, b]$, measured by the seminorm $\norm{g^{(k)}}_p$.
Then the quantity $K(t^k, f)$ is bounded above and below by constant multiples of the [[modulus of smoothness|CRPZ1RVNKQ]] $\omega_k(f, t)_p$ for small $t$.
