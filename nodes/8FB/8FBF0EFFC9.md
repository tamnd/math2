---
tag: 8FBF0EFFC9
kind: concept
name: Semantic conception of truth
aliases: [convention-t, tarskis-theory-of-truth, material-adequacy]
msc: ["03A05", "03B10"]
topics: [6Q4JJ2MMV8]
audience: grad
uses: [D9G8M42GKC, MFJXPAF0R0, DKFGQTRYZE, 71X7TB3F98]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section S
    note: adopted
    mention: wikipedia://en/76765067#JKYY
    sections: [Summary]
  - url: https://plato.stanford.edu/entries/tarski-truth/
    locator: "Tarski's Truth Definitions, 1.2 Formal correctness"
  - url: https://plato.stanford.edu/entries/tarski-truth/
    locator: "Tarski's Truth Definitions, 1.3 Material adequacy"
  - url: https://en.wikipedia.org/wiki/Semantic_theory_of_truth
    locator: Criteria for a definition of truth
inventory: [3F7DX4F79T]
---

## Summary

The *semantic conception of truth* is Tarski's set of conditions for a definition of "true sentence of $L$", where $L$ is a formalized [[object language|D9G8M42GKC]].
The definition is given in a metalanguage $M$ that contains a translation of $L$ and can name the sentences of $L$.
It must be *formally correct*: it has the form $\forall x\,(\mathrm{True}(x) \leftrightarrow \varphi(x))$ with $\mathrm{True}$ not in $\varphi$, or is provably equivalent to this form.
It must be *materially adequate* (Convention T): for each [[sentence|DKFGQTRYZE]] $S$ of $L$, the axioms of $M$ prove $\mathrm{True}(\ulcorner S \urcorner) \leftrightarrow S^{*}$.
Here $S^{*}$ is the translation of $S$ into $M$.
The conception makes truth a mathematical notion, and it is the base of the definition of [[truth in a structure|71X7TB3F98]] in model theory.

## Motivation

Before Tarski, truth was a philosophical notion, and the [[liar paradox|KBYY281V8T]] showed that careless use of "true" leads to contradiction.
Logic needs a precise notion of truth to state soundness and completeness theorems.
Tarski asked two questions.
What is a satisfactory definition of truth for a given language?
For which languages does such a definition exist?
Convention T answers the first question: every instance "$S$ is true if and only if $S$" must follow from the definition.
The answer to the second question is that the definition exists, in a metalanguage that is essentially stronger than the object language.

## Notation

1. $\ulcorner S \urcorner$ is a name of the sentence $S$ in $M$, for example a quotation or the numeral of a [[Gödel number|MFJXPAF0R0]].
2. The instances $\mathrm{True}(\ulcorner S \urcorner) \leftrightarrow S^{*}$ are called T-sentences, T-biconditionals, or instances of the T-schema.
3. Tarski called a formally correct definition *normal*; the SEP entry says that today it is called *explicit*.
4. In arithmetic one often writes $\mathrm{Tr}$ or $T$ in place of $\mathrm{True}$.

## Remarks

### Examples

1. For a propositional language with a fixed valuation, an inductive truth definition satisfies Convention T; see [[this example|PWRQX8JKYQ]].
2. For a finite language with finitely many sentences, a list of the true sentences is a formally correct and materially adequate definition. The SEP entry reports that this was one of Tarski's four examples.
3. In set theory, the set of true sentences of the [[language of arithmetic|D8SD54M5PN]] has an explicit definition that proves every T-sentence; see [[this example|QS0FWVFZWZ]].
4. For each $n$, a [[partial truth predicate|Y2MF1EZAM7]] for $\Sigma_n$ sentences satisfies Convention T restricted to $\Sigma_n$ sentences. It is a formula of arithmetic itself.

### Non-examples

1. [[Provability in PA|KV0MA19KSX]] is formally correct, but it is not materially adequate: by [[Gödel's first incompleteness theorem|X9WYNYE29C]] some true sentence is not provable.
2. Take a formula of arithmetic that is meant to define truth for arithmetic, with $\mathsf{PA}$ as the metalanguage. It can be formally correct, but it is not materially adequate, by [[Tarski's undefinability theorem|YRV6SYK2BY]].
3. A definition that uses an undefined primitive such as "denotes" is not formally correct in Tarski's sense. The formula $\varphi$ may use only syntax, set theory and the notions of $L$.

### Basic properties

1. Let $\mathrm{True}_1$ and $\mathrm{True}_2$ be two materially adequate definitions in $M$. Then $M$ proves $\mathrm{True}_1(\ulcorner S \urcorner) \leftrightarrow \mathrm{True}_2(\ulcorner S \urcorner)$ for each sentence $S$ of $L$, since both sides are equivalent to $S^{*}$.
2. If $L$ can express its own syntax and $M = L$, then Convention T leads to the liar paradox. This is the content of the undefinability theorem.
3. So a truth definition for $L$ must be given in a metalanguage that is essentially stronger than $L$. Iterating this gives the [[Tarskian hierarchy|Z6MCGB0ZFX]].
4. For first-order languages the definition goes through [[satisfaction|1WTCZB4DVB]] of formulas by assignments. The reason is that some objects can have no name in $L$.

### History

The SEP entry states that Tarski published his analysis of the notion of a true sentence in 1933, in Polish.
It also states that Tarski called the criterion of material adequacy Convention T.
His name for the whole approach was the semantic conception of truth.
In 1956 Tarski and Vaught published a revision of one of the 1933 definitions for model-theoretic languages, per the same entry.

### Common errors

1. Reading the semantic conception as the [[correspondence theory of truth|M3PW4PPX2Z]]. It gives conditions on a definition of truth for a formal language, and it does not say what truth is in general.
2. Confusing two results called "Tarski's theorem": the undefinability of truth inside one language, and the definition of [[truth in a structure|K7XDVK5854]] in a stronger metalanguage. The first is negative and the second is positive.
3. Thinking that Convention T is a single sentence of $M$. It is a schema: infinitely many T-sentences, one for each sentence of $L$.

## Explanations

### L1 human

The sentence "snow is white" is true exactly when snow is white.
Tarski asked for a definition of the word "true" that gives every statement of this kind.
He also asked that the definition use no words like "true" or "means" in its own right side.
For simple formal languages, he showed how to write such a definition.
The definition must be written in a second, richer language that can talk about the first one.

### L2 human

Take the propositional language with atoms $p, q$ and the valuation $v(p) = 1$, $v(q) = 0$.

1. Define $\mathrm{True}(p)$ and not $\mathrm{True}(q)$, since $p$ is true and $q$ is false under $v$.
2. Define $\mathrm{True}(\neg A)$ if and only if not $\mathrm{True}(A)$.
3. Define $\mathrm{True}(A \wedge B)$ if and only if $\mathrm{True}(A)$ and $\mathrm{True}(B)$.
4. Then $\mathrm{True}(\ulcorner p \wedge \neg q \urcorner)$ holds, by steps 1, 2 and 3.
5. The T-sentence for $p \wedge \neg q$ is "$\mathrm{True}(\ulcorner p \wedge \neg q \urcorner)$ if and only if $p$ is true and $q$ is false", and it holds.

The typical use is to check that a proposed truth predicate is correct, by proving each T-sentence.
The trap is to give the T-sentences as the definition: infinitely many biconditionals do not form one explicit definition.

### L3 human

The semantic conception is the model-theoretic notion of [[truth in a structure|K7XDVK5854]], seen from the side of definability.
Its two conditions split the problem of truth into a syntactic part (formal correctness) and a semantic part (material adequacy).
The undefinability theorem shows that the two conditions cannot both hold inside one sufficiently strong language.
The later theories of this topic keep Convention T as a guide, but weaken it.
[[Kripke's theory of truth|ES71QTSTNV]] weakens it by gaps.
[[Axiomatic theories of truth|KE8ZX8KVA3]] restrict it to some sentences, and give axioms in place of a definition.
