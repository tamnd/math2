---
tag: P8TMYNPSYD
kind: statement
role: theorem
name: Lorentz's characterization of almost convergence
msc: [40H05, 40C05]
uses: [8HTHB1QPZY, SYF2ND6J97, 0A8JNBGT2Z, QB5AE3VYZZ]
about: [8HTHB1QPZY]
sources:
  - url: https://en.wikipedia.org/wiki/Banach_limit
---

## Statement

Let $x = (x_n)_{n \ge 1}$ be a [[bounded sequence|0A8JNBGT2Z]] of real numbers and let $L$ be a real number.
Then $x$ is [[almost convergent|8HTHB1QPZY]] to $L$ if and only if
$$\lim_{p \to \infty} \frac{1}{p} \sum_{k = n}^{n + p - 1} x_k = L \quad \text{uniformly in } n \ge 1.$$

## Remarks

Proof idea for "if": let $\varphi$ be a [[Banach limit|SYF2ND6J97]] and $\varepsilon > 0$.
By shift invariance, $\varphi(x)$ equals $\varphi$ of the sequence of block averages $y_n = \frac{1}{p} \sum_{k=n}^{n+p-1} x_k$.
For $p$ large, $\abs{y_n - L} \le \varepsilon$ for all $n$, and positivity of $\varphi$ then gives $\abs{\varphi(x) - L} \le \varepsilon$.
For "only if", one shows with the [[Hahn–Banach theorem|QB5AE3VYZZ]] that Banach limits take every value between the lower and upper limits of the uniform block averages.

Example: for $x = (1, 0, 1, 0, \dots)$, any block of $p$ consecutive terms has sum $\floor{p/2}$ or $\ceil{p/2}$, so the averages tend to $1/2$ uniformly in $n$.

The uniformity in $n$ is necessary.
Let $x_n = 1$ when $4^k \le n < 4^k + k$ for some integer $k \ge 1$, and $x_n = 0$ otherwise.
Among $x_1, \dots, x_N$ there are at most about $(\log_4 N)^2$ ones, so the averages starting at $n = 1$ tend to $0$.
But the block of length $k$ starting at $4^k$ has average $1$, so the convergence is not uniform in $n$ and $x$ is not almost convergent.

## Explanations

### L1 human

A bounded sequence is almost convergent to $L$ exactly when the average of any long run of consecutive terms is close to $L$, no matter where the run starts.
This turns a definition about abstract functionals into a concrete test.

### L2 human

The definition of almost convergence quantifies over all Banach limits, which exist only by the Hahn–Banach theorem and cannot be written down.
Lorentz's theorem replaces this by a computable condition on block averages.
It also shows that almost convergence is a summability method in its own right.
For bounded sequences it lies between ordinary convergence and Cesàro summability, because the case $n = 1$ of the condition is Cesàro convergence.
