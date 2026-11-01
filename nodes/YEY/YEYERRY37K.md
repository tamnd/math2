---
tag: YEYERRY37K
kind: concept
name: HNN extension
msc: ["20E06", "20F05"]
sources:
  - url: https://en.wikipedia.org/wiki/HNN_extension
same_as:
  wikidata: Q3062521
  wikipedia: HNN extension
---

## Summary

An HNN extension of a [[group|G5S1M9]] $G$ adds one new element $t$.
This element conjugates a [[subgroup|0X1JXT47GA]] $H$ of $G$ onto another subgroup $K$ by a given [[isomorphism|08MG7H8JW5]].
The group $G$ embeds in the new group, so two isomorphic subgroups of $G$ become conjugate in a larger group.
The construction is named after Graham Higman, Bernhard Neumann and Hanna Neumann.
Together with the [[free product|TM7QS7P7X9]] with amalgamation, it is a basic way to build groups from smaller ones.
It is used in the proof of the [[Higman embedding theorem|P7TZ694FCM]].

## Explanations

### L1 human

Start with a group $G$ in which two subgroups $H$ and $K$ look alike, through an isomorphism $\alpha$ from $H$ to $K$.
Inside $G$ there may be no element that turns $H$ into $K$ by conjugation.
The HNN extension adds a new letter $t$ and the rules $t h t^{-1} = \alpha(h)$, and nothing else.
For example, take $G = \Z$ written as the powers of $a$, take $H = \langle a \rangle$, $K = \langle a^2 \rangle$ and $\alpha(a) = a^2$.
The HNN extension is $\langle a, t \mid t a t^{-1} = a^2 \rangle$, the [[Baumslag–Solitar group|429JJ5ZNBY]] $BS(1, 2)$.
