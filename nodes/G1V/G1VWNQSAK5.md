---
tag: G1VWNQSAK5
kind: statement
role: theorem
name: James's theorem
msc: [46B10]
uses: [06GZ956657, 4A82S5FVRT, NN8RWPC8WG]
about: [NN8RWPC8WG]
sources:
  - url: https://en.wikipedia.org/wiki/James%27s_theorem
same_as:
  wikidata: Q1780722
  wikipedia: James's theorem
---

## Statement

Let $X$ be a [[Banach space|06GZ956657]] over $\R$ or $\C$, and let $X^*$ be its [[continuous dual space|4A82S5FVRT]].
Then $X$ is [[reflexive|NN8RWPC8WG]] if and only if every $f \in X^*$ attains its norm on the closed unit ball.
That is, for every $f \in X^*$ there is $x \in X$ with $\norm{x} \le 1$ and $\abs{f(x)} = \norm{f}$.

## Remarks

The direction "reflexive implies norm attaining" is short.
In a reflexive space the closed unit ball is weakly compact, and $x \mapsto \abs{f(x)}$ is weakly continuous, so it attains its maximum $\norm{f}$.
The converse is the deep part, and its proof by James is long and combinatorial.

The theorem gives a concrete test for non-reflexivity.
On $c_0$, the functional $f(x) = \sum_{n \ge 1} 2^{-n} x_n$ has norm $\sum_n 2^{-n} = 1$.
For $x \in c_0$ with $\norm{x}_\infty \le 1$, some coordinate has $\abs{x_n} < 1$, so $\abs{f(x)} < 1$.
So $f$ does not attain its norm, and $c_0$ is not reflexive.

## Explanations

### L1 human

Every bounded linear functional has a norm, which is the supremum of its values on the unit ball.
The theorem says that this supremum is always a maximum exactly in the reflexive spaces.
So reflexivity, which is defined through the double dual, can be seen by looking at single functionals.

### L2 human

James's theorem is used in optimization and convex analysis, where the existence of maximizers of linear functionals on the unit ball matters.
It contrasts with the Bishop–Phelps theorem, which says that in every Banach space the norm-attaining functionals are dense in $X^*$.
It sits beside the [[Eberlein–Šmulian theorem|2MTN8CQWME]] and the [[Goldstine theorem|K4S9G3AQBM]] as a main characterization of weak compactness and reflexivity.
