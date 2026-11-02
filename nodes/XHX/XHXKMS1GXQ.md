---
tag: XHXKMS1GXQ
kind: statement
role: theorem
name: Decay of Fourier coefficients and smoothness
msc: [42A16]
uses: [5NN2YZZR3V, WVKDC011KP, 0V33BNKZ9S, CSYZGA5YKS, 0ATF6Q0633]
about: [5NN2YZZR3V]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_series
---

## Statement

Let $f \colon \R \to \C$ be a [[periodic function|0ATF6Q0633]] of period $2\pi$ that is integrable on $[-\pi, \pi]$, with [[Fourier coefficients|5NN2YZZR3V]] $\hat f(n)$, and let $k \ge 0$ be an integer.

1. If $f$ is $k$ times continuously differentiable, then $\widehat{f^{(k)}}(n) = (in)^k \hat f(n)$ for all $n$, and $\abs{n}^k \abs{\hat f(n)} \to 0$ as $\abs{n} \to \infty$.
2. If $\sum_{n \in \Z} \abs{n}^k \abs{\hat f(n)} < \infty$, then $f$ is equal almost everywhere to a $k$ times continuously differentiable function $g$, and $g^{(j)}(x) = \sum_{n \in \Z} (in)^j \hat f(n) e^{inx}$ for $0 \le j \le k$ and all $x$.
3. $f$ is equal almost everywhere to a [[smooth function|0V33BNKZ9S]] if and only if, for every $m \ge 0$, some constant $C_m$ satisfies $\abs{\hat f(n)} \le C_m (1 + \abs{n})^{-m}$ for all $n$.

## Remarks

For part 1, integration by parts over a period gives $\widehat{f'}(n) = in \hat f(n)$, since the boundary terms cancel by periodicity; induction gives the formula for $f^{(k)}$.
The [[Riemann–Lebesgue lemma|WVKDC011KP]] applied to $f^{(k)}$ then gives $\widehat{f^{(k)}}(n) \to 0$.
For part 2, the series $\sum (in)^j \hat f(n) e^{inx}$ converge uniformly by the Weierstrass M-test, so their sums are continuous.
This justifies term-by-term differentiation.
The sum $g$ has the same Fourier coefficients as $f$, so $g = f$ almost everywhere, as in the [[uniform convergence of absolutely summable Fourier series|CSYZGA5YKS]].
Part 3 follows from parts 1 and 2, since a bound $C_{m+2} (1 + \abs{n})^{-m-2}$ makes $\sum \abs{n}^m \abs{\hat f(n)}$ finite.
Example: the sawtooth $f(x) = x$ on $(-\pi, \pi)$ has a jump, and $\abs{\hat f(n)} = 1/\abs{n}$ decays only like $1/\abs{n}$.
The triangle wave $\abs{x}$ is continuous with a piecewise continuous derivative, and its coefficients decay like $1/n^2$.
Part 1 gives only $o(\abs{n}^{-k})$ and part 2 needs slightly more than $O(\abs{n}^{-k-1})$, so there is a gap between the two directions for a fixed $k$.

## Explanations

### L1 human

A smooth function has small high-frequency content, and a rough function has a lot of it.
Each derivative that $f$ possesses makes its Fourier coefficients decay faster by one power of $\abs{n}$.
A jump or a corner in the graph shows up as slow decay of the coefficients.

### L2 human

This dictionary between regularity and decay is used constantly.
It explains why Fourier series of smooth functions converge very fast, and why the Fourier series of a function with a jump converges slowly and shows the Gibbs phenomenon.
It is the starting point of Sobolev spaces on the circle, where smoothness of order $s$ is measured by $\sum (1 + n^2)^s \abs{\hat f(n)}^2 < \infty$.
For real analytic functions the coefficients decay exponentially, and conversely.
