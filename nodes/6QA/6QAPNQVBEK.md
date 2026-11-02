---
tag: 6QAPNQVBEK
kind: definition
name: HOMFLY polynomial
msc: [57K14]
defines: QBQ0BH589C
uses: [1A5WRCNTM3, 1TQ06R4Q66]
sources:
  - url: https://en.wikipedia.org/wiki/HOMFLY_polynomial
---

## Definition

Let $\mathcal{L}$ be the set of isotopy classes of oriented tame [[links|1A5WRCNTM3]] in $S^3$.
Let $L_+$, $L_-$ and $L_0$ be oriented links whose diagrams agree outside a small disk.
Inside it, they have a positive crossing, a negative crossing, and the oriented resolution.
The *HOMFLY polynomial* is the unique map $P \colon \mathcal{L} \to \Z[a, a^{-1}, z, z^{-1}]$ such that:

1. $P(O) = 1$ for the [[unknot|1TQ06R4Q66]] $O$;
2. $a \, P(L_+) - a^{-1} P(L_-) = z \, P(L_0)$ for every such triple.

## Remarks

Several conventions for the variables are in use; they differ by substitutions.
Example: a one-crossing diagram of the unknot gives $a - a^{-1} = z \, P(O \sqcup O)$, so the two-component unlink has $P = (a - a^{-1}) z^{-1}$.
Non-example: the map $L \mapsto 1$ satisfies clause 1 but violates clause 2, since $a - a^{-1} \ne z$.
The substitution $a = t^{-1}$, $z = t^{1/2} - t^{-1/2}$ gives the [[Jones polynomial|4SPC17FPXE]].
The substitution $a = 1$, $z = t^{1/2} - t^{-1/2}$ gives the Conway-normalized [[Alexander polynomial|JKA25KDPQP]].
