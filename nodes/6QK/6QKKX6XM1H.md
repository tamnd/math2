---
tag: 6QKKX6XM1H
kind: statement
role: theorem
name: BPHZ theorem
msc: [81T15, 81T18]
uses: [BS6HVNMTWC, 1X0W3AEBEJ, 0Z49YH6ZWY]
about: [1X0W3AEBEJ]
sources:
  - url: https://en.wikipedia.org/wiki/Bogoliubov%E2%80%93Parasyuk_theorem
same_as:
  wikidata: Q4937691
  wikipedia: Bogoliubov–Parasyuk theorem
---

## Statement

Consider a Euclidean scalar field theory in $d$ dimensions with propagators $(k^2 + m^2)^{-1}$, $m > 0$, and polynomial interaction vertices.
Let $\Gamma$ be a [[Feynman diagram|BS6HVNMTWC]] with integrand $I_\Gamma$ in its loop momenta.
For a subgraph $\gamma$ with $L(\gamma)$ independent loops and $E(\gamma)$ internal edges, let $\omega(\gamma) = d\,L(\gamma) - 2E(\gamma)$ be its superficial degree of divergence.
A renormalization part is a connected one-particle-irreducible subgraph $\gamma$ with $\omega(\gamma) \ge 0$.
A forest is a set of renormalization parts, any two of which are disjoint or nested.
Let $T_\gamma$ take the [[Taylor polynomial|0Z49YH6ZWY]] of degree $\omega(\gamma)$ in the external momenta of $\gamma$.
Define Zimmermann's forest formula
$$R_\Gamma = \sum_{F} \prod_{\gamma \in F} (-T_\gamma) \, I_\Gamma,$$
summed over all forests $F$, including the empty one, with the operators applied from the inside out.
Then the integral of $R_\Gamma$ over all loop momenta converges absolutely.
Moreover, the subtractions are equivalent to adding to the Lagrangian local counterterms, polynomials in the fields and their derivatives.

## Remarks

The proof by Zimmermann bounds the integrand in each sector of loop-momentum space, where the momenta are ordered by size.
In each sector the forest formula subtracts exactly the subgraphs that are dangerous there, and power counting (Weinberg's theorem) then gives convergence.
Bogoliubov and Parasyuk gave the recursive form of the subtraction, and Hepp completed their proof.

Example: in the four-dimensional [[quartic interaction|HVGDXMPB29]], the one-loop four-point diagram has $\omega = 4 - 4 = 0$.
Subtracting its value at zero external momentum gives a convergent integral, which corresponds to a counterterm $\delta\lambda\,\phi^4$.
For a renormalizable theory, the counterterms required by the theorem are of the form of the original interaction, at every order.

The mass $m > 0$ prevents infrared divergences; massless theories need modified subtractions.
Overlapping divergences, which are neither disjoint nor nested, are never subtracted together, and the forest structure handles them correctly.

## Explanations

### L1 human

Feynman diagrams with loops often give divergent integrals, and diagrams can contain divergent pieces inside divergent pieces.
The BPHZ theorem gives a precise recipe for subtracting all these divergences at once.
It proves that, after the recipe, every diagram gives a finite number, and the recipe is the same as adjusting finitely many parameters of the theory.

### L2 human

The theorem is the mathematical foundation of perturbative [[renormalization|1X0W3AEBEJ]].
It shows that renormalizability by power counting really works to all orders.
In dimensional regularization with minimal subtraction, the same forest structure appears in the counterterms.
Connes and Kreimer showed that the combinatorics of the forest formula is the antipode of a Hopf algebra of Feynman graphs.
