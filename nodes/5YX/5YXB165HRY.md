---
tag: 5YXB165HRY
kind: statement
role: fact
name: Ryu–Takayanagi formula
msc: [81T35, "83E05", 81P17]
uses: [92T9TPF13Y, EQX6M75VB1, H53TSRFWQ4, 41X0YW2R9N, ANNJ7JR36T, 837V89WJKS]
about: [92T9TPF13Y, H53TSRFWQ4]
sources:
  - url: https://en.wikipedia.org/wiki/Ryu–Takayanagi_conjecture
same_as:
  wikidata: Q30673556
  wikipedia: Ryu–Takayanagi conjecture
---

## Statement

Let a [[conformal field theory|837V89WJKS]] in $d$ dimensions be dual, by the [[AdS/CFT correspondence|92T9TPF13Y]], to classical Einstein gravity with Newton constant $G_N$.
The gravity side lives on an asymptotically [[anti-de Sitter|EQX6M75VB1]] spacetime of dimension $d+1$.
Consider a static state, a constant-time slice $\Sigma$ of the bulk, and a region $A$ of the boundary of $\Sigma$.
Let $\gamma_A$ be a codimension-two [[minimal surface|41X0YW2R9N]] in $\Sigma$ with $\partial \gamma_A = \partial A$ that is homologous to $A$.
Among such surfaces, $\gamma_A$ is chosen with the least area.
Let $S_A$ be the [[von Neumann entropy|H53TSRFWQ4]] of the reduced state of the boundary theory on $A$.
Then, to leading order in $G_N$ and in units $\hbar = c = 1$,
$$S_A = \frac{\operatorname{Area}(\gamma_A)}{4 G_N}.$$

## Remarks

Ryu and Takayanagi proposed the formula in 2006, modelled on the [[Bekenstein–Hawking entropy|ANNJ7JR36T]] of a horizon.
Lewkowycz and Maldacena (2013) derived it within AdS/CFT by a gravitational version of the replica trick, which computes $\tr \rho_A^n$ from bulk geometries and takes $n \to 1$.
Example: for $d = 2$ and an interval of length $\ell$ in the vacuum, $\gamma_A$ is a geodesic in $\mathrm{AdS}_3$ of radius $L$ with regularized length $2L \log(\ell/\epsilon)$, where $\epsilon$ is a cutoff.
With the Brown–Henneaux central charge $c = 3L/(2G_N)$ this gives $S_A = \frac{c}{3} \log(\ell/\epsilon)$, the known entanglement entropy of an interval in a two-dimensional conformal field theory.
For a time-dependent state, the minimal surface on a slice is replaced by an extremal surface in the full spacetime.
This is the covariant formula of Hubeny, Rangamani and Takayanagi (2007).
Quantum corrections add the entropy of bulk fields between $A$ and $\gamma_A$.

## Explanations

### L1 human

The formula says that how much a piece of a quantum system is entangled with the rest equals an area in a higher-dimensional curved space.
It extends the famous fact that the entropy of a black hole is a quarter of its horizon area.
It is one of the clearest signs that the geometry of space can emerge from quantum entanglement.

### L2 human

In AdS/CFT the boundary entanglement entropy is hard to compute directly, but the right-hand side is a classical minimal-surface problem in the bulk.
The formula implies inequalities such as strong subadditivity and the monogamy of mutual information, which can be proved geometrically by cutting and gluing minimal surfaces.
When the bulk contains a black hole and $A$ is the whole boundary, $\gamma_A$ wraps the horizon and the formula reduces to the Bekenstein–Hawking entropy of the thermal state.
It is the starting point of entanglement wedge reconstruction and of the quantum extremal surface prescription used for the black hole information problem.
