---
tag: RNPDXXBSMG
kind: definition
name: Batalin–Vilkovisky formalism
msc: [81T70, 81T13, 58A50]
defines: 3QM47B8TYP
uses: [0MDMZ965VE, ARMX1P0X0S, Z0SB9HQBAJ, DCHKJBKCMR]
sources:
  - url: https://en.wikipedia.org/wiki/Batalin%E2%80%93Vilkovisky_formalism
---

## Definition

Consider, for simplicity, finitely many even fields $\phi^1, \dots, \phi^n$, which are real coordinates on $\R^n$.
Introduce one *antifield* $\phi^*_i$ for each $\phi^i$, of opposite (odd) parity.
The algebra of functions of fields and antifields is $\mathcal{A} = C^\infty(\R^n) \otimes \Lambda[\phi^*_1, \dots, \phi^*_n]$.
It is the algebra of a [[supermanifold|Z0SB9HQBAJ]], whose odd part is an [[exterior algebra|0MDMZ965VE]].
The *BV Laplacian* is the operator on $\mathcal{A}$
$$\Delta = \sum_{i=1}^n \frac{\partial}{\partial \phi^i} \frac{\partial}{\partial \phi^*_i},$$
with left derivatives in the odd variables.
The *antibracket* of $F, G \in \mathcal{A}$, with $F$ of parity $\abs{F}$, is
$$(F, G) = (-1)^{\abs{F}} \left( \Delta(FG) - (\Delta F)\, G - (-1)^{\abs{F}} F\, \Delta G \right).$$
In the *BV formalism*, a gauge theory is described by an even formal power series $S$ in $\hbar$ with coefficients in $\mathcal{A}$, the BV action.
It must satisfy the *quantum master equation*
$$\tfrac12 (S, S) = i\hbar\, \Delta S,$$
equivalently $\Delta\, e^{iS/\hbar} = 0$.
For theories with odd fields (ghosts) the same construction is made with fields of both parities and the usual sign rules.

## Remarks

The operator $\Delta$ satisfies $\Delta^2 = 0$, since the derivatives in the even variables commute and those in the odd variables anticommute.
With the bracket $(\cdot, \cdot)$, the algebra $\mathcal{A}$ is a [[Batalin–Vilkovisky algebra|ARMX1P0X0S]].
The equivalence of the two forms of the master equation follows from $\Delta e^{f} = \left( \Delta f + \frac12 (f, f) \right) e^{f}$ for even $f$, applied to $f = iS/\hbar$.
At order $\hbar^0$ the master equation gives the classical master equation $(S_0, S_0) = 0$.

Example: if $S = S_0(\phi)$ does not depend on the antifields, then $\Delta S = 0$ and $(S, S) = 0$, so $S$ satisfies the quantum master equation; this is a theory without gauge symmetry.

Non-example: for $n = 2$ and $S = \phi^1 \phi^*_1 \phi^*_2$, one has $S^2 = 0$ and $S\, \Delta S = 0$, so $(S, S) = 0$ and the classical master equation holds.
But $\Delta S = \frac{\partial}{\partial \phi^1}(\phi^1 \phi^*_2) = \phi^*_2 \ne 0$, so $S$ does not satisfy the quantum master equation.

In the gauge theory case the antifield of each field enters $S$ through the BRST transformation: to first order in antifields, $S = S_0 + \sum_i \phi^*_i\, s\phi^i + \cdots$, where $s$ is the [[BRST|DCHKJBKCMR]] differential.
Gauge fixing restricts the integral of $e^{iS/\hbar}$ to a Lagrangian submanifold for the odd symplectic structure.
The master equation makes the result independent of small deformations of this submanifold.
