---
tag: 43BSXNWQBG
kind: concept
name: Predicative mathematics
aliases: [predicative-mathematics-logic, predicativism-in-analysis]
msc: ["03F35", "03B30", "03A05", "03F15"]
topics: [BY8AAFN7C5]
audience: research
uses: [PTA0GDJWZQ, AWWS4VDNQX, NAASTN80QN, MKB74TX3Z8, T21WETAHN5, C72RBH0CDR, JQFAE9S2F4]
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

Most of classical analysis survives if you refuse every definition that quantifies over a totality containing the object being defined.
*Predicative mathematics* is mathematics under that restriction.
The natural numbers are taken as given, and every further set must be built in stages from sets already built.
Reverse mathematics gives this old idea a precise measure.
Much of classical analysis can be developed in [[ACA0|NAASTN80QN]], which is predicative.
The limit of predicativity, in the analysis of Feferman and Schütte, is the ordinal $\Gamma_0$, which is also the strength of [[ATR0|MKB74TX3Z8]].
[[Π¹₁-CA0|T21WETAHN5]] is impredicative.

## Motivation

Around 1900 the paradoxes of set theory raised the question of which definitions are legitimate.
Henri Poincaré proposed the vicious circle principle: a definition must not refer to a totality to which the defined object belongs.
Bertrand Russell introduced the terms "predicative" and "impredicative", and his ramified type theory obeys the principle.
The [[predicative functions of Principia|AWWS4VDNQX]] come from this setting.
The least upper bound of a bounded set of reals is a standard impredicative definition.
It is defined by a quantification over all reals, and the least upper bound is itself one of them.
A predicativist accepts the natural numbers as a completed totality but not the power set of the natural numbers.
The question is then how much of mathematics survives, and the subsystems of second-order arithmetic answer it theorem by theorem.

## Notation

A definition of a set $X \subseteq \mathbb{N}$ by a formula $\theta(n)$ is *predicative* relative to a stock of sets when $\theta$ quantifies only over numbers and over sets of the stock.
The arithmetical formulas, which quantify only over numbers, give the first stage.
Iterating the step along well-orders gives the ramified analytic hierarchy.
An *autonomous* progression accepts only those well-orders that have been shown to be well-orders at an earlier stage.
$\Gamma_0$ is the least ordinal $\alpha$ with $\varphi_\alpha(0) = \alpha$, where $\varphi$ is the [[Veblen function|JQFAE9S2F4]].
The entry [[finitism and predicativism|PTA0GDJWZQ]] collects the related foundational positions.

## Remarks

### Predicative theorems

Arithmetical comprehension is predicative: the set $\{n : \theta(n)\}$ for an arithmetical $\theta$ refers only to numbers and to sets already given, and this is the axiom of $\mathsf{ACA}_0$.
The sequential form of completeness is predicative.
Every bounded sequence of reals has a least upper bound, and every bounded sequence has a convergent subsequence by the [[Bolzano-Weierstrass theorem|0KDJD249DT]], and $\mathsf{ACA}_0$ proves both.
Transfinite iteration of the jump along a well-order is predicative in the sense of Feferman and Schütte, as long as the well-order was accepted at an earlier stage.
$\mathsf{ATR}_0$ uses this principle without the autonomy condition.

### Impredicative theorems

The [[completeness axiom|0AXWET80YW]] for arbitrary sets of reals is impredicative, and Weyl replaced it by its form for sequences.
$\Pi^1_1$ comprehension forms a set by quantifying over all sets of numbers, including the set being defined.
Theorems equivalent to $\Pi^1_1\text{-}\mathsf{CA}_0$ over $\mathsf{RCA}_0$ are impredicative in this sense.
An example is the Cantor-Bendixson theorem: every closed set of reals is the union of a [[perfect set|628242KN0T]] and a countable set.
[[Kruskal's tree theorem|XVHKCX4F5Y]] is not provable in $\mathsf{ATR}_0$, by a theorem of Harvey Friedman, so it is not predicatively provable in the sense of Feferman and Schütte.

### Ordinals and strength

$\mathsf{ACA}_0$ proves the same arithmetical sentences as [[Peano arithmetic|HACXBCM7SS]], as the [[conservation example|HPA6HX3114]] shows.
So the predicative analysis of $\mathsf{ACA}_0$ costs nothing beyond the arithmetic of the natural numbers.
The [[proof-theoretic ordinal|C72RBH0CDR]] of $\mathsf{ACA}_0$ is $\varepsilon_0$, the same as for Peano arithmetic.
Feferman and Schütte identified $\Gamma_0$ as the limit of autonomous [[progressions|F7Z4BV2KHD]] of ramified systems.
An ordinal is often called predicative when it is less than $\Gamma_0$.
$\Gamma_0$ is the proof-theoretic ordinal of $\mathsf{ATR}_0$.
So $\mathsf{ATR}_0$, although its axiom is not predicative in the autonomous sense, has exactly the strength of predicative mathematics in this analysis.
$\Pi^1_1\text{-}\mathsf{CA}_0$ has proof-theoretic ordinal $\psi(\Omega_\omega)$, far beyond $\Gamma_0$, so it is not predicatively justified in this analysis.

### Watch out

Do not call $\Gamma_0$ "the first impredicative ordinal" without qualification.
The identification depends on the analysis of Feferman and Schütte, and Nik Weaver argued in "Predicativity beyond $\Gamma_0$" (2005) that predicative reasoning reaches further.
Do not treat predicative and constructive as the same.
Predicativism accepts classical logic and the completed set of natural numbers, and it restricts the sets that may be formed, not the logic.
Do not read "$\mathsf{ATR}_0$ is predicative" as a statement about its axioms.
Its axiom accepts every well-order, and only its proof-theoretic strength matches the predicative limit.

### History

The vicious circle principle and the terms "predicative" and "impredicative" come from Poincaré and Russell in the first decade of the twentieth century.
Hermann Weyl, in *Das Kontinuum* (1918), developed the analysis of continuous functions on a predicative basis.
Feferman later showed that Weyl's development fits in a system that is conservative over Peano arithmetic.
Feferman (1964) and Schütte (1965) independently identified $\Gamma_0$ as the limit of predicative provability.
Feferman held that the mathematics needed for the sciences can be developed predicatively; this is his view, and it is not a theorem.
$\mathsf{ATR}_0$ is $\Pi^1_1$-conservative over Feferman's predicative system $\mathsf{IR}$, and Simpson calls the resulting program predicative reductionism.

### Try it

Is the set $\{n : \text{program } n \text{ halts on input } n\}$ predicatively defined?
Answer: yes, the definition "some stage $s$ has program $n$ halted on input $n$ by stage $s$" quantifies only over numbers, so it is arithmetical, and $\mathsf{ACA}_0$ proves that the set exists.

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
3. For the sequence, a rational $p$ lies below the supremum if and only if some $k$ has $p < x_k$.
4. This condition quantifies only over numbers, so arithmetical comprehension gives the set of rationals below the supremum, and $\mathsf{ACA}_0$ proves the statement.

Check with $x_k = 1 - 2^{-k}$: a rational $p$ satisfies $p < x_k$ for some $k$ exactly when $p < 1$, so the supremum is $1$.
The typical use: one checks that a classical theorem has a proof that uses only arithmetical comprehension, and calls it predicative.
The trap: a theorem may be predicatively provable even if its textbook proof is impredicative.
The right test is the weakest system that proves it, which is what reverse mathematics measures.

### L3 human

The reverse-mathematics picture of predicativity has three levels.
$\mathsf{ACA}_0$ is predicative in the strictest sense and conservative over Peano arithmetic.
$\mathsf{ATR}_0$ reaches the Feferman-Schütte limit $\Gamma_0$ and proves the comparability of well-orders and the perfect set theorem for closed sets.
$\Pi^1_1\text{-}\mathsf{CA}_0$ lies beyond, and theorems such as Cantor-Bendixson, or Kruskal's theorem beyond $\mathsf{ATR}_0$, show where predicative methods stop.
Predicative mathematics is a foundational position as well as a mathematical one.
The concept of [[partial realizations of Hilbert's program|Z26S516BKH]] treats the related finitist position.
