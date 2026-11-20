---
tag: 3P0FM0AQF3
kind: concept
name: Dialetheism
aliases: [dialethic-logic, dialethism, dialetheia, true-contradiction]
msc: ["03B53", "03A05"]
topics: [NJB94B39QK]
audience: ug2
uses: [MP4R7T546Z, C7YWCR87QJ, TTKZGJEEK7, WH94DG6D3Q, ~26a0362d]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section D
    note: adopted
    mention: wikipedia://en/76765067#RC3V
    sections: [Summary]
  - url: https://plato.stanford.edu/entries/dialetheism/
    locator: Dialetheism (SEP entry), sections 1, 2.4, 3 and 4.1
  - book: isbn:9780521670265
inventory: [R3XS78DGB2]
---

## Summary

*Dialetheism* is the view that some contradictions are true.
A *dialetheia* is a sentence $A$ such that $A$ and its negation $\neg A$ are both true; in a many-valued semantics, it is a [[truth-value glut|WH94DG6D3Q]].
So dialetheism rejects the [[law of non-contradiction|MP4R7T546Z]] in its strong form.
A dialetheist must use a [[paraconsistent logic|C7YWCR87QJ]], since in an [[explosive|TTKZGJEEK7]] logic one true contradiction would make every sentence true.
The glossary name "dialethic logic" refers to the logics that dialetheists use, such as the [[logic of paradox|~26a0362d]].

## Motivation

The main argument for dialetheism comes from the paradoxes of self-reference.
The liar sentence "this sentence is false" seems to be true if and only if it is false.
Classical replies restrict the language or add truth-value gaps, and each reply meets a "strengthened" or revenge liar, such as "this sentence is not true".
Priest argues that the simplest description of these facts is that the liar is both true and false.
The same move applies to set theory: with unrestricted comprehension, the Russell set is and is not a member of itself.

## Notation

We write $A$ is a dialetheia when $A$ and $\neg A$ are both true.
In the logic of paradox, this is the value $\mathsf{B}$, and a dialetheia is a formula $A$ with $v(A) = \mathsf{B}$.

## Remarks

### Examples

- [[The liar sentence in LP|~0dda8b01]] has the value $\mathsf{B}$ in every model of the truth schema.
- [[The Russell set in naive set theory|~40e3adc4]] is and is not a member of itself, under LP.
- Other proposed dialetheias include borderline cases of vague predicates and the instant at which a moving object leaves a place.

### Non-examples

- [[Reasoning from an inconsistent database with LP|~794ba27b]] is paraconsistent but not dialetheic, since it makes no claim that a contradiction is true.
- Trivialism, the view that every sentence is true, implies dialetheism but is not implied by it: "some" does not imply "all".

### Basic properties

- Dialetheism implies the use of a paraconsistent logic, but the converse fails. Most paraconsistent logicians are not dialetheists.
- The SEP entry follows Beall and Restall in distinguishing four grades of paraconsistency: gentle, full, industrial and dialetheic strength. Only the last is dialetheism.
- A dialetheic theory of truth can keep the full T-schema and the law of excluded middle, and it locates the paradoxes at the value $\mathsf{B}$.
- A dialetheic theory must still avoid Curry's paradox, which does not use negation. The standard reply uses a conditional that does not validate contraction.

### History

The word "dialetheism" was coined by Priest and Routley (later Sylvan) in 1981, after a passage of Wittgenstein on Russell's paradox.
Asenjo assumed in 1966 that atomic propositions may have one or two truth values.
Routley and Meyer developed a "dialectical" position in the mid-1970s.
Priest's 1979 paper "The Logic of Paradox", later developed into the book *In Contradiction*, gave the best-known arguments for dialetheism.

### Common errors

- To identify dialetheism with paraconsistency. Paraconsistency is a property of a logic; dialetheism is a claim about truth.
- To say that the dialetheist accepts all contradictions. The view says that some, usually very specific, sentences are dialetheias.
- To argue against dialetheism by explosion. The argument assumes that explosion is valid, which the dialetheist denies.

## Explanations

### L1 human

Most people think a statement cannot be both true and false.
Dialetheists say that a few special statements are.
The standard case is "this sentence is false": if it is true, it is false, and if it is false, it is true.
A dialetheist says it is both, and uses a logic in which this does not lead to nonsense.

### L2 human

We reason about the liar $\lambda$, which says $\neg T(\lambda)$, in a logic with the truth schema $T(A) \leftrightarrow A$.

1. By the truth schema, $T(\lambda) \leftrightarrow \lambda$.
2. By the definition of $\lambda$, $\lambda \leftrightarrow \neg T(\lambda)$.
3. So $\lambda \leftrightarrow \neg\lambda$.
4. By cases on excluded middle $\lambda \lor \neg\lambda$, we get $\lambda \land \neg\lambda$.

A classical logician must reject the truth schema or the definition of $\lambda$.
A dialetheist accepts line 4 and uses LP to stop line 4 from proving every sentence.
A trap is to think that line 4 proves "everything is true"; it does so only in an explosive logic.

### L3 human

Dialetheism is a thesis in the philosophy of logic, so its mathematical content lies in the theories it supports.
Inconsistent but non-trivial theories of truth and sets are formulated over LP or over relevant logics with a non-contractive conditional.
Priest's Inclosure Schema gives a common structure to the semantic and set-theoretic paradoxes, and his principle of uniform solution then argues for one dialetheic treatment.
Objections include the arguments from exclusion and from negation: the dialetheist seems unable to express that a sentence is only true.
