---
tag: 3EVAF9NG5Z
kind: statement
role: theorem
name: Ending lamination theorem
msc: [57K32, 30F40]
uses: [GHVW1Z35BS, S1XK3HXHFX, DE1Z7R9T05]
about: [GHVW1Z35BS]
sources:
  - url: https://en.wikipedia.org/wiki/Ending_lamination_theorem
same_as:
  wikidata: Q5376147
  wikipedia: Ending lamination theorem
---

## Statement

Let $M$ be a [[hyperbolic 3-manifold|GHVW1Z35BS]] with finitely generated [[fundamental group|S1XK3HXHFX]].
Each end of $M$ carries an *end invariant*.
For a geometrically finite end, it is a point of a Teichmüller space.
For a degenerate end, it is an ending lamination on a surface.
Then $M$ is determined up to isometry by its topological type together with its end invariants.

## Remarks

Thurston conjectured the theorem.
Brock, Canary and Minsky proved it, first for manifolds homeomorphic to $S \times \R$ for a surface $S$, building on earlier work of Minsky.
The general case uses the [[tameness theorem|DE1Z7R9T05]], which makes the ends of $M$ products of a surface and a half-line, so that end invariants make sense.
The proof builds a combinatorial model manifold from the end invariants, using the curve complex, and shows that $M$ is bilipschitz to this model.
For example, a quasi-Fuchsian manifold $S \times \R$ has two geometrically finite ends.
The theorem then recovers Bers simultaneous uniformization: the manifold is determined by a pair of points in the [[Teichmüller space|ZZGC6BZNJ5]] of $S$.

## Explanations

### L1 human

A hyperbolic $3$-manifold with finitely generated fundamental group may have ends that open out to infinity.
Each end leaves a trace at infinity, either a shape of surface or a pattern of curves called a lamination.
The theorem says that the topology and these traces at infinity pin down the whole geometry.

### L2 human

The theorem completes the classification of hyperbolic $3$-manifolds with finitely generated fundamental group.
Together with tameness, it was used to prove the density theorem: every finitely generated Kleinian group is a limit of geometrically finite ones.
It also makes rigorous Thurston's picture of doubly degenerate surface groups, such as the fiber group of a fibered hyperbolic $3$-manifold.
