---
tag: ~94fb8ffd
kind: statement
role: theorem
name: Power series of cosine
msc: [33B10, 30B10]
uses: [~45dd0733, ~e909ddc3, ~c87f36c5]
sources:
  - url: https://en.wikipedia.org/wiki/Sine_and_cosine
    locator: Series and polynomials
---

## Statement

For every real $x$, the series $\sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!}$ converges absolutely, and
$$\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots.$$
This series is the [[Maclaurin series|~c87f36c5]] of the cosine function.

## Remarks

The [[ratio of the terms|~e909ddc3]] is $\frac{x^2}{(2n+1)(2n+2)} \to 0$. So the radius of convergence is $\infty$.
For $|x| \le 1$, the terms decrease in size. So the partial sums lie alternately above and below $\cos x$.
Mathlib states the series as `Real.hasSum_cos`.

## Explanations

### L1 human

Cosine is an infinite even polynomial with alternating signs.
Near $0$, $\cos x$ is close to $1 - x^2/2$.
