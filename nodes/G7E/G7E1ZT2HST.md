---
tag: G7E1ZT2HST
kind: example
name: Provability in Q is not a Π1 truth predicate
msc: ["03F30", "03F40"]
topics: [HXHHWY3328]
audience: grad
not_instance_of:
  - target: Y2MF1EZAM7
    note: "The true Pi1 sentence for all x, 0 + x = x, is not provable in Q."
uses: [Y2MF1EZAM7, SFEBD4RB0X, F14YSZ3XKZ, NB2BCZR40F, 3K1AKGXF8A]
sources:
  - url: https://en.wikipedia.org/wiki/Robinson_arithmetic
    locator: Metamathematics
  - book: isbn:9780521857840
---

## Example

The formula $\mathrm{Prov}_{\mathsf{Q}}(x)$ [[is a Σ1 truth predicate|SFEBD4RB0X]] in $\mathbb{N}$.
We show that it is not a [[partial truth predicate|Y2MF1EZAM7]] for $\Pi_1$ sentences: one true $\Pi_1$ sentence is enough to break the biconditional.

1. Let $\pi := \forall x \, (0 + x = x)$.
   The formula $0 + x = x$ has no quantifiers, so $\pi$ is a $\Pi_1$ sentence.
2. $\pi$ is true in $\mathbb{N}$, because $0 + n = n$ for every natural number $n$.
3. [[Robinson arithmetic does not prove π|F14YSZ3XKZ]].
   Add two new elements $a$ and $b$ to $\mathbb{N}$ and define $+$ and $\cdot$ on them so that every axiom of [[Robinson arithmetic|3K1AKGXF8A]] holds but $0 + a \ne a$.
   The axioms of $\mathsf{Q}$ fix $x + 0$ and $x + Sy$, but say nothing about $0 + x$ for a non-standard $x$, and this leaves room for such a model.
   By soundness, $\mathsf{Q} \nvdash \pi$.
4. By step 3 and the meaning of the [[provability predicate|NB2BCZR40F]], $\mathbb{N} \models \neg \mathrm{Prov}_{\mathsf{Q}}(\ulcorner \pi \urcorner)$.
   By step 2, $\mathbb{N} \models \pi$.
5. So the biconditional $\mathrm{Prov}_{\mathsf{Q}}(\ulcorner \pi \urcorner) \leftrightarrow \pi$ is false in $\mathbb{N}$, and the formula is not a truth predicate for $\Pi_1$ sentences.

## Remarks

Only one direction fails.
"Provable implies true" holds for every sentence, by soundness, so the failure is "true implies provable".
Each instance $0 + \underline{n} = \underline{n}$ is a true $\Delta_0$ sentence, and $\mathsf{Q}$ proves it; only the universal sentence escapes.

Replace $\mathsf{Q}$ by $\mathsf{PA}$ and this sentence is proved, by induction on $x$.
But the gap does not close: for every consistent theory $T \supseteq \mathsf{Q}$ with computable axioms, some true $\Pi_1$ sentence is unprovable in $T$, by the first incompleteness theorem.
A $\Pi_1$ truth predicate does exist, as the negation of a $\Sigma_1$ one applied to the negated sentence, but it is a $\Pi_1$ formula, not a $\Sigma_1$ one.

## Explanations

### L1 human

For statements of the form "every number has a property that can be checked", proof and truth come apart.
The law "$0 + x = x$ for every $x$" is true for whole numbers.
Robinson arithmetic can check it for $x = 0$, $x = 1$, $x = 2$ and so on, one number at a time, but it cannot prove it for all $x$ at once.

### L2 human

We test the biconditional on $\pi := \forall x \, (0 + x = x)$.
The right side is true in $\mathbb{N}$.
The left side says "$\mathsf{Q}$ proves $\pi$", and a model of $\mathsf{Q}$ with two extra elements, in which $0 + a \ne a$, shows that this is false.
So the two sides disagree, and $\mathrm{Prov}_{\mathsf{Q}}$ is wrong about $\pi$.
The typical use is to show where $\Sigma_1$-completeness stops.
Watch out: switching to $\mathsf{PA}$ fixes this one sentence, but by the first incompleteness theorem it cannot fix all true $\Pi_1$ sentences.
