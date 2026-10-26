---
tag: 0A8JXHYTJC
kind: counterexample
name: x^2 is not uniformly continuous on the real line
msc: [26A15]
uses: [0Q4DR37DVE, 0P27W9RW0G]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_continuity
    locator: Nonexamples
---

## Counterexample

The function $f \colon \mathbb{R} \to \mathbb{R}$ with $f(x) = x^2$ is [[continuous|0P27W9RW0G]] but not [[uniformly continuous|0Q4DR37DVE]].
For $n \ge 1$, let $x_n = n$ and $y_n = n + 1/n$. Then $|x_n - y_n| = 1/n \to 0$, but
$$f(y_n) - f(x_n) = 2 + \frac{1}{n^2} > 2.$$
So no $\delta$ works for $\varepsilon = 2$.

## Remarks

On each bounded interval $[-c, c]$, the function $x^2$ is Lipschitz with constant $2c$. So it is uniformly continuous there.
The problem is that the slope $2x$ is not bounded on $\mathbb{R}$.

## Explanations

### L1 human

The graph of $x^2$ gets steeper and steeper as $x$ grows.
So a fixed small change in $x$ gives larger and larger changes in $x^2$.
