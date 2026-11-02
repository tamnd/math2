---
tag: R1XGWTVY3N
kind: definition
name: Lambert W function
msc: ["33E20", "33B10"]
defines: FW2JKAN14B
uses: [0J0FCWV32D, 0J2WAR83WP]
sources:
  - url: https://en.wikipedia.org/wiki/Lambert_W_function
---

## Definition

Let $f \colon \R \to \R$ be $f(w) = w e^w$, where $e^w$ is the [[exponential function|0J0FCWV32D]].
1. The *principal branch* $W_0 \colon [-1/e, \infty) \to [-1, \infty)$ is the [[inverse|0J2WAR83WP]] of the restriction of $f$ to $[-1, \infty)$.
2. The *lower branch* $W_{-1} \colon [-1/e, 0) \to (-\infty, -1]$ is the inverse of the restriction of $f$ to $(-\infty, -1]$.

Thus $W(x)\, e^{W(x)} = x$ for both branches $W$ on their domains.

## Remarks

The two restrictions are bijections because $f'(w) = (1 + w) e^w$ is positive for $w > -1$ and negative for $w < -1$, $f(-1) = -1/e$, $f(w) \to 0^-$ as $w \to -\infty$, and $f(w) \to \infty$ as $w \to \infty$.

Example: $W_0(e) = 1$, because $1 \cdot e^1 = e$ and $1 \ge -1$.
Also $W_0(0) = 0$, $W_0(-1/e) = W_{-1}(-1/e) = -1$, and $W_0(1) = \Omega \approx 0.5671$, the omega constant.

Non-example: $x = -1$ is in the domain of neither branch, because $w e^w \ge -1/e > -1$ for every real $w$.

Over $\C$, the equation $w e^w = z$ has infinitely many solutions for $z \ne 0$, and they are grouped into branches $W_k$, $k \in \Z$, which extend $W_0$ and $W_{-1}$.
Implicit differentiation gives $W'(x) = \frac{W(x)}{x\,(1 + W(x))}$ for $x \ne 0, -1/e$.
