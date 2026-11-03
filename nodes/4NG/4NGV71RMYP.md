---
tag: 4NGV71RMYP
kind: statement
role: theorem
name: Freudenthal multiplicity formula
msc: [17B10]
uses: [EY9DN7QAX1, BB098JPWGA, C5W8BE1DRY, KFVNC2W720, J1EFY61K87, TWVQT18JXE]
about: [KFVNC2W720, J1EFY61K87]
sources:
  - url: https://en.wikipedia.org/wiki/Weyl_character_formula
---

## Statement

Let $\mathfrak{g}$ be a complex [[semisimple Lie algebra|EY9DN7QAX1]] with [[Cartan subalgebra|BB098JPWGA]] $\mathfrak{h}$ and positive roots $\Phi^+$, and let $\rho = \frac{1}{2} \sum_{\alpha \in \Phi^+} \alpha$.
Let $(\cdot, \cdot)$ be the bilinear form on $\mathfrak{h}^*$ induced by the [[Killing form|TWVQT18JXE]].
Let $\lambda$ be a dominant integral weight, let $L(\lambda)$ be the finite-dimensional irreducible module of [[highest weight|C5W8BE1DRY]] $\lambda$, and let $m(\mu) = \dim L(\lambda)_\mu$ for $\mu \in \mathfrak{h}^*$.
Then for every $\mu \in \mathfrak{h}^*$,
$$\big( (\lambda + \rho, \lambda + \rho) - (\mu + \rho, \mu + \rho) \big)\, m(\mu) = 2 \sum_{\alpha \in \Phi^+} \sum_{k \ge 1} (\mu + k\alpha, \alpha)\, m(\mu + k\alpha).$$

## Remarks

The proof computes the trace of the [[Casimir element|K6VVP66GKB]] on the weight space $L(\lambda)_\mu$ in two ways.
The Casimir element acts on $L(\lambda)$ by the scalar $(\lambda + \rho, \lambda + \rho) - (\rho, \rho)$, and the root vector terms give the right side.
For $\mu < \lambda$ with $\mu$ a [[weight|KFVNC2W720]], the coefficient on the left is nonzero, so $m(\mu)$ is computed from multiplicities of higher weights, starting from $m(\lambda) = 1$.
Example: for $\mathfrak{sl}_2(\C)$, identify $\mathfrak{h}^*$ with $\C$ by $\lambda \mapsto \lambda(h)$; the form is a multiple of $(a, b) = ab$, and both sides scale alike.
For $\lambda = 2$ and $\mu = 0$, with $\rho = 1$ and $\alpha = 2$, the left side is $(9 - 1)\, m(0)$.
The right side is $2 \big( (2, 2)\, m(2) + (4, 2)\, m(4) \big) = 2 (4 \cdot 1 + 8 \cdot 0) = 8$, so $m(0) = 1$.

## Explanations

### L1 human

The formula computes how often each weight occurs in an irreducible representation.
It works from the top down: the highest weight occurs once, and each lower multiplicity is computed from the ones above it.
This makes it a practical algorithm, used by hand and by computer programs.

### L2 human

The formula is equivalent to the [[Weyl character formula|G2SA2YNA33]] but avoids its large alternating sums over the Weyl group.
It was found by Hans Freudenthal.
The left coefficient is the difference of the Casimir eigenvalues on $L(\lambda)$ and on a module of highest weight $\mu$.
