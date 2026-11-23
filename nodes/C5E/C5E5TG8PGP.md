---
tag: C5E5TG8PGP
kind: concept
name: Ordinal analysis
msc: ["03F15", "03F05"]
topics: [XTTKZTYDSD]
audience: research
uses: [N4EDJNMTEF, C72RBH0CDR, 0QFT7Z76N5]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Table of ordinal analyses
same_as:
  wikidata: Q7100782
  wikipedia: Ordinal analysis
---

## Summary

Peano arithmetic can prove that every decreasing sequence below $\omega^{\omega^\omega}$ is finite, and the same for any finite tower of $\omega$'s, but not for all ordinals below $\varepsilon_0$.
Ordinal analysis turns this kind of fact into a measure of strength: it assigns to a theory the length of the well-orders that the theory can prove well-founded.

Precisely, an ordinal analysis of a theory $T$ determines its [[proof-theoretic ordinal|C72RBH0CDR]] $\lvert T \rvert$.
We use the $\Pi^1_1$ definition: $\lvert T \rvert$ is the supremum of the order types of the primitive recursive well-orders $\lhd$ for which $T$ proves [[transfinite induction|0ZHQMQ2C1N]] along $\lhd$.
An analysis that shows $\lvert T \rvert = \alpha$ has three parts, made exact in the [[formal definition|57PTMS2ADY]].
It gives a natural [[ordinal notation system|7MBX59Y7N9]] for $\alpha$, a lower bound (a proof in $T$ of induction along each proper initial segment), and an upper bound (no provable well-order reaches $\alpha$).
Ordinal analysis is a part of [[proof theory|N4EDJNMTEF]].

## Motivation

[[Gödel's incompleteness theorems|X9WYNYE29C]] show that a consistent theory such as [[Peano arithmetic|0QFT7Z76N5]] cannot prove its own consistency.
So the finitary consistency proofs that [[Hilbert's program|P1RW6JWX73]] asked for cannot exist in their first form.
Gentzen asked what must be added to finitary reasoning to prove the consistency of PA, and in 1936 he found the answer: induction along a well-order of type $\varepsilon_0$.
In 1943 he showed that this is sharp, because PA itself does not prove that induction.

This changes the vague question "how strong is $T$?" into a precise one: "how long a well-order can $T$ prove well-founded?"
The answer is an ordinal, and ordinals can be compared.
One analysis then gives three more results at once: a consistency proof, a true statement that $T$ cannot prove, and a description of the functions that $T$ proves total.
The rest of the sub-area computes these ordinals, from $\varepsilon_0$ up to the ordinals of strong subsystems of analysis.

## Notation

The ordinal is written $\lvert T \rvert$, $\lvert T \rvert_{\Pi^1_1}$ or $\operatorname{ord}(T)$.
Other definitions give other ordinals, such as the $\Pi^0_2$ ordinal $\lvert T \rvert_{\Pi^0_2}$, so a book must say which one it means; see [[proof-theoretic ordinal|C72RBH0CDR]].
The names of large ordinals depend on the notation system.
For example, the ordinal of $\Pi^1_1\text{-}\mathrm{CA}_0$ is $\psi_0(\Omega_\omega)$ in the notation of [[Buchholz's psi functions|E7WEFRMQTB]], and other collapsing functions give it other names.
When a page of the sub-area writes $\psi$, it names the system it uses.

## Remarks

### A first analysis: Peano arithmetic

The model case is Gentzen's [[analysis of Peano arithmetic|7ANX5PDRDM]], with the answer $\lvert \mathrm{PA} \rvert = \varepsilon_0$.
The notation system is the set of Cantor normal forms below $\varepsilon_0$.
For the lower bound, PA proves induction up to $\omega$, then up to $\omega^\omega$, then up to $\omega^{\omega^\omega}$, and so on, one level of the tower for each use of [[Gentzen's jump|ZE54ABPMJ0]].
For the upper bound, a PA proof becomes an infinitary derivation, and cut elimination brings its height below $\varepsilon_0$.
The two bounds meet at the limit of the tower $\omega, \omega^\omega, \omega^{\omega^\omega}, \ldots$, which is $\varepsilon_0$.

### A scale of theories

The same method gives a table of standard theories.
Primitive recursive arithmetic and $\mathrm{I}\Sigma_1$ have the ordinal $\omega^\omega$.
PA and [[ACA0|GXZZW7G54P]] both have $\varepsilon_0$, because ACA0 proves no new arithmetical facts.
$\mathrm{ATR}_0$ of [[reverse mathematics|7SQS69T17R]] has the [[Feferman-Schütte ordinal|CNN7BK5YAW]] $\Gamma_0$, the ordinal of predicative analysis.
$\mathrm{ID}_1$ and Kripke-Platek set theory have the [[Bachmann-Howard ordinal|QH3ENXFRSV]].
$\Pi^1_1\text{-}\mathrm{CA}_0$ has $\psi_0(\Omega_\omega)$ in Buchholz's notation; see [[ordinal analysis of Π¹₁ comprehension|2MGJJTSRFD]].

### What it is not

A [[consistency proof of PA in ZF|4GRT452DB9]] is correct but is no analysis.
It uses the set of natural numbers as a model, so it gives no ordinal and no bound on what PA proves.
Gödel's [[Dialectica interpretation|HZ17ES9PDY]] reduces the consistency of PA to a theory of functionals of finite type.
It is a proof interpretation, not an ordinal analysis, though the two can be compared.
A proof that $T$ proves one well-order of type $\alpha$ is also not an analysis, because it gives only a lower bound.

### What one analysis gives

Take an analysis with ordinal $\alpha$ and a natural notation system $\prec$.
Gentzen's method gives consistency: primitive recursive arithmetic with quantifier-free induction along $\prec$ proves the [[consistency|VM8TQ70CVJ]] of $T$, as in [[Gentzen's consistency proof|QPV0HNP22S]].
It gives independence: $T$ does not prove induction along all of $\prec$, and combinatorial statements that encode it, such as [[Goodstein's theorem|XQMNJF241J]] for PA, are true and unprovable in $T$.
It describes the provably total functions with a fast-growing hierarchy $(f_\beta)$: for PA they are the functions computable in time bounded by some $f_\beta$ with $\beta < \varepsilon_0$.
It often explains conservativity: [[ACA0 is conservative over PA|HPA6HX3114]] for arithmetical sentences, and both have the ordinal $\varepsilon_0$.

### Watch out

The ordinal is not a property of a theory alone until the definition is fixed.
The $\Pi^1_1$ ordinal of PRA is $\omega^\omega$, but PRA proves total only the primitive recursive functions, which the levels $f_n$ with $n < \omega$ already bound.
So the $\Pi^0_2$ ordinal of PRA, measured by the fast-growing hierarchy, is $\omega$.
Measured by the Hardy hierarchy, where $H_{\omega^n} = f_n$, the same functions give $\omega^\omega$, so even the $\Pi^0_2$ ordinal depends on the scale.

The lower bound also depends on the notation system.
An artificial primitive recursive order of type $\omega$ can hide a statement such as $\operatorname{Con}(\mathrm{PA})$ in its definition, so that PA cannot prove it well-founded.
The supremum in the definition is not affected, since natural notations still reach it.
Finally, an analysis does not make consistency finitary: it reduces consistency to an induction that $T$ itself does not prove.

### History

Gentzen gave the first ordinal analysis, of PA, in his consistency proofs of 1936 and 1938, and in his 1943 paper on the unprovability of transfinite induction up to $\varepsilon_0$.
Schütte introduced infinitary derivations with the [[ω-rule|XAMKAB1BZM]] in 1951, which simplified the method.
Feferman (1964) and Schütte (1965) independently identified $\Gamma_0$ as the ordinal of predicative analysis.
Takeuti's consistency proof for $\Pi^1_1$ comprehension (1967) began the analysis of impredicative theories.
Full second-order arithmetic and ZF have no ordinal analysis today.

### Try it

PA proves induction along every initial segment of the Cantor normal forms below $\varepsilon_0$, and no longer initial segment.
What is $\lvert \mathrm{PA} \rvert$?
The supremum of the provable order types is $\varepsilon_0$, so $\lvert \mathrm{PA} \rvert = \varepsilon_0$, even though PA does not prove induction up to $\varepsilon_0$ itself.

$\mathrm{ACA}_0$ and PA have the same ordinal.
Does that make them the same theory?
No: ACA0 has set variables and proves statements about sets that PA cannot express, but the two prove the same arithmetical sentences.

## Explanations

### L1 human

Theories of arithmetic and of sets differ in strength, and ordinal analysis gives a ruler to measure them.
The marks on the ruler are ordinals, which extend the counting numbers past infinity: $0, 1, 2, \ldots, \omega, \omega + 1, \ldots$.
To place a theory, we show that it can prove "there is no endless way down" for every mark below some point, and that it cannot pass that point.
For Peano arithmetic the point is $\varepsilon_0$, the limit of $\omega$, $\omega^\omega$, $\omega^{\omega^\omega}$ and so on.
Stronger theories get much larger ordinals.

### L2 human

What does the analysis $\lvert \mathrm{ACA}_0 \rvert = \varepsilon_0$ give, and how is it proved?
The notation system is the [[Cantor normal form notation for ε0|R3BJR7TM2Z]].
For the lower bound, ACA0 proves well-foundedness below each notation by the jump of [[transfinite induction in arithmetic|ZE54ABPMJ0]], applied with a set parameter.
For the upper bound, ACA0 is conservative over PA with a free set variable, so it proves no more transfinite induction than PA does.
So ACA0 does not prove Goodstein's theorem, and its provably total functions are those of PA.

This is the typical use: an ordinal analysis places a new theory on the scale of known ones.
Equal ordinals for natural notations suggest equal strength for arithmetical consequences of low complexity, but not equal theories.

### L3 human

Each ordinal analysis has a lower half and an upper half.
The lower half is a well-ordering proof inside $T$, built from jumps such as Gentzen's, or from accessible parts in second-order systems.
The upper half embeds $T$ into an infinitary system and bounds the heights of derivations by cut elimination.
For predicative theories the infinitary system uses the [[ω-rule|XAMKAB1BZM]], and for impredicative ones it adds [[collapsing functions|8S6CT4TMB7]] or Buchholz's $\Omega$-rule.
The ordinals reached so far run from $\varepsilon_0$ through $\Gamma_0$ and the Bachmann-Howard ordinal to the ordinals of set theories with strong reflection principles.
At the top, the countable notation systems are built from names of large cardinals.
