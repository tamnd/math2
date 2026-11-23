---
tag: TNZ995J8AP
kind: concept
name: Conservation theorems
msc: ["03F25", "03F30", "03F35"]
topics: [8XY7JYZKFW]
audience: grad
uses: [N238J43XNE, 0QFT7Z76N5, RXHJPVMPJH, DC60FYCSPM, 7SQS69T17R, AYRZ98Y0NW, P1RW6JWX73, QSCE4HJEZ7]
sources:
  - url: https://en.wikipedia.org/wiki/Conservative_extension
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Heyting_arithmetic
    locator: Conservativity
  - url: https://en.wikipedia.org/wiki/Second-order_arithmetic
    locator: lead section
---

## Summary

A conservation theorem says that a strong theory, for all its extra power, proves no new statements of some chosen simple kind.
It lets us use infinite objects or classical logic in a proof and still keep the conclusion in a weak, safe or computational theory.

The model case is WKL0, the subsystem of [[second-order arithmetic|DC60FYCSPM]] with weak König's lemma, which proves the Heine-Borel theorem for $[0, 1]$ and many other compactness results.
Harvey Friedman showed that [[WKL0 is Pi-0-2-conservative over primitive recursive arithmetic|V609D9SZ05]]: every sentence $\forall x\, \exists y\, \varphi(x, y)$ with $\varphi$ primitive recursive that WKL0 proves is already a theorem of PRA.
Leo Harrington showed that [[WKL0 is Pi-1-1-conservative over RCA0|8G2GVRXWG5]].

In general, let $T \subseteq T'$ be theories and $\Gamma$ a class of sentences in the language of $T$.
Then $T'$ is $\Gamma$-[[conservative|N238J43XNE]] over $T$ if
$$\sigma \in \Gamma \text{ and } T' \vdash \sigma \quad \text{imply} \quad T \vdash \sigma.$$

## Motivation

Strong theories make proofs shorter and more natural, with sets of numbers, classical logic, choice and compactness.
A conservation theorem shows that these tools change nothing about a chosen class of statements.
For [[Hilbert's program|P1RW6JWX73]], the hope was that ideal mathematics is conservative over finitary mathematics for simple statements such as $\Pi^0_1$ sentences.
Gödel's second incompleteness theorem rules out the full program, but the WKL0 result realizes a part of it: compactness arguments in analysis can be eliminated from proofs of $\Pi^0_2$ sentences.

The $\Pi^0_2$ class has a computational meaning.
A $\Pi^0_2$ sentence $\forall x\, \exists y\, \varphi(x, y)$ says that the search for $y$ ends.
So if $T'$ is $\Pi^0_2$-conservative over $T$, then every search that $T'$ proves to end, $T$ proves to end as well, and $T'$ proves no new computable functions total.
In [[reverse mathematics|7SQS69T17R]], conservation results measure how much arithmetic a system really adds.

## Notation

We write "$T'$ is $\Gamma$-conservative over $T$" for the condition in the Summary.
The classes $\Pi^0_n$ and $\Sigma^0_n$ contain the arithmetic formulas with $n$ alternating blocks of number quantifiers in front of a bounded formula, starting with $\forall$ or $\exists$.
A $\Pi^1_1$ formula has the form $\forall X\, \psi$ with $\psi$ arithmetic, possibly with set parameters.
PRA is primitive recursive arithmetic, $\mathrm{I}\Sigma_1$ is arithmetic with induction for $\Sigma^0_1$ formulas, and WKL0 is RCA0 plus weak König's lemma.
Some books write "$T'$ is conservative over $T$" with no class, and then they mean all sentences of the language of $T$.

## Remarks

### The standard examples

[[ACA0 is conservative over PA|HPA6HX3114]] for all arithmetic sentences, so arithmetic comprehension adds nothing to first-order Peano arithmetic.
[[PA is Pi-0-2-conservative over HA|PY679V9MVR]], by the double-negation translation followed by Friedman's A-translation.
[[PA is conservative over HA for negative formulas|DC1X1S0DJE]], by the double-negation translation alone.
[[Parsons's theorem|2VYJXZZDGB]] says that $\mathrm{I}\Sigma_1$ is $\Pi^0_2$-conservative over PRA, so the provably total functions of $\mathrm{I}\Sigma_1$ are the primitive recursive functions.
Together with Friedman's result, this places WKL0, $\mathrm{I}\Sigma_1$ and PRA at the same $\Pi^0_2$ level.
At the most basic level, [[extensions by definitions are conservative|QSCE4HJEZ7]] for all sentences of the old language.

### What is not conservative

[[PA plus the consistency of PA|EQH7XTZ29V]] is not conservative over PA, even for $\Pi^0_1$ sentences, since it proves $\mathrm{Con}(\mathsf{PA})$.
[[PA is not Pi-0-3-conservative over HA|HVHEKG9FA5]]: a $\Pi^0_3$ form of the excluded middle for halting separates them.
$\mathrm{I}\Sigma_2$ is not $\Pi^0_2$-conservative over PRA.
It proves that the Ackermann function is total, and that function is not primitive recursive, as the [[failed Herbrand analysis|88FJKEX4SH]] explains.

### Three ways to prove one

The model method expands models.
If every model of $T$ expands to a model of $T'$ with the same first-order part, then $T'$ is conservative over $T$ for sentences of the language of $T$, by the completeness theorem.
For ACA0 over PA, add to a model of PA all its sets definable with parameters.
For WKL0 over RCA0, Harrington's forcing argument adds sets to a countable model of RCA0 without changing its numbers.

The proof-theoretic method uses [[cut elimination|AYRZ98Y0NW]].
A proof of a simple conclusion is reduced to a proof in which every formula is simple, and that proof is then read in $T$; Parsons's theorem goes this way.
The interpretation method sends proofs in $T'$ to proofs in $T$ and fixes the formulas of $\Gamma$ up to provable equivalence; the A-translation and the Dialectica interpretation go this way.

### The rules you can use

Conservation composes.
If $T'$ is $\Gamma$-conservative over $T$ and $T$ is $\Gamma'$-conservative over $T''$, then $T'$ is $(\Gamma \cap \Gamma')$-conservative over $T''$, since a sentence in both classes passes down twice.
Conservation for $\Pi^0_1$ sentences preserves consistency: $0 = 1$ is a $\Pi^0_1$ sentence, so if $T$ is consistent, so is $T'$.
For a class $\Gamma$ closed under negation, $\Gamma$-conservativity also means that $T'$ refutes no new sentences of $\Gamma$.

### Conservation is not interpretability

The two ideas are easy to confuse, because both compare a strong theory with a weak one.
Conservation is about theorems: $T'$ proves no new sentences of a class.
[[Interpretability|8H03GRMDYG]] is about translations: the weak theory can define a copy of the strong one, so $T'$ is consistent if $T$ is.

The two come apart.
By [[an interpretation|H34RWH89JJ]], PA interprets $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$, but that theory proves the $\Sigma^0_1$ sentence $\neg \mathrm{Con}(\mathsf{PA})$, which PA does not prove.
So interpretability gives equiconsistency, and it does not give conservation for $\Sigma^0_1$ sentences.

### Watch out

The class matters.
PA is $\Pi^0_2$-conservative over HA, but not $\Pi^0_3$-conservative, so always state which class you mean.

Watch out for the WKL0 results as well, because two different base theories appear in them.
WKL0 is $\Pi^1_1$-conservative over RCA0 and $\Pi^0_2$-conservative over PRA.
It is not $\Pi^1_1$-conservative over PRA, which has no set variables at all.

A conservation theorem also says nothing about the length of proofs.
The step from $T'$ to $T$ can make proofs much longer, and often it does.

### History

The 1933 translation of Gödel and Gentzen gave a conservation result between classical and intuitionistic arithmetic for negative formulas.
Charles Parsons proved the conservativity of $\mathrm{I}\Sigma_1$ over PRA in 1970.
Friedman proved the $\Pi^0_2$-conservativity of WKL0 over PRA in the 1970s, and Harrington proved the $\Pi^1_1$ result by forcing.
Friedman's A-translation of 1978, found independently by Dragalin, gave a short proof of the $\Pi^0_2$-conservativity of PA over HA.

### Try it

First, is $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$ conservative over PA for $\Sigma^0_1$ sentences?
Yes, if PA is sound: a true $\Sigma^0_1$ sentence is provable in PA, and $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$ is sound, so it proves only true $\Sigma^0_1$ sentences.

Second, ACA0 is conservative over PA for arithmetic sentences, and PA is $\Pi^0_2$-conservative over HA.
What does composition give?
It gives that ACA0 is $\Pi^0_2$-conservative over HA, for the arithmetic $\Pi^0_2$ sentences.

## Explanations

### L1 human

A conservation theorem says that a strong method proves no new facts of a certain simple kind.
For example, a theory that reasons with infinite sets of numbers may prove no new facts of the form "this search always ends" beyond those that a simple theory of whole numbers proves.
So the strong method is safe to use for those facts.
It can still make the proofs much shorter and clearer.

### L2 human

We prove a conservation theorem by the model method, in general form.
Assume that every model $M$ of $T$ expands to a model $M'$ of $T'$, with the same elements and the old symbols unchanged.
Let $\sigma$ be a sentence of the old language with $T' \vdash \sigma$.
For any model $M$ of $T$, the expansion $M'$ satisfies $\sigma$, and $\sigma$ uses only old symbols, so $M$ satisfies $\sigma$.
So every model of $T$ satisfies $\sigma$, and the completeness theorem gives $T \vdash \sigma$.

The typical use is ACA0 over PA, where $M'$ adds the definable sets of $M$.
Watch out at the expansion step: the new sets must satisfy the comprehension axioms of $T'$.
Definable sets satisfy arithmetic comprehension, but they do not satisfy $\Pi^1_1$ comprehension, so the same trick fails for stronger systems.

### L3 human

Conservation theorems compare theories by their consequences in a fixed class, and so they measure strength relative to that class.
The $\Pi^0_2$ consequences of a theory determine its provably total functions, computed through [[proof-theoretic ordinals|C72RBH0CDR]] or by functional interpretations.
If $T'$ is $\Pi^1_1$-conservative over $T$, then the two theories prove the well-foundedness of the same recursive orderings, so they have the same proof-theoretic ordinal.
Partial conservation results are a main tool of reverse mathematics, and their proofs combine forcing, model theory and proof theory.
