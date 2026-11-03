---
tag: ZYVEVYBA41
kind: statement
role: theorem
name: Iwasawa decomposition
msc: ["17B20", "22E46"]
uses: [K7VVYFE9YJ, EY9DN7QAX1, N43CM5H99K, MEJ9PGMJ9H, W7A2R0GR3T]
about: [EY9DN7QAX1]
sources:
  - url: https://en.wikipedia.org/wiki/Iwasawa_decomposition
---

## Statement

Let $\mathfrak{g}_0$ be a finite-dimensional real [[semisimple Lie algebra|EY9DN7QAX1]] with a [[Cartan decomposition|K7VVYFE9YJ]] $\mathfrak{g}_0 = \mathfrak{k} \oplus \mathfrak{p}$.
Let $\mathfrak{a}$ be a maximal abelian subspace of $\mathfrak{p}$.
For $\lambda \in \mathfrak{a}^*$, let $\mathfrak{g}_\lambda = \set{X \in \mathfrak{g}_0 : [H, X] = \lambda(H) X \text{ for all } H \in \mathfrak{a}}$.
Let $\Sigma$ be the set of nonzero $\lambda$ with $\mathfrak{g}_\lambda \ne 0$, the restricted roots.
Let $\Sigma^+$ be the positive elements of $\Sigma$ for some ordering of $\mathfrak{a}^*$.
Put $\mathfrak{n} = \bigoplus_{\lambda \in \Sigma^+} \mathfrak{g}_\lambda$.
Then:

1. $\mathfrak{g}_0 = \mathfrak{k} \oplus \mathfrak{a} \oplus \mathfrak{n}$ as a direct sum of vector spaces;
2. $\mathfrak{a}$ is an [[abelian|N43CM5H99K]] subalgebra, $\mathfrak{n}$ is a [[nilpotent|MEJ9PGMJ9H]] subalgebra, and $[\mathfrak{a}, \mathfrak{n}] \subseteq \mathfrak{n}$;
3. $\mathfrak{a} \oplus \mathfrak{n}$ is a [[solvable|W7A2R0GR3T]] subalgebra.

## Remarks

The operators $\operatorname{ad} H$, $H \in \mathfrak{a}$, are symmetric for the inner product $B_\theta$ of the Cartan decomposition, and they commute, so they diagonalize together with real eigenvalues.
So $\mathfrak{g}_0$ is the direct sum of the centralizer $\mathfrak{m} \oplus \mathfrak{a}$ of $\mathfrak{a}$, with $\mathfrak{m} \subseteq \mathfrak{k}$, and of the spaces $\mathfrak{g}_\lambda$, $\lambda \in \Sigma$.
The Cartan involution $\theta$ maps $\mathfrak{g}_\lambda$ onto $\mathfrak{g}_{-\lambda}$.
For $\lambda < 0$ and $X \in \mathfrak{g}_\lambda$, one writes $X = (X + \theta X) - \theta X$ with $X + \theta X \in \mathfrak{k}$ and $\theta X \in \mathfrak{n}$; this gives the sum in item 1, and a short argument gives directness.
Example: for $\mathfrak{sl}_n(\R)$ with $\mathfrak{k} = \mathfrak{so}(n)$, one can take $\mathfrak{a}$ the diagonal matrices of trace $0$ and $\mathfrak{n}$ the strictly upper triangular matrices.
Then item 1 is the Lie algebra form of the Gram–Schmidt process; the group form is the [[Iwasawa decomposition of a Lie group|4YDR9Q36DS]].

## Explanations

### L1 human

A real semisimple Lie algebra splits into three pieces: a rotation part, a commutative stretching part and a nilpotent part.
For real matrices of trace $0$, these are the skew-symmetric, the diagonal and the strictly upper triangular matrices.

### L2 human

The Iwasawa decomposition refines the Cartan decomposition by splitting $\mathfrak{p}$ with the help of the restricted roots.
It integrates to the decomposition $G = KAN$ of the group, which is basic in harmonic analysis on semisimple Lie groups and in the theory of parabolic subgroups.
