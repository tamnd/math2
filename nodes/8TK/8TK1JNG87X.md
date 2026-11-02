---
tag: 8TK1JNG87X
kind: definition
name: Tempered distribution
msc: [46F05, 46F10]
defines: AES2T5JPFP
uses: [CG9JEATW3Q, 03TM135G0N]
sources:
  - url: https://en.wikipedia.org/wiki/Distribution_(mathematical_analysis)
---

## Definition

Let $n \ge 1$ and let $\mathcal{S}(\R^n)$ be the [[Schwartz space|CG9JEATW3Q]] of smooth functions $\varphi \colon \R^n \to \C$ such that
$$p_{\alpha,\beta}(\varphi) = \sup_{x \in \R^n} \abs{x^\alpha \partial^\beta \varphi(x)} < \infty$$
for all multi-indices $\alpha$ and $\beta$.
A *tempered distribution* on $\R^n$ is a linear map $T \colon \mathcal{S}(\R^n) \to \C$ for which there are a constant $C \ge 0$ and an integer $N \ge 0$ such that
$$\abs{T(\varphi)} \le C \sum_{\abs{\alpha} \le N, \, \abs{\beta} \le N} p_{\alpha,\beta}(\varphi) \quad \text{for all } \varphi \in \mathcal{S}(\R^n).$$
The space of tempered distributions is written $\mathcal{S}'(\R^n)$.

## Remarks

The inequality says that $T$ is a [[continuous linear map|03TM135G0N]] for the Fréchet topology of $\mathcal{S}(\R^n)$ given by the seminorms $p_{\alpha,\beta}$.
Equivalently, $T(\varphi_k) \to 0$ whenever $p_{\alpha,\beta}(\varphi_k) \to 0$ for all $\alpha, \beta$.

Example: the Dirac delta $\delta(\varphi) = \varphi(0)$ is tempered.
It is linear, and $\abs{\delta(\varphi)} \le p_{0,0}(\varphi)$, so the condition holds with $C = 1$ and $N = 0$.
More generally, if $f$ is measurable and $\int \abs{f(x)} (1 + \abs{x})^{-m} \, dx < \infty$ for some $m \ge 0$, then $\varphi \mapsto \int f \varphi \, dx$ is tempered.

Non-example: on $\R$, the function $\varphi(x) = e^{-\sqrt{1 + x^2}}$ lies in $\mathcal{S}(\R)$, but $\int e^x \varphi(x) \, dx = \infty$.
So the formula $\varphi \mapsto \int e^x \varphi \, dx$ does not define a linear map on all of $\mathcal{S}(\R)$, and $e^x$ gives no tempered distribution.
It still defines a distribution on compactly supported test functions.

Derivatives act by $(\partial^\beta T)(\varphi) = (-1)^{\abs{\beta}} T(\partial^\beta \varphi)$, and the Fourier transform acts by $\hat{T}(\varphi) = T(\hat{\varphi})$.
