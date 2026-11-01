---
tag: 4CZMWQVC30
kind: statement
role: theorem
name: g-theorem
msc: [52B05, "05E45"]
uses: [DCK64GFPD7, 4WKHF5BCTA, 0GBZM0MT0F]
about: [DCK64GFPD7]
sources:
  - url: https://en.wikipedia.org/wiki/Simplicial_sphere
---

## Statement

Let $d \ge 1$ and let $(h_0, h_1, \dots, h_d)$ be a sequence of integers.
Let $g_0 = h_0$ and $g_i = h_i - h_{i-1}$ for $1 \le i \le \floor{d/2}$.
Then $(h_0, \dots, h_d)$ is the [[h-vector|DCK64GFPD7]] of the boundary complex of a simplicial convex polytope of dimension $d$ if and only if the following hold:

1. $h_i = h_{d-i}$ for $0 \le i \le d$.
2. $g_0 = 1$.
3. $0 \le g_{i+1} \le g_i^{\langle i \rangle}$ for $1 \le i \le \floor{d/2} - 1$, and $g_1 \ge 0$.

Here, for integers $a \ge 0$ and $i \ge 1$, write $a = \binom{n_i}{i} + \binom{n_{i-1}}{i-1} + \dots + \binom{n_j}{j}$ with $n_i > n_{i-1} > \dots > n_j \ge j \ge 1$ (this expansion exists and is unique), and set $a^{\langle i \rangle} = \binom{n_i + 1}{i + 1} + \binom{n_{i-1} + 1}{i} + \dots + \binom{n_j + 1}{j + 1}$, with $0^{\langle i \rangle} = 0$.

## Remarks

Condition 1 is the [[Dehn–Sommerville equations|4WKHF5BCTA]].
Conditions 2 and 3 say that $(g_0, \dots, g_{\floor{d/2}})$ is an M-sequence, the Hilbert function of a graded quotient of a polynomial ring generated in degree $1$; in particular $h_0 \le h_1 \le \dots \le h_{\floor{d/2}}$.
The conditions were conjectured by McMullen.
Billera and Lee proved sufficiency by constructing polytopes, and Stanley proved necessity with the hard Lefschetz theorem for toric varieties.

Example: the boundary of the $4$-dimensional cross-polytope has $h = (1, 4, 6, 4, 1)$ and $g = (1, 3, 2)$.
Here $3 = \binom{3}{1}$, so $3^{\langle 1 \rangle} = \binom{4}{2} = 6 \ge 2$, and all conditions hold.

The sequence $(1, 1, 3, 1, 1)$ is symmetric, but $g = (1, 0, 2)$ and $0^{\langle 1 \rangle} = 0 < 2$, so it is not the h-vector of a simplicial $4$-polytope.

## Explanations

### L1 human

The theorem lists exactly which face counts a polytope with simplex faces can have.
Besides the mirror symmetry of Dehn–Sommerville, the h-vector must rise up to its middle, and it cannot rise too fast.
"Too fast" is measured by a precise rule from commutative algebra due to Macaulay.

### L2 human

The g-theorem is a model of how commutative algebra and algebraic geometry solve combinatorial problems.
The h-vector of a simplicial polytope is the Hilbert function of an Artinian reduction of its Stanley–Reisner ring.
The hard Lefschetz property gives an injective multiplication map, and this forces the g-vector to be an M-sequence.
The same characterization for all simplicial spheres was a long-standing conjecture; Adiprasito announced a proof in 2018.
