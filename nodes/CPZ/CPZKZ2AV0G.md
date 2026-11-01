---
tag: CPZKZ2AV0G
kind: statement
role: theorem
name: Gleason's theorem on projective compact spaces
msc: [54G05, 18G05, 54D30]
uses: [0TVJZYB6SH, 0S1FJ8VEX9, 0VGFHTM75Y, 370PJ5BF70]
about: [370PJ5BF70]
sources:
  - url: https://en.wikipedia.org/wiki/Extremally_disconnected_space
---

## Statement

A [[compact|0TVJZYB6SH]] [[Hausdorff space|0S1FJ8VEX9]] $P$ is *projective* if it satisfies the following lifting property.
For all compact Hausdorff spaces $Y$ and $Z$, every continuous surjection $f \colon Y \to Z$ and every [[continuous map|0VGFHTM75Y]] $g \colon P \to Z$, there is a continuous map $h \colon P \to Y$ with $f \circ h = g$.

Let $P$ be a compact Hausdorff space.
Then $P$ is projective if and only if $P$ is [[extremally disconnected|370PJ5BF70]].

## Remarks

For one direction, let $D$ be the set $P$ with the discrete topology.
The identity $D \to P$ extends to a surjection $\beta D \to P$ from the [[Stone–Čech compactification|D9MWP5C85W]].
If $P$ is projective, it is a retract of $\beta D$, which is extremally disconnected, and retracts inherit the property.
The other direction uses a closed subset of the pullback that is minimal among those mapping onto $P$, found by Zorn's lemma.

Example at work: $\beta \N$ is extremally disconnected, so it is projective.

## Explanations

### L1 human

Projective compact Hausdorff spaces are those from which maps can always be lifted along surjections.
Gleason's theorem says that, among compact Hausdorff spaces, these are exactly the spaces where closures of open sets are open.
So a categorical property is matched with a concrete topological one.

### L2 human

Every compact Hausdorff space $X$ is a continuous image of a projective one, namely $\beta D$ for $D$ the set $X$ with the discrete topology.
In fact $X$ has a projective cover, often called its Gleason cover.
Through Stone duality, extremally disconnected compact Hausdorff spaces correspond to complete [[Boolean algebras|0XADJKM699]].
