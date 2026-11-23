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

True arithmetic $\mathrm{TA}$ is the set of all sentences of the language $\{0, S, +, \cdot\}$ that are true in $\mathbb{N}$.
We show that no decidable set $A$ of sentences has exactly the sentences of $\mathrm{TA}$ as its consequences.
So [[arithmetization of syntax|6M12VR1GT6]] has no proof predicate to build for $\mathrm{TA}$.

1. Suppose that $A$ is decidable and that the consequences of $A$ are exactly the sentences in $\mathrm{TA}$.
2. Since $A$ is decidable, the relation "$y$ codes a proof from $A$ of the sentence with code $x$" is decidable, by arithmetization of syntax.
3. A program can run through $y = 0, 1, 2, \ldots$ and print each $x$ that $y$ proves.
   So $\mathrm{TA}$ is [[computably enumerable|TN9G24VABN]].
4. $\mathrm{TA}$ is a [[complete theory|655K8Y7VS8]]: for each sentence $\sigma$, exactly one of $\sigma$ and $\neg \sigma$ is true in $\mathbb{N}$.
5. So a sentence $\sigma$ lies outside $\mathrm{TA}$ exactly when $\neg \sigma$ lies in $\mathrm{TA}$.
   List $\mathrm{TA}$, and print $\sigma$ whenever a sentence of the form $\neg \sigma$ appears.
   This lists the complement, so the complement is also computably enumerable.
6. A set that is computably enumerable and has a computably enumerable complement is decidable, by [[this theorem|EZ6Z9V91C2]].
   So $\mathrm{TA}$ is decidable.
7. Every decidable set of numbers is definable in $\mathbb{N}$, because the formula that represents it in $\mathsf{Q}$ defines it in the model $\mathbb{N}$ of $\mathsf{Q}$.
8. So the set of codes of true sentences is definable in $\mathbb{N}$.
   This contradicts [[Tarski's undefinability theorem|YRV6SYK2BY]], so no such $A$ exists.

## Remarks

The decidability condition of arithmetization fails here, and the failure is not a defect of one particular axiom list: no list works.
Step 3 shows that the argument also rules out a computably enumerable axiom set.

The [[first incompleteness theorem|X9WYNYE29C]] gives the same result from the other side.
Every consistent extension of $\mathsf{Q}$ with a decidable axiom set is incomplete, while $\mathrm{TA}$ is complete, so $\mathrm{TA}$ is not such an extension.
So $\mathrm{TA}$ is not a counterexample to the incompleteness theorem: it fails the hypothesis of computable axioms.

Change the structure and the answer changes.
For $(\mathbb{N}, 0, S, +)$, without multiplication, the set of true sentences is decidable, and the axioms of Presburger arithmetic form a decidable axiom set for it.

## Explanations

### L1 human

The set of all true statements about whole numbers is a perfectly good set.
But no computer program can list axioms that prove exactly these statements.
If one could, a program could answer every question of arithmetic by searching for a proof of the statement or of its negation.
Tarski's theorem shows that no program can do that.

### L2 human

We follow the argument as a search.
Assume a program lists axioms whose consequences are exactly the true sentences.
Then a second program lists all true sentences, by checking every possible proof in turn.
To decide a sentence $\sigma$, run the second program until $\sigma$ or $\neg \sigma$ appears, and one of them must appear because one of them is true.
This decides truth, which contradicts Tarski's theorem.
The typical use is to see why the incompleteness theorems need the axioms to be computable.
Watch out: $\mathrm{TA}$ is complete and consistent, and that is no contradiction, because it has no computable axiom set.
