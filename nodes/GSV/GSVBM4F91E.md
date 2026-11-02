---
tag: GSVBM4F91E
kind: definition
name: Hyers–Ulam stability
msc: [39B82]
defines: TPYXQTYND6
uses: [0VKD1TP7F3, SRAN4EKWS0]
sources:
  - url: https://en.wikipedia.org/wiki/Hyers%E2%80%93Ulam%E2%80%93Rassias_stability
---

## Definition

Let $X$ be a nonempty set, let $k \ge 1$, and let $(Y, d)$ be a [[metric space|0VKD1TP7F3]].
Let $\mathcal{F}$ be a set of maps $X \to Y$, and let $E_1, E_2$ assign to each $f \in \mathcal{F}$ a map $X^k \to Y$.
Consider the [[functional equation|SRAN4EKWS0]] $E_1(f)(u) = E_2(f)(u)$ for all $u \in X^k$.
The equation is *Hyers–Ulam stable* in $\mathcal{F}$ if there is a constant $K > 0$ such that the following holds for every $\delta \ge 0$.
If $f \in \mathcal{F}$ satisfies $d(E_1(f)(u), E_2(f)(u)) \le \delta$ for all $u \in X^k$, then there is a solution $g \in \mathcal{F}$ of the equation with $d(f(x), g(x)) \le K \delta$ for all $x \in X$.

## Remarks

Example: the Cauchy equation $f(x + y) = f(x) + f(y)$ for maps from a normed space to a Banach space is Hyers–Ulam stable with $K = 1$; here $k = 2$, $E_1(f)(x, y) = f(x + y)$ and $E_2(f)(x, y) = f(x) + f(y)$.
Non-example: the periodicity equation $f(x + 1) = f(x)$ for maps $\R \to \R$ is not stable.
For $\delta > 0$ the map $f(x) = \delta x$ satisfies $\abs{f(x + 1) - f(x)} = \delta$.
If $g$ is $1$-periodic, then $f(x + n) - g(x + n) = f(x) - g(x) + n\delta$ for every integer $n$, so $f - g$ is unbounded and no $K$ works.
Some authors use a weaker form: for every $\varepsilon > 0$ there is $\delta > 0$ such that a $\delta$-approximate solution lies within $\varepsilon$ of a solution.
In the Hyers–Ulam–Rassias form, the constant bound $\delta$ is replaced by a control function such as $\theta(\norm{x}^p + \norm{y}^p)$.
