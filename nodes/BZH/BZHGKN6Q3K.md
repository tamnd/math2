---
tag: BZHGKN6Q3K
kind: statement
role: theorem
name: Mordell's theorem
msc: [11G05, 14G05, 14H52]
uses: [427N6S6QQW, P7V1BQJPSS, 0NCJ5WXN6Z, 082DWWXMRJ, 082GHNPJ53]
about: [427N6S6QQW, P7V1BQJPSS]
sources:
  - url: https://en.wikipedia.org/wiki/Mordell%E2%80%93Weil_theorem
---

## Statement

Let $E$ be an [[elliptic curve|427N6S6QQW]] over the field $\Q$ of [[rational numbers|0NCJ5WXN6Z]].
Then the group $E(\Q)$ of rational points of $E$, with the [[chord-and-tangent law|P7V1BQJPSS]], is a [[finitely generated|082DWWXMRJ]] [[abelian group|082GHNPJ53]].

## Remarks

By the structure theorem for finitely generated abelian groups, $E(\Q) \cong \Z^r \oplus T$, where $T$ is the finite torsion subgroup and $r \ge 0$ is the rank of $E$.
The proof has two steps.
The weak Mordell theorem says that $E(\Q)/2E(\Q)$ is finite; it is proved with a descent map into a finite group built from square classes of rationals.
Then a height function $h$ on $E(\Q)$, with finitely many points of bounded height and $h(2P) \approx 4h(P)$, lets one show by descent that finitely many points together with $2E(\Q)$ generate everything.
Example: for $y^2 = x^3 - x$ one has $E(\Q) = \set{O, (0,0), (1,0), (-1,0)}$, of rank $0$.
Weil extended the theorem to abelian varieties over number fields; the general result is the Mordell–Weil theorem.

## Explanations

### L1 human

An elliptic curve over the rationals can have infinitely many rational points.
Mordell's theorem says that they are never a shapeless infinite mess: finitely many of them generate all others by the chord-and-tangent construction.

### L2 human

The theorem gives the two basic invariants of an elliptic curve over $\Q$.
The torsion subgroup is described by [[Mazur's torsion theorem|RQS6YHAR8N]], and the rank is the subject of the [[Birch and Swinnerton-Dyer conjecture|ZWEFBG40H9]].
The descent step uses [[height functions|F1FF505PWH]], and the obstruction to making descent effective is measured by the [[Selmer group|36YNSTESMQ]] and the [[Tate–Shafarevich group|BK9WBMF56G]].
No algorithm is known that provably computes the rank in all cases.
