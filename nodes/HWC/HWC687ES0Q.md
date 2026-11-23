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

A theory is decidable when a computer program can tell, for every sentence, whether the sentence is a theorem of the theory.
Take the theory of dense linear orders without endpoints.
It proves $\forall x \, \exists y \, (x < y)$, and it does not prove $\exists x \, \forall y \, (x \le y)$, and a program can settle every question of this kind.
For the natural numbers with addition and multiplication, no program can.

In exact terms, let $L$ be a signature whose symbols are coded by natural numbers, so that a [[Gödel numbering|MFJXPAF0R0]] makes the set of $L$-[[sentences|DKFGQTRYZE]] a [[computable set|PPGD5KW8JC]] of codes.
A [[theory|92SWXST1ZM]] $T$ in $L$, taken closed under [[logical consequence|1HK0VYWTV7]], is decidable when the set of codes of the sentences in $T$ is computable.
Equivalently, there is an algorithm that takes any $L$-sentence $\sigma$, always stops, and answers "yes" exactly when $T \models \sigma$.
A structure $\mathcal{M}$ is called decidable when its complete theory $\operatorname{Th}(\mathcal{M})$ is decidable.

## Motivation

Many classical results give an algorithm for a whole family of questions.
Euclid's algorithm decides divisibility, and Sturm's theorem counts the real roots of a polynomial.
Logic asks for more: one algorithm that settles every first-order statement about a given structure or a given system of axioms.
For the ordered field of real numbers such an algorithm exists, by Tarski's work, and for the natural numbers with addition and multiplication it does not.
To state results like these, we need an exact notion of a theory whose theorems can be computed.

The [[Entscheidungsproblem|DJNYM72Z4G]] is the case of the empty theory, where the question is which sentences are valid.
Later pages build on the notion in two directions.
Decision methods such as quantifier elimination give decidable theories, for example [[Presburger arithmetic|4W0E9G7PPV]].
[[Essential undecidability|9JDDFN8PT7]] and interpretation give undecidable ones.

## Notation

For a set $\Gamma$ of $L$-sentences, $\operatorname{Cn}(\Gamma) = \{ \sigma : \Gamma \models \sigma \}$ is the set of its consequences, and we say that $\Gamma$ axiomatizes the theory $\operatorname{Cn}(\Gamma)$.
For an $L$-structure $\mathcal{M}$, $\operatorname{Th}(\mathcal{M})$ is the set of $L$-sentences true in $\mathcal{M}$.

Three notions sit next to decidability.
A theory $T$ is computably enumerable, or [[semi-decidable|KYTG12Z059]], when the set of its sentences is [[computably enumerable|TN9G24VABN]].
It is axiomatizable, or recursively axiomatizable, when $T = \operatorname{Cn}(A)$ for a computable set $A$ of sentences.
It is finitely axiomatizable when $T = \operatorname{Cn}(A)$ for a finite set $A$.
Older books say "recursive" for computable and "recursively enumerable" for computably enumerable, and some books call a decidable theory "solvable".

## Remarks

### A first decision

Let $\mathcal{M}$ be the structure with domain $\{0, 1, 2\}$ and the usual order $<$.
To decide whether $\forall x \, \exists y \, (x < y)$ is true in $\mathcal{M}$, try each value of $x$:
$$x = 0 \colon y = 1 \text{ works}, \qquad x = 1 \colon y = 2 \text{ works}, \qquad x = 2 \colon \text{no } y \text{ works}.$$
So the sentence is false in $\mathcal{M}$.
The same loop over the three elements evaluates every sentence, one quantifier at a time.
So the theory of every finite structure in a finite signature is decidable.

### Decidable theories you will meet

The theory of infinite sets in the empty signature is decidable, as [[the theory of infinite sets is decidable|1886MXD8S5]] shows.
Its axioms say that there are at least $n$ elements, for each $n$, and the theory is complete.
The theory of dense linear orders without endpoints is decidable, as [[the decidability of dense linear orders|NF13NBMSVJ]] shows.
It is finitely axiomatized and complete.
[[Presburger arithmetic|4W0E9G7PPV]], the theory of $(\mathbb{N}, 0, 1, +)$, is decidable by quantifier elimination.
The theory of the ordered field of real numbers is decidable by the [[Tarski-Seidenberg theorem|3W5JGDZAN0]] and the axioms of [[real closed fields|DDY3Q3PJ6W]].

### Theories that are not decidable

The set of valid sentences of a signature with a binary relation symbol is not decidable, by [[Church's theorem|VA6BNNY2YC]].
Here the theory $\operatorname{Cn}(\emptyset)$ fails to be computable.
[[Robinson arithmetic is finitely axiomatizable but undecidable|C0ZBS445B4]], so a finite list of axioms does not give decidability.
True arithmetic $\operatorname{Th}(\mathbb{N}, 0, S, +, \cdot)$ is complete but not decidable, by the essential undecidability of [[Robinson arithmetic|3K1AKGXF8A]].
So completeness alone does not give decidability either.

### How the notions fit together

A decidable theory is computably enumerable: list all sentences, and keep those that the decision algorithm accepts.
An axiomatizable theory is computably enumerable too: list all formal proofs from the axioms, and output their last lines.
That step uses [[Gödel's completeness theorem|WQ1ZE255SF]], which turns $\models$ into provability.

Conversely, a computably enumerable theory is axiomatizable, by Craig's trick.
If $\sigma_0, \sigma_1, \ldots$ lists $T$, then the sentences $\sigma_n \wedge \cdots \wedge \sigma_n$, with $n + 1$ copies of $\sigma_n$, form a computable set of axioms for $T$.
The set is computable because the number of copies tells you which $n$ to check.

The bridge to decidability is completeness.
[[A complete axiomatizable theory is decidable|HZ7A7B2ERA]], and this is the main source of decidable theories.

### Two rules for finite extensions

If $T$ is decidable and $\varphi$ is a sentence, then $\operatorname{Cn}(T \cup \{ \varphi \})$ is decidable.
The reason is that $T \cup \{ \varphi \} \models \sigma$ holds if and only if $T \models \varphi \to \sigma$.

If $T = \operatorname{Cn}(\{ \alpha_1, \ldots, \alpha_n \})$, then $T \models \sigma$ holds if and only if $\alpha_1 \wedge \cdots \wedge \alpha_n \to \sigma$ is valid.
So an undecidable finitely axiomatizable theory, such as Robinson arithmetic, gives an undecidable set of valid sentences.
This is one route to Church's theorem.

### Watch out

The word "decide" has two uses.
A theory $T$ decides a sentence $\sigma$ when $T \models \sigma$ or $T \models \neg \sigma$, and that is about completeness.
A theory is decidable when an algorithm computes its members, and that is about computability.
For example, the theory of groups fails on both counts.
It decides neither $\forall x \, \forall y \, (xy = yx)$ nor its negation, so it is incomplete, and no algorithm computes it, so it is undecidable.

A computable structure need not have a decidable theory.
The operations of $(\mathbb{N}, +, \cdot)$ are computable, but its theory is undecidable.
Also, finitely many axioms do not make a theory decidable: group theory and Robinson arithmetic are finitely axiomatized and undecidable.

### History

Presburger proved in 1929 that the theory of the natural numbers with addition is decidable.
After Church and Turing made the notion of algorithm exact in 1936, decidability of theories became a mathematical question.
Tarski found a decision method for elementary algebra and geometry, written in a 1948 report and published in 1951.
Tarski, Mostowski and Robinson developed the general methods for undecidable theories in their 1953 book Undecidable Theories.

### Try it

Is the theory of the two-element group $(\{0, 1\}, +)$ decidable?
Yes: it is the theory of a finite structure, so you evaluate each sentence by looping over the two elements.

Let $T$ be axiomatizable, and let $T \cup \{ \neg \sigma \}$ be inconsistent.
Does the proof search from the axioms of $T$ ever confirm $\sigma$?
Yes: then $T \models \sigma$, so a proof of $\sigma$ from the axioms exists, and the search reaches it.

## Explanations

### L1 human

A theory is a collection of statements, for example all true statements about whole numbers and addition.
The theory is decidable when a computer program can take any statement in its language and say, after finite time, whether the statement belongs to the theory.
For whole numbers with addition alone such a program exists.
It can decide, for example, that "every number is even or one more than an even number" is true.
When multiplication is added, no program can do this for all statements.
So decidability separates the parts of mathematics that a machine can settle completely from the parts where it cannot.

### L2 human

We show that the theory $T$ of infinite sets in the empty signature is decidable, with the result on complete theories.
Let $\lambda_n$ be the sentence $\exists x_1 \cdots \exists x_n \bigwedge_{i < j} x_i \neq x_j$, which says that there are at least $n$ elements.
Then $T = \operatorname{Cn}(A)$ for $A = \{ \lambda_2, \lambda_3, \ldots \}$.
The map $n \mapsto \lambda_n$ is computable, so $A$ is a computable set.

Next, $T$ is complete, by the [[Łoś-Vaught test|ZR7Y5C235P]], which the example of infinite sets works through.
By the theorem on [[complete axiomatizable theories|HZ7A7B2ERA]], $T$ is decidable.
The algorithm is concrete: for a sentence $\sigma$, list the proofs from $A$ until a proof of $\sigma$ or of $\neg \sigma$ appears.

The typical use goes in this order: find an axiomatization, prove completeness by a method of model theory, and conclude decidability.
Watch out: completeness of $\operatorname{Th}(\mathcal{M})$ is automatic, but without a computable set of axioms there is no algorithm.

### L3 human

Decidable theories are the bottom of a hierarchy.
A decidable theory is $\Delta^0_1$, an axiomatizable theory is $\Sigma^0_1$, and $\operatorname{Th}(\mathbb{N}, +, \cdot)$ is not arithmetical at all, by Tarski's undefinability theorem.
The positive results come from model theory: quantifier elimination, as for Presburger arithmetic and real closed fields, completeness by categoricity, or interpretation in a decidable structure such as the monadic second-order theory of the binary tree, as in [[Rabin's tree theorem|PXKKP038RG]].
The negative results come from essential undecidability and interpretations: once a theory interprets enough arithmetic, every consistent extension is undecidable.

Decidability also has a side of complexity.
By Fischer and Rabin (1974), every decision procedure for Presburger arithmetic needs at least doubly exponential time on some inputs.
The weak monadic second-order theory of one successor is decidable but not elementary recursive.
