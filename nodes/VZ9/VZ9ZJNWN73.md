---
tag: VZ9ZJNWN73
kind: definition
name: Supersymmetry
msc: [81T60, 17B81, "83E50"]
defines: S847N922FY
uses: [7CZ4Q5H78N, 8ZQ9TA4Q2Q, 7JA7WH92K0, W031YNVRE3]
sources:
  - url: https://en.wikipedia.org/wiki/Supersymmetry
---

## Definition

Let $\mathfrak{p}$ be the Lie algebra of the [[Poincaré group|8ZQ9TA4Q2Q]] of Minkowski space $\R^{1, d-1}$, spanned by translations $P_\mu$ and Lorentz generators $M_{\mu\nu}$.
A *supersymmetry algebra* is a [[Lie superalgebra|7CZ4Q5H78N]] $\mathfrak{s} = \mathfrak{s}_0 \oplus \mathfrak{s}_1$ with the following properties.

1. The even part is $\mathfrak{s}_0 = \mathfrak{p} \oplus \mathfrak{k}$, where $\mathfrak{k}$ is a Lie algebra of internal symmetries that commutes with $\mathfrak{p}$.
2. The odd part $\mathfrak{s}_1$, spanned by the supercharges, is a sum of spinor representations of the Lorentz algebra under the bracket with the $M_{\mu\nu}$.
3. The supercharges commute with translations: $[P_\mu, Q] = 0$ for $Q \in \mathfrak{s}_1$.
   The bracket $\mathfrak{s}_1 \times \mathfrak{s}_1 \to \mathfrak{s}_0$ is non-zero, with values in the span of the translations and of central elements of $\mathfrak{k}$.

A [[quantum field theory|W031YNVRE3]] has *supersymmetry* if its symmetry algebra contains a supersymmetry algebra acting on its Hilbert space.
The supercharges act by operators that exchange the bosonic and fermionic states.
The number $N$ of irreducible real spinor representations in $\mathfrak{s}_1$ is the number of supersymmetries.

## Remarks

Example: the $N = 1$ supersymmetry algebra in four dimensions.
In two-component notation the supercharges are $Q_\alpha$ and $\bar Q_{\dot\alpha}$, with $\alpha, \dot\alpha \in \set{1, 2}$, and the only non-zero brackets among them are
$$\set{Q_\alpha, \bar Q_{\dot\beta}} = 2 \sigma^\mu_{\alpha\dot\beta} P_\mu,$$
where $\sigma^\mu = (I_2, \sigma^1, \sigma^2, \sigma^3)$ uses the Pauli matrices.
The supercharges $Q_\alpha$ and $\bar Q_{\dot\alpha}$ form the two spinor representations of $\mathfrak{sl}(2, \C)$, together one real (Majorana) spinor, so $N = 1$, and their anticommutators are translations, so clauses 2 and 3 hold.

Non-example: a Lie superalgebra whose odd part is a vector representation of the Lorentz algebra fails clause 2.
By the spin–statistics connection, odd generators of a spacetime symmetry must have half-integer spin.

Consequences: in a unitary representation the energy is non-negative, because $H$ is a sum of terms $Q Q^\dagger + Q^\dagger Q \ge 0$.
In each irreducible representation with $P^2 > 0$, all states have the same mass, and the bosonic and fermionic states have equal numbers.
Supersymmetry in a theory that includes gravity is supergravity.
