---
tag: RTA8BG53KZ
kind: definition
name: Chebyshev polynomials of the second kind
msc: [33C45, 42C05]
defines: 7CATGEN6KH
uses: [0SDC934R52]
sources:
  - url: https://en.wikipedia.org/wiki/Chebyshev_polynomials
---

## Definition

The *Chebyshev polynomials of the second kind* are the polynomials $U_n \in \Z[x]$, $n \ge 0$, in the [[polynomial ring|0SDC934R52]] $\Z[x]$ given by
$$U_0 = 1, \qquad U_1 = 2x, \qquad U_{n+1} = 2x \, U_n - U_{n-1} \quad (n \ge 1).$$

## Remarks

Equivalently, $U_n$ is the unique polynomial with $U_n(\cos \theta) \sin \theta = \sin((n + 1)\theta)$ for all real $\theta$.
Example: $U_2 = 2x \cdot 2x - 1 = 4x^2 - 1$, and indeed $\sin(3\theta) = \sin \theta \, (3 - 4 \sin^2 \theta) = \sin \theta \, (4 \cos^2 \theta - 1)$.
Non-example: the [[Chebyshev polynomials|M6EAR1JHPP]] of the first kind $T_n$ satisfy the same recurrence but start with $T_1 = x$, so they fail the clause $U_1 = 2x$.
The polynomial $U_n$ has degree $n$, leading coefficient $2^n$, and roots $\cos \frac{k\pi}{n + 1}$ for $k = 1, \dots, n$.
They are orthogonal: $\int_{-1}^{1} U_m(x) U_n(x) \sqrt{1 - x^2} \, dx = \frac{\pi}{2} \delta_{mn}$.
They are linked to the first kind by $T_n' = n \, U_{n-1}$ for $n \ge 1$.
