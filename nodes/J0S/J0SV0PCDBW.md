---
tag: J0SV0PCDBW
kind: definition
name: Region of convergence
msc: [44A55, 30B10]
defines: 1P8WX3EGHF
uses: [5FY0JQGHYZ, 0GXMPDNYX3, 0CW52NV5TC, 0N288P2TB5]
sources:
  - url: https://en.wikipedia.org/wiki/Z-transform
    locator: Region of convergence
---

## Definition

Let $x = (x_n)_{n \in \Z}$ be a sequence of complex numbers, with [[Z-transform|5FY0JQGHYZ]] $X(z) = \sum_{n \in \Z} x_n z^{-n}$.
The *region of convergence* of $X$ is the set
$$\mathrm{ROC}(x) = \set{ z \in \C \setminus \set{0} : \sum_{n \in \Z} \abs{x_n} \abs{z}^{-n} < \infty }.$$

## Remarks

Let $r = \limsup_{n \to \infty} \abs{x_n}^{1/n}$ and $1/R = \limsup_{n \to \infty} \abs{x_{-n}}^{1/n}$, with the conventions $1/0 = \infty$ and $1/\infty = 0$.
By the root test, the open [[annulus|0CW52NV5TC]] $r < \abs{z} < R$ lies in the region, and no point with $\abs{z} < r$ or $\abs{z} > R$ does.
This is the [[radius of convergence|0N288P2TB5]] argument applied to each half of the [[Laurent series|0GXMPDNYX3]].
Points on the circles $\abs{z} = r$ and $\abs{z} = R$ may or may not belong to it.
Example: $x_n = 1$ for $n \ge 0$ and $x_n = 0$ for $n < 0$ has region $\abs{z} > 1$; the point $z = 1$ fails because $\sum_{n \ge 0} 1$ diverges.
Non-example: $z = 1/2$ is not in the region of $x_n = 2^n$ ($n \ge 0$), since $\sum 2^n 2^n$ diverges.
Some texts add the point $z = \infty$ to the region of a sequence with $x_n = 0$ for $n < 0$, or $z = 0$ for a sequence with $x_n = 0$ for $n > 0$.
