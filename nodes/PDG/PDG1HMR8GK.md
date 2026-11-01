---
tag: PDG1HMR8GK
kind: definition
name: Laguerre–Pólya class
msc: ["30D15", "30C15", "26C10"]
defines: X9SRCEENV3
uses: [0419794R0T, 00EHX6FWC0, 08FPABDQ4C, ACSF58HYDH]
sources:
  - url: https://en.wikipedia.org/wiki/Laguerre%E2%80%93P%C3%B3lya_class
---

## Definition

An [[entire function|0419794R0T]] $f$ belongs to the *Laguerre–Pólya class* if there is a sequence $(P_k)$ of polynomials such that:

1. each $P_k$ has real coefficients;
2. all [[roots|00EHX6FWC0]] of each $P_k$ are real;
3. $P_k \to f$ [[uniformly|08FPABDQ4C]] on every compact subset of $\C$.

The class is written $\mathcal{L}\text{-}\mathcal{P}$.

## Remarks

A function $f$ that is not identically zero belongs to the class if and only if
$$f(z) = c\, z^m e^{-a z^2 + b z} \prod_{n} \left(1 - \frac{z}{x_n}\right) e^{z/x_n}.$$
Here $c, b \in \R$ with $c \ne 0$, $a \ge 0$, and $m \ge 0$ is an integer.
The $x_n$ are nonzero real numbers with $\sum_n x_n^{-2} < \infty$, and the product is a [[Weierstrass product|ACSF58HYDH]].
Example: $e^{-z^2}$ is the limit of the polynomials $(1 - z^2/k)^k$, which have real coefficients and only the real roots $\pm\sqrt{k}$.
Example: $\sin z = z \prod_{n \ge 1} (1 - z^2/(n^2\pi^2))$ is in the class.
Non-example: $1 + z^2$ has real coefficients but the roots $\pm i$.
It is not a limit of real-rooted real polynomials, because by Hurwitz's theorem such limits, when not identically zero, have only real zeros.
Non-example: $e^{z^2}$ has no zeros, but its product form would need $a = -1 < 0$.
The class is closed under differentiation.
