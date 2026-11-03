---
tag: GBM9TF1V7K
kind: statement
role: theorem
name: Kramers–Wannier duality
msc: [82B20, 82B26, 05C10]
uses: [R0KGM32QN6, 0NC9R64TXP, FPYQWE8X12]
about: [R0KGM32QN6]
sources:
  - url: https://en.wikipedia.org/wiki/Kramers%E2%80%93Wannier_duality
same_as:
  wikidata: Q6436046
  wikipedia: Kramers–Wannier duality
---

## Statement

Consider the [[Ising model|R0KGM32QN6]] on the square lattice $\Z^2$ with nearest-neighbour coupling and no external field.
Let $K > 0$ be the coupling times the inverse temperature.
Let $\varphi(K) = \lim_{n \to \infty} n^{-2} \ln Z_n(K)$ be the free energy per site in the [[thermodynamic limit|FPYQWE8X12]], where $Z_n(K)$ is the partition function on the $n \times n$ box.
Define the dual coupling $K^* > 0$ by
$$e^{-2K^*} = \tanh K, \qquad \text{equivalently} \qquad \sinh(2K) \sinh(2K^*) = 1.$$
Then
$$\varphi(K) - \tfrac12 \ln \sinh(2K) = \varphi(K^*) - \tfrac12 \ln \sinh(2K^*).$$

## Remarks

The proof compares two expansions of the partition function on a large [[planar graph|0NC9R64TXP]] and its dual graph.
The high-temperature expansion writes $Z(K) = 2^{N} (\cosh K)^{E} \sum_{G} (\tanh K)^{\abs{G}}$, summing over the edge sets $G$ in which every vertex has even degree; $N$ and $E$ are the numbers of vertices and edges.
The low-temperature expansion on the dual lattice writes $Z^*(K^*) = 2 e^{K^* E} \sum_{G} e^{-2K^* \abs{G}}$ over the same sets $G$, now seen as domain walls between spins on the dual sites.
The two sums agree when $\tanh K = e^{-2K^*}$; the square lattice is self-dual and has $E \approx 2N$, which gives the identity after taking logarithms and the limit.
The map $K \mapsto K^*$ is a decreasing involution that exchanges high and low temperature, with a single fixed point $K_c$ satisfying $\sinh(2K_c) = 1$, that is $K_c = \frac12 \ln(1 + \sqrt 2)$.

## Explanations

### L1 human

The square-lattice Ising model at high temperature looks, mathematically, like the same model at low temperature on the dual lattice.
The duality turns a hot disordered magnet into a cold ordered one and back.
If there is only one temperature where the free energy is singular, it must be the one that is its own dual.
Kramers and Wannier used this in 1941 to locate the critical temperature before the model was solved.

### L2 human

Onsager's exact solution later confirmed that the singularity is indeed at the self-dual point.
The same idea works for the Potts model on the square lattice, giving the self-dual point $e^{K} = 1 + \sqrt q$, and it extends to abelian lattice models on general planar graphs.
In modern language it is a Fourier transform on the configuration space, and it relates order and disorder operators.
For the Ising model on the triangular lattice the dual is the honeycomb lattice, and combining duality with the star–triangle relation still locates the critical point.
