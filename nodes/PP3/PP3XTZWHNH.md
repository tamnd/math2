---
tag: PP3XTZWHNH
kind: definition
name: Butterfly effect
msc: [37D45, 37B02, 37N10]
defines: G0ZT1SDQGS
uses: [0VKD1TP7F3, 0X3WGX95FE, AYVTR2ES5B]
sources:
  - url: https://en.wikipedia.org/wiki/Butterfly_effect
---

## Definition

Let $(X, d)$ be a [[metric space|0VKD1TP7F3]] and let $f \colon X \to X$ be a [[continuous map|0X3WGX95FE]], with [[iterates|AYVTR2ES5B]] $f^n$.
The map $f$ has *sensitive dependence on initial conditions*, the butterfly effect, if there is a constant $\delta > 0$ with the following property.
For every $x \in X$ and every $\varepsilon > 0$, there are a point $y \in X$ with $d(x, y) < \varepsilon$ and an integer $n \ge 0$ with $d(f^n(x), f^n(y)) > \delta$.

## Remarks

The constant $\delta$ is the same for all $x$; the point $y$ and the time $n$ depend on $x$ and $\varepsilon$.
For a flow $(\varphi_t)$ one asks instead for a time $t \ge 0$ with $d(\varphi_t(x), \varphi_t(y)) > \delta$.
Sensitive dependence is one of the conditions in Devaney's definition of chaos.

Example: the doubling map $f(x) = 2x \bmod 1$ on the circle $\R / \Z$, with the distance $d$ to the nearest integer of the difference.
Take $\delta = 1/8$.
Given $x$ and $\varepsilon > 0$, choose $n$ with $2^{-n} < \varepsilon$ and let $y = x + 2^{-n-2}$.
Then $d(x, y) < \varepsilon$, and $f^n(y) - f^n(x) = 1/4 \bmod 1$, so $d(f^n(x), f^n(y)) = 1/4 > \delta$.

Non-example: the rotation $f(x) = x + \alpha \bmod 1$ on $\R / \Z$ is an isometry, so $d(f^n(x), f^n(y)) = d(x, y)$ for all $n$.
Points closer than $\delta$ stay closer than $\delta$ forever, so no $\delta > 0$ works.
