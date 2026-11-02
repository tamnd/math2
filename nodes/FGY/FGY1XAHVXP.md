---
tag: FGY1XAHVXP
kind: definition
name: Abel function
msc: [39B12, 26A18]
defines: 2QBWT7T02Y
uses: [68SHB7Z721, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Abel_equation
---

## Definition

Let $X$ be a set and let $f \colon X \to X$ be a map.
An *Abel function* of $f$ is a [[function|0EPAT51DXQ]] $\alpha \colon X \to \C$ that satisfies the [[Abel equation|68SHB7Z721]]
$$\alpha(f(x)) = \alpha(x) + 1 \quad \text{for all } x \in X.$$
Many authors also require $\alpha$ to be injective, or, for real $X$, continuous and strictly monotone.

## Remarks

Example: for $f(x) = 3x$ on $X = (0, \infty)$, $\alpha(x) = \log_3 x$ is an Abel function, since $\log_3(3x) = \log_3 x + 1$.
Non-example: for the same $f$, $\alpha(x) = \ln x$ is not an Abel function, since $\ln(3x) = \ln x + \ln 3$ and $\ln 3 \ne 1$.
If $\alpha$ is an injective Abel function and $t$ is real with $\alpha(X) + t \subseteq \alpha(X)$, then $f^t(x) = \alpha^{-1}(\alpha(x) + t)$ satisfies $f^1 = f$ and $f^s \circ f^t = f^{s + t}$, so $(x, t) \mapsto f^t(x)$ solves the translation equation where it is defined.
In the example, $f^t(x) = 3^t x$.
