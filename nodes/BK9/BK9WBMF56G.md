---
tag: BK9WBMF56G
kind: concept
name: Tate–Shafarevich group
msc: [11G05, 11R34, 14H52]
sources:
  - url: https://en.wikipedia.org/wiki/Tate%E2%80%93Shafarevich_group
same_as:
  wikidata: Q7688027
  wikipedia: Tate–Shafarevich group
---

## Summary

Let $E$ be an [[elliptic curve|427N6S6QQW]] over a [[number field|MWBDFS2KJ5]] $K$.
Its Tate–Shafarevich group $\text{Ш}(E/K)$ measures the failure of the [[Hasse principle|EMAR4X3W8D]] for twisted forms of $E$.
Its elements are classes of genus one curves that become isomorphic to $E$ over an algebraic closure.
These curves have points over every completion of $K$, and the trivial class is that of curves with a point over $K$.
It is conjectured to be finite, and its order enters the [[Birch and Swinnerton-Dyer conjecture|ZWEFBG40H9]].

## Explanations

### L1 human

To find rational points on a curve, one first checks whether the curve has points over the real numbers and over every $p$-adic field.
For some curves of genus one, all these local tests succeed, and yet there is no rational point.
The Tate–Shafarevich group collects exactly these deceptive curves, attached to a given elliptic curve.
A classical example is Selmer's curve $3x^3 + 4y^3 + 5z^3 = 0$: it has points over $\R$ and every $\Q_p$, but no rational point other than $(0,0,0)$.
When the group is trivial, local information is enough to decide such questions for that elliptic curve.
