---
tag: 0TXCQ9CST1
kind: concept
name: Integration over a non-rectangular region
aliases: [integral-over-a-normal-domain, type-i-and-type-ii-regions]
msc: [26B15]
uses: [0WAR4F23B4, 0WZCHE1ZF9, 0KTGJW1ZTH]
sources:
  - url: https://en.wikipedia.org/wiki/Multiple_integral
    locator: Double integral over a normal domain
  - url: https://en.wikipedia.org/wiki/Multiple_integral
    locator: Mathematical definition
---

## Summary

To integrate a function $f$ over a bounded region $D$ that is not a rectangle, take a rectangle $R \supseteq D$. Then integrate over $R$ the function equal to $f$ on $D$ and to $0$ on $R \setminus D$.
For a region between two graphs, $D = \{(x, y) : a \le x \le b, \ \varphi_1(x) \le y \le \varphi_2(x)\}$ with $\varphi_1 \le \varphi_2$ continuous, a continuous $f$ gives $\iint_D f \, dA = \int_a^b \int_{\varphi_1(x)}^{\varphi_2(x)} f(x, y) \, dy \, dx$.

## Remarks

Such a region is normal with respect to the $x$-axis. A region of the form $\{c \le y \le d, \ \psi_1(y) \le x \le \psi_2(y)\}$ is normal with respect to the $y$-axis.
The definition does not depend on the choice of $R$. For continuous $f$, the integral exists when the boundary of $D$ has [[Jordan content|0KTGJW1ZTH]] zero.
Example: for $D = \{0 \le x \le 1, \ x^2 \le y \le 1\}$, $\iint_D x \, dA = \int_0^1 x (1 - x^2) \, dx = 1/4$.
The [[double integral|0WAR4F23B4]] over $D$ is computed as an [[iterated integral|0WZCHE1ZF9]] with variable bounds.

## Explanations

### L1 human

Most regions in practice are not rectangles, but many lie between two curves.
Then the inner integral runs from the lower curve to the upper curve, and the outer integral runs over the range of the other variable.
