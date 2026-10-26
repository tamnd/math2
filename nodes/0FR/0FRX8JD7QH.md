---
tag: 0FRX8JD7QH
kind: definition
name: Grönwall bound
msc: [34A40]
defines: 0ZPQHH37PF
uses: [07EJHQYR9A]
sources:
  - url: https://en.wikipedia.org/wiki/Gr%C3%B6nwall%27s_inequality
    locator: Differential form
---

## Definition

Let $\delta, K, \varepsilon$ be real numbers.
The Grönwall bound with these parameters is the function $G_{\delta, K, \varepsilon} : \mathbb{R} \to \mathbb{R}$ given by
$$G_{\delta, K, \varepsilon}(x) = \begin{cases} \delta\, e^{K x} + \dfrac{\varepsilon}{K} \left( e^{K x} - 1 \right) & \text{if } K \neq 0, \\ \delta + \varepsilon x & \text{if } K = 0. \end{cases}$$

## Remarks

The function $v = G_{\delta, K, \varepsilon}$ is the unique solution of $v' = K v + \varepsilon$, $v(0) = \delta$.
For $\varepsilon = 0$, it is $\delta e^{K x}$.
A form of [[Grönwall's inequality|07EJHQYR9A]] uses it: let $f : [a, b] \to \mathbb{R}^n$ be continuous and differentiable on $(a, b)$, with $\|f(a)\| \le \delta$ and $\|f'(x)\| \le K \|f(x)\| + \varepsilon$ on $(a, b)$. Then $\|f(x)\| \le G_{\delta, K, \varepsilon}(x - a)$ on $[a, b]$.
The [[estimate for approximate solutions|0JTPMCCZT2]] is stated with this bound.

## Explanations

### L1 human

Suppose that a quantity starts at most at $\delta$ and grows at most at rate $K$ times itself plus $\varepsilon$. The Grönwall bound is the largest value that it can reach.
It is the solution of the extreme case, where both inequalities are equalities.
