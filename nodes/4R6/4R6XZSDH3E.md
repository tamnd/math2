---
tag: 4R6XZSDH3E
kind: definition
name: Weak and strong extremum
msc: [49K05, 49K99]
defines: WMPCR723MJ
uses: [G7T008BEWY, 1EQM0DJ4NC, 0V2WP9B1MF]
sources:
  - url: https://en.wikipedia.org/wiki/Calculus_of_variations
---

## Definition

Let $a < b$, let $\mathcal{A} \subseteq C^1([a, b])$ be a class of [[admissible functions|G7T008BEWY]], and let $J \colon \mathcal{A} \to \R$ be a [[functional|1EQM0DJ4NC]].
For $y \in C^1([a, b])$ use the [[norms|0V2WP9B1MF]]
$$\norm{y}_0 = \max_{[a, b]} \abs{y}, \qquad \norm{y}_1 = \max_{[a, b]} \abs{y} + \max_{[a, b]} \abs{y'}.$$
Let $y_0 \in \mathcal{A}$.

1. $y_0$ is a *strong local minimum* of $J$ if there is $\varepsilon > 0$ with $J(y_0) \le J(y)$ for all $y \in \mathcal{A}$ with $\norm{y - y_0}_0 < \varepsilon$.
2. $y_0$ is a *weak local minimum* of $J$ if there is $\varepsilon > 0$ with $J(y_0) \le J(y)$ for all $y \in \mathcal{A}$ with $\norm{y - y_0}_1 < \varepsilon$.

Strong and weak local maxima are defined with $J(y_0) \ge J(y)$.
A strong (weak) local extremum is a strong (weak) local minimum or maximum.

## Remarks

Since $\norm{y}_0 \le \norm{y}_1$, every strong local minimum is a weak local minimum.

Example: let $J(y) = \int_0^1 y'^2 \, dx$ on $\mathcal{A} = \set{y \in C^1([0, 1]) : y(0) = 0, \ y(1) = 1}$, and $y_0(x) = x$.
For $y \in \mathcal{A}$ write $y' = 1 + \eta$; then $\int_0^1 \eta \, dx = 0$, so $J(y) = 1 + \int_0^1 \eta^2 \, dx \ge J(y_0)$.
So $y_0$ is a global, hence strong, minimum.

Non-example: let $J(y) = \int_0^1 y'^3 \, dx$ on the same class, and $y_0(x) = x$.
With $y' = 1 + \eta$ one gets $J(y) = 1 + \int_0^1 \eta^2 (3 + \eta) \, dx$, which is at least $1$ when $\abs{\eta} < 3$; so $y_0$ is a weak local minimum.
It is not a strong local minimum.
Fix $h > 0$, let $N$ be large and $\delta = h/N$, and let $y$ have slope $-N$ on $[0, \delta]$ and slope $(1 + h)/(1 - \delta)$ on $[\delta, 1]$, with corners rounded off.
Then $\norm{y - y_0}_0 \le h + \delta$, while $J(y)$ is close to $-N^2 h + (1 + h)^3/(1 - \delta)^2$, which tends to $-\infty$ as $N \to \infty$.
