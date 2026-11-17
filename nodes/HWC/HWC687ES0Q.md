---
tag: HWC687ES0Q
kind: concept
name: Decidable theory
aliases: [effectively-decidable-theory, decidable-first-order-theory, decidability-of-a-theory]
msc: ["03B25"]
topics: [E4AVTNWE9E]
audience: ug2
uses: [92SWXST1ZM, DKFGQTRYZE, PPGD5KW8JC, TN9G24VABN, MFJXPAF0R0, 655K8Y7VS8, 1HK0VYWTV7]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section E
    note: adopted
    mention: wikipedia://en/76765067#BWB6
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Decidability_(logic)
    locator: lead section
  - url: https://builds.openlogicproject.org/
    locator: Undecidability
  - book: isbn:9780521701464
inventory: [Q7991TCMXC]
---

## Summary

Let $L$ be a signature whose symbols are coded by natural numbers, so that a [[Gödel numbering|MFJXPAF0R0]] makes the set of $L$-[[sentences|DKFGQTRYZE]] a [[computable set|PPGD5KW8JC]] of codes.
A [[theory|92SWXST1ZM]] $T$ in $L$, taken closed under [[logical consequence|1HK0VYWTV7]], is decidable when the set of codes of the sentences in $T$ is computable.
Equivalently, there is an algorithm that takes any $L$-sentence $\sigma$, always stops, and answers "yes" exactly when $T \models \sigma$.
A structure $\mathcal{M}$ is called decidable when its complete theory $\operatorname{Th}(\mathcal{M})$ is decidable.
Decidability is the precise form of the question whether a branch of mathematics can be settled by calculation.

## Motivation

Many classical results give an algorithm for a whole family of questions.
Euclid's algorithm decides divisibility questions, and Sturm's theorem counts the real roots of a polynomial.
Logic asks for more: an algorithm that settles every first-order statement about a given structure or a given axiom system.
For the real field such an algorithm exists, by Tarski's work; for the natural numbers with addition and multiplication it does not.
To state such results, one needs a precise notion of a theory whose theorems can be computed.
The [[Entscheidungsproblem|DJNYM72Z4G]] is the case of the empty theory: decide which sentences are valid.

## Notation

For a set $\Gamma$ of $L$-sentences, $\operatorname{Cn}(\Gamma) = \set{\sigma : \Gamma \models \sigma}$ is the set of its consequences, and $\Gamma$ axiomatizes the theory $\operatorname{Cn}(\Gamma)$.
For an $L$-structure $\mathcal{M}$, $\operatorname{Th}(\mathcal{M})$ is the set of $L$-sentences true in $\mathcal{M}$.
The following notions sit next to decidability.

- $T$ is computably enumerable, or [[semi-decidable|KYTG12Z059]], when the set of its sentences is [[computably enumerable|TN9G24VABN]].
- $T$ is axiomatizable, or recursively axiomatizable, when $T = \operatorname{Cn}(A)$ for a computable set $A$ of sentences.
- $T$ is finitely axiomatizable when $T = \operatorname{Cn}(A)$ for a finite set $A$.

Older books say "recursive" for computable and "recursively enumerable" for computably enumerable.
Some books call a theory "solvable" when it is decidable.

## Remarks

### Examples

1. The theory of infinite sets in the empty signature is decidable; see [[the theory of infinite sets is decidable|1886MXD8S5]]. Its axioms say that there are at least $n$ elements, for each $n$, and the theory is complete.
2. The theory of dense linear orders without endpoints is decidable; see [[the decidability of dense linear orders|NF13NBMSVJ]]. It is finitely axiomatized and complete.
3. [[Presburger arithmetic|4W0E9G7PPV]], the theory of $(\N, 0, 1, +)$, is decidable, by quantifier elimination.
4. The theory of the ordered field of real numbers is decidable, by the [[Tarski-Seidenberg theorem|3W5JGDZAN0]] and the axioms of [[real closed fields|DDY3Q3PJ6W]].
5. The theory of a finite structure in a finite signature is decidable. To evaluate a sentence, one checks each quantifier over the finitely many elements.

### Non-examples

1. The set of valid sentences of a signature with a binary relation symbol is not decidable, by [[Church's theorem|VA6BNNY2YC]]. The condition that fails is computability of the theory $\operatorname{Cn}(\emptyset)$.
2. [[Robinson arithmetic is finitely axiomatizable but undecidable|C0ZBS445B4]]. So a finite list of axioms does not give decidability.
3. True arithmetic $\operatorname{Th}(\N, 0, S, +, \cdot)$ is complete but not decidable, by the [[essential undecidability|9JDDFN8PT7]] of [[Robinson arithmetic|3K1AKGXF8A]]. So completeness alone does not give decidability.

### Basic properties

1. A decidable theory is computably enumerable: list all sentences and keep those that the decision algorithm accepts.
2. An axiomatizable theory is computably enumerable: list all formal proofs from the axioms and output their last lines. This uses [[Gödel's completeness theorem|WQ1ZE255SF]], which turns $\models$ into provability.
3. A computably enumerable theory is axiomatizable, by Craig's trick: if $\sigma_0, \sigma_1, \ldots$ lists $T$, the computable set of sentences $\sigma_n \wedge \cdots \wedge \sigma_n$ ($n + 1$ copies) axiomatizes $T$.
4. [[A complete axiomatizable theory is decidable|HZ7A7B2ERA]]. This is the main source of decidable theories.
5. If $T$ is decidable and $\varphi$ is a sentence, then $\operatorname{Cn}(T \cup \set{\varphi})$ is decidable, since $T \cup \set{\varphi} \models \sigma$ holds if and only if $T \models \varphi \to \sigma$.
6. If $T = \operatorname{Cn}(\set{\alpha_1, \ldots, \alpha_n})$ is finitely axiomatizable, then $T \models \sigma$ holds if and only if $\alpha_1 \wedge \cdots \wedge \alpha_n \to \sigma$ is valid. So an undecidable finitely axiomatizable theory gives an undecidable set of valid sentences.

### History

Presburger proved in 1929 that the theory of the natural numbers with addition is decidable.
After Church and Turing made the notion of algorithm precise in 1936, decidability of theories became a mathematical question.
Tarski found a decision method for elementary algebra and geometry, written in a 1948 report and published in 1951.
Tarski, Mostowski and Robinson developed the general methods for undecidable theories in their 1953 book Undecidable Theories.

### Common errors

- Confusing the two uses of "decide". A theory $T$ decides a sentence $\sigma$ when $T \models \sigma$ or $T \models \neg \sigma$; this is about completeness. A theory is decidable when an algorithm computes its members; this is about computability.
- Thinking that a computable structure has a decidable theory. The structure $(\N, +, \cdot)$ has computable operations, but its theory is undecidable.
- Thinking that finitely many axioms make a theory decidable. Group theory and Robinson arithmetic are finitely axiomatized and undecidable.

## Explanations

### L1 human

A theory is a collection of statements, for example all true statements about whole numbers and addition.
The theory is decidable when a computer program can take any statement in its language and say, after finite time, whether the statement belongs to the theory.
For whole numbers with addition alone, such a program exists: it can decide, for example, that "every number is even or one more than an even number" is true.
When multiplication is added, no program can do this for all statements.
So decidability separates the parts of mathematics that a machine can settle completely from the parts where it cannot.

### L2 human

We show that the theory $T$ of infinite sets in the empty signature is decidable, with the result on complete theories.

1. $T$ is $\operatorname{Cn}(A)$ for $A = \set{\lambda_2, \lambda_3, \ldots}$, where $\lambda_n$ is $\exists x_1 \cdots \exists x_n \bigwedge_{i < j} x_i \neq x_j$. The map $n \mapsto \lambda_n$ is computable, so $A$ is a computable set.
2. $T$ is complete; see the example page for the proof with the [[Łoś-Vaught test|ZR7Y5C235P]].
3. By the theorem on [[complete axiomatizable theories|HZ7A7B2ERA]], $T$ is decidable.
4. The algorithm is concrete: for a sentence $\sigma$, list the proofs from $A$ until a proof of $\sigma$ or of $\neg \sigma$ appears.

The typical use is in this order: find an axiomatization, prove completeness by a model-theoretic method, and conclude decidability.
A trap is to skip the axiomatization: completeness of $\operatorname{Th}(\mathcal{M})$ is automatic, but without a computable set of axioms there is no algorithm.

### L3 human

Decidable theories are the bottom of a hierarchy: a theory is $\Delta^0_1$, an axiomatizable theory is $\Sigma^0_1$, and $\operatorname{Th}(\N, +, \cdot)$ is not arithmetical at all, by Tarski's undefinability theorem.
The positive results come from model theory: quantifier elimination, as for Presburger arithmetic and real closed fields, or completeness by categoricity, or interpretation in a decidable structure such as the monadic second-order theory of the binary tree.
The negative results come from [[essential undecidability|9JDDFN8PT7]] and interpretations: once a theory interprets enough arithmetic, every consistent extension is undecidable.
Decidability also has a complexity side: Presburger arithmetic needs doubly exponential time in the worst case, and the weak monadic second-order theory of one successor is not elementary recursive.
