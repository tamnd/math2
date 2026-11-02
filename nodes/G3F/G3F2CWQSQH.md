---
tag: G3F2CWQSQH
kind: example
name: Bounded sequences ℓ∞
msc: [46B45, 46A45]
instance_of: [XYTN19EPF2, 06GZ956657]
uses: [0A8JNBGT2Z, 08P6T2WH6R, 0BDTTM24DP, 0Z2P41SVDP]
sources:
  - url: https://en.wikipedia.org/wiki/Sequence_space
---

## Example

Let $\ell^\infty$ be the set of [[bounded sequences|0A8JNBGT2Z]] $x = (x_n)_{n \ge 1}$ of real (or complex) numbers, with the norm $\norm{x}_\infty = \sup_n \abs{x_n}$.
Then $\ell^\infty$ is a [[sequence space|XYTN19EPF2]] and a [[Banach space|0BDTTM24DP]]; this is the case $p = \infty$ of the [[spaces ℓ^p|08P6T2WH6R]].

Check of completeness: let $(x^{(j)})$ be a Cauchy sequence in $\ell^\infty$.
For each $n$, $\abs{x^{(j)}_n - x^{(i)}_n} \le \norm{x^{(j)} - x^{(i)}}_\infty$, so $(x^{(j)}_n)_j$ is a Cauchy sequence of numbers with a limit $x_n$.
Given $\varepsilon > 0$, choose $J$ with $\norm{x^{(j)} - x^{(i)}}_\infty \le \varepsilon$ for $i, j \ge J$.
Letting $i \to \infty$ gives $\abs{x^{(j)}_n - x_n} \le \varepsilon$ for all $n$ and all $j \ge J$.
So $x$ is bounded and $x^{(j)} \to x$ in norm.

## Remarks

The space $\ell^\infty$ is not [[separable|0Z2P41SVDP]].
The sequences with all terms in $\set{0, 1}$ form an uncountable set, and any two of them are at distance $1$.
So the open balls of radius $1/2$ around them are disjoint, and no countable set meets all of them.
The spaces of convergent sequences and of null sequences are closed subspaces of $\ell^\infty$.
The space $\ell^\infty$ is isometrically isomorphic to the dual of $\ell^1$.

## Explanations

### L1 human

A sequence is bounded when all its terms stay within some fixed distance of $0$.
The bounded sequences form a vector space, and the size of a sequence is the least bound on its terms.
This space is so large that no countable family of sequences can approximate all of its elements.
