---
tag: HMXVAGW2KD
kind: problem
name: Tannaka–Artin problem
msc: [19B99, "16K20"]
uses: [5HRKJBAY2V, 0EA5BTA0CX, 2FATVDAN2E, 0ASGSTXSBW, AAB05HS00Y]
about: [AAB05HS00Y, 2FATVDAN2E]
sources:
  - url: https://en.wikipedia.org/wiki/Central_simple_algebra
  - url: http://www.mathnet.ru/eng/im2107
history:
  posed_by: "Tadao Tannaka and Emil Artin"
---

## Problem

Let $F$ be a field.
Let $D$ be a [[division ring|0EA5BTA0CX]] that is a [[central simple algebra|5HRKJBAY2V]] of finite dimension over $F$.
Let $\mathrm{Nrd} \colon D^\times \to F^\times$ be the [[reduced norm|2FATVDAN2E]].
Let $SL_1(D) = \set{d \in D^\times : \mathrm{Nrd}(d) = 1}$ and let $[D^\times, D^\times]$ be the [[commutator subgroup|0ASGSTXSBW]] of $D^\times$.
The reduced Whitehead group is $SK_1(D) = SL_1(D) / [D^\times, D^\times]$.
The Tannaka–Artin problem asks: is $SK_1(D)$ trivial for every such $D$?
Equivalently: is every element of reduced norm $1$ a product of commutators?

## Remarks

The quotient makes sense because $\mathrm{Nrd}$ is multiplicative with values in the commutative group $F^\times$, so every commutator has reduced norm $1$.
The group $SK_1(D)$ is the kernel of the map $K_1(D) \to F^\times$ induced by the reduced norm, so it is the group [[SK1|AAB05HS00Y]] of $D$.
[[Wang's theorem|AG1C9C04K5]] gives a positive answer when the degree of $D$ is squarefree and when $F$ is an algebraic number field.
The answer is negative in general.
Platonov settled the problem in 1975 with division algebras of degree $p^2$, for a prime $p$, over fields of iterated Laurent series, whose group $SK_1$ is not trivial.
His method computes $SK_1(D)$ through a group of projective conorms, and it connects the problem with number theory.

## Explanations

### L1 human

In a division algebra the reduced norm plays the part of the determinant.
Commutators $aba^{-1}b^{-1}$ always have reduced norm $1$, just as commutators of matrices have determinant $1$.
The problem asks whether the converse always holds: does reduced norm $1$ force an element to be a product of commutators?
It holds in many familiar cases, but Platonov found division algebras where it fails.
