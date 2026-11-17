---
tag: 7ANX5PDRDM
kind: example
name: Ordinal analysis of Peano arithmetic
msc: ["03F15", "03F30"]
topics: [XTTKZTYDSD]
audience: research
instance_of: [C5E5TG8PGP]
uses: [57PTMS2ADY, 0QFT7Z76N5, R3BJR7TM2Z, ZE54ABPMJ0, QPV0HNP22S, XAMKAB1BZM, XQMNJF241J]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Theories with proof-theoretic ordinal ε0
  - url: https://en.wikipedia.org/wiki/Gentzen's_consistency_proof
    locator: Gentzen's theorem
---

## Example

Let PA be first-order [[Peano arithmetic|0QFT7Z76N5]].
We check the three results of an [[ordinal analysis|57PTMS2ADY]] with $\alpha = \varepsilon_0$.

1. Notation system. Take [[the Cantor normal form notation for epsilon nought|R3BJR7TM2Z]]. It is primitive recursive, and its order type is $\varepsilon_0$.
2. Lower bound. By part 1 of [[transfinite induction in arithmetic|ZE54ABPMJ0]], PA proves transfinite induction along the initial segment below each notation $a$, for every formula. This includes formulas with a new predicate symbol $X$, since the proof works for any formula.
3. Upper bound, embedding. Embed PA into the infinitary system with the [[ω-rule|XAMKAB1BZM]]. A PA-proof becomes an infinitary derivation of height below $\omega \cdot 2$ with cuts of finite rank.
4. Upper bound, cut elimination. Eliminating the cuts gives a cut-free derivation of height below $\varepsilon_0$.
5. Upper bound, boundedness. A cut-free derivation of $\operatorname{TI}(\lhd, X)$ of height $\beta < \varepsilon_0$ bounds the order type of $\lhd$ by an ordinal below $\varepsilon_0$. Steps 3 to 5 are cited results, and books differ in the exact bounds.
6. So $\abs{\mathrm{PA}} = \varepsilon_0$.

What the analysis yields:

7. Consistency: $\mathrm{PRA} + \mathrm{QF}\text{-}\mathrm{TI}(\varepsilon_0)$ proves $\operatorname{Con}(\mathrm{PA})$, by [[Gentzen's consistency proof|QPV0HNP22S]].
8. Independence: PA does not prove transfinite induction along the whole system, and [[Goodstein's theorem|XQMNJF241J]] is true but unprovable in PA.
9. Provably total functions: a function has an algorithm that PA proves total exactly when it is computable in time bounded by some $f_\beta$ with $\beta < \varepsilon_0$. This result is cited.

## Remarks

This is the model case of every ordinal analysis.
If the induction schema of PA is restricted to $\Sigma_1$ formulas, the ordinal drops to $\omega^\omega$, and the provably total functions become the primitive recursive ones.
If PA is extended by a set variable and arithmetical comprehension, giving $\mathrm{ACA}_0$, the ordinal stays $\varepsilon_0$; see [[the ordinal analysis of ACA0|GXZZW7G54P]].

## Explanations

### L1 human

Peano arithmetic is the usual set of axioms for $0, 1, 2, \ldots$ with addition and multiplication.
Its ordinal is $\varepsilon_0$: it can prove induction along every list of ordinal names that stops before $\varepsilon_0$, and no further.
From this one ordinal, logicians read off three results.
They get a proof of consistency, a true statement that PA cannot prove, and the functions that PA can prove to be defined everywhere.

### L2 human

We see how the ordinal limits the functions that PA proves total.

1. Define $f_0(n) = n + 1$, $f_{\beta+1}(n) = f_\beta^{\,n}(n)$ ($n$-fold iteration), and $f_\lambda(n) = f_{\lambda[n]}(n)$ for limits, with the fundamental sequences of $\varepsilon_0$.
2. Then $f_1(n) = 2n$, $f_2(n) = 2^n n$, and $f_\omega(n) = f_n(n)$ grows like the Ackermann function.
3. PA proves that each $f_\beta$ with $\beta < \varepsilon_0$ is total, by transfinite induction up to $\beta$.
4. The function $f_{\varepsilon_0}$ grows faster than each of them, and PA does not prove it total.

The typical use is to show that a fast-growing combinatorial function is not provably total in PA.
The trap: the exact values of the hierarchy depend on the fundamental sequences, but the class of functions that it bounds does not.
