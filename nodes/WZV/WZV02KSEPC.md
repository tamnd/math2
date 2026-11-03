---
tag: WZV02KSEPC
kind: statement
role: theorem
name: Riemann–Roch without denominators
msc: ["14C40", "19L10", "14C17"]
uses: [EBEF6PEK4N, PAD37GKDPD, P4DZM975BV, 56RXEJ8Z6S]
about: [PAD37GKDPD, EBEF6PEK4N]
sources:
  - url: https://en.wikipedia.org/wiki/Grothendieck–Riemann–Roch_theorem
---

## Statement

Let $Y$ be a nonsingular quasi-projective variety over a field.
Let $i \colon X \to Y$ be the inclusion of a nonsingular closed subvariety of codimension $d \ge 1$ with normal bundle $N$.
Let $E$ be a [[vector bundle|P4DZM975BV]] of rank $e$ on $X$.
Let $c(i_* E)$ be the total [[Chern class|PAD37GKDPD]] of the [[coherent sheaf|56RXEJ8Z6S]] $i_* E$ on $Y$, computed from a finite resolution by vector bundles.
Then there is a polynomial $P_{d,e}$ with integer coefficients, depending only on $d$ and $e$, such that
$$c(i_* E) = 1 + i_* P_{d,e}\big(c_1(E), \ldots, c_e(E), c_1(N), \ldots, c_d(N)\big)$$
in the integral [[Chow ring|EBEF6PEK4N]] $\operatorname{CH}^*(Y)$.

## Remarks

The Grothendieck–Riemann–Roch theorem computes the Chern character of $i_* E$, but only with rational coefficients, because the Chern character and the Todd class have denominators.
The theorem above gives the Chern classes themselves with integer coefficients, at the price of an unknown universal polynomial.
It is due to Jouanolou.
The proof uses deformation to the normal bundle to reduce to the zero section of a vector bundle, where the Koszul complex gives an explicit resolution.

Since $i_*$ raises codimension by $d$, the formula gives $c_k(i_* E) = 0$ for $0 < k < d$.
Comparing with the leading term $e[X]$ of the Chern character in codimension $d$, Newton's identities then give $c_d(i_* E) = (-1)^{d-1} (d-1)! \, e \, [X]$.

Example: for a point $p$ on a nonsingular curve $Y$, the exact sequence $0 \to \mathcal{O}(-p) \to \mathcal{O} \to \mathcal{O}_p \to 0$ gives $c(\mathcal{O}_p) = (1 - [p])^{-1} = 1 + [p]$, in line with $d = e = 1$.

## Explanations

### L1 human

When a vector bundle lives on a subvariety, one can push it forward to the big variety, where it becomes a sheaf supported on the subvariety.
Its Chern classes on the big variety are then determined by the Chern classes of the bundle and of the normal directions, through one fixed polynomial with integer coefficients.
The name says that no fractions are needed, unlike in the usual Riemann–Roch formulas.

### L2 human

This result refines the [[Grothendieck–Riemann–Roch theorem|3HKREN3Y3F]] for a closed embedding, where that theorem involves the Todd class of the normal bundle and rational coefficients.
It matters for torsion phenomena in the Chow ring, which rational statements cannot see.
The special case $c_d(i_* E) = (-1)^{d-1}(d-1)! \, e \, [X]$ shows for instance that the class of a point on a surface appears as $-c_2(\mathcal{O}_p)$.
