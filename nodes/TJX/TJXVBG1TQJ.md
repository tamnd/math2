---
tag: TJXVBG1TQJ
kind: definition
name: T-duality
msc: [81T30, "83E30"]
defines: RD9MTZ0PEP
uses: [GM58M1HFY0, 060W5CBZP6, HFEGZQB8SV]
sources:
  - url: https://en.wikipedia.org/wiki/T-duality
---

## Definition

Consider closed bosonic [[string theory|GM58M1HFY0]], with Regge slope $\alpha' > 0$, on the spacetime $\R^{1,24} \times S^1_R$, where $S^1_R$ is a [[circle|060W5CBZP6]] of radius $R > 0$.
A closed string state has a momentum number $n \in \Z$, with momentum $n/R$ along the circle, a winding number $w \in \Z$, and oscillator levels $N, \tilde N \in \N$.
Its mass $M$ in the $25$ non-compact dimensions satisfies
$$M^2 = \frac{n^2}{R^2} + \frac{w^2 R^2}{\alpha'^2} + \frac{2}{\alpha'}\big(N + \tilde N - 2\big), \qquad N - \tilde N = n w.$$
*T-duality* is the equivalence of the theory at radius $R$ with the theory at radius $\alpha'/R$.
It maps states by exchanging $n$ and $w$ and keeping $N$ and $\tilde N$.
On the worldsheet fields it acts by $X_L \mapsto X_L$ and $X_R \mapsto -X_R$ on the left- and right-moving parts of the circle coordinate.

## Remarks

Check on the spectrum: the mass formula and the condition $N - \tilde N = nw$ are unchanged by $R \mapsto \alpha'/R$ together with $n \leftrightarrow w$.
The duality also holds for interactions.
Example: at the self-dual radius $R = \sqrt{\alpha'}$ the map sends the theory to itself, and extra massless states appear, giving an enhanced $SU(2) \times SU(2)$ gauge symmetry.
Non-example: on a non-compact direction $\R$ there are no winding states, and there is no T-duality in that direction.
For open strings, T-duality exchanges Neumann and Dirichlet boundary conditions, and so relates D-branes of different dimensions.
For type II [[superstrings|N993FCEJY2]], T-duality on one circle maps type IIA on radius $R$ to type IIB on radius $\alpha'/R$.
The [[Polyakov action|HFEGZQB8SV]] gives the worldsheet theory on which the duality acts.
