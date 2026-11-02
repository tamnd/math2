---
tag: 3MHP17HY7N
kind: definition
name: Uniform convergence of series
msc: [40A30]
defines: MAHHKQST2A
uses: [0MRE6XRE5V, 08FPABDQ4C, 08HJRTG5N7]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_convergence
---

## Definition

Let $S$ be a set, and let $f_n \colon S \to \C$ be functions for $n \ge 0$.
Let $s_N = \sum_{n=0}^{N} f_n$ be the partial sums of the [[series of functions|0MRE6XRE5V]] $\sum_{n=0}^{\infty} f_n$, and let $f \colon S \to \C$ be a function.
The series *converges uniformly* to $f$ on $S$ if the sequence $(s_N)$ converges [[uniformly|08FPABDQ4C]] to $f$ on $S$.
That is, for every $\varepsilon > 0$ there is an integer $N_0$ such that $\abs{s_N(x) - f(x)} < \varepsilon$ for all $N \ge N_0$ and all $x \in S$.

## Remarks

Equivalently, the series converges at each point of $S$ and $\sup_{x \in S} \abs{\sum_{n > N} f_n(x)} \to 0$ as $N \to \infty$.
A Cauchy form also holds: the series converges uniformly on $S$ if and only if for every $\varepsilon > 0$ there is $N_0$ with $\abs{\sum_{n=M+1}^{N} f_n(x)} < \varepsilon$ for all $N > M \ge N_0$ and all $x \in S$.
For a subset of a larger domain, this is [[uniform convergence on a set|08HJRTG5N7]] of the partial sums.

Example: let $0 < r < 1$ and $f_n(x) = x^n$ on $S = [0, r]$, with $f(x) = 1/(1 - x)$.
The tail is $\sum_{n > N} x^n = x^{N+1}/(1 - x) \le r^{N+1}/(1 - r)$ for all $x \in S$, and this bound tends to $0$.
So the series converges uniformly on $[0, r]$.

Non-example: the same series on $S = [0, 1)$ converges at each point to $1/(1 - x)$, but not uniformly.
For each $N$, the tail $x^{N+1}/(1 - x)$ tends to $\infty$ as $x \to 1^-$, so its supremum over $S$ is infinite.

The [[Weierstrass M-test|0NX5NWAFC9]] is the usual way to prove uniform convergence.

## Explanations

### L1 human

At each point $x$, the series is an ordinary series of numbers, and its partial sums approach $f(x)$.
The series converges uniformly when one number of terms is enough to make the error small at every point at once.
For $\sum x^n$, this works on $[0, r]$ with $r < 1$, but not on $[0, 1)$, where points near $1$ need more and more terms.
