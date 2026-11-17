---
tag: ~531abfcc
kind: concept
name: Predicative mathematics
aliases: [predicative-mathematics-logic, predicativism-in-analysis]
msc: ["03F35", "03B30", "03A05", "03F15"]
topics: [BY8AAFN7C5]
audience: research
uses: [PTA0GDJWZQ, AWWS4VDNQX, ~08f6623a, ~ff80e550, ~0d0109c9, C72RBH0CDR, JQFAE9S2F4]
sources:
  - url: https://en.wikipedia.org/wiki/Impredicativity
    locator: lead section and History
  - url: https://en.wikipedia.org/wiki/Hermann_Weyl
    locator: Logic
  - url: https://en.wikipedia.org/wiki/Feferman%E2%80%93Sch%C3%BCtte_ordinal
    locator: lead section and Properties
  - url: https://en.wikipedia.org/wiki/Solomon_Feferman
    locator: Contributions
---

## Summary

*Predicative mathematics* is mathematics that defines no object by a quantification over a totality that contains the object being defined.
The natural numbers are taken as given, and every further set must be built in stages from sets already built.
Reverse mathematics gives this old idea a precise measure.
Much of classical analysis can be developed in [[ACA0|~08f6623a]], which is predicative.
The limit of predicativity, in the analysis of Feferman and Schütte, is the ordinal $\Gamma_0$, which is also the strength of [[ATR0|~ff80e550]].
[[Π¹₁-CA0|~0d0109c9]] is impredicative.

## Motivation

Around 1900 the paradoxes of set theory raised the question of which definitions are legitimate.
Henri Poincaré suggested the vicious circle principle: a definition must not refer to a totality to which the defined object belongs.
Bertrand Russell introduced the terms "predicative" and "impredicative", and his ramified type theory obeys the principle; the [[predicative functions of Principia|AWWS4VDNQX]] come from this setting.
The least upper bound of a bounded set of reals is a standard impredicative definition.
It is defined by a quantification over all reals, and the least upper bound is itself one of them.
A predicativist accepts the natural numbers as a completed totality but not the power set of the natural numbers.
The question is then how much of mathematics survives, and the subsystems of second-order arithmetic answer it theorem by theorem.

## Notation

A definition of a set $X \subseteq \N$ by a formula $\theta(n)$ is *predicative* relative to a stock of sets when $\theta$ quantifies only over numbers and over sets of the stock.
The arithmetical formulas, which quantify only over numbers, give the first stage.
Iterating the step along well-orders gives the ramified analytic hierarchy, and an *autonomous* progression accepts only those well-orders that have been shown to be well-orders at an earlier stage.
$\Gamma_0$ is the least ordinal $\alpha$ with $\varphi_\alpha(0) = \alpha$, where $\varphi$ is the [[Veblen function|JQFAE9S2F4]].
The entry [[finitism and predicativism|PTA0GDJWZQ]] collects the related foundational positions.

## Remarks

### Examples

- Arithmetical comprehension is predicative: the set $\set{n : \theta(n)}$ for an arithmetical $\theta$ refers only to numbers and to sets already given. This is the axiom of $\mathsf{ACA}_0$.
- Hermann Weyl, in *Das Kontinuum* (1918), showed that the classical analysis of pointwise continuous functions can be carried out predicatively. Feferman showed that Weyl's development can be formalized in $\mathsf{ACA}_0$.
- The sequential form of completeness is predicative: every bounded sequence of reals has a least upper bound, and every bounded sequence has a convergent subsequence by the [[Bolzano-Weierstrass theorem|0KDJD249DT]]. Both are provable in $\mathsf{ACA}_0$.
- Transfinite iteration of the jump along a given well-order is predicative in the sense of Feferman and Schütte, as long as the well-order has been accepted at an earlier stage. $\mathsf{ATR}_0$ uses this principle without the autonomy condition.

### Non-examples

- The [[completeness axiom|0AXWET80YW]] for arbitrary sets of reals is impredicative. Weyl did not keep it, and he used its form for sequences.
- $\Pi^1_1$ comprehension forms a set by quantifying over all sets of numbers, including the set being defined. Theorems equivalent to $\Pi^1_1\text{-}\mathsf{CA}_0$ over $\mathsf{RCA}_0$, such as the Cantor-Bendixson theorem that every closed set of reals is the union of a [[perfect set|628242KN0T]] and a countable set, are impredicative in this sense.
- [[Kruskal's tree theorem|XVHKCX4F5Y]] is not provable in $\mathsf{ATR}_0$, by a theorem of Harvey Friedman. Its proof-theoretic strength lies beyond $\Gamma_0$, so it is not predicatively provable in the sense of Feferman and Schütte.

### Basic properties

1. $\mathsf{ACA}_0$ proves the same arithmetical sentences as [[Peano arithmetic|HACXBCM7SS]], as the [[conservation example|HPA6HX3114]] shows. So the predicative analysis of $\mathsf{ACA}_0$ costs nothing beyond the arithmetic of the natural numbers.
2. The [[proof-theoretic ordinal|C72RBH0CDR]] of $\mathsf{ACA}_0$ is $\varepsilon_0$, the same as for Peano arithmetic.
3. Feferman (1964) and Schütte (1965) independently identified $\Gamma_0$ as the limit of autonomous [[progressions|F7Z4BV2KHD]] of ramified systems. An ordinal is often called predicative when it is less than $\Gamma_0$.
4. $\Gamma_0$ is the proof-theoretic ordinal of arithmetical transfinite recursion. So $\mathsf{ATR}_0$, although it is not itself predicative in the autonomous sense, has exactly the strength of predicative mathematics in this analysis.
5. The theories at the level of $\Pi^1_1\text{-}\mathsf{CA}_0$ have proof-theoretic ordinals far beyond $\Gamma_0$, so they are not predicatively justified in this analysis.

### History

The terms and the vicious circle principle come from Russell and Poincaré in the first decade of the twentieth century.
Weyl's *Das Kontinuum* of 1918 was the first sustained development of analysis on a predicative basis, and it is now regarded as a founding text of modern predicative mathematics.
Solomon Feferman, influenced by Weyl, made predicativity precise through proof theory, introduced the Feferman-Schütte ordinal as a measure of the strength of predicative systems, and was a proponent of predicativism.
Feferman held that the mathematics needed for the sciences can be developed predicatively; this is his view, and it is not a theorem.
Reverse mathematics in the sense of Friedman and Simpson made the comparison concrete: the theorems provable in $\mathsf{ACA}_0$ and $\mathsf{ATR}_0$ mark what predicative methods reach.

### Common errors

- Calling $\Gamma_0$ "the first impredicative ordinal" without qualification. The identification depends on the analysis of Feferman and Schütte, and it is disputed: Nik Weaver argued in "Predicativity beyond $\Gamma_0$" (2005) that predicative reasoning reaches further.
- Treating predicative and constructive as the same. Predicativism accepts classical logic and the completed set of natural numbers; it restricts the sets that may be formed, not the logic.
- Confusing this notion with Russell's predicative functions. The [[older notion|AWWS4VDNQX]] concerns the orders of propositional functions in Principia Mathematica, not the provability of theorems.
- Reading "$\mathsf{ATR}_0$ is predicative" as a statement about its axioms. Its axiom accepts every well-order, and only its proof-theoretic strength matches the predicative limit.

## Explanations

### L1 human

Some definitions describe an object by comparing it with all objects of its kind, including itself.
"The smallest number in a set" is harmless, because the numbers are given in advance.
"The least upper bound of a set of reals" compares against all reals, and the reals are built from sets that are not given in advance.
Predicative mathematics forbids definitions of this circular kind and builds every set from the natural numbers in stages.
A surprising amount of analysis survives: continuous functions, limits of sequences, and most of calculus.

### L2 human

Here is how a predicative proof replaces an impredicative one.

1. The impredicative statement: a bounded set $S$ of reals has a least upper bound.
2. The predicative replacement: a bounded sequence $(x_k)$ of reals has a least upper bound.
3. For the sequence, the upper bound is described by the arithmetical condition "for every rational $p$, $p < \sup_k x_k$ if and only if some $k$ has $p < x_k$".
4. This condition quantifies only over numbers, so arithmetical comprehension gives the set of rationals below the supremum, and $\mathsf{ACA}_0$ proves the statement.

The typical use: one checks that a classical theorem has a proof that uses only arithmetical comprehension, and calls it predicative.
The trap: a theorem may be predicatively provable even if its textbook proof is impredicative; the right test is the weakest system that proves it, which is what reverse mathematics measures.

### L3 human

The reverse-mathematics picture of predicativity has three levels.
$\mathsf{ACA}_0$ is predicative in the strictest sense and conservative over Peano arithmetic.
$\mathsf{ATR}_0$ reaches the Feferman-Schütte limit $\Gamma_0$ and proves the comparability of well-orders and the perfect set theorem for closed sets.
$\Pi^1_1\text{-}\mathsf{CA}_0$ lies beyond, and theorems such as Cantor-Bendixson, or Kruskal's theorem beyond $\mathsf{ATR}_0$, show where predicative methods stop.
Predicative mathematics is a foundational position as well as a mathematical one, and the essay on [[Hilbert's program|~f3242591]] treats the related finitist position and its partial realization.
