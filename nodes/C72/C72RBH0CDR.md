---
tag: C72RBH0CDR
kind: concept
name: Proof-theoretic ordinal
msc: ["03F15", "03F30"]
topics: [XTTKZTYDSD]
audience: grad
specializes: [0YSCSX5YZC]
uses: [0YSCSX5YZC, 0QFT7Z76N5, 0ZHQMQ2C1N, KT50SMH3EC, C19Z3B6V4P, 6GD30FGYDZ, 01CGSJ0GNQ, QQQRJA90EP]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Table of ordinal analyses
---

## Summary

Let $T$ be a recursively axiomatized theory that interprets enough arithmetic, and add to its language a new unary predicate $X$.
For a [[primitive recursive|QQQRJA90EP]] linear order $\prec$ on $\N$, let $\operatorname{TI}(\prec, X)$ say: if $X$ is progressive along $\prec$, then $X$ holds of every number.
The *proof-theoretic ordinal* $\abs{T}$ is the supremum of the order types of those primitive recursive [[well-orders|01CGSJ0GNQ]] $\prec$ for which $T$ proves $\operatorname{TI}(\prec, X)$.
The precise definition is in [[the definition node|C19Z3B6V4P]].
The ordinal measures how much [[transfinite induction|0ZHQMQ2C1N]] a theory can prove, and it puts theories of very different kinds on one scale.

## Motivation

Gödel's second incompleteness theorem shows that a consistent theory such as PA cannot prove its own consistency.
Gentzen found what is missing: transfinite induction up to $\varepsilon_0$, which PA proves for each smaller ordinal but not for $\varepsilon_0$ itself.
This suggests attaching to each theory the first ordinal that it cannot reach, and this ordinal is the proof-theoretic ordinal.
Computing it is the aim of an [[ordinal analysis|57PTMS2ADY]].

## Notation

The usual notation is $\abs{T}$, and some books write $\abs{T}_{\Pi^1_1}$ to separate it from other ordinals of $T$.
The $\Pi^0_2$ ordinal $\abs{T}_{\Pi^0_2}$ is defined by the provably total functions instead of transfinite induction.
For PA and many stronger theories the two agree, but for weak theories they can differ.

## Remarks

### Examples

- $\abs{\mathrm{PA}} = \varepsilon_0$, by [[the ordinal analysis of PA|7ANX5PDRDM]].
- $\abs{\mathrm{ACA}_0} = \varepsilon_0$, because $\mathrm{ACA}_0$ is conservative over PA, by [[the ordinal analysis of ACA0|GXZZW7G54P]].
- $\abs{\mathrm{I\Sigma}_1} = \abs{\mathrm{PRA}} = \omega^\omega$, by [[the example of IΣ1|8KPSC3GE1B]].
- $\abs{\mathrm{ACA}} = \varepsilon_{\varepsilon_0}$, by [[the example of ACA|JHYZ2A3VPJ]].
- $\abs{\mathrm{ATR}_0} = \Gamma_0$, the [[Feferman-Schütte ordinal|CNN7BK5YAW]], and $\abs{\mathrm{ATR}} = \Gamma_{\varepsilon_0}$.
- $\abs{\mathrm{ID}_1} = \abs{\mathrm{KP}}$ is the [[Bachmann-Howard ordinal|QH3ENXFRSV]].

### Non-examples

- The least uncountable ordinal $\omega_1$ is not $\abs{T}$ for any theory $T$: every order in the supremum is a well-order on $\N$, so it has countable order type.
- Without soundness the definition breaks: [[PA plus the negation of Con(PA)|FWY2SE83Q4]] proves transfinite induction along an order that is not well-founded.
- The order type of one particular order that $T$ proves well-founded is only a lower bound. By [[the artificial notation system|PXMATF6B16]], PA can fail to prove that an order of type $\omega$ is well-founded.

### Basic properties

- If $T$ is $\Pi^1_1$-sound, then $\abs{T} < \omega_1^{\mathrm{CK}}$, the least ordinal that is not the order type of a computable well-order. The argument is in [[the definition node|C19Z3B6V4P]].
- If $T \subseteq T'$, then $\abs{T} \le \abs{T'}$.
- The values for the standard theories form a strictly increasing table: $\omega^\omega$ (PRA), $\varepsilon_0$ (PA, $\mathrm{ACA}_0$), $\varepsilon_{\varepsilon_0}$ (ACA), $\Gamma_0$ ($\mathrm{ATR}_0$), $\Gamma_{\varepsilon_0}$ (ATR), the Bachmann-Howard ordinal ($\mathrm{ID}_1$, KP).

### History

Gentzen computed the first such ordinal, $\varepsilon_0$ for PA, in his work of 1936 and 1943.
Schütte and Feferman found $\Gamma_0$ as the bound of predicative mathematics in the 1960s.
Heinz Bachmann introduced the notation behind the Bachmann-Howard ordinal in 1950, and William Howard used it for the theory $\mathrm{ID}_1$ of inductive definitions in the early 1970s.

### Common errors

- Reading $\abs{T}$ as the order type of one fixed notation system. The supremum is over all primitive recursive well-orders, and a single order of small type can already be out of reach.
- Forgetting the soundness hypothesis. An unsound theory can prove an ill-founded order to be well-founded.
- Confusing $\abs{T}$ with the $\Pi^0_2$ ordinal for weak theories, where the two may differ.

## Explanations

### L1 human

Some orderings of the natural numbers are well-orderings: every decreasing sequence in them stops.
A theory can prove this for some such orderings and not for others.
The longest orderings that the theory still trusts give an ordinal, its proof-theoretic ordinal.
A stronger theory trusts longer orderings, so it gets a larger ordinal.
For example, Peano arithmetic trusts each ordering shorter than $\varepsilon_0$, but not the ordering of length $\varepsilon_0$ itself.

### L2 human

We read off a lower bound for $\abs{\mathrm{PA}}$ from one proof.

1. Let $\prec$ be the order on the [[Cantor normal forms|6GD30FGYDZ]] below $\omega^\omega$, which compares polynomials $\omega^k c_k + \cdots + c_0$ by their leading terms.
2. This order is primitive recursive, and its order type is $\omega^\omega$.
3. [[Transfinite induction in arithmetic|ZE54ABPMJ0]] shows that PA proves $\operatorname{TI}(\prec, X)$.
4. So $\omega^\omega \le \abs{\mathrm{PA}}$.

Repeating this with the towers $\omega^{\omega^\omega}$, $\omega^{\omega^{\omega^\omega}}$, and so on gives $\varepsilon_0 \le \abs{\mathrm{PA}}$.
The typical use is to place a new theory on the scale by proving a lower bound like this and an upper bound by cut elimination.
The trap: a lower bound needs one order of the given type that $T$ proves well-founded, not every such order.

### L3 human

The proof-theoretic ordinal measures the $\Pi^1_1$ part of a theory: the sentences of the form "$\prec$ is well-founded" that $T$ proves.
Other measures look at other parts: the $\Pi^0_2$ ordinal at the provably total functions, and the $\Pi^1_2$ ordinals at stronger consequences.
Beyond the [[Bachmann-Howard ordinal|QH3ENXFRSV]], the analyses use [[collapsing functions|8S6CT4TMB7]] and reach theories such as [[Π¹₁-comprehension|2MGJJTSRFD]].
The analysis of full second-order arithmetic is open.
