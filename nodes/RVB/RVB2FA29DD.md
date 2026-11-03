---
tag: RVB2FA29DD
kind: statement
role: theorem
name: Nagaoka ferromagnetism
msc: [82B20, 82D40, 82B10]
uses: [3B76W03AN7]
about: [3B76W03AN7]
sources:
  - url: https://en.wikipedia.org/wiki/Hubbard_model
---

## Statement

Let $\Lambda$ be a finite set of sites.
Consider the [[Hubbard model|3B76W03AN7]]
$$H = \sum_{x, y \in \Lambda} \sum_{\sigma} t_{xy}\, c_{x\sigma}^\dagger c_{y\sigma} + U \sum_{x \in \Lambda} n_{x\uparrow} n_{x\downarrow}$$
with real symmetric hopping $t_{xy} = t_{yx} \ge 0$.
Take the limit $U = \infty$, that is, restrict to states with no doubly occupied site.
Let the number of electrons be $\abs{\Lambda} - 1$, so that there is exactly one hole.
Assume the connectivity condition: any two spin configurations with one hole are joined by some sequence of hops of the hole along bonds with $t_{xy} > 0$.
Then the ground states have the maximal total spin $S_{\max} = (\abs{\Lambda} - 1)/2$, and they form a single spin multiplet, of dimension $2S_{\max} + 1$.

## Remarks

The proof uses a Perron–Frobenius argument.
In a suitable basis of configurations of the hole and the spins, the off-diagonal matrix elements of $-H$ are non-negative, thanks to the sign condition on $t_{xy}$.
The connectivity condition makes this matrix irreducible within each sector of fixed $S^z_{\mathrm{tot}}$.
So the ground state in each sector is unique and has positive coefficients, and comparing with the fully polarized state shows that it has maximal total spin.
Nagaoka proved the result in 1966, and Thouless gave a related argument independently; Tasaki gave the general version above.
The square and simple cubic lattices with nearest-neighbour hopping satisfy the connectivity condition.
They are bipartite, so the sign of the hopping can be reversed by a gauge transformation, and the sign condition is no restriction there.
A one-dimensional open chain does not satisfy the connectivity condition, since the hole cannot change the order of the spins.
With two or more holes, or at finite $U$, the ground state is not known in general.

## Explanations

### L1 human

In a lattice packed with electrons, one per site, which repel each other infinitely strongly, nothing can move.
Remove one electron: now the hole can move, and it moves most easily when all spins point the same way, because then its motion does not scramble anything.
To lower its kinetic energy, the hole forces all spins to align, giving a ferromagnet.
This is one of the few rigorous results showing that repulsion between electrons can produce ferromagnetism.

### L2 human

Nagaoka's theorem is a rare exact result about the Hubbard model away from half filling.
It shows that kinetic energy, not exchange, can drive ferromagnetism, a mechanism that is very different from the Heisenberg picture.
Its hypotheses are delicate: the sign of the hopping matters on non-bipartite lattices, and a single hole is a vanishing density.
The stability of the ferromagnet at a finite density of holes is an open problem.
Related rigorous results on flat-band ferromagnetism, by Mielke and Tasaki, give other routes to ferromagnetism in Hubbard models.
