---
tag: MJGPW5EVB3
kind: statement
role: theorem
name: Ekeland's variational principle
msc: ["58E30", 49J53]
uses: [0BY52JW6NK, RN4G8SGP6P, 4724KRNHAT]
about: [0BY52JW6NK]
sources:
  - url: https://en.wikipedia.org/wiki/Ekeland%27s_variational_principle
same_as:
  wikidata: Q1945203
  wikipedia: Ekeland's variational principle
---

## Statement

Let $(X, d)$ be a [[complete metric space|0BY52JW6NK]].
Let $f \colon X \to (-\infty, +\infty]$ be [[lower semicontinuous|RN4G8SGP6P]], bounded below, and not identically $+\infty$.
Let $\varepsilon > 0$ and $\lambda > 0$, and let $x_0 \in X$ satisfy $f(x_0) \le \inf_X f + \varepsilon$.
Then there is a point $v \in X$ such that:

1. $f(v) \le f(x_0)$;
2. $d(x_0, v) \le \lambda$;
3. $f(w) > f(v) - \dfrac{\varepsilon}{\lambda} d(v, w)$ for every $w \in X$ with $w \ne v$.

## Remarks

The proof builds a sequence $x_0, x_1, x_2, \ldots$.
Each $x_{n+1}$ is chosen in the set of points $y$ with $f(y) \le f(x_n) - (\varepsilon / \lambda) d(x_n, y)$, with $f(x_{n+1})$ close to the infimum of $f$ on that set.
These sets are closed and nested, their diameters tend to $0$, and completeness gives a limit point $v$, which has the three properties.
Taking $\lambda = 1$ on a Banach space with $f$ Gateaux differentiable gives a point $v$ with $f(v) \le \inf f + \varepsilon$ and $\norm{f'(v)} \le \varepsilon$: an almost minimizer with small derivative.
With this, a $C^1$ function that is bounded below and satisfies the [[Palais–Smale condition|4724KRNHAT]] attains its minimum.
Completeness is needed: on $X = (0, 1]$ with $f(x) = x$, $\varepsilon = 1/2$ and $\lambda = 1$, every $v$ violates clause 3 for any $w < v$, because $f(w) = v - (v - w) < v - \tfrac12 (v - w)$.

## Explanations

### L1 human

A function that is bounded below need not have a minimum point.
Ekeland's principle says that one can always find a point that is almost as good as the infimum and that is a strict minimum of a slightly tilted function.
The tilt is a cone of slope $\varepsilon / \lambda$ around the point.
So near-minimizers can always be taken to be "stable" in a precise sense.

### L2 human

The principle is a basic tool of nonsmooth analysis and of critical point theory.
It produces Palais–Smale sequences for functionals bounded below, and it gives short proofs of the Caristi fixed point theorem and of the Bishop–Phelps theorem.
Conversely, a metric space in which the conclusion holds for all such functions is complete, so the principle characterizes completeness.
