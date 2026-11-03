---
tag: GMA7HAE86K
kind: definition
name: Global optimization
msc: [90C26]
defines: ZCFQEZ0A0V
uses: [09WRNGPTMV, 04KFTA34C5]
sources:
  - url: https://en.wikipedia.org/wiki/Global_optimization
---

## Definition

Let $X$ be a nonempty set and let $f \colon X \to \R$.
A point $x^* \in X$ is a *global minimizer* of $f$ on $X$ if $f(x^*) \le f(x)$ for all $x \in X$.
Then $f(x^*)$ is the *global minimum* of $f$ on $X$.
For $\varepsilon > 0$, a point $x \in X$ is an *$\varepsilon$-global minimizer* if $f(x) \le \inf_X f + \varepsilon$, where $\inf_X f$ is the [[infimum|04KFTA34C5]] of $f$ on $X$.
*Global optimization* is the problem of finding a global minimizer, or an $\varepsilon$-global minimizer, and the global minimum value.

## Remarks

When $X \subseteq \R^n$, a global minimizer is a [[local minimizer|09WRNGPTMV]], but a local minimizer need not be global.
Maximization problems are included, since a global maximizer of $f$ is a global minimizer of $-f$.

Example: let $f(x) = (x^2 - 1)^2$ on $X = \R$.
Then $f \ge 0$, and $f(1) = f(-1) = 0$, so $1$ and $-1$ are global minimizers and the global minimum is $0$.

Non-example: let $f(x) = x^3 - 3x$ on $X = \R$.
The point $x = 1$ is a local minimizer, with $f(1) = -2$.
It is not a global minimizer, since $f(-3) = -18 < -2$; indeed $f$ is unbounded below, and there is no global minimizer.
