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

An ordinal analysis of a formal theory $T$ is the determination of its [[proof-theoretic ordinal|C72RBH0CDR]] $\abs{T}$, in the [[precise sense|57PTMS2ADY]] of three results.
First, a natural [[ordinal notation system|~f8083877]] $(A, \prec)$ for an ordinal $\alpha$.
Second, a lower bound: $T$ proves [[transfinite induction|0ZHQMQ2C1N]] along each proper initial segment of $\prec$.
Third, an upper bound: every primitive recursive well-order that $T$ proves well-founded has order type below $\alpha$.
Then $\abs{T} = \alpha$.
Ordinal analysis is a part of [[proof theory|N4EDJNMTEF]].
One analysis gives at once a consistency proof, an independence result and a description of the provably total functions of $T$.

## Motivation

[[Gödel's incompleteness theorems|X9WYNYE29C]] show that a consistent theory such as [[Peano arithmetic|0QFT7Z76N5]] does not prove its own consistency.
So the finitary consistency proofs of [[Hilbert's program|P1RW6JWX73]] cannot exist in their first form.
Gentzen found what is needed in addition for PA: transfinite induction along a primitive recursive order of type $\varepsilon_0$, and nothing less.
This turns the vague question "how strong is $T$?" into a precise one: "how long a well-order can $T$ prove well-founded?"
The answer is an ordinal, and ordinals can be compared.

## Notation

The ordinal is written $\abs{T}$, $\abs{T}_{\Pi^1_1}$ or $\operatorname{ord}(T)$.
Variants of the definition give the $\Pi^0_2$ ordinal $\abs{T}_{\Pi^0_2}$ and other ordinals; see [[proof-theoretic ordinal|C72RBH0CDR]].
Names of the ordinals depend on the notation system.
For example, the ordinal of $\Pi^1_1\text{-}\mathrm{CA}_0$ is $\psi_0(\Omega_\omega)$ in the notation of [[Buchholz's psi functions|E7WEFRMQTB]], and other collapsing functions name it differently.

## Remarks

### Examples

- [[The ordinal analysis of Peano arithmetic|~633a5219]]: $\abs{\mathrm{PA}} = \varepsilon_0$, by Gentzen.
- [[The ordinal analysis of ACA0|~90da434a]]: $\abs{\mathrm{ACA}_0} = \varepsilon_0$, by conservativity over PA.
- Primitive recursive arithmetic and $\mathrm{I}\Sigma_1$ have the ordinal $\omega^\omega$.
- $\mathrm{ATR}_0$, the theory of arithmetical transfinite recursion of [[reverse mathematics|7SQS69T17R]], has the [[Feferman-Schütte ordinal|~5f65c1fc]] $\Gamma_0$.
- The theory $\mathrm{ID}_1$ of one inductive definition and Kripke-Platek set theory have the [[Bachmann-Howard ordinal|~fcf34cb0]].
- $\Pi^1_1\text{-}\mathrm{CA}_0$ has the ordinal $\psi_0(\Omega_\omega)$ of Buchholz's notation; see [[ordinal analysis of Π¹₁ comprehension|~9776e851]].

### Non-examples

- [[The consistency proof of PA in ZF|~346165b4]]: a proof of consistency in a much stronger theory gives no ordinal and no lower or upper bound.
- Gödel's [[Dialectica interpretation|HZ17ES9PDY]] reduces the consistency of PA to a theory of functionals of finite type. It is a proof interpretation, not an ordinal analysis, although the two can be compared.
- A proof that one order of type $\alpha$ is well-founded in $T$ gives only a lower bound. Without the upper bound, it is not an analysis.

### Basic properties

An analysis of $T$ with ordinal $\alpha$ usually gives the following, for a natural notation system.

- Consistency: PRA together with quantifier-free transfinite induction along $\prec$ proves the [[consistency|VM8TQ70CVJ]] of $T$, as in [[Gentzen's consistency proof|QPV0HNP22S]] for PA.
- Independence: $T$ does not prove transfinite induction along all of $\prec$. Combinatorial statements that encode this induction are true and unprovable in $T$, such as [[Goodstein's theorem|XQMNJF241J]] for PA.
- Provably total functions: the analysis describes the functions that $T$ proves total with a fast-growing hierarchy $(f_\beta)$. For PA they are the functions computable in time bounded by some $f_\beta$ with $\beta < \varepsilon_0$. For weak theories the $\Pi^0_2$ ordinal can be smaller: $\abs{\mathrm{PRA}} = \omega^\omega$, but PRA proves total only the primitive recursive functions, the levels $f_n$ with $n < \omega$.
- Conservativity: theories with the same analysis often prove the same arithmetical statements of low complexity. For example, [[ACA0 is conservative over PA|HPA6HX3114]], and both have the ordinal $\varepsilon_0$.

### History

Gerhard Gentzen gave the first ordinal analysis, of PA, in his consistency proofs of 1936 and 1938, and in his work of 1943 on transfinite induction.
Kurt Schütte introduced infinitary derivations with the [[ω-rule|~e0034cfd]] in 1951, which simplified the method.
Solomon Feferman and Kurt Schütte independently identified $\Gamma_0$ as the ordinal of predicative analysis in 1964 and 1965.
Gaisi Takeuti's consistency proof for $\Pi^1_1$ comprehension (1967) began the analysis of impredicative theories.

### Common errors

- Treating $\abs{T}$ as a property of $T$ alone. The upper bound and the meaning of the lower bound depend on the notation system. An artificial system can make PA fail to prove well-foundedness of an order of type $\omega$.
- Thinking that an ordinal analysis proves the consistency of $T$ by finitary means. It reduces consistency to transfinite induction along $\prec$, which $T$ itself does not prove.
- Thinking that all strong theories are analysed. Full second-order arithmetic and ZF have no ordinal analysis today.

## Explanations

### L1 human

Theories of arithmetic and of sets differ in strength, and ordinal analysis gives a ruler to measure them.
The marks on the ruler are countable ordinals, written in a finite notation system.
To place a theory, one shows that it proves induction up to every mark below some ordinal, and that it cannot reach that ordinal.
For Peano arithmetic the answer is $\varepsilon_0$.
Stronger theories, such as parts of second-order arithmetic, get much larger ordinals.

### L2 human

We read off what the analysis $\abs{\mathrm{ACA}_0} = \varepsilon_0$ gives, from known results.

1. Notation: the [[Cantor normal form notation for ε0|~abf54fbe]].
2. Lower bound: ACA0 proves well-foundedness of each initial segment below $\varepsilon_0$, by the jump of [[transfinite induction in arithmetic|~e065bc19]] with a set parameter.
3. Upper bound: ACA0 is conservative over PA with a free set variable, so it proves no more transfinite induction than PA.
4. Consequences: ACA0 does not prove Goodstein's theorem, and its provably total functions are those of PA.

The typical use is to compare theories: equal ordinals for natural notations suggest equal strength for arithmetical consequences of low complexity.
The trap: equal ordinals do not mean equal theories; ACA0 and PA have the same ordinal, but ACA0 has set variables and PA does not.

### L3 human

Ordinal analysis has a lower half and an upper half.
The lower half is a well-ordering proof inside $T$, built from jumps such as Gentzen's, or from accessible parts in second-order systems.
The upper half embeds $T$ into an infinitary system and bounds the ordinal heights by cut elimination.
The system uses the [[ω-rule|~e0034cfd]] for predicative theories, and [[collapsing functions|~766739ea]] or the Ω-rule for impredicative ones.
The scale of ordinals reached so far runs from $\varepsilon_0$ through $\Gamma_0$ and the [[Bachmann-Howard ordinal|~fcf34cb0]] to the ordinals of theories with reflection and of $\Pi^1_2$ comprehension.
At the top, the countable notation systems use names of large cardinals.
