---
tag: T6FK1E7GJ1
kind: topic
name: Natural independence results and fast-growing functions
msc: ["03F30", "03F15", "05D10"]
topics: [DYJ0KGTPMR]
---

## Summary

Write $3$ in base $2$, raise the base to $3$, subtract one, and repeat: the numbers $3, 3, 3, 2, 1, 0$ reach zero, and so does every such sequence.
Goodstein proved this in 1944, and Kirby and Paris showed in 1982 that [[Peano arithmetic|MPSCREYC3M]] cannot prove it.
This topic, a part of [[mathematical logic|DYJ0KGTPMR]], collects true statements about numbers, trees and colorings that a given theory cannot prove.

The method is the same each time.
Each statement says that some process stops, and the time it takes is a function of the input.
A theory proves the statement only if it proves that function total, and each function that $\mathsf{PA}$ proves total is eventually dominated by some $f_\alpha$ with $\alpha < \varepsilon_0$.
So a statement whose witness grows like $f_{\varepsilon_0}$ escapes $\mathsf{PA}$.
$\mathsf{PA}$ with transfinite induction up to $\varepsilon_0$, the ordinal of Gentzen's consistency proof of 1936, proves it.
Stronger statements, such as Friedman's finite form of Kruskal's theorem of 1960, escape stronger theories by the same mechanism.

## Remarks

### Reading order

1. [[Goodstein's theorem|XQMNJF241J]]: a sequence you can run by hand, and the first proof by ordinals below $\varepsilon_0$.
2. [[Provably total function|Z742YPHPNS]]: why a fast witness function makes a statement unprovable.
3. [[Fast-growing hierarchy|R6ZC4BJGXV]]: the ruler $f_\alpha$, with $f_2(x) = x \cdot 2^x$, that measures theories.
4. [[Hardy hierarchy|X8RKXQASR9]]: the functions $H_\alpha$ that give the exact length of a Goodstein sequence.
5. [[Slow-growing hierarchy|VDF6R9EVJ2]]: a contrast that shows how much growth comes from the fundamental sequences.
6. [[Kirby-Paris hydra|C028FF4TWM]]: the same ordinals as a game on trees, with a battle that ends after $37$ cuts.
7. [[Beklemishev's worm principle|MHDZGDNEPS]]: the same ordinals once more, read from provability logic.
8. [[Strengthened finite Ramsey theorem|4P2BAT6YC3]]: a small change to Ramsey's theorem, proved by compactness.
9. [[Paris-Harrington theorem|509ZWA0R26]]: the first natural statement proved independent of $\mathsf{PA}$, in 1977.
10. [[Indicators|JWTZ8NVVGK]]: the model-theoretic tool behind that proof, with worked examples of cuts.
11. [[Kanamori-McAloon theorem|NM5WYBK6BG]]: a second Ramsey-type statement, about regressive colorings.
12. [[Buchholz hydra theorem|9APRFM0G7F]]: labeled hydras that escape a much stronger theory.
13. [[Friedman's finite form of Kruskal's theorem|12XRGBWH59]]: sequences of trees that $\mathsf{ATR}_0$ cannot control.
14. [[Unprovability of the graph minor theorem|WXNTPQGJ38]]: the same phenomenon for graphs and $\Pi^1_1\text{-}\mathsf{CA}_0$.
15. [[Concrete mathematical incompleteness|E2H655A7BS]]: the whole program at a glance, from $\mathsf{PA}$ upward.

### Prerequisites

- [[Gödel's incompleteness theorems and related limits|HXHHWY3328]]: the incompleteness theorems and consistency statements.
- [[Ordinal analysis and ordinal notations|XTTKZTYDSD]]: [[epsilon nought|KT50SMH3EC]], Cantor normal form and transfinite induction.
- [[Formal arithmetic and its fragments|QHCRN4JVG0]]: [[Peano arithmetic|MPSCREYC3M]], its fragments and [[non-standard models|1QWN5CV4CG]].
