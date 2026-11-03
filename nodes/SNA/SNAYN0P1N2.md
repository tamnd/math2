---
tag: SNAYN0P1N2
kind: statement
role: theorem
name: Zamolodchikov c-theorem
msc: [81T40, 82B28]
uses: [5XTSCZCF7Z, H0B5TN4139, R9WFXME6GC]
about: [5XTSCZCF7Z]
sources:
  - url: https://en.wikipedia.org/wiki/C-theorem
same_as:
  wikidata: Q5005965
  wikipedia: C-theorem
---

## Statement

Consider a two-dimensional quantum field theory that is unitary (reflection positive), invariant under rotations and translations, and has a conserved, symmetric stress-energy tensor.
Let it depend on coupling constants $g = (g^1, \dots, g^n)$ that flow under the [[renormalization group|5XTSCZCF7Z]].
Then there is a real function $C(g)$ on the space of couplings with these properties.

1. $C$ is non-increasing along the renormalization group flow toward long distances, and it is constant along a flow line only at a [[fixed point|H0B5TN4139]].
2. At a fixed point $g^*$ the theory is a conformal field theory, and $C(g^*)$ equals its central charge $c$.
   This is the number that appears in the [[Virasoro algebra|R9WFXME6GC]] of the theory.

## Remarks

The theorem was proved by Alexander Zamolodchikov in 1986.
In complex coordinates, write $T$ for the component $T_{zz}$ of the stress tensor and $\Theta$ for its trace.
The function $C$ is an explicit linear combination of the two-point functions $\langle T T \rangle$, $\langle T \Theta \rangle$ and $\langle \Theta \Theta \rangle$ at distance $r$.
Each of them is multiplied by the power of $z$ and $\bar z$ that makes it dimensionless.
Conservation of the stress tensor shows that the derivative of $C$ with respect to $\log r$ is a negative multiple of $r^4 \langle \Theta(r) \Theta(0) \rangle$.
Reflection positivity makes this two-point function non-negative, which gives the monotonicity; it vanishes only when $\Theta = 0$, that is, at a conformal point.

Consequence: if a flow starts near a fixed point with central charge $c_{\mathrm{UV}}$ and ends at one with central charge $c_{\mathrm{IR}}$, then $c_{\mathrm{UV}} \ge c_{\mathrm{IR}}$.
For example, a massive deformation of the critical Ising model, which has $c = 1/2$, flows to a theory with no long-range degrees of freedom, which has $c = 0$.

Unitarity is necessary for the argument: in non-unitary theories the positivity of $\langle \Theta \Theta \rangle$ fails, and the central charge can increase along a flow.

## Explanations

### L1 human

The central charge of a critical system roughly counts how many independent kinds of fluctuations it has.
Coarse-graining a system can only throw information away, never create it.
The c-theorem makes this precise in two dimensions: there is a quantity that decreases along every renormalization flow and equals the central charge at critical points.
So a flow from one critical point to another always lowers the central charge.

### L2 human

The theorem forbids renormalization group flows in two dimensions from being periodic.
Since $C$ strictly decreases along nontrivial flow lines, flows run from fixed points with larger $c$ to fixed points with smaller $c$.
It is a strong constraint on the phase diagrams of two-dimensional statistical models, whose critical points are described by conformal field theories.
In four dimensions the analogous statement for the coefficient $a$ of the trace anomaly is the a-theorem.
