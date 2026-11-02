---
tag: MCW8V4RFYJ
kind: definition
name: Complete atomic Boolean algebra
msc: ["06E10", "06E05"]
defines: P5MA4CDRNA
uses: [75BPV95AAS, TTVCTW6TNC, 5SE8EMSDNY]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_Boolean_algebra
---

## Definition

Let $B$ be a Boolean algebra.
An [[atom|TTVCTW6TNC]] of $B$ is an element $a \ne 0$ such that there is no $b$ with $0 < b < a$.
The algebra $B$ is a *complete atomic Boolean algebra* if:

1. $B$ is a [[complete Boolean algebra|75BPV95AAS]].
2. $B$ is [[atomic|5SE8EMSDNY]]: for every $b \ne 0$ in $B$ there is an atom $a$ with $a \le b$.

## Remarks

If $B$ is complete and atomic, with set of atoms $A$, then $b \mapsto \set{a \in A : a \le b}$ is an isomorphism from $B$ onto the power set of $A$.
So the complete atomic Boolean algebras are, up to isomorphism, the power set algebras.

Example: the power set of a set $X$.
It is complete, and every nonempty $Y \subseteq X$ contains a singleton $\set{x}$, which is an atom.

Non-example: the algebra of [[regular open sets|833XAA2Q65]] of $\R$ is complete but has no atom at all.
Every nonempty regular open set contains an open interval, which contains two disjoint smaller open intervals, and these are regular open and strictly smaller.
So clause 2 fails.

In Mathlib the notion is `CompleteAtomicBooleanAlgebra`.
