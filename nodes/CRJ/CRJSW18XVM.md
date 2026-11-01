---
tag: CRJSW18XVM
kind: definition
name: Smoothness classes
msc: [26A24, "26E10"]
defines: WK5HPW5Y24
uses: [0P27W9RW0G, 084NGSTWM7, 06SKCHDQT5, 0BE3QDH73A, 0JD5ZNW0F4, 0TCBZMEYGN]
sources:
  - url: https://en.wikipedia.org/wiki/Smoothness
    locator: Differentiability classes
---

## Definition

Let $I \subseteq \R$ be an open interval and let $f \colon I \to \R$.

1. The function $f$ is of *class* $C^0$ on $I$ if it is [[continuous|0P27W9RW0G]] on $I$.
2. Let $k \ge 1$ be an integer. The function $f$ is of *class* $C^k$ on $I$ if the [[higher derivatives|084NGSTWM7]] $f', \ldots, f^{(k)}$ exist on $I$. Moreover $f^{(k)}$ must be continuous on $I$.
3. The function $f$ is of *class* $C^\infty$ on $I$ if it is of class $C^k$ for every $k \ge 0$.

The set of functions of class $C^k$ on $I$ is written $C^k(I)$.

## Remarks

The classes are nested: $C^\infty(I) \subseteq \cdots \subseteq C^2(I) \subseteq C^1(I) \subseteq C^0(I)$.
The class $C^1$ is the class of [[continuously differentiable functions|06SKCHDQT5]], and $C^\infty$ is the class of [[smooth functions|0BE3QDH73A]].
The class $C^\omega$ of real [[analytic functions|0JD5ZNW0F4]] lies inside $C^\infty$.
For functions of several variables, $C^k$ is defined by continuous partial derivatives up to order $k$; see [[the characterisation by derivatives|0TCBZMEYGN]].

Example: $f(x) = x \abs{x}$ on $\R$ is of class $C^1$.
Its derivative is $f'(x) = 2 \abs{x}$, which is continuous.
It is not of class $C^2$, because $2\abs{x}$ is not differentiable at $0$.
More generally, $x^k \abs{x}$ is of class $C^k$ but not of class $C^{k+1}$.

Non-example: $g(x) = x^2 \sin(1/x)$ for $x \ne 0$, with $g(0) = 0$, is differentiable on $\R$ but not of class $C^1$.
Its derivative is $g'(x) = 2x \sin(1/x) - \cos(1/x)$ for $x \ne 0$ and $g'(0) = 0$, and $g'$ has no limit at $0$.
