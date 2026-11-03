---
tag: Q4YP8M4HY0
kind: definition
name: Membrane theory of shells
msc: [74K25, 74K15]
defines: 1ND17AY99Y
uses: [DF7RPJHHY1, 9KHQR16P1B, MAJ3DH7MZS]
sources:
  - url: https://en.wikipedia.org/wiki/Membrane_theory_of_shells
---

## Definition

Let $S$ be the middle surface of a thin shell, with metric $a_{\alpha\beta}$, the [[first fundamental form|MAJ3DH7MZS]], and covariant derivative $\nabla_\beta$.
Let $b_{\alpha\beta}$ be its [[second fundamental form|9KHQR16P1B]] with respect to a unit normal $a_3$.
Let the load per unit area of $S$ have tangential components $p^\alpha$ and normal component $p^3$ along $a_3$.
The *membrane theory of shells* is the [[shell theory|DF7RPJHHY1]] in which the bending moments and transverse shear forces are zero.
The symmetric membrane forces $N^{\alpha\beta}$ satisfy
$$\nabla_\beta N^{\alpha\beta} + p^\alpha = 0, \qquad b_{\alpha\beta} N^{\alpha\beta} + p^3 = 0.$$
Indices run over $1, 2$ and repeated indices are summed.

## Remarks

Example: a sphere of radius $R$ under an internal pressure $p$.
With $a_3$ the inward normal, $b_{\alpha\beta} = a_{\alpha\beta}/R$ and the load is $p^3 = -p$.
The uniform tension $N^{\alpha\beta} = N a^{\alpha\beta}$ has $\nabla_\beta N^{\alpha\beta} = 0$ and $b_{\alpha\beta}N^{\alpha\beta} = 2N/R$, so $N = pR/2$.
For a closed circular cylinder of radius $R$ the normal equation gives the hoop force $pR$, and the equilibrium of an end cap gives the axial force $pR/2$.

Non-example: a flat plate under a transverse load has $b_{\alpha\beta} = 0$, so the normal equation forces $p^3 = 0$; a membrane state cannot carry the load, which the plate must carry by bending.

The equations are three equations for three unknowns $N^{11}, N^{12}, N^{22}$, so the membrane forces are statically determinate given suitable edge conditions.
The sign of the normal equation depends on the choice of $a_3$.
