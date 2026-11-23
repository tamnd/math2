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
We claim $\lvert \mathrm{PA} \rvert = \varepsilon_0$ for the $\Pi^1_1$ ordinal, and we check the three results of an [[ordinal analysis|57PTMS2ADY]].

1. Notation system.
   Take [[the Cantor normal form notation for epsilon nought|R3BJR7TM2Z]].
   Its comparison is primitive recursive, and its order type is $\varepsilon_0$.
2. Lower bound.
   By the first part of [[transfinite induction in arithmetic|ZE54ABPMJ0]], PA proves induction below each notation $a$, for every formula.
   This includes formulas with a new predicate symbol $X$, because the proof never looks inside the formula.
3. Upper bound, embedding.
   Embed PA into the infinitary system with the [[ω-rule|XAMKAB1BZM]].
   A PA proof becomes an infinitary derivation of height below $\omega \cdot 2$ whose cuts have finite rank.
4. Upper bound, cut elimination.
   Each step that lowers the cut rank by one raises the height $\beta$ to at most $\omega^\beta$, so after finitely many steps the height is below a finite tower of $\omega$'s, which is below $\varepsilon_0$.
5. Upper bound, boundedness.
   A cut-free derivation of $\operatorname{TI}(\lhd, X)$ of height $\beta$ bounds the order type of $\lhd$ by an ordinal computed from $\beta$ that stays below $\varepsilon_0$.
   The exact constants in steps 3 to 5 differ between books.
6. So the supremum of the provable order types is $\varepsilon_0$, and $\lvert \mathrm{PA} \rvert = \varepsilon_0$.

The analysis then yields three further results.
First, $\mathrm{PRA}$ with quantifier-free induction up to $\varepsilon_0$ proves $\operatorname{Con}(\mathrm{PA})$, by [[Gentzen's consistency proof|QPV0HNP22S]].
Second, PA does not prove induction along the whole system, and [[Goodstein's theorem|XQMNJF241J]] is true but unprovable in PA.
Third, the functions that PA proves total are those computable in time bounded by some $f_\beta$ of the fast-growing hierarchy with $\beta < \varepsilon_0$.

## Remarks

This is the model case of every ordinal analysis, and later analyses follow its outline.
Change the theory and the ordinal moves.
If induction is restricted to $\Sigma_1$ formulas, giving $\mathrm{I}\Sigma_1$, the ordinal drops to $\omega^\omega$, and the provably total functions become the primitive recursive ones.
If set variables and arithmetical comprehension are added, giving $\mathrm{ACA}_0$, the ordinal stays $\varepsilon_0$; see [[the ordinal analysis of ACA0|GXZZW7G54P]].

## Explanations

### L1 human

Peano arithmetic is the usual list of axioms for $0, 1, 2, \ldots$ with addition and multiplication.
Its ordinal is $\varepsilon_0$, the limit of $\omega$, $\omega^\omega$, $\omega^{\omega^\omega}$ and so on.
PA can prove induction along every list of ordinal names that stops before $\varepsilon_0$, and no further.
From this one ordinal we get a consistency proof, a true statement that PA cannot prove, and the functions that PA can prove to be defined everywhere.

### L2 human

How does the ordinal limit the functions that PA proves total?
Define $f_0(n) = n + 1$, let $f_{\beta+1}(n)$ be the $n$-fold iterate $f_\beta^{\,n}(n)$, and let $f_\lambda(n) = f_{\lambda[n]}(n)$ at limits, with the standard fundamental sequences below $\varepsilon_0$.
The first levels are:

$$f_1(n) = 2n, \qquad f_2(n) = 2^n n, \qquad f_\omega(n) = f_n(n).$$

Check: $f_2(3) = f_1(f_1(f_1(3))) = 24 = 2^3 \cdot 3$.
The function $f_\omega$ grows like the Ackermann function.
PA proves each $f_\beta$ with $\beta < \varepsilon_0$ total, by transfinite induction up to $\beta$.
The function $f_{\varepsilon_0}$ eventually grows faster than each of them, and PA does not prove it total.
This is the typical use: to show that a fast-growing combinatorial function is not provably total in PA.
Watch out: the values of the hierarchy depend on the fundamental sequences, but the class of functions that it bounds does not.
