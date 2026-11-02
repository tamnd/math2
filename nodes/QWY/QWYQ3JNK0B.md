---
tag: QWYQ3JNK0B
kind: definition
name: Numerical stability
msc: [65G50, 65F35]
defines: 1AKB4XHMTH
uses: [CMXHRNWY35, JA3QXVF2B8, 0TGV80E6A4, 0V2WP9B1MF]
sources:
  - url: https://en.wikipedia.org/wiki/Numerical_stability
---

## Definition

Let $X$ and $Y$ be normed spaces with [[norms|0V2WP9B1MF]] $\norm{\cdot}$, and let $f \colon X \to Y$ be a problem.
An *algorithm* for $f$ is a family of maps $\tilde f \colon X \to Y$, one for each floating-point system, with unit roundoff $u$ as in [[machine epsilon|JA3QXVF2B8]].
All [[$O$ bounds|0TGV80E6A4]] below are as $u \to 0$, uniform in $x \ne 0$.

1. The algorithm is *backward stable* if for each $x$ there is $\tilde x$ with $\tilde f(x) = f(\tilde x)$ and $\norm{\tilde x - x}/\norm{x} = O(u)$.
2. The algorithm is *stable* if for each $x$ there is $\tilde x$ with $\norm{\tilde x - x}/\norm{x} = O(u)$ and $\norm{\tilde f(x) - f(\tilde x)}/\norm{f(\tilde x)} = O(u)$.
3. The algorithm is *forward stable* if $\norm{\tilde f(x) - f(x)}/\norm{f(x)} = O(\kappa(x) \, u)$, where $\kappa(x)$ is the relative condition number of $f$ at $x$.

## Remarks

Example: computing $x_1 + x_2$ as $\mathrm{fl}(x_1 + x_2) = (x_1 + x_2)(1 + \delta)$, $\abs{\delta} \le u$, is backward stable, with $\tilde x = (x_1(1 + \delta), x_2(1 + \delta))$; this is the [[backward error|CMXHRNWY35]] computation.
Non-example: computing $1 - \cos t$ by forming $\mathrm{fl}(\cos t)$ and subtracting it from $1$ is not stable for small $t$.
The result, of order $t^2/2$, carries an absolute error of order $u$, so its relative error is of order $u/t^2$.
This is not $O(u)$, and a relative perturbation of $t$ of order $u$ cannot explain it.
The formula $2 \sin^2(t/2)$ computes the same quantity stably.
Backward stability implies stability, and a backward stable algorithm has relative forward error $O(\kappa(x) u)$.
