---
tag: 0WZTM0EFR6
kind: definition
name: Hölder continuity
msc: [26A16]
defines: 012PBA0FMD
uses: [063W5JMY85, 0TMZ21WKCN]
sources:
  - url: https://en.wikipedia.org/wiki/H%C3%B6lder_condition
    locator: lead section
inventory: [T29TVJPTN2]
---

## Definition

Let $(X, d_X)$ and $(Y, d_Y)$ be [[metric spaces|063W5JMY85]], let $f \colon X \to Y$ be a function, and let $C \ge 0$ and $\alpha > 0$ be real numbers.
The map $f$ is Hölder continuous with constant $C$ and exponent $\alpha$ when
$$d_Y\bigl(f(x), f(y)\bigr) \le C \, d_X(x, y)^{\alpha} \quad \text{for all } x, y \in X.$$

## Remarks

For $\alpha = 1$, this is the condition for a [[Lipschitz map|0TMZ21WKCN]] with constant $C$.
The map $x \mapsto \sqrt{x}$ on $[0, \infty)$ is Hölder continuous with $C = 1$ and $\alpha = 1/2$.
A Hölder continuous map is uniformly continuous: for $\varepsilon > 0$ and $C > 0$, take $\delta = (\varepsilon / C)^{1/\alpha}$.
For a real function on an interval, Hölder continuity with an exponent $\alpha > 1$ forces the function to be constant.

## Explanations

### L1 human

The Hölder condition is a weaker form of the Lipschitz condition.
It allows a map to be steep, as $\sqrt{x}$ is near $0$, but it still controls how fast the values can change.
