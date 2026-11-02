---
tag: WDH6QSH1Z6
kind: example
name: Space of null sequences
msc: [46B45, 46A45]
instance_of: [XYTN19EPF2, 06GZ956657]
uses: [0W4CN9E2W5, G3F2CWQSQH, 0BDTTM24DP, GWCBGYG5RA, 528G11SDWR]
sources:
  - url: https://en.wikipedia.org/wiki/Sequence_space
---

## Example

Let $c_0$ be the set of sequences $x = (x_n)_{n \ge 1}$ of real (or complex) numbers with $x_n \to 0$, with the norm $\norm{x}_\infty = \sup_n \abs{x_n}$.
Then $c_0$ is a [[sequence space|XYTN19EPF2]] and a [[Banach space|0BDTTM24DP]].

Check: $c_0$ is the kernel of the linear functional $x \mapsto \lim_n x_n$ on the [[space of convergent sequences|GWCBGYG5RA]] $c$.
This functional satisfies $\abs{\lim_n x_n} \le \norm{x}_\infty$, so it is continuous, and its kernel is a closed linear subspace of $c$.
A closed subspace of a Banach space is complete, and $c$ is a Banach space, so $c_0$ is a Banach space.

## Remarks

The unit vectors $e_k$, with $1$ in place $k$ and $0$ elsewhere, form a [[Schauder basis|528G11SDWR]] of $c_0$: for $x \in c_0$, $\norm{x - \sum_{k \le N} x_k e_k}_\infty = \sup_{k > N} \abs{x_k} \to 0$.
In particular $c_0$ is separable, unlike the space $\ell^\infty$ of [[bounded sequences|G3F2CWQSQH]].
The dual space of $c_0$ is isometrically isomorphic to $\ell^1$, through the pairing $(a, x) \mapsto \sum_n a_n x_n$.
The space $c$ is the direct sum of $c_0$ and the line of constant sequences.

## Explanations

### L1 human

The null sequences are the sequences that tend to $0$, such as $1, 1/2, 1/3, \dots$.
They form a vector space, and the largest absolute value of the terms is a good way to measure their size.
This space is one of the basic examples of an infinite-dimensional Banach space.
