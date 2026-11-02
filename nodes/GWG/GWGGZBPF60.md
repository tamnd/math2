---
tag: GWGGZBPF60
kind: definition
name: Enough projectives
msc: [18G05, 18G10]
defines: J2TX4TDPCX
uses: [A2DE66937D, YXMXAGVC1Q, RVXDSY04KG]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_object
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]].
The category $\mathcal{C}$ *has enough projectives* if for every object $X$ of $\mathcal{C}$ there are a [[projective object|YXMXAGVC1Q]] $P$ and an [[epimorphism|RVXDSY04KG]] $P \to X$.

## Remarks

Example: the category of modules over a [[ring|0B1261B5ED]] $R$ has enough projectives.
For a module $M$, let $F$ be the [[free module|0DZ9DKAKZR]] with basis $\set{e_m : m \in M}$.
The map $F \to M$ with $e_m \mapsto m$ is surjective, and free modules are [[projective|BFFA03GE3V]].
Non-example: the category of finite abelian groups has no nonzero projective object.
For $n \ge 2$ the quotient map $\Z/n^2\Z \to \Z/n\Z$ does not split, since $\Z/n^2\Z$ is cyclic, so $\Z/n\Z$ is not projective there.
Every nonzero finite abelian group has such a cyclic direct summand, and a direct summand of a projective object is projective.
So no epimorphism from a projective object onto $\Z/2\Z$ exists.
The dual notion is *enough injectives*: every object admits a monomorphism into an [[injective object|5QRFTBF4PG]].
