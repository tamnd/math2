---
tag: NAASTN80QN
kind: concept
name: ACA0
msc: ["03B30", "03F35"]
topics: [BY8AAFN7C5]
audience: grad
uses: [DC60FYCSPM, XQENB067R3, 60P2XWY5QX, HACXBCM7SS]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Arithmetical comprehension ACA0
  - url: https://en.wikipedia.org/wiki/Second-order_arithmetic
    locator: Arithmetical comprehension
---

## Summary

$\mathsf{ACA}_0$ is the subsystem of [[second-order arithmetic|DC60FYCSPM]] with the basic axioms, the set induction axiom, and comprehension for all arithmetical formulas, as in its [[definition|K9XG0Z2N9V]].
It is the third of the big five systems of reverse mathematics, and it contains [[RCA0|XQENB067R3]] and $\mathsf{WKL}_0$.
Its $\omega$-models are the Turing ideals closed under the [[Turing jump|60P2XWY5QX]], and it proves exactly the same arithmetic sentences as [[Peano arithmetic|HACXBCM7SS]].

## Motivation

Many theorems of analysis and algebra have computable instances whose solutions compute the halting problem.
For example, a computable bounded increasing sequence of rationals can have a limit that computes $\emptyset'$.
Such theorems need a system that is closed under the jump, and arithmetical comprehension is the natural one: it gives every set defined by number quantifiers.

## Notation

The name abbreviates "arithmetical comprehension axiom", and the subscript $0$ marks the restriction of induction.
$\mathsf{ACA}$ is the version with induction for all formulas; $\mathsf{ACA}_0^+$ adds the existence of the $\omega$-th jump of every set.

## Remarks

### Examples

- The [[arithmetical sets|9KPCZ6NA32]] form the least $\omega$-model of $\mathsf{ACA}_0$.
- The [[existence of Turing jumps|10NR4PGXHW]] is equivalent to $\mathsf{ACA}_0$ over $\mathsf{RCA}_0$.
- The [[Bolzano-Weierstrass theorem|HV153Y95MQ]] and [[König's lemma|3P2J5NWCM1]] are equivalent to $\mathsf{ACA}_0$ over $\mathsf{RCA}_0$.
- $\mathsf{ACA}_0$ [[is conservative over Peano arithmetic|HPA6HX3114]].

### Non-examples

- The [[ω-model of low sets|8B045KSKW5]] satisfies $\mathsf{WKL}_0$, but not $\mathsf{ACA}_0$, since it omits the halting set.
- The [[sets computable from the halting set|7KCGVY6XJM]] satisfy $\mathsf{RCA}_0$, but not $\mathsf{ACA}_0$, since they omit $\emptyset''$.

### Basic properties

- Over $\mathsf{RCA}_0$, $\mathsf{ACA}_0$ is equivalent to $\Sigma^0_1$ comprehension and to the [[existence of ranges of one-to-one functions|3MQ39PRCYJ]].
- $\mathsf{ACA}_0$ proves weak König's lemma, so it contains $\mathsf{WKL}_0$, and the low model shows that the inclusion is strict.
- $\mathsf{ACA}_0$ proves the induction scheme for arithmetical formulas.
- Over $\mathsf{RCA}_0$, $\mathsf{ACA}_0$ is equivalent to each of these: every bounded increasing sequence of reals converges; every Cauchy sequence of reals converges; every countable vector space over $\Q$ has a basis; every countable commutative ring has a maximal ideal; Ramsey's theorem for triples and two colors.
- $\mathsf{ACA}_0$ does not prove $\mathsf{ATR}_0$, since the arithmetical sets do not form a model of $\mathsf{ATR}_0$.

### History

Hermann Weyl's book *Das Kontinuum* (1918) developed analysis with sets defined by number quantifiers, close to $\mathsf{ACA}_0$.
$\mathsf{ACA}_0$ was among the systems of Friedman's reverse mathematics program in the 1970s.

### Common errors

- $\mathsf{ACA}_0$ does not prove the existence of $\emptyset^{(\omega)}$, the sequence of all finite jumps of $\emptyset$ as one set.
- The conservativity over Peano arithmetic is for $\mathsf{ACA}_0$, not for $\mathsf{ACA}$: with full induction the system proves the consistency of Peano arithmetic.
- A proof in $\mathsf{ACA}_0$ may use induction only for arithmetical formulas.

## Explanations

### L1 human

$\mathsf{ACA}_0$ allows a set to exist whenever it can be described using quantifiers over numbers.
This is enough for most of classical analysis on sequences, such as the Bolzano-Weierstrass theorem.
It proves no more facts about numbers than Peano arithmetic does.

### L2 human

To show that a theorem implies $\mathsf{ACA}_0$, one usually builds, from a one-to-one function $f$, an instance of the theorem whose solution computes the range of $f$.
To prove a theorem in $\mathsf{ACA}_0$, one forms the sets of the classical proof, and checks that their definitions use number quantifiers only.
A trap is to iterate the jump along a variable number of steps in one set; this needs more than $\mathsf{ACA}_0$.

### L3 human

The $\omega$-models of $\mathsf{ACA}_0$ are the jump ideals, and the theory of jump ideals connects $\mathsf{ACA}_0$ to degree theory.
$\mathsf{ACA}_0$ has the same proof-theoretic ordinal as Peano arithmetic, namely $\varepsilon_0$.
Systems between $\mathsf{ACA}_0$ and $\mathsf{ATR}_0$, such as $\mathsf{ACA}_0^+$, are also studied.
For example, Hindman's theorem is provable in $\mathsf{ACA}_0^+$ and implies $\mathsf{ACA}_0$ over $\mathsf{RCA}_0$.
