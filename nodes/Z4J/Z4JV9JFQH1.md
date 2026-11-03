---
tag: Z4JV9JFQH1
kind: conjecture
name: Bass conjecture
msc: [19D50, "19E08"]
uses: [5GVFZWMWC8, 0670T59HGE, YZSR4QKDQQ, PXYP8675C2]
about: [5GVFZWMWC8]
sources:
  - url: https://en.wikipedia.org/wiki/Bass_conjecture
history:
  posed_by: Hyman Bass
  first_stated: "1973"
---

## Statement

Let $A$ be a commutative regular [[Noetherian ring|0670T59HGE]] that is finitely generated as an algebra over $\Z$.
Then for every $n \ge 0$ the [[algebraic K-group|5GVFZWMWC8]] $K_n(A)$ is a finitely generated abelian group.

## Remarks

A form often stated uses [[G-theory|YZSR4QKDQQ]]: for every commutative ring $A$ finitely generated over $\Z$, the groups $G_n(A)$ are finitely generated.
It implies the first form, because $K_n(A) \cong G_n(A)$ for regular $A$.

The conjecture is open in general.
The ring of integers $\mathcal{O}_F$ of a number field $F$ is regular and finitely generated over $\Z$, and for it the conjecture is [[Quillen's finite generation theorem|PXYP8675C2]].
With the localization sequence and the K-theory of finite fields, the same follows for the rings $\mathcal{O}_F[1/N]$.

## Explanations

### L1 human

For the simplest arithmetic rings, such as $\Z$ or the integers of a number field, all K-groups are built from finitely many generators.
Bass asked whether this stays true for every regular ring that is finitely generated over $\Z$.
The question is still open in general.
