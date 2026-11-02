---
tag: G0VTGXYHQK
kind: definition
name: Strip of convergence of the bilateral transform
msc: [44A10]
defines: HYA7QQ1E38
uses: [V94VYJ2RR1, DWJF7ABPR1, 0DG0Z72CQD]
sources:
  - url: https://en.wikipedia.org/wiki/Two-sided_Laplace_transform
---

## Definition

Let $f \colon \R \to \C$ be [[integrable|DWJF7ABPR1]] on each bounded interval.
Let
$$\alpha = \inf \left\{ \sigma \in \R : \int_0^\infty \abs{f(t)} e^{-\sigma t} \, dt < \infty \right\}, \qquad \beta = \sup \left\{ \sigma \in \R : \int_{-\infty}^0 \abs{f(t)} e^{-\sigma t} \, dt < \infty \right\},$$
with $\inf \emptyset = +\infty$ and $\sup \emptyset = -\infty$.
If $\alpha < \beta$, the *strip of convergence* of the [[two-sided Laplace transform|V94VYJ2RR1]] of $f$ is the open vertical strip
$$S = \{ s \in \C : \alpha < \operatorname{Re} s < \beta \}.$$
If $\alpha \ge \beta$, the strip of convergence is empty.

## Remarks

The integral defining $\mathcal{B}\{f\}(s)$ converges absolutely for every $s \in S$, and $\mathcal{B}\{f\}$ is [[holomorphic|0DG0Z72CQD]] on $S$.
The integral may also converge on one or both boundary lines; these points are not counted in the open strip.
Example: for $f(t) = e^{-\abs{t}}$, one finds $\alpha = -1$ and $\beta = 1$, so $S = \{-1 < \operatorname{Re} s < 1\}$.
Non-example: for $f = 1$, $\alpha = 0$ and $\beta = 0$, so the strip is empty, and indeed the two-sided integral converges nowhere.
The strip is part of the data of a transform.
The function $1/(1 - s)$ on $\operatorname{Re} s < 1$ inverts to $e^t$ on $t < 0$ and $0$ on $t > 0$, while on $\operatorname{Re} s > 1$ it inverts to $-e^t$ on $t > 0$ and $0$ on $t < 0$.
