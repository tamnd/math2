---
tag: 0CDMXGPSES
kind: definition
name: Riemann sphere
msc: [30F10]
defines: 0J78KBPFZB
uses: [09FTAET5Z4, 0CTE7A31XQ]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann_sphere
    locator: Extended complex numbers
  - url: https://en.wikipedia.org/wiki/Riemann_sphere
    locator: As a sphere
---

## Definition

The Riemann sphere, or extended complex plane, is the set $\widehat{\mathbb{C}} = \mathbb{C} \cup \{\infty\}$, where $\mathbb{C}$ is the set of [[complex numbers|09FTAET5Z4]] and $\infty$ is one new point.
Its topology is as follows.
A set $V \subseteq \widehat{\mathbb{C}}$ is open if the following two conditions hold. First, $V \cap \mathbb{C}$ is open in the [[complex plane|0CTE7A31XQ]]. Second, in the case $\infty \in V$, $V$ also contains the set $\{ z \in \mathbb{C} : |z| > R \}$ for some $R > 0$.
Let $S^2 = \{ (x_1, x_2, x_3) \in \mathbb{R}^3 : x_1^2 + x_2^2 + x_3^2 = 1 \}$ and $N = (0, 0, 1)$.
The stereographic projection $\sigma : S^2 \to \widehat{\mathbb{C}}$ is $\sigma(x_1, x_2, x_3) = \frac{x_1 + i x_2}{1 - x_3}$ for points other than $N$, and $\sigma(N) = \infty$.
The map $\sigma$ is a homeomorphism, so $\widehat{\mathbb{C}}$ is a sphere as a topological space.

## Remarks

A sequence $(z_n)$ of complex numbers tends to $\infty$ in $\widehat{\mathbb{C}}$ exactly when $|z_n| \to \infty$.
Some arithmetic extends to $\infty$: $z + \infty = \infty$ for $z \in \mathbb{C}$, and $\frac{z}{0} = \infty$ and $\frac{z}{\infty} = 0$ for $z \neq 0$, but the expressions $\infty - \infty$, $0 \cdot \infty$, $\frac{0}{0}$ and $\frac{\infty}{\infty}$ stay undefined.
With the value $\infty$ at each [[pole|0WPQYW8MTE]], a [[meromorphic function|0NSD1TPHR0]] on an open set $U$ becomes a continuous map from $U$ to $\widehat{\mathbb{C}}$.
The Riemann sphere is a compact Riemann surface, with the two charts $z$ near points of $\mathbb{C}$ and $\frac{1}{z}$ near $\infty$.

## Explanations

### L1 human

Imagine a ball that sits on the complex plane at $0$.
Draw a line from the top of the ball to a point of the plane; the line meets the ball at one more point.
Points far from $0$ go to points near the top, so the top of the ball plays the role of $\infty$.
