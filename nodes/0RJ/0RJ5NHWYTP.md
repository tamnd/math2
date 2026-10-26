---
tag: 0RJ5NHWYTP
kind: concept
name: Picard iteration
aliases: [successive-approximations]
msc: [34A12, 34A45]
uses: [00WAVB68F9, 015KK993C5, 08XDXP86XE]
sources:
  - url: https://en.wikipedia.org/wiki/Picard%E2%80%93Lindel%C3%B6f_theorem
    locator: Proof sketch
  - url: https://en.wikipedia.org/wiki/Picard%E2%80%93Lindel%C3%B6f_theorem
    locator: Example of Picard iteration
---

## Summary

Picard iteration is the construction of a solution of $x' = f(t, x)$, $x(t_0) = x_0$ as a limit of successive approximations.
One starts with the constant curve $\varphi_0(t) = x_0$ and sets $\varphi_{k+1} = P \varphi_k$, where $P$ is the [[Picard operator|00WAVB68F9]]: $\varphi_{k+1}(t) = x_0 + \int_{t_0}^{t} f(s, \varphi_k(s))\, ds$.
Under the [[Picard–Lindelöf hypotheses|0J7HF2PF1H]], the curves $\varphi_k$ converge uniformly on the time interval to the unique solution.

## Remarks

Example: for $x' = x$, $x(0) = 1$, the iterates are $\varphi_k(t) = \sum_{j=0}^{k} t^j / j!$. They converge to $e^t$.
Let $K$ be the Lipschitz constant and $T$ the length of the time interval. The error after $k$ steps is at most $C (K T)^{k} / k!$ for a constant $C$. See [[an iterate of the Picard operator is a contraction|08XDXP86XE]].

## Explanations

### L1 human

Start with a rough guess, the constant $x_0$.
Put the guess into the right side of the integral equation to get a better guess, and repeat.
Each step improves the approximation, and the guesses converge to the solution.
