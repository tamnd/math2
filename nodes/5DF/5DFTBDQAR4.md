---
tag: 5DFTBDQAR4
kind: example
name: Explosion and excluded middle fail in first-degree entailment
msc: ["03B50", "03B47"]
topics: [WZP584JQ06]
audience: research
instance_of: [KXTP4P3GHT]
uses: [AWEG5PR3GF]
sources:
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: 2.3 True, False, Neither, and Both
  - url: https://en.wikipedia.org/wiki/Four-valued_logic
    locator: Belnap
---

## Example

We use the [[Belnap-Dunn tables|AWEG5PR3GF]], in which a value is designated iff it contains $T$.
For explosion, let $v(p) = \mathbf{B}$ and $v(q) = \mathbf{F}$.

1. $\neg \mathbf{B} = \mathbf{B}$, since $\mathbf{B}$ contains both $T$ and $F$.
2. $v(p \land \neg p) = \mathbf{B} \land \mathbf{B} = \mathbf{B}$, which contains $T$.
3. $v(q) = \mathbf{F}$ does not contain $T$.
4. So $p \land \neg p \not\models_{\mathsf{FDE}} q$, and also $p, \neg p \not\models_{\mathsf{FDE}} q$.

For excluded middle, let $v(p) = \mathbf{T}$ and $v(q) = \mathbf{N}$.

5. $\neg \mathbf{N} = \mathbf{N}$, since $\mathbf{N}$ contains neither value.
6. $v(q \lor \neg q) = \mathbf{N} \lor \mathbf{N} = \mathbf{N}$, which does not contain $T$.
7. $v(p) = \mathbf{T}$ is designated.
8. So $p \not\models_{\mathsf{FDE}} q \lor \neg q$, and $q \lor \neg q$ is not a tautology.

## Remarks

Read as entailments, the two "paradoxes of implication" $A \land \neg A \models B$ and $A \models B \lor \neg B$ fail by these valuations.
Belnap's database example is step 4: the data $p$ and $\neg p$ from two users do not make the computer accept $q$.
Disjunctive syllogism $p, \neg p \lor q \models q$ fails with the valuation of steps 1 to 3, since $\neg p \lor q = \mathbf{B} \lor \mathbf{F} = \mathbf{B}$.

## Explanations

### L1 human

A computer hears "$p$ is true" from one user and "$p$ is false" from another.
Then $p$ is "both".
That does not make it believe an unrelated fact $q$ that someone reported false.
And if it has heard nothing about $q$, it does not believe "$q$ or not $q$" either.

### L2 human

Use $\mathbf{B}$ to make a contradiction designated, and use $\mathbf{N}$ to make a classical law undesignated.
Then choose the other variables to block the conclusion.
The typical use is this pair of counter-models, one per failure.
Watch out: one value cannot refute both inferences, because $\mathbf{B}$ makes $q \lor \neg q$ designated and $\mathbf{N}$ makes $p \land \neg p$ undesignated.
