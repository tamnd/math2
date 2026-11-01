---
tag: M6EAR1JHPP
kind: object
name: Chebyshev polynomials
msc: [33C45, "12E10", 41A50]
sources:
  - url: https://en.wikipedia.org/wiki/Chebyshev_polynomials
same_as:
  wikidata: Q619511
  wikipedia: Chebyshev polynomials
---

## Description

The Chebyshev polynomials of the first kind are the polynomials $T_n \in \Z[x]$, $n \ge 0$, given by
$$T_0 = 1, \qquad T_1 = x, \qquad T_{n+1} = 2x \, T_n - T_{n-1} \quad (n \ge 1).$$
They are characterised by $T_n(\cos \theta) = \cos(n \theta)$ for all real $\theta$.
The Chebyshev polynomials of the second kind $U_n$ satisfy the same recursion with $U_0 = 1$ and $U_1 = 2x$, and $U_n(\cos \theta) \sin \theta = \sin((n + 1) \theta)$.

## Remarks

The first values are $T_2 = 2x^2 - 1$, $T_3 = 4x^3 - 3x$ and $T_4 = 8x^4 - 8x^2 + 1$.
Check for $T_2$: $\cos(2\theta) = 2 \cos^2 \theta - 1$.
For $n \ge 1$, $T_n$ has degree $n$ and leading coefficient $2^{n-1}$.
Its roots are the $n$ numbers $\cos \frac{(2k - 1)\pi}{2n}$, $k = 1, \dots, n$, all in $(-1, 1)$.
On $[-1, 1]$ one has $\abs{T_n(x)} \le 1$, and the $T_n$ are orthogonal for the weight $(1 - x^2)^{-1/2}$: $\int_{-1}^{1} T_m(x) T_n(x) (1 - x^2)^{-1/2} \, dx = 0$ for $m \ne n$.
They also satisfy $T_m(T_n(x)) = T_{mn}(x)$.
Their roots are good nodes for [[polynomial interpolation|SS1YMS2NPC]] on $[-1, 1]$.

## Explanations

### L1 human

The formula for $\cos(n\theta)$ in terms of $\cos \theta$ is a polynomial, and this polynomial is $T_n$.
For example, $\cos(3\theta) = 4\cos^3 \theta - 3 \cos \theta$, so $T_3 = 4x^3 - 3x$.
Because cosines stay between $-1$ and $1$, these polynomials wave between $-1$ and $1$ on the interval $[-1, 1]$.
