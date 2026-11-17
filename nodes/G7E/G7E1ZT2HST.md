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

The formula $\mathrm{Prov}_{\mathsf{Q}}(x)$ [[is a Σ1 truth predicate|SFEBD4RB0X]] in $\N$.
We show that it is not a [[partial truth predicate|Y2MF1EZAM7]] for $\Pi_1$ sentences.

1. Let $\pi := \forall x \, (0 + x = x)$. It is a $\Pi_1$ sentence, since $0 + x = x$ has no quantifiers.
2. $\pi$ is true in $\N$.
3. [[Robinson arithmetic does not prove π|F14YSZ3XKZ]]: a model of $\mathsf{Q}$ with two extra elements fails it.
4. So $\N \models \neg \mathrm{Prov}_{\mathsf{Q}}(\ulcorner \pi \urcorner)$ while $\N \models \pi$.
5. So the biconditional $\mathrm{Prov}_{\mathsf{Q}}(\ulcorner \pi \urcorner) \leftrightarrow \pi$ fails in $\N$, and the formula is not a truth predicate for $\Pi_1$.

## Remarks

The direction "provable implies true" holds for all sentences, by soundness; only "true implies provable" fails.
The same happens for every consistent c.e. theory $T \supseteq \mathsf{Q}$: some true $\Pi_1$ sentence is unprovable in $T$, by the first incompleteness theorem.
A $\Pi_1$ truth predicate does exist, as the negation of a $\Sigma_1$ one, but it is $\Pi_1$, not $\Sigma_1$.

## Explanations

### L1 human

For statements of the form "every number has a checkable property", proof in Robinson arithmetic and truth come apart.
The law "$0 + x = x$ for all $x$" is true, but Robinson arithmetic cannot prove it.

### L2 human

1. Take the true $\Pi_1$ sentence $\forall x \, (0 + x = x)$.
2. A model of $\mathsf{Q}$ in which it fails shows that $\mathsf{Q}$ does not prove it.
3. So provability in $\mathsf{Q}$ misses a true $\Pi_1$ sentence.

The typical use is to show where $\Sigma_1$-completeness stops.
A trap: replacing $\mathsf{Q}$ by $\mathsf{PA}$ fixes this sentence, but not all true $\Pi_1$ sentences.
