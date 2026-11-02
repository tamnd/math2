---
tag: X2AMH38NCR
kind: definition
name: Regularization of ill-posed problems
msc: [65J20, 65F22, 47A52]
defines: WTY54BFC46
uses: [HM2HHE3J51, 0YY8VX28JR, W09B9NZ9B5, M2NEP1K5AE, M68V0M5A3R]
sources:
  - url: https://en.wikipedia.org/wiki/Regularization_(mathematics)
---

## Definition

Let $X, Y$ be [[Hilbert spaces|HM2HHE3J51]], let $T \colon X \to Y$ be a bounded linear operator, and let $T^\dagger$ be its [[Moore–Penrose generalized inverse|0YY8VX28JR]], defined on $\mathcal{D}(T^\dagger) = \mathcal{R}(T) + \mathcal{R}(T)^\perp$.
A *regularization* of $T^\dagger$ is a family $(R_\alpha)_{\alpha > 0}$ of maps $Y \to X$ together with a *parameter choice rule* $\alpha \colon (0, \infty) \times Y \to (0, \infty)$ such that:

1. each $R_\alpha$ is continuous;
2. for every $y \in \mathcal{D}(T^\dagger)$, $\sup \set{ \alpha(\delta, y^\delta) : y^\delta \in Y, \ \norm{y^\delta - y} \le \delta } \to 0$ as $\delta \to 0$;
3. for every $y \in \mathcal{D}(T^\dagger)$, $\sup \set{ \norm{R_{\alpha(\delta, y^\delta)} y^\delta - T^\dagger y} : y^\delta \in Y, \ \norm{y^\delta - y} \le \delta } \to 0$ as $\delta \to 0$.

The pair is then called a *convergent regularization method*.

## Remarks

Example: [[Tikhonov regularization|M68V0M5A3R]] $R_\alpha = (T^* T + \alpha I)^{-1} T^*$ with an a priori rule $\alpha = \alpha(\delta)$ such that $\alpha(\delta) \to 0$ and $\delta^2 / \alpha(\delta) \to 0$.
Each $R_\alpha$ is bounded with $\norm{R_\alpha} \le 1/(2\sqrt{\alpha})$, which gives clause 1.
The error splits as $\norm{R_\alpha y^\delta - T^\dagger y} \le \norm{R_\alpha y - T^\dagger y} + \delta/(2\sqrt{\alpha})$.
The first term tends to $0$ as $\alpha \to 0$ by spectral calculus, and the second by the choice of $\alpha$, which gives clause 3.
Non-example: $R_\alpha = T^\dagger$ for all $\alpha$ fails clause 1 whenever $\mathcal{R}(T)$ is not closed, because $T^\dagger$ is then unbounded.
This happens for every injective [[compact operator|M2NEP1K5AE]] with infinite-dimensional range, the typical model of an ill-posed problem.
Other standard methods are truncated singular value decomposition, [[Landweber iteration|87DV5ZTJ9J]] with the iteration index as parameter, and the discrepancy principle as a parameter choice rule.

## Explanations

### L1 human

A regularization method replaces the unstable inverse by stable approximations, one for each value of a parameter.
The parameter is chosen from the noise level.
The method is convergent when the answers approach the true solution as the noise goes to zero.
