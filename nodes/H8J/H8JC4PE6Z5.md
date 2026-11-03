---
tag: H8JC4PE6Z5
kind: definition
name: Causal sets
msc: [83C45, 06A06]
defines: 1VDKXSAFRE
uses: [0QV2JS9RJ3, TV1V4JDRDD, KZWG5F0TSB, 0MTNR28K60]
sources:
  - url: https://en.wikipedia.org/wiki/Causal_sets
---

## Definition

A *causal set* is a set $C$ with a binary relation $\preceq$ such that:

1. $\preceq$ is a [[partial order|0QV2JS9RJ3]]: reflexive, antisymmetric and transitive;
2. $\preceq$ is locally finite: for all $x, z \in C$ the interval $\set{y \in C : x \preceq y \preceq z}$ is finite.

So a causal set is a [[locally finite poset|TV1V4JDRDD]].
Let $(M, g)$ be a Lorentzian manifold and let $\phi \colon C \to M$ be an injective map.
The map $\phi$ is a *faithful embedding* if two conditions hold.
First, $x \preceq y$ exactly when $\phi(x)$ is in the causal past of $\phi(y)$.
Second, the image looks like a [[Poisson sprinkling|0MTNR28K60]] of density $\rho$: each region of volume $V$ contains about $\rho V$ points.

## Remarks

Example: take a Poisson sprinkling of density $\rho$ into a bounded region of Minkowski space, with the order "lies in the causal past of".
This is a causal set, since every interval lies in a compact causal diamond, which almost surely contains finitely many points.
Non-example: the set of all points of Minkowski space with the causal order is a partial order but not locally finite, since every nontrivial interval is uncountable.
The use of Poisson sprinkling makes the discreteness compatible with Lorentz invariance in a statistical sense.
The central conjecture of the programme (the Hauptvermutung) is that a causal set faithfully embeds into two spacetimes only if they are approximately isometric at scales large compared to $\rho^{-1/4}$.
