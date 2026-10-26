---
tag: ~0e7ed5aa
kind: statement
role: theorem
name: Uniform limits of holomorphic functions are holomorphic
aliases: [weierstrass-convergence-theorem]
msc: [30A99]
uses: [~1a187203, ~34ebf5e1, ~d54124c3]
sources:
  - url: https://en.wikipedia.org/wiki/Morera%27s_theorem
    locator: Uniform limits
  - url: https://en.wikipedia.org/wiki/Holomorphic_function
    locator: Properties
---

## Statement

Let $U \subseteq \mathbb{C}$ be an open set and let $f_1, f_2, \dots$ be functions $U \to \mathbb{C}$ that are [[holomorphic|~1a187203]] on $U$.
Let $f : U \to \mathbb{C}$ be a function such that $f_n \to f$ uniformly on each compact subset of $U$.
Then $f$ is holomorphic on $U$. Moreover, $f_n' \to f'$ uniformly on each compact subset of $U$.

## Remarks

Proof idea: $f$ is continuous. On each disc in $U$, [[Cauchy's integral theorem|~d54124c3]] gives $\oint_{\partial T} f_n = 0$ for each triangle $T$, so $\oint_{\partial T} f = 0$ by the uniform convergence, and [[Morera's theorem|~34ebf5e1]] applies.
A main use: if a series $\sum g_k$ of holomorphic functions converges uniformly on compact subsets of $U$, then its sum is holomorphic on $U$.
There is no real analogue. On $[-1, 1]$, the polynomials converge uniformly to $|x|$, which is not differentiable at $0$.

## Explanations

### L1 human

If holomorphic functions get close to a function $f$ uniformly, then $f$ is holomorphic too, and their derivatives get close to the derivative of $f$.
This lets us build new holomorphic functions as limits of series, for example the zeta function $\sum n^{-z}$.
