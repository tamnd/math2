---
tag: VSQGBJVRJN
kind: definition
name: Supergravity
msc: ["83E50", 81T60]
defines: VWBEWVT29C
uses: [7M7M55TKXA, S847N922FY, 6JZW4JC68Z, BY4QYYS788]
sources:
  - url: https://en.wikipedia.org/wiki/Supergravity
---

## Definition

Let $M$ be a $D$-dimensional spin manifold.
A *supergravity theory* on $M$ is a classical field theory with the following properties.

1. Its fields include a vielbein $e^a{}_\mu$, which defines a [[Lorentzian|BY4QYYS788]] metric $g_{\mu\nu} = \eta_{ab} e^a{}_\mu e^b{}_\nu$, and $N \ge 1$ spin-$3/2$ fields $\psi^I_\mu$ (gravitini), and possibly further bosonic and fermionic fields.
2. Its action is invariant under diffeomorphisms of $M$ and local Lorentz transformations of the vielbein.
3. Its action is invariant under local [[supersymmetry|S847N922FY]] transformations, whose parameters are spinor fields $\epsilon^I(x)$, under which $\delta e^a{}_\mu$ is proportional to $\bar\epsilon^I \gamma^a \psi^I_\mu$ and $\delta \psi^I_\mu = D_\mu \epsilon^I + \cdots$.

## Remarks

The commutator of two local supersymmetry transformations contains a diffeomorphism, so local supersymmetry is a gauge version of a super-Poincaré [[superalgebra|6JZW4JC68Z]] that includes translations.
Example: pure $N = 1$ supergravity in $D = 4$ has only the vierbein and one Majorana gravitino, with the Einstein–Hilbert action plus the Rarita–Schwinger action for $\psi_\mu$, written with the torsionful spin connection.
Non-example: the Wess–Zumino model on flat spacetime is supersymmetric but is not supergravity.
It has no vielbein or gravitino, and its supersymmetry parameter is constant, so clauses 1 and 3 fail.
If all fields have spin at most $2$, supergravity exists only for $D \le 11$, and in $D = 4$ one has $N \le 8$.
