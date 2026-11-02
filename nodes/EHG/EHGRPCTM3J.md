---
tag: EHGRPCTM3J
kind: definition
name: Haagerup property
msc: [22D55, 20F65]
defines: 5FG1BKZXKS
uses: [AHV05ZBCYW, 74BPYJNZTM, HM2HHE3J51, 0TVJZYB6SH]
sources:
  - url: https://en.wikipedia.org/wiki/Haagerup_property
---

## Definition

Let $G$ be a second countable [[locally compact group|AHV05ZBCYW]].
A [[unitary representation|74BPYJNZTM]] $\pi$ of $G$ on a [[Hilbert space|HM2HHE3J51]] $\mathcal{H}$ is *mixing* if $\ip{\pi(g)\xi}{\eta} \to 0$ as $g \to \infty$, for all $\xi, \eta \in \mathcal{H}$.
Here $g \to \infty$ means that $g$ leaves every [[compact|0TVJZYB6SH]] subset of $G$.
The representation $\pi$ *almost has invariant vectors* if the following holds.
For every compact $Q \subseteq G$ and $\varepsilon > 0$, there is a unit vector $\xi$ with $\norm{\pi(g)\xi - \xi} < \varepsilon$ for all $g \in Q$.
The group $G$ has the *Haagerup property* if it has a mixing unitary representation that almost has invariant vectors.

## Remarks

Example: $G = \Z$ and the regular representation on $\ell^2(\Z)$.
For finitely supported $\xi$ and $\eta$, the coefficient $\ip{\pi(n)\xi}{\eta}$ is $0$ once $\abs{n}$ is large, and by density the representation is mixing.
The unit vectors $N^{-1/2} \mathbf{1}_{\set{0, \ldots, N-1}}$ are almost invariant for large $N$.

Non-example: $\mathrm{SL}_3(\Z)$ does not have the Haagerup property.
It has [[property (T)|GTFZ277047]], so a representation that almost has invariant vectors has a nonzero invariant vector $\xi$.
Then $\ip{\pi(g)\xi}{\xi} = \norm{\xi}^2$ for all $g$, which does not tend to $0$ on the infinite group.

Equivalently, $G$ has a proper continuous conditionally negative definite function $\psi \colon G \to [0, \infty)$.
Another equivalent form: $G$ has a continuous affine isometric action on a Hilbert space that is metrically proper.
Amenable groups, free groups and $\mathrm{SL}_2(\R)$ have the Haagerup property.
