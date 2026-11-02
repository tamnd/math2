---
tag: TQ1QDAK2BR
kind: conjecture
name: Lang's conjectures
msc: [14G05, 11G35, 14G40]
uses: [MWBDFS2KJ5, SWJYG87QQH, ZW00Q0SAGR, 8SQK7RTB63]
about: [SWJYG87QQH]
sources:
  - url: https://en.wikipedia.org/wiki/Bombieri%E2%80%93Lang_conjecture
history:
  posed_by: "Enrico Bombieri and Serge Lang"
  first_stated: "1980"
---

## Statement

Let $K$ be an [[algebraic number field|MWBDFS2KJ5]] and let $X$ be a projective variety of general type over $K$.
This means that the [[Kodaira dimension|ZW00Q0SAGR]] of $X$ equals its dimension.

1. The set $X(K)$ of $K$-[[rational points|SWJYG87QQH]] is not dense in $X$ for the [[Zariski topology|8SQK7RTB63]].
2. There is a nonempty Zariski open subset $U \subseteq X$ such that $U(L)$ is finite for every finite extension $L$ of $K$.

## Remarks

Part 1 is often called the Bombieri–Lang conjecture.
Bombieri posed it for surfaces in a 1980 lecture, and Lang posed it in general.
For curves, general type means genus at least $2$, and both parts follow from [[Faltings's theorem|H0DB07WM20]].
The conjecture is open for surfaces.
It follows from [[Vojta's conjecture|QQ717VSFNN]].
Caporaso, Harris and Mazur showed in 1997 that it implies a uniform bound for curves.
The number of $K$-rational points on a curve of genus $g \ge 2$ over $K$ would be bounded in terms of $g$ and $K$ only.

## Explanations

### L1 human

Faltings proved that a curve of genus at least two has only finitely many rational points.
Lang's conjectures predict the same kind of scarcity in higher dimension, for varieties "of general type", the most curved ones.
Rational points may be infinite, but they should all lie on a smaller subvariety, outside of which there are only finitely many.
