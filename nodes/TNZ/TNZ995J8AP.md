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

A conservation theorem says that a stronger theory $T'$ is [[conservative|N238J43XNE]] over a weaker theory $T$ for a class $\Gamma$ of sentences: every sentence in $\Gamma$ that $T'$ proves, $T$ already proves.
The usual classes are the $\Pi^0_1$ and $\Pi^0_2$ sentences of arithmetic, all arithmetic sentences, and the $\Pi^1_1$ sentences of second-order arithmetic.
Standard examples are ACA0 over Peano arithmetic for arithmetic sentences, PA over Heyting arithmetic for $\Pi^0_2$ sentences, and $\mathrm{I}\Sigma_1$ over primitive recursive arithmetic for $\Pi^0_2$ sentences.
They are proved by expanding models, by cut elimination, or by proof interpretations.
The idea matters because a conservation theorem lets a mathematician use strong principles while keeping the finitary or constructive content of the conclusion.

## Motivation

Strong theories make proofs shorter and more natural: sets of numbers, classical logic, choice, compactness.
A conservation theorem shows that these tools do not change what can be proved about a chosen class of statements.
For [[Hilbert's program|P1RW6JWX73]], the goal was conservativity of ideal mathematics over finitary mathematics for simple statements, such as $\Pi^0_1$ sentences.
The $\Pi^0_2$ case has a computational meaning: a $\Pi^0_2$ sentence $\forall x\, \exists y\, \varphi(x, y)$ states that a computable function is total.
So $\Pi^0_2$-conservativity of $T'$ over $T$ means that $T'$ and $T$ have the same provably total computable functions.
In [[reverse mathematics|7SQS69T17R]], conservation theorems measure the strength of a system by the arithmetic it proves.

## Notation

For a class $\Gamma$, "$T'$ is $\Gamma$-conservative over $T$" means: if $\sigma \in \Gamma$ and $T' \vdash \sigma$, then $T \vdash \sigma$.
$\Pi^0_n$ and $\Sigma^0_n$ are the classes of arithmetic formulas with $n$ alternating blocks of unbounded number quantifiers, starting with $\forall$ or $\exists$.
$\Pi^1_1$ formulas have the form $\forall X\, \psi$ with $\psi$ arithmetic, possibly with set parameters.
PRA is primitive recursive arithmetic, $\mathrm{I}\Sigma_1$ is arithmetic with induction for $\Sigma^0_1$ formulas, and WKL0 is RCA0 with weak König's lemma.

## Remarks

### Examples

- [[ACA0 is conservative over PA|HPA6HX3114]] for arithmetic sentences, by expanding each model of PA with its definable sets.
- [[PA is conservative over HA for Pi-0-2 sentences|PY679V9MVR]], by the double-negation translation and the A-translation.
- [[PA is conservative over HA for negative formulas|DC1X1S0DJE]], by the double-negation translation alone.
- [[Parsons's theorem|2VYJXZZDGB]]: $\mathrm{I}\Sigma_1$ is $\Pi^0_2$-conservative over PRA.
- WKL0 is $\Pi^1_1$-conservative over RCA0 (Harrington), and $\Pi^0_2$-conservative over PRA (Friedman).
- [[Extensions by definitions are conservative|QSCE4HJEZ7]], for all sentences of the old language.

### Non-examples

- [[PA plus the consistency of PA|EQH7XTZ29V]] is not conservative over PA, even for $\Pi^0_1$ sentences: it proves $\mathrm{Con}(\mathsf{PA})$.
- [[PA is not conservative over HA for Pi-0-3 sentences|HVHEKG9FA5]]: a $\Pi^0_3$ form of excluded middle for halting separates them.
- $\mathrm{I}\Sigma_2$ is not $\Pi^0_2$-conservative over PRA: it proves the totality of the Ackermann function, which is not primitive recursive.

### Basic properties

- If $T'$ is $\Gamma$-conservative over $T$ and $T$ is $\Gamma'$-conservative over $T''$, then $T'$ is $(\Gamma \cap \Gamma')$-conservative over $T''$.
- $\Pi^0_1$-conservativity over a consistent $T$ implies the consistency of $T'$, since $0 = 1$ is a $\Pi^0_1$ sentence with no quantifiers.
- Model method: if every model of $T$ expands to a model of $T'$, then $T'$ is conservative over $T$ for all sentences of the language of $T$, by the completeness theorem.
- Proof-theoretic method: by [[cut elimination|AYRZ98Y0NW]] or partial cut elimination, a proof of a simple conclusion is transformed into a proof whose formulas are simple, and then into a proof in $T$.
- Interpretation method: a proof interpretation maps proofs in $T'$ to proofs in $T$ and leaves the formulas of $\Gamma$ unchanged up to provable equivalence.

### History

The 1933 translation of Gödel and Gentzen gave a conservation result between classical and intuitionistic arithmetic, for negative formulas.
Friedman's A-translation of 1978 gave a short proof of the $\Pi^0_2$-conservativity of PA over HA.
Parsons proved the conservativity of $\mathrm{I}\Sigma_1$ over PRA in 1970, and the results on WKL0 became central in reverse mathematics.

### Common errors

- To confuse conservativity with equiconsistency. $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ is consistent if PA is, but it proves a $\Sigma^0_1$ sentence that PA does not prove.
- To forget the class $\Gamma$. PA is $\Pi^0_2$-conservative over HA, but not $\Pi^0_3$-conservative.
- To assume that a conservation theorem gives short proofs in $T$. The translation from $T'$ to $T$ can make proofs much longer.

## Explanations

### L1 human

A conservation theorem says that a strong method proves no new facts of a certain simple kind.
For example, reasoning with infinite sets proves no new facts about whole numbers beyond those that reasoning about whole numbers alone proves, for a suitable system of sets.
So the strong method is safe to use for those facts.
It can still make the proofs much shorter and clearer.

### L2 human

We use the model method to show that a theory $T'$ is conservative over $T$.

1. Assume every model $M$ of $T$ expands to a model $M'$ of $T'$, with the same elements and the old symbols unchanged.
2. Let $\sigma$ be a sentence of the old language with $T' \vdash \sigma$.
3. For any model $M$ of $T$, the expansion $M'$ satisfies $\sigma$, and $\sigma$ only uses old symbols, so $M$ satisfies $\sigma$.
4. So every model of $T$ satisfies $\sigma$, and by the completeness theorem $T \vdash \sigma$.

The typical use is the proof that ACA0 is conservative over PA, where $M'$ adds the definable sets of $M$.
A trap is step 1 for second-order theories: the expansion must satisfy the comprehension axioms, which holds for definable sets only for arithmetic comprehension.

### L3 human

Conservation theorems compare theories by their consequences in a fixed class, and so they define the proof-theoretic strength of a theory relative to that class.
The $\Pi^0_2$ consequences of a theory are its provably total functions, and they are computed by ordinal analysis or by functional interpretations.
The $\Pi^1_1$ consequences correspond to the proof-theoretic ordinal.
Partial conservation results are the main tool of reverse mathematics, and their proofs combine forcing, model theory and proof theory.
