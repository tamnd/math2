---
tag: JM2RBQJ0MG
kind: proof
name: Proof of the power series of the complex logarithm
msc: [30B10]
proves: 09BG0Y7SZD
uses: [0YKY4M3KRQ, 0VARVQ9ZW1, 045EWAXY9P, 04Z5G0THN6, 0Q7K4AXE53, 05APWSX53S, 0YMP521ZR5, 0XVGJE7Q04, 0YQ458D7PF, 0SQSQP748R]
sources:
  - url: https://en.wikipedia.org/wiki/Mercator_series
    locator: Complex series
---

## Proof

We show that the series and $-\operatorname{Log}(1 - z)$ have the same derivative and agree at $0$.

1. Let $D = \set{z : \abs{z} < 1}$ and $z \in D$. Then $\abs{z^n / n} \le \abs{z}^n$, and $\sum \abs{z}^n$ converges. By the [[comparison test|04Z5G0THN6]], $\sum_{n \ge 1} z^n / n$ converges absolutely.
2. Consider the [[power series|0VARVQ9ZW1]] $\sum_{n \ge 1} z^n / n$. For $0 \le s < 1$, $s^n / n \le 1$ for all $n \ge 1$. So its [[radius of convergence|045EWAXY9P]] is at least $1$, and $D$ lies in its disc of convergence.
3. Put $g(z) = \sum_{n=1}^{\infty} z^n / n$ for $z \in D$. Since [[power series are holomorphic in the disc of convergence|0YMP521ZR5]], $g$ is holomorphic on $D$ and $g'(z) = \sum_{n=1}^{\infty} z^{n-1}$.
4. By the [[finite geometric sum|05APWSX53S]], $\sum_{n=1}^{N} z^{n-1} = \frac{1 - z^N}{1 - z}$. Since $\abs{z}^N \to 0$ by [[the limit of $r^N$|0Q7K4AXE53]], we get $g'(z) = \frac{1}{1 - z}$.
5. For $z \in D$, $\operatorname{Re}(1 - z) \ge 1 - \abs{z} > 0$. So $1 - z$ lies in the slit plane $S = \C \setminus (-\infty, 0]$.
6. Put $h(z) = \operatorname{Log}(1 - z)$ for $z \in D$, with $\operatorname{Log}$ the [[principal branch|0YKY4M3KRQ]]. Fix $z_0 \in D$, $\zeta_0 = 1 - z_0$, and $k \ne 0$ small. Then $\frac{h(z_0 + k) - h(z_0)}{k} = - \frac{\operatorname{Log}(\zeta_0 - k) - \operatorname{Log} \zeta_0}{-k}$.
7. As $k \to 0$, also $-k \to 0$. Since [[$\operatorname{Log}$ is holomorphic on $S$ with derivative $1/\zeta$|0XVGJE7Q04]], the quotient in step 6 tends to $-1/\zeta_0$. So $h$ is holomorphic on $D$ with $h'(z) = -\frac{1}{1 - z}$.
8. Put $F = g + h$ on $D$. By steps 3, 4 and 7, $F$ is holomorphic on $D$ and $F'(z) = 0$ for all $z \in D$.
9. Fix $z \in D$ and let $\gamma(t) = t z$ for $t \in [0, 1]$, a path in $D$. By the [[fundamental theorem of contour integration|0YQ458D7PF]] for $F$ and the continuous function $0$, $F(z) - F(0) = \int_\gamma 0 \, dw = 0$.
10. We have $g(0) = 0$. Also $\operatorname{Arg} 1 = 0$ by the [[principal argument|0SQSQP748R]], since $1 = \cos 0 + i \sin 0$. So $h(0) = \operatorname{Log} 1 = \ln 1 + 0 = 0$, and $F(0) = 0$.
11. By steps 9 and 10, $g(z) + \operatorname{Log}(1 - z) = 0$. So $-\operatorname{Log}(1 - z) = \sum_{n=1}^{\infty} z^n / n$ for each $z \in D$.

## Idea

Differentiating the series term by term gives the geometric series $1/(1 - z)$, which is also the derivative of $-\operatorname{Log}(1 - z)$. Two functions on a disc with the same derivative differ by a constant, and both vanish at $0$.
