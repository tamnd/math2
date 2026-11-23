---
tag: XTTKZTYDSD
kind: topic
name: Ordinal analysis and ordinal notations
msc: ["03F15", "03F05"]
topics: [DYJ0KGTPMR]
---

## Summary

Peano arithmetic proves that the ordinals below $\omega^{\omega^\omega}$ are well-ordered, but it cannot prove the same for $\varepsilon_0$, the limit of the tower $\omega, \omega^\omega, \omega^{\omega^\omega}, \ldots$.
Gentzen showed in 1936 that induction up to $\varepsilon_0$ is exactly what is needed to prove the consistency of PA, and in 1943 that PA cannot prove this induction itself.
Ordinal analysis, a part of [[mathematical logic|DYJ0KGTPMR]], turns this into a measure of strength: a theory gets the least ordinal that its proofs of well-foundedness cannot reach.
To name such ordinals one needs ordinal notation systems, which write countable ordinals as finite terms with a computable order, from Cantor normal forms up to the Veblen function and collapsing functions.
Infinitary derivations with the $\omega$-rule give the upper bounds, and well-ordering proofs give the lower bounds.
The results form a scale: $\varepsilon_0$ for PA and $\mathrm{ACA}_0$, $\Gamma_0$ for $\mathrm{ATR}_0$ and predicative analysis, the Bachmann-Howard ordinal for KP and $\mathrm{ID}_1$, and $\psi_0(\Omega_\omega)$ for $\Pi^1_1\text{-}\mathrm{CA}_0$.

## Remarks

### Reading order

1. [[Ordinal analysis|C5E5TG8PGP]] and its [[precise definition|57PTMS2ADY]]: what an analysis measures, and the scale of theories it produces.
2. [[Ordinal notation system|7MBX59Y7N9]] and its [[precise definition|3CNSYYX2HF]]: how to write countable ordinals as finite terms, and why the natural choice of system matters.
3. [[Epsilon nought|KT50SMH3EC]]: the first ordinal that needs a new symbol, with its Cantor normal form notation and fundamental sequences.
4. [[Gentzen's consistency proof|QPV0HNP22S]]: how lowering an ordinal at each reduction of a derivation proves the consistency of PA.
5. [[Transfinite induction in arithmetic|ZE54ABPMJ0]]: the jump that lets PA climb the tower below $\varepsilon_0$, and why it stops there.
6. [[Proof-theoretic ordinal|C72RBH0CDR]] and its [[precise definition|C19Z3B6V4P]]: the ordinal of a theory, with the table of standard theories.
7. [[ω-rule and infinitary derivations|XAMKAB1BZM]]: infinitary proofs, where cut elimination gives the upper bound $\varepsilon_0$ directly.
8. [[Veblen function|JQFAE9S2F4]] and its [[definition|6QFEVWKE25]]: functions that list fixed points, the tool for notations past $\varepsilon_0$.
9. [[Feferman-Schütte ordinal|CNN7BK5YAW]]: $\Gamma_0$, the limit of predicative analysis and the ordinal of $\mathrm{ATR}_0$.
10. [[Small and large Veblen ordinals|ZHDM657G3D]]: how far the Veblen function reaches with more arguments.
11. [[Bachmann-Howard ordinal|QH3ENXFRSV]]: the first ordinal of an impredicative theory, the ordinal of KP and $\mathrm{ID}_1$.
12. [[Ordinal collapsing function|8S6CT4TMB7]]: how an uncountable ordinal helps to name large countable ones.
13. [[Buchholz's psi functions|E7WEFRMQTB]]: the collapsing functions $\psi_\nu$ for $\nu \le \omega$, the standard notation for strong theories.
14. [[Rathjen's psi function|M7D1HEJQVH]]: collapsing from large cardinals, for theories beyond $\Pi^1_1$ comprehension.
15. [[Takeuti-Feferman-Buchholz ordinal|NZWRK062WQ]]: the ordinal $\psi_0(\varepsilon_{\Omega_\omega + 1})$ of $\Pi^1_1$ comprehension with bar induction.
16. [[Theories of iterated inductive definitions|5VNT564Y2W]] and their [[definition|45GQ3KQVT3]]: the theories $\mathrm{ID}_\nu$, which link inductive definitions to collapsing functions.
17. [[Ordinal analysis of Π¹₁ comprehension|2MGJJTSRFD]]: Takeuti's analysis of a strong impredicative subsystem of analysis.
18. [[Takeuti's conjecture|W560YMCPA3]]: cut elimination for simple type theory, first proved by semantic means.
19. [[Local predicativity and Buchholz's Ω-rule|5C4YBXQV15]]: two methods that extend cut elimination to impredicative theories.

### Prerequisites

- [[Structural proof theory|R10RMQCJQX]]: sequent calculus and cut elimination, the machinery of the upper bounds.
- [[Formal arithmetic and its fragments|QHCRN4JVG0]]: Peano arithmetic and its fragments, the first theories to analyze.
- [[Well-orders, transfinite induction and ordinals|QZ033VCGVF]]: well-orders and transfinite induction, the principle that is measured.
- [[Ordinal arithmetic and normal functions|Z092EDNW9B]]: sums, powers, Cantor normal form and fixed points, the raw material of notations.
