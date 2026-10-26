---
tag: 02JGYG0T7M
kind: statement
role: proposition
name: Characteristic function of a sum of independent random variables
msc: ["60E10"]
uses: [0MYDNRT7PP, 05AW1G0WE1, 0XCE070V8B]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_function_(probability_theory)
    locator: Basic manipulations of distributions
---

## Statement

Let $X_1, \dots, X_n$ be [[independent|0XCE070V8B]] real random variables, and let $S = X_1 + \dots + X_n$.
Then for each $t \in \mathbb{R}$, the [[characteristic functions|0MYDNRT7PP]] satisfy
$$\varphi_S(t) = \varphi_{X_1}(t) \, \varphi_{X_2}(t) \cdots \varphi_{X_n}(t).$$

## Remarks

Proof: $e^{itS} = e^{itX_1} \cdots e^{itX_n}$. The factors are independent and bounded, so the [[product rule for expectations|05AW1G0WE1]] applies to their real and imaginary parts.
For i.i.d. $X_i$, $\varphi_S(t) = \varphi_{X_1}(t)^n$. The sample mean has $\varphi_{S/n}(t) = \varphi_{X_1}(t/n)^n$.
The converse is false: $\varphi_{X+Y} = \varphi_X \varphi_Y$ does not imply that $X$ and $Y$ are independent.

## Explanations

### L1 human

Adding independent variables corresponds to multiplying their characteristic functions.
This is the key step in the usual proof of the central limit theorem.
