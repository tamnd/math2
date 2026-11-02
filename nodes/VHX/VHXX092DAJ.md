---
tag: VHXX092DAJ
kind: definition
name: Riesz basis
msc: [42C15, 46B15, 46C05]
defines: ZYDYD7FB1Z
uses: [HM2HHE3J51, 0S9GGTR0EX]
sources:
  - url: https://en.wikipedia.org/wiki/Riesz_sequence
---

## Definition

Let $H$ be a separable [[Hilbert space|HM2HHE3J51]].
A sequence $(x_n)_{n \ge 1}$ in $H$ is a *Riesz sequence* if there are constants $0 < A \le B < \infty$ such that for every finite sequence of scalars $c_1, \dots, c_N$,
$$A \sum_{n=1}^{N} \abs{c_n}^2 \le \Big\| \sum_{n=1}^{N} c_n x_n \Big\|^2 \le B \sum_{n=1}^{N} \abs{c_n}^2.$$
A *Riesz basis* of $H$ is a Riesz sequence whose closed linear span is $H$.

## Remarks

Equivalently, $(x_n)$ is a Riesz basis if and only if $x_n = T e_n$ for an [[orthonormal basis|0S9GGTR0EX]] $(e_n)$ of $H$ and a bounded linear operator $T \colon H \to H$ with a bounded inverse.
Then every $x \in H$ has a unique expansion $x = \sum_n c_n x_n$, the series converges unconditionally, and $A \sum \abs{c_n}^2 \le \norm{x}^2 \le B \sum \abs{c_n}^2$.
The best constants are $A = \norm{T^{-1}}^{-2}$ and $B = \norm{T}^2$.

Example: let $(e_n)$ be an orthonormal basis of $H$ and $x_n = e_n + \frac12 e_{n+1}$.
Then $x_n = T e_n$ with $T = I + \frac12 S$, where $S$ is the shift $e_n \mapsto e_{n+1}$, of norm $1$.
Since $\norm{\frac12 S} < 1$, the Neumann series shows that $T$ is invertible with bounded inverse, so $(x_n)$ is a Riesz basis.

Non-example: $x_n = e_n / n$.
Its closed span is $H$ and the upper bound holds with $B = 1$.
The lower bound fails: for $c = (0, \dots, 0, 1)$ with the $1$ in place $n$, the middle term is $1/n^2$, which is not bounded below by a positive $A$.
