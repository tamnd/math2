---
tag: 69TTX21TRJ
kind: example
name: True arithmetic has no decidable axiom set
msc: ["03F40", "03D35"]
topics: [HXHHWY3328]
audience: grad
not_instance_of:
  - target: 6M12VR1GT6
    note: "The method needs a decidable set of axioms, and true arithmetic has none."
uses: [6M12VR1GT6, YRV6SYK2BY, EZ6Z9V91C2, TN9G24VABN, 655K8Y7VS8]
sources:
  - url: https://en.wikipedia.org/wiki/True_arithmetic
    locator: lead section
  - book: isbn:9780521857840
---

## Example

True arithmetic $\mathrm{TA}$ is the set of all sentences of the language $\set{0, S, +, \cdot}$ that are true in $\N$.
We show that no decidable set $A$ of sentences has exactly the sentences of $\mathrm{TA}$ as its consequences.
So [[arithmetization of syntax|6M12VR1GT6]] gives no proof predicate for $\mathrm{TA}$.

1. Suppose that $A$ is decidable and that the consequences of $A$ are exactly the sentences in $\mathrm{TA}$.
2. Since $A$ is decidable, the relation $\mathrm{Prf}_A(y, x)$ is decidable, by arithmetization of syntax.
3. A program can run through $y = 0, 1, 2, \ldots$ and list each $x$ with $\mathrm{Prf}_A(y, x)$. So $\mathrm{TA}$ is [[computably enumerable|TN9G24VABN]].
4. $\mathrm{TA}$ is a [[complete theory|655K8Y7VS8]]: for each sentence $\sigma$, exactly one of $\sigma$ and $\neg \sigma$ is true in $\N$.
5. So a sentence $\sigma$ is outside $\mathrm{TA}$ exactly when $\neg \sigma \in \mathrm{TA}$. Listing $\mathrm{TA}$ and taking negations lists the complement, so the complement is also computably enumerable.
6. A set that is computably enumerable and has a computably enumerable complement is decidable, by [[this theorem|EZ6Z9V91C2]]. So $\mathrm{TA}$ is decidable.
7. Every decidable set of numbers is definable in $\N$, because the formula that represents it in $\mathsf{Q}$ defines it in the model $\N$ of $\mathsf{Q}$.
8. So the set of codes of true sentences is definable in $\N$. This contradicts [[Tarski's undefinability theorem|YRV6SYK2BY]], so no such $A$ exists.

## Remarks

The decidability condition of arithmetization fails here, and the failure is not a defect of a particular axiom list: no list works.
The argument also excludes a computably enumerable axiom set, by Craig's trick or directly by step 3.
The first incompleteness theorem gives the same result for every consistent extension of $\mathsf{Q}$ with a decidable axiom set: such a theory is incomplete, while $\mathrm{TA}$ is complete.
If $\N$ is replaced by $(\N, +)$, the theory becomes decidable, and it has a decidable axiom set, the axioms of Presburger arithmetic.

## Explanations

### L1 human

The set of all true statements about whole numbers is a perfectly good set.
But no computer program can list axioms that prove exactly these statements.
If one could, a program could decide every question of arithmetic, and that is impossible.
So the method of turning proofs into numbers has nothing to work on for this theory.

### L2 human

1. Assume a program lists axioms whose consequences are the true sentences.
2. Then a program lists all true sentences, by checking all proofs.
3. To decide a sentence $\sigma$, list the true sentences until $\sigma$ or $\neg \sigma$ appears; one of them must appear.
4. This decides truth, which contradicts Tarski's theorem.

The typical use is to see why incompleteness needs the axioms to be computable.
A trap: $\mathrm{TA}$ is complete and consistent, so it is not a counterexample to the incompleteness theorem; it fails its hypothesis.
