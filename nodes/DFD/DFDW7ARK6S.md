---
tag: DFDW7ARK6S
kind: definition
name: Coherent ring
msc: ["13E15", "13E99"]
defines: W453BM8T6P
uses: [0GYGHKX834, 030TZ0DQWT, 3EH4C3M5GV, 09VDS2W1E8]
sources:
  - url: https://en.wikipedia.org/wiki/Coherent_ring
---

## Definition

Let $R$ be a [[commutative ring|0GYGHKX834]].
The ring $R$ is *coherent* if every [[finitely generated ideal|030TZ0DQWT]] of $R$ is [[finitely presented|3EH4C3M5GV]] as an $R$-[[module|09VDS2W1E8]].

## Remarks

Equivalently, for every $a_1, \dots, a_n \in R$, the module of relations $\set{(r_1, \dots, r_n) \in R^n : r_1 a_1 + \cdots + r_n a_n = 0}$ is finitely generated.
Example: every [[Noetherian ring|0MVH4Y1CRZ]] is coherent, because the module of relations is a submodule of $R^n$, which is a Noetherian module.
Non-example: let $R = k[x, y_1, y_2, \dots]/(x y_1, x y_2, \dots)$ over a field $k$.
The relations of the single element $x$ form the ideal $(y_1, y_2, \dots)$ of $R$, which is not finitely generated.
So the ideal $(x)$ is finitely generated but not finitely presented.
For a noncommutative ring one defines left coherent rings: every finitely generated left ideal is finitely presented.

## Explanations

### L1 human

A ring is coherent when every finite list of elements has a finite list of basic relations, from which all relations follow.
