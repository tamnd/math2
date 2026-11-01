---
tag: DA8M8VZZHC
kind: statement
role: theorem
name: Hadamard gap theorem
msc: [30B10, 30B40]
uses: [0VARVQ9ZW1, 0660QX1VPR, WER1M071EK]
about: [PQFEA12AHA]
sources:
  - url: https://en.wikipedia.org/wiki/Lacunary_function
---

## Statement

Let $(n_k)_{k \ge 1}$ be a strictly increasing sequence of positive integers, and assume there is $\lambda > 1$ with $n_{k+1} / n_k \ge \lambda$ for all $k$.
Let $(a_k)$ be complex numbers such that the [[power series|0VARVQ9ZW1]] $f(z) = \sum_{k \ge 1} a_k z^{n_k}$ has [[radius of convergence|0660QX1VPR]] $1$.
Then the unit circle is a [[natural boundary|WER1M071EK]] of $f$.

## Remarks

Proof idea: suppose that $f$ extends holomorphically across an arc of the circle, and rotate so that the arc contains $1$.
A standard proof composes $f$ with the polynomial $w \mapsto (w^m + w^{m+1})/2$, for an integer $m$ chosen from $\lambda$.
This map sends the closed unit disc into the unit disc except at $1$, so the composed series would converge on a disc of radius greater than $1$.
Because of the gaps, the expansion of $f$ composed with this map in powers of $w$ splits into disjoint blocks, one for each term $a_k z^{n_k}$.
So the series of $f$ would converge at some real point greater than $1$, a contradiction.
Example: $\sum_{n \ge 0} z^{2^n}$ and $\sum_{n \ge 1} z^{n!}$ have the unit circle as natural boundary.
In the second series, $n_{k+1}/n_k = k + 1 \ge 2$.
The gap condition cannot just be dropped: $\sum_{n \ge 0} z^n = \frac{1}{1 - z}$ has radius $1$ but extends across every point except $1$.
The [[Fabry gap theorem|GE0HX2KMMZ]] reaches the same conclusion under the weaker condition $n_k / k \to \infty$.

## Explanations

### L1 human

A power series with only very few terms, spaced out so that the exponents grow at least geometrically, behaves wildly at every point of its circle of convergence.
It cannot be extended past any arc of the circle.
So sparse power series give simple explicit functions whose domain cannot be enlarged at all.

### L2 human

The theorem is the classical source of functions with a natural boundary, called lacunary functions.
It shows that the obstruction to [[analytic continuation|0M3YQJ81NB]] can be spread over the whole circle of convergence.
It is a special case of the [[Fabry gap theorem|GE0HX2KMMZ]], and its proof is closely related to the phenomenon of overconvergence studied by Ostrowski.
