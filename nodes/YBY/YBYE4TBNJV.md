---
tag: YBYE4TBNJV
kind: statement
role: theorem
name: Approximation by convolution with mollifiers
msc: ["46E35", 42B35, "46E30"]
uses: [CQMK4YPE1J, 2Z29JN3VES, SASP14MA1Z, 0V33BNKZ9S, 0X3WGX95FE]
about: [CQMK4YPE1J]
sources:
  - url: https://en.wikipedia.org/wiki/Mollifier
---

## Statement

Let $\varphi$ be a [[mollifier|CQMK4YPE1J]] on $\R^n$, let $\varphi_\varepsilon(x) = \varepsilon^{-n} \varphi(x/\varepsilon)$ for $\varepsilon > 0$, and let $f$ be a locally integrable function on $\R^n$.
Put $f_\varepsilon = \varphi_\varepsilon * f$, the [[convolution|2Z29JN3VES]] $f_\varepsilon(x) = \int_{\R^n} \varphi_\varepsilon(x - y) f(y) \, dy$.
Then:

1. $f_\varepsilon$ is a [[smooth function|0V33BNKZ9S]], and $\partial^\alpha f_\varepsilon = (\partial^\alpha \varphi_\varepsilon) * f$ for every multi-index $\alpha$.
2. If $f$ vanishes almost everywhere outside a closed set $K$, then $f_\varepsilon$ vanishes outside $\set{x : \operatorname{dist}(x, K) \le \varepsilon}$.
3. If $f$ is [[continuous|0X3WGX95FE]], then $f_\varepsilon \to f$ uniformly on every compact set as $\varepsilon \to 0$.
4. If $f \in L^p(\R^n)$ with $1 \le p < \infty$, then $\norm{f_\varepsilon}_{L^p} \le \norm{f}_{L^p}$ and $\norm{f_\varepsilon - f}_{L^p} \to 0$ as $\varepsilon \to 0$.

## Remarks

Part 1 follows by differentiating under the integral sign, which is allowed because $\varphi_\varepsilon$ has bounded derivatives and compact support.
Part 2 holds because $\varphi_\varepsilon(x - y) = 0$ when $\abs{x - y} > \varepsilon$.
For parts 3 and 4, write $f_\varepsilon(x) - f(x) = \int \varphi_\varepsilon(y) \big( f(x - y) - f(x) \big) dy$, an average of differences over $\abs{y} \le \varepsilon$.
For continuous $f$, uniform continuity on compact sets makes it small.
For $f \in L^p$, Minkowski's integral inequality bounds its norm by $\sup_{\abs{y} \le \varepsilon} \norm{f(\cdot - y) - f}_{L^p}$.
This tends to $0$ by the continuity of translation in $L^p$.
The bound $\norm{f_\varepsilon}_{L^p} \le \norm{f}_{L^p}$ is [[Young's convolution inequality|JXDKJCBXJ8]] with $\norm{\varphi_\varepsilon}_{L^1} = 1$.

Consequence: for $1 \le p < \infty$ the [[bump functions|HS65DW0HXH]] are dense in $L^p(\R^n)$.
Indeed, first cut $f$ off to a large ball, then mollify, and use parts 1, 2 and 4.

Part 4 fails for $p = \infty$.
If $f$ is the indicator function of $[0, \infty)$ on $\R$, then each $f_\varepsilon$ is continuous, so $\norm{f_\varepsilon - f}_{L^\infty} \ge 1/2$ for all $\varepsilon$.

## Explanations

### L1 human

Blurring a function with a narrow smooth blob gives a smooth function.
If the blob is narrow enough, the blurred function is as close as one wants to the original.
The closeness is uniform for continuous functions and in the $L^p$ sense for $L^p$ functions.
So rough functions can be replaced by smooth ones, at a small cost.

### L2 human

This theorem is the workhorse behind density arguments in analysis.
To prove an identity or an inequality for all $f \in L^p$ or all $f$ in a [[Sobolev space|M4CEZ5K9HP]], one proves it for smooth functions and passes to the limit.
Mollification commutes with weak derivatives, $\partial^\alpha (\varphi_\varepsilon * f) = \varphi_\varepsilon * \partial^\alpha f$, so the same argument shows that smooth functions are dense in $W^{k,p}(\R^n)$.
At a Lebesgue point of $f$, $f_\varepsilon(x) \to f(x)$, so the convergence also holds almost everywhere.
