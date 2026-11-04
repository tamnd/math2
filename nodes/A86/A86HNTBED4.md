---
tag: A86HNTBED4
kind: proof
name: Proof of the derivative of the logarithm by the inverse function rule
msc: [33B10, 26A24]
proves: 07X1QA6BRW
uses: [0044CPHJBV, 0RKW2X63YR, 0RMVS7RXZX, 0M0RZ3HSB0, 0EX9GFJ0B3, 07ZMX4ANJS, 0KN2V7840E, 0P9BNBW2W3]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_function_rule
---

## Proof

1. Let $f = \exp \colon \mathbb{R} \to \mathbb{R}$ be the [[exponential function|0RMVS7RXZX]]. The domain $\mathbb{R}$ is an open interval.
2. By [[$\exp' = \exp$|0EX9GFJ0B3]], $f$ is differentiable at every point, with $f'(y) = e^y$.
3. A [[differentiable function is continuous|07ZMX4ANJS]], so $f$ is continuous. By [[this result|0KN2V7840E]], $f$ is strictly increasing.
4. By [[positivity of the exponential|0P9BNBW2W3]], $f'(y) = e^y > 0$ for every real $y$. In particular $f'(y) \ne 0$.
5. Let $x > 0$, and let $a = \ln x$, where $\ln$ is the [[natural logarithm|0044CPHJBV]]. By [[the inverse relation of $\ln$ and $\exp$|0RKW2X63YR]], $f(a) = e^{\ln x} = x$.
6. Every value $e^y$ is positive, and every $x > 0$ equals $e^{\ln x}$. So the image $f(\mathbb{R})$ is $(0, \infty)$.
7. Also $\ln(e^y) = y$ for every real $y$. So $\ln \colon (0, \infty) \to \mathbb{R}$ is the inverse function $f^{-1}$.
8. By the [[inverse function rule|0M0RZ3HSB0]] at the point $a$, the function $f^{-1} = \ln$ is differentiable at $x = f(a)$.
9. The same rule gives $\ln'(x) = \frac{1}{f'(a)} = \frac{1}{e^{\ln x}} = \frac{1}{x}$.
10. Since $x > 0$ was arbitrary, $\ln$ is differentiable on $(0, \infty)$, and $\frac{d}{dx} \ln x = \frac{1}{x}$ for $x > 0$.

## Idea

The logarithm undoes the exponential, so its graph is the graph of $\exp$ reflected in the line $y = x$. Reflection turns a tangent slope $m$ into $1/m$. The slope of $\exp$ at $\ln x$ is $e^{\ln x} = x$, so the slope of $\ln$ at $x$ is $1/x$.
