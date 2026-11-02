---
tag: J3MJEDDHNY
kind: definition
name: Decreasing rearrangement
msc: ["46E30", 28A20]
defines: BWS042NC2P
uses: [HQVXKEMN5N, 04KFTA34C5]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_decreasing_rearrangement
---

## Definition

Let $(X, \Sigma, \mu)$ be a measure space and let $f$ be a real or complex measurable function on $X$.
Let $d_f(s) = \mu(\set{\abs{f} > s})$ be the [[distribution function|HQVXKEMN5N]] of $f$.
The *decreasing rearrangement* of $f$ is the function $f^* \colon [0, \infty) \to [0, \infty]$ given by the [[infimum|04KFTA34C5]]
$$f^*(t) = \inf \set{s \ge 0 : d_f(s) \le t},$$
with the convention $\inf \varnothing = \infty$.

## Remarks

Example: let $X = [0, 1]$ with Lebesgue measure and $f(x) = x$.
Then $d_f(s) = 1 - s$ for $0 \le s \le 1$ and $d_f(s) = 0$ for $s \ge 1$.
For $0 \le t < 1$ the condition $d_f(s) \le t$ means $s \ge 1 - t$, so $f^*(t) = 1 - t$.
For $t \ge 1$ every $s \ge 0$ works, so $f^*(t) = 0$.

Non-example: the function $f(x) = x$ on $[0, 1]$ is not its own decreasing rearrangement, since it is increasing.
A function $g \ge 0$ on $[0, \infty)$ is its own rearrangement exactly when it is non-increasing and right-continuous.

The function $f^*$ is non-increasing and right-continuous.
It has the same distribution function as $\abs{f}$ for Lebesgue measure on $[0, \infty)$.
Hence $\int_0^\infty (f^*)^p \, dt = \int_X \abs{f}^p \, d\mu$ for $0 < p < \infty$.
The *symmetric decreasing rearrangement* of a function on $\R^n$ is a related notion: it is radial, decreasing in $\abs{x}$, and equimeasurable with $\abs{f}$.
