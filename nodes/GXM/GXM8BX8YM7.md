---
tag: GXM8BX8YM7
kind: statement
role: theorem
name: Closed graph theorem
msc: [46A30, 47A05]
uses: [06GZ956657, 0NRYHJPQG2, 03TM135G0N, 0JBJYT69ZV, 0ZCK8DQYN1]
about: [03TM135G0N, 0JBJYT69ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Closed_graph_theorem_(functional_analysis)
same_as:
  wikidata: Q104845546
  wikipedia: Closed graph theorem (functional analysis)
---

## Statement

Let $X$ and $Y$ be [[Banach spaces|06GZ956657]] over $\R$ or $\C$, and let $T \colon X \to Y$ be a [[linear map|0NRYHJPQG2]].
Give $X \times Y$ the norm $\norm{(x, y)} = \norm{x} + \norm{y}$.
Then $T$ is [[continuous|03TM135G0N]] if and only if its [[graph|0JBJYT69ZV]] $\Gamma(T) = \set{(x, Tx) : x \in X}$ is [[closed|0ZCK8DQYN1]] in $X \times Y$.

## Remarks

If $T$ is continuous, its graph is closed because $Y$ is Hausdorff.
Conversely, if $\Gamma(T)$ is closed, it is a Banach space, and the projection $(x, Tx) \mapsto x$ is a continuous linear bijection from $\Gamma(T)$ onto $X$.
The [[bounded inverse theorem|MR5FJXR348]] makes its inverse $x \mapsto (x, Tx)$ continuous, and so $T$ is continuous.

In practice the closed graph condition is easier to check: it says that if $x_n \to x$ and $T x_n \to y$, then $y = Tx$.
One does not have to show that $T x_n$ converges.
Completeness is necessary.
Let $X = C^1[0, 1]$ and $Y = C[0, 1]$, both with the sup norm, and let $T f = f'$.
If $f_n \to f$ and $f_n' \to g$ uniformly, then $f$ is differentiable with $f' = g$, so the graph is closed.
But $T$ is not continuous, since $f_n(t) = t^n$ has $\norm{f_n} = 1$ and $\norm{f_n'} = n$; here $X$ is not complete.

## Explanations

### L1 human

To show that a linear map between complete normed spaces is continuous, it is enough to show that its graph is a closed set.
This means: whenever inputs converge and outputs converge, the limit output is the image of the limit input.
That is often much easier than finding a bound directly.

### L2 human

The theorem is used to prove automatic continuity: for example, a linear map $T$ defined on a whole Hilbert space with $\ip{Tx}{y} = \ip{x}{Ty}$ for all $x, y$ is bounded (Hellinger–Toeplitz theorem).
It is also used to show that a projection onto a closed subspace along a closed complement is bounded, see [[complemented subspace|Q0TY362K0V]].
Unbounded operators in quantum mechanics are typically closed operators defined only on dense subspaces, which is consistent with the theorem.
