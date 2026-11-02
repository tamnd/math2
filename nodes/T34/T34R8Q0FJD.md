---
tag: T34R8Q0FJD
kind: definition
name: Rate of convergence
msc: [40A05, 65B99]
defines: YWZQC5E54B
uses: [0CTV783HYT, 05M5SWSZZD]
sources:
  - url: https://en.wikipedia.org/wiki/Rate_of_convergence
---

## Definition

Let $(x_k)_{k \ge 0}$ be a [[real sequence|0CTV783HYT]] that converges to a [[limit|05M5SWSZZD]] $L$, with $x_k \ne L$ for all $k$.
Let $e_k = \abs{x_k - L}$ be the error at step $k$.

1. The sequence *converges linearly* with *rate* $\mu$ if $\lim_{k \to \infty} e_{k+1} / e_k = \mu$ for some $\mu \in (0, 1)$.
2. It *converges superlinearly* if $\lim_{k \to \infty} e_{k+1} / e_k = 0$, and *sublinearly* if $\lim_{k \to \infty} e_{k+1} / e_k = 1$.
3. For a real number $q > 1$, it *converges with order* $q$ if $\lim_{k \to \infty} e_{k+1} / e_k^q = \mu$ for some $\mu > 0$.

Order $2$ is called *quadratic* convergence and order $3$ *cubic* convergence.
The same definitions apply to sequences in a normed space, with $e_k = \norm{x_k - L}$.

## Remarks

Example: $x_k = 2^{-k}$ tends to $0$, and $e_{k+1} / e_k = 1/2$, so it converges linearly with rate $1/2$.
Example: $x_k = 2^{-2^k}$ tends to $0$, and $e_{k+1} / e_k^2 = 2^{-2^{k+1}} / 2^{-2^{k+1}} = 1$, so it converges quadratically.
Non-example of clause 1: $x_k = 1/(k+1)$ tends to $0$, but $e_{k+1} / e_k = (k+1)/(k+2) \to 1$, so it converges only sublinearly.
These notions are often called Q-linear and Q-quadratic convergence, where Q stands for "quotient".
A weaker notion, R-convergence, asks only that $e_k \le \varepsilon_k$ for some sequence $(\varepsilon_k)$ that tends to $0$ with the given order.
