---
tag: 2N4RJCW5JK
kind: example
name: Space of convergent sequences c
msc: [46B45, 46B25]
instance_of: [06GZ956657]
uses: [06GZ956657, 0W4CN9E2W5, 0A8JNBGT2Z]
sources:
  - url: https://en.wikipedia.org/wiki/C_space
---

## Example

Let $c$ be the set of real [[convergent sequences|0W4CN9E2W5]] $x = (x_n)_{n \ge 1}$, with the norm $\norm{x}_\infty = \sup_n \abs{x_n}$.
Then $c$ is a [[Banach space|06GZ956657]].

Check.
Every convergent sequence is [[bounded|0A8JNBGT2Z]], so $c$ is a linear subspace of the Banach space $\ell^\infty$ of bounded sequences.
It suffices to show that $c$ is closed in $\ell^\infty$.
Let $x^{(k)} \in c$ tend to $x$ in $\ell^\infty$.
For all $k$, $m$ and $n$,
$$\abs{x_m - x_n} \le 2 \norm{x - x^{(k)}}_\infty + \abs{x^{(k)}_m - x^{(k)}_n}.$$
Choose $k$ to make the first term small, then $m, n$ large to make the second term small.
So $x$ is a Cauchy sequence of real numbers, and it converges.

## Remarks

The sequences with limit $0$ form the closed subspace $c_0$ of codimension $1$ in $c$.
The map $x \mapsto (\ell, x_1 - \ell, x_2 - \ell, \dots)$, with $\ell = \lim_n x_n$, is a linear isomorphism of $c$ onto $c_0$.
But $c$ and $c_0$ are not isometric.
The constant sequence $(1, 1, \dots)$ is an extreme point of the unit ball of $c$, while the unit ball of $c_0$ has no extreme points.
The dual of $c$ is isometric to $\ell^1$.

## Explanations

### L1 human

The space $c$ collects all sequences of real numbers that settle down to a limit.
Two sequences are close when they are close at every index.
A uniform limit of sequences that settle down also settles down, so the space has no holes.
