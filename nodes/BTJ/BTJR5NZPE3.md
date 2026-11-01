---
tag: BTJR5NZPE3
kind: definition
name: Landau's constants
msc: [30C25, 30D20]
defines: AC3FNJ8Y1Y
uses: [0DG0Z72CQD, 8G5ABXRK85, 0PVG1CRAJN, R91E83SDBD]
sources:
  - url: https://en.wikipedia.org/wiki/Bloch%27s_theorem_(complex_analysis)
---

## Definition

Let $\mathbb{D}$ be the [[unit disc|8G5ABXRK85]], and let $\mathcal{F}$ be the set of [[holomorphic|0DG0Z72CQD]] functions $f \colon \mathbb{D} \to \C$ with $f'(0) = 1$.
For $f \in \mathcal{F}$:

1. $L_f$ is the supremum of the radii $r$ such that $f(\mathbb{D})$ contains an open disc of radius $r$.
2. $B_f$ is the supremum of the radii $r$ of the open discs $f(\Omega)$, where $\Omega \subseteq \mathbb{D}$ is open and $f$ is [[injective|0PVG1CRAJN]] on $\Omega$.

*Landau's constants* are the three numbers
$$B = \inf_{f \in \mathcal{F}} B_f, \qquad L = \inf_{f \in \mathcal{F}} L_f, \qquad A = \inf \set{L_f : f \in \mathcal{F},\ f \text{ injective}}.$$
The number $B$ is the *Bloch constant*, $L$ is the *Landau constant*, and $A$ is the *univalent Landau constant*.

## Remarks

Since a disc covered injectively is a disc contained in the image, $B_f \le L_f$ for all $f$, so $B \le L$.
The infimum $A$ is taken over a smaller set of functions than $L$, so $L \le A$.
Example: for $f(z) = z$, the image is $\mathbb{D}$, so $L_f = B_f = 1$.
For an injective $f \in \mathcal{F}$, the [[Koebe quarter theorem|WX0HMW4GT7]] gives a disc of radius $1/4$ in the image, so $A \ge 1/4$.
Non-example: $f(z) = 2z$ is not in $\mathcal{F}$, because $f'(0) = 2$; without the normalisation the infimum would be $0$, as $f(z) = \varepsilon z$ shows.
[[Bloch's theorem|KW31KDX7TB]] is the statement $B > 0$.
