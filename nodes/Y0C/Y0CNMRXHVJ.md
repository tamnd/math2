---
tag: Y0CNMRXHVJ
kind: concept
name: Free logic
aliases: [free-logics, logic-free-of-existence-assumptions, positive-free-logic, negative-free-logic, neutral-free-logic]
msc: ["03B60", "03B10"]
topics: [NJB94B39QK]
audience: ug2
uses: [086QKPF0A6, XK9WZW5B68, 33ZNXRFVJJ, PD2R4XT79Q]
sources:
  - url: https://plato.stanford.edu/entries/logic-free/
    locator: Free Logic (SEP entry), sections 1, 1.1, 1.2 and 3.1
  - url: https://en.wikipedia.org/wiki/Free_logic
    locator: lead section
  - book: isbn:9780521818162
---

## Summary

A *free logic* is a version of [[first-order logic|086QKPF0A6]] in which singular terms need not denote existing objects.
Its quantifiers range over existing objects only, and an [[existence predicate|XK9WZW5B68]] $E!$ marks the terms that denote.
So the rules of universal specification and [[existential generalization|33ZNXRFVJJ]] need an extra premise $E!t$.
There are three main variants.
*Positive* free logic lets some atoms with non-denoting terms be true, at least $t = t$; *negative* free logic makes all such atoms false; *neutral* free logic gives them no truth value.

## Motivation

Classical first-order logic assumes that every name denotes an object in the domain.
So from "Sleipnir does not exist" it derives "something does not exist", by existential generalization.
Ordinary reasoning uses names for fictional, mythical or not yet known objects, and [[definite descriptions|PD2R4XT79Q]] such as "the largest prime" that may fail to denote.
Mathematics also uses partial terms, such as $1/x$ at $x = 0$.
Free logic changes only the rules that move between names and quantifiers, and keeps the rest of first-order logic.

## Notation

We write $E!t$ for "$t$ exists", or "$t$ is defined".
The *inner domain* $D_i$ is the set of existing objects, over which the quantifiers range.
In positive semantics, an *outer domain* $D_o \supseteq D_i$ gives denotations to non-denoting terms.

## Remarks

### Examples

- [[Universal specification fails for an empty name|PBRNFHNJS3]]: $\forall x Px \to Pt$ is not valid.
- In positive free logic, $t = t$ holds for every term $t$, but $\exists x\,(x = t)$ holds only if $E!t$.
- Hintikka's law $E!t \leftrightarrow \exists x\,(x = t)$ is a theorem of positive free logic.

### Non-examples

- [[Classical first-order logic|EY0TDAVPRA]] proves $\exists x\,(x = t)$ for every term $t$, so it is not free.
- [[Inclusive logic|ESK5RPV8PC]] allows the empty domain but may have no non-denoting terms; it is a related but different idea.

### Basic properties

- The free form of specification is $\forall x A \to (E!t \to A[t/x])$.
- Negative free logic adds the axiom $P(t_1, \ldots, t_n) \to E!t_1 \land \cdots \land E!t_n$ for each predicate $P$, and replaces $t = t$ with $E!t \to t = t$.
- Inclusive logic and free logic are orthogonal: a logic can allow the empty domain without allowing empty names, and the converse.
- Free logics are used for definite descriptions, partial functions, programming languages, logics of fiction, and modal logics with varying domains.

### History

A passage of Aristotle on "Socrates is sick" when Socrates does not exist anticipates the issue.
Inclusive logic was studied in the first half of the twentieth century; Quine named it in 1954.
Modern free logic arose in the middle of the century, with work of Hintikka (1959) and Lambert.
The name is due to Lambert and abbreviates "logic free of existence assumptions with respect to its terms, singular and general".

### Common errors

- To think that free logic allows the empty domain. That is inclusive logic; most free logics keep a nonempty domain.
- To read $E!$ as an ordinary predicate with no logical role. Its extension is the domain of the quantifiers.
- To think that negative free logic makes $t = t$ true for empty $t$. It makes all atoms with empty terms false, including $t = t$.

## Explanations

### L1 human

"Pegasus is a winged horse" uses a name for something that does not exist.
Ordinary logic would then conclude "there exists a winged horse".
Free logic blocks this step.
It requires the extra fact "Pegasus exists" before moving from a name to "there exists".

### L2 human

We compare classical and free specification.

1. Classical: from $\forall x\, Px$ infer $Pt$.
2. Free: from $\forall x\, Px$ and $E!t$ infer $Pt$.

Let $Px$ be "$x$ is a physical object", and let $t$ be "Sherlock Holmes".
Every existing thing may be physical, while "Holmes is a physical object" is false or truth-valueless.
A trap is to think that free logic changes the quantifiers; it changes only the link between names and quantifiers.

### L3 human

The semantic options differ in the treatment of atoms with empty terms: dual-domain (Meinongian) semantics for positive free logic, partial interpretations with all such atoms false for negative free logic, and three-valued or supervaluational semantics for neutral free logic.
In sequent calculus, free logic restricts the quantifier rules with an $E!t$ in the context, and a rule that introduces $E!t$ for fresh $t$ recovers a nonempty domain.
Negative free logic is the logic of definedness in Feferman-style theories of partial functions: $t \downarrow$ is $E!t$, and atoms imply definedness of their arguments.
