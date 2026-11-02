---
tag: 11MYA5W3KT
kind: statement
role: theorem
name: Willmore conjecture
msc: [53A10, 53C42, 49Q05]
uses: [R7WFJGJBV4, 6RW68JGBHC]
about: [R7WFJGJBV4]
sources:
  - url: https://en.wikipedia.org/wiki/Willmore_conjecture
same_as:
  wikidata: Q17091514
  wikipedia: Willmore conjecture
---

## Statement

Let $T$ be a torus and let $f \colon T \to \R^3$ be a smooth [[immersion|6RW68JGBHC]].
Then the [[Willmore energy|R7WFJGJBV4]] of $f$ satisfies
$$\mathcal{W}(f) = \int_T H^2 \, dA \ge 2\pi^2.$$
Let $T_0$ be the torus of revolution whose generating circle has radius $1$ and center at distance $\sqrt{2}$ from the axis.
Equality holds if and only if $f(T)$ is the image of $T_0$ under a Möbius transformation of $\R^3 \cup \set{\infty}$.

## Remarks

Willmore stated the conjecture in 1965, and Marques and Neves proved it; their proof appeared in 2014.
The torus in the equality case is the stereographic image of the Clifford torus in the three-sphere.
If $f$ is not an embedding, a theorem of Li and Yau gives $\mathcal{W}(f) \ge 8\pi > 2\pi^2$, so only embedded tori need work.
For those, Marques and Neves used conformal invariance to move the problem to the three-sphere and applied Almgren–Pitts min-max theory to a five-parameter family of surfaces built from the torus.
A key step is that every closed embedded minimal surface of positive genus in the three-sphere has area at least $2\pi^2$.
Equality holds there only for the Clifford torus, up to isometry.

For every closed surface $\mathcal{W} \ge 4\pi$, so the conjecture says that being a torus costs at least $2\pi^2 - 4\pi$ extra energy.

## Explanations

### L1 human

The Willmore energy measures how much a closed surface bends overall.
Among all surfaces it is smallest for a round sphere.
The conjecture, now a theorem, finds the least possible energy for a doughnut-shaped surface: $2\pi^2$, reached by one particular fat doughnut and its Möbius images.

### L2 human

Because $\mathcal{W}$ is invariant under Möbius transformations, the minimizers come in whole families, and the natural setting is conformal geometry.
The proof is one of the main applications of min-max theory for minimal surfaces.
It belongs to a larger program of finding the least Willmore energy for each genus.
