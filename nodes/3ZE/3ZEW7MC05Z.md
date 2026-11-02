---
tag: 3ZEW7MC05Z
kind: definition
name: Method of multiple scales
msc: ["34E13", "34E10"]
defines: 2V5E1B1Q9H
uses: [0NT64JV96A, Q26QN6GYZX]
sources:
  - url: https://en.wikipedia.org/wiki/Multiple-scale_analysis
---

## Definition

Consider an [[ordinary differential equation|0NT64JV96A]] $F(t, x, x', x'', \varepsilon) = 0$ for $x(t)$, depending on a small parameter $\varepsilon > 0$.
The *method of multiple scales* (two-timing, in its simplest form) proceeds as follows.

1. Introduce the slow time $T = \varepsilon t$ and seek $x(t) = X(t, T)$, where $X$ is a function of two independent variables.
2. Replace $\frac{d}{dt}$ by $\partial_t + \varepsilon \partial_T$, and expand $X = X_0(t, T) + \varepsilon X_1(t, T) + \cdots$.
3. Collect powers of $\varepsilon$; this gives equations in $t$ for $X_0, X_1, \ldots$ in which $T$ is a parameter.
4. Choose the dependence of $X_0, X_1, \ldots$ on $T$ so that each $X_k$ stays bounded in $t$.
   This means that the equations have no resonant forcing that produces secular terms.

The result is an [[asymptotic expansion|Q26QN6GYZX]] intended to be valid for $0 \le t \le C / \varepsilon$.
More slow times $\varepsilon^2 t, \varepsilon^3 t, \ldots$ can be added to reach longer time intervals.

## Remarks

Example: $x'' + 2\varepsilon x' + x = 0$.
Order $0$ gives $\partial_t^2 X_0 + X_0 = 0$, so $X_0 = A(T) \cos t + B(T) \sin t$.
Order $1$ gives $\partial_t^2 X_1 + X_1 = -2 \partial_t \partial_T X_0 - 2 \partial_t X_0 = 2(A' + A) \sin t - 2(B' + B) \cos t$.
Bounded $X_1$ requires $A' = -A$ and $B' = -B$, so $X_0 = e^{-T} (a \cos t + b \sin t)$.
Every exact solution has the form $e^{-\varepsilon t} \bigl(c_1 \cos(\sqrt{1 - \varepsilon^2}\, t) + c_2 \sin(\sqrt{1 - \varepsilon^2}\, t)\bigr)$.
Its frequency differs from $1$ by $O(\varepsilon^2)$, so the approximation has error $O(\varepsilon)$ for $0 \le t \le C / \varepsilon$.

Non-example: the regular expansion $x = x_0(t) + \varepsilon x_1(t)$ with one time gives $x_1$ containing $t \cos t$ and $t \sin t$ terms, so the error is not small when $t \ge 1/\varepsilon$.

## Explanations

### L1 human

Use a fast clock and a slow clock at the same time, and let the slow clock govern how the fast motion changes.
