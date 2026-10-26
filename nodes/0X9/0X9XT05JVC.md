---
tag: 0X9XT05JVC
kind: statement
role: theorem
name: Uniform limit theorem
aliases: [uniform-limit-of-continuous-functions-is-continuous]
msc: [40A30, 26A15]
uses: [08HJRTG5N7, 0EEE2CZB2A]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_limit_theorem
    locator: Statement
same_as:
  wikidata: Q7885107
  wikipedia: Uniform limit theorem
---

## Statement

Let $S \subseteq \mathbb{R}$, and let $f_n \colon S \to \mathbb{R}$ be continuous for each $n$.
If $f_n \to f$ [[uniformly on $S$|08HJRTG5N7]], then $f$ is continuous on $S$.

## Remarks

Fix $c \in S$ and $\varepsilon > 0$. Choose $n$ with $|f_n - f| < \varepsilon/3$ on $S$, and $\delta$ for the [[continuity|0EEE2CZB2A]] of $f_n$ at $c$.
Then $|f(x) - f(c)| \le |f(x) - f_n(x)| + |f_n(x) - f_n(c)| + |f_n(c) - f(c)| < \varepsilon$ for $|x - c| < \delta$.
The [[sequence $x^n$ on $[0, 1]$|0YSRR1JTKZ]] shows that pointwise convergence is not enough. Mathlib states the theorem as `TendstoUniformly.continuous`.

## History

Augustin-Louis Cauchy claimed in 1821 that a series of continuous functions has a continuous sum, whenever it converges.
In 1826, Niels Henrik Abel found counterexamples among Fourier series. In modern terms, Cauchy's argument needs uniform convergence.

## Explanations

### L1 human

If continuous graphs approach a limit graph uniformly, the limit graph has no jumps.
A jump in the limit would force some $f_n$ to jump as well.
