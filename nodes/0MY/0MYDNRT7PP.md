---
tag: 0MYDNRT7PP
kind: definition
name: Characteristic function
msc: ["60E10"]
defines: 0V5B6D6BQH
uses: [0DCT0QZVQ1, 01ZWX875AT, 04R3CY41VJ, 09FTAET5Z4]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_function_(probability_theory)
    locator: Definition
---

## Definition

Let $X$ be a real random variable with law $\mu_X$. Let $i$ be the imaginary unit in the [[complex numbers|09FTAET5Z4]].
The characteristic function of $X$ is the function $\varphi_X \colon \mathbb{R} \to \mathbb{C}$ with
$$\varphi_X(t) = E\left[e^{itX}\right] = E[\cos(tX)] + i \, E[\sin(tX)] = \int_{\mathbb{R}} e^{itx} \, \mu_X(dx).$$

## Remarks

The expectation exists for all $t$, because $|e^{itX}| = 1$. The second form uses [[Euler's formula|04R3CY41VJ]].
Always $\varphi_X(0) = 1$, $|\varphi_X(t)| \le 1$, and $\varphi_X$ is uniformly continuous on $\mathbb{R}$.
For $a, b \in \mathbb{R}$, $\varphi_{aX + b}(t) = e^{itb} \varphi_X(at)$.
If $E[|X|^k] < \infty$, then $\varphi_X$ is $k$ times continuously differentiable and $\varphi_X^{(k)}(0) = i^k E[X^k]$.

## Explanations

### L1 human

The characteristic function is like the moment-generating function, but with an imaginary argument.
This small change makes it finite for every distribution, so it is a tool that always works.
