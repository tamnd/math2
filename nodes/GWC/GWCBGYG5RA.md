---
tag: GWCBGYG5RA
kind: example
name: Space of convergent sequences
msc: [46B45, 46A45]
instance_of: [XYTN19EPF2, 06GZ956657]
uses: [0W4CN9E2W5, G3F2CWQSQH, 0BDTTM24DP, 0QZMTN5AXX]
sources:
  - url: https://en.wikipedia.org/wiki/Sequence_space
---

## Example

Let $c$ be the set of [[convergent sequences|0W4CN9E2W5]] $x = (x_n)_{n \ge 1}$ of real (or complex) numbers, with the norm $\norm{x}_\infty = \sup_{n} \abs{x_n}$.
Then $c$ is a [[sequence space|XYTN19EPF2]] and a [[Banach space|0BDTTM24DP]].

Check that $c$ is a sequence space: the sum of two convergent sequences converges, and so does a scalar multiple of a convergent sequence.

Check that $c$ is complete: convergent sequences are bounded, so $c$ is a subspace of the Banach space $\ell^\infty$ of [[bounded sequences|G3F2CWQSQH]].
So it suffices to show that $c$ is closed in $\ell^\infty$.
Let $x^{(j)} \in c$ with $\norm{x^{(j)} - x}_\infty \to 0$ for some $x \in \ell^\infty$.
For all $m, n$ and $j$,
$$\abs{x_m - x_n} \le 2 \norm{x - x^{(j)}}_\infty + \abs{x^{(j)}_m - x^{(j)}_n}.$$
Choose $j$ to make the first term small, then use that $x^{(j)}$ is a [[Cauchy sequence|0QZMTN5AXX]].
So $x$ is a Cauchy sequence of numbers, hence convergent, and $x \in c$.

## Remarks

The map $x \mapsto \lim_n x_n$ is a linear functional on $c$ with $\abs{\lim_n x_n} \le \norm{x}_\infty$, so it is continuous.
Its kernel is the [[space of null sequences|WDH6QSH1Z6]] $c_0$.

## Explanations

### L1 human

The convergent sequences form a vector space: you can add them and scale them, and they still converge.
Measuring the size of a sequence by its largest term in absolute value makes this space complete, so limits of convergent sequences, in this size, are again convergent sequences.
