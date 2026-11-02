---
tag: H4XSF8ZPRS
kind: definition
name: Asymptotic scale
msc: [41A60, "30E15"]
defines: XEGB8Y44GG
uses: [00T5EPFQB9]
sources:
  - url: https://en.wikipedia.org/wiki/Asymptotic_expansion
---

## Definition

Let $D$ be a subset of $\R$ or of $\C$ and let $x_0$ be a limit point of $D$, possibly $\infty$.
An *asymptotic scale* (or *asymptotic sequence*) at $x_0$ is a sequence of functions $\varphi_0, \varphi_1, \varphi_2, \dots \colon D \to \C$ such that:

1. each $\varphi_n$ has no zero in $D \cap V$ for some punctured neighbourhood $V$ of $x_0$;
2. for each $n \ge 0$, $\varphi_{n+1}(x) = o\big(\varphi_n(x)\big)$ as $x \to x_0$ in $D$, in [[little o notation|00T5EPFQB9]].

## Remarks

Example: $\varphi_n(x) = (x - x_0)^n$ on $D = \R$ at a finite $x_0$.
These have no zero for $x \ne x_0$, and $\varphi_{n+1}(x) / \varphi_n(x) = x - x_0 \to 0$.

Mixed scales such as $1, \frac{\log x}{x}, \frac1x, \frac{\log x}{x^2}, \frac{1}{x^2}, \dots$ at $\infty$ are also asymptotic scales.

Non-example: $\varphi_n(x) = x^{-n}$ is not an asymptotic scale at $x_0 = 0$, since $\varphi_{n+1}(x)/\varphi_n(x) = 1/x$ does not tend to $0$ there; it is a scale at $\infty$.

Non-example: $\varphi_n(x) = \sin(x)\, x^{-n}$ at $\infty$ on $D = (1, \infty)$ fails clause 1, since every $\varphi_n$ has zeros at $x = k\pi$ for all large $k$.

Some authors drop clause 1 and write the condition 2 as $\varphi_{n+1} = o(\varphi_n)$ in the sense of an inequality $\abs{\varphi_{n+1}} \le \varepsilon \abs{\varphi_n}$ near $x_0$.
