---
tag: VDGDD8Q61N
kind: definition
name: Markov kernel
msc: [60J05, 28A35]
defines: 2AVNDP8BJP
uses: [N4KDT83V3S, 059TJN0NZ1, YYNCJSR0PJ]
sources:
  - url: https://en.wikipedia.org/wiki/Markov_kernel
---

## Definition

Let $(X, \mathcal{A})$ and $(Y, \mathcal{B})$ be [[measurable spaces|N4KDT83V3S]].
A *Markov kernel* from $X$ to $Y$ is a map $\kappa \colon X \times \mathcal{B} \to [0, 1]$ such that:

1. for each $B \in \mathcal{B}$, the map $x \mapsto \kappa(x, B)$ is [[measurable|YYNCJSR0PJ]] from $(X, \mathcal{A})$ to $[0, 1]$;
2. for each $x \in X$, the map $B \mapsto \kappa(x, B)$ is a [[probability measure|059TJN0NZ1]] on $(Y, \mathcal{B})$.

## Remarks

Example: let $X = Y = \set{1, \ldots, n}$ with all subsets measurable, and let $P = (p_{ij})$ be a matrix with nonnegative entries and row sums $1$.
Then $\kappa(i, B) = \sum_{j \in B} p_{ij}$ is a Markov kernel: clause 1 holds because every function on a finite discrete space is measurable, and clause 2 because row $i$ is a probability vector.

Non-example: on $\R$ with its Borel sets, $\kappa(x, B) = 2 \, \mathbf{1}_B(x)$ fails clause 2, since $\kappa(x, \R) = 2$; it also takes values outside $[0, 1]$.

Another standard example: for a measurable map $f \colon X \to Y$, the kernel $\kappa(x, B) = \mathbf{1}_B(f(x))$ is a Markov kernel, the deterministic kernel of $f$.
A kernel acts on bounded measurable functions by $(\kappa g)(x) = \int_Y g(y) \, \kappa(x, dy)$ and on probability measures by $(\mu \kappa)(B) = \int_X \kappa(x, B) \, \mu(dx)$.
Markov kernels are also called stochastic kernels, transition kernels or probability kernels.
