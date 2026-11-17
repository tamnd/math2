---
tag: 8G2GVRXWG5
kind: statement
role: theorem
name: WKL0 is Π¹₁-conservative over RCA0
msc: ["03B30", "03F35"]
topics: [BY8AAFN7C5]
audience: research
about: [7W9EG02T79, XQENB067R3]
uses: [DNXCKXZZ08, K5YPW1NTHZ, N238J43XNE]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Weak Kőnig's lemma WKL0
---

## Statement

For every $\Pi^1_1$ sentence $\sigma$ of $L_2$: if [[WKL0|K5YPW1NTHZ]] proves $\sigma$, then [[RCA0|DNXCKXZZ08]] proves $\sigma$.

A $\Pi^1_1$ sentence has the form $\forall X\, \theta(X)$ with $\theta$ arithmetical, that is, without set quantifiers.
In particular, $\mathsf{WKL}_0$ is a [[conservative extension|N238J43XNE]] of $\mathsf{RCA}_0$ for arithmetic sentences.

## Remarks

### Why each hypothesis is needed

- The class $\Pi^1_1$ cannot be replaced by $\Pi^1_2$. Weak König's lemma itself is a $\Pi^1_2$ sentence, $\mathsf{WKL}_0$ proves it, and $\mathsf{RCA}_0$ does not.

### Consequences

- $\mathsf{WKL}_0$ and $\mathsf{RCA}_0$ prove the same arithmetic sentences, so the first-order part of $\mathsf{WKL}_0$ is $\mathrm{I}\Sigma_1$.
- $\mathsf{WKL}_0$ is consistent if $\mathsf{RCA}_0$ is: an inconsistency would give a proof of the $\Pi^1_1$ sentence $0 = 1$ in $\mathsf{WKL}_0$.
- With Parsons's theorem, $\mathsf{WKL}_0$ is [[Π⁰₂-conservative over primitive recursive arithmetic|V609D9SZ05]].

### Converse

The converse is trivial: $\mathsf{WKL}_0$ contains $\mathsf{RCA}_0$, so it proves every theorem of $\mathsf{RCA}_0$.

### Generalizations

The same method shows that $\mathsf{WKL}_0 + \Sigma^0_n$ induction is $\Pi^1_1$-conservative over $\mathsf{RCA}_0 + \Sigma^0_n$ induction, for each $n \ge 1$.
The theory $\mathsf{ACA}_0$ is not $\Pi^1_1$-conservative over $\mathsf{RCA}_0$, since it proves the consistency of $\mathrm{I}\Sigma_1$.

## History

The theorem is due to Leo Harrington, who proved it with a forcing argument; the result was not published by him and appears in the literature on $\mathsf{WKL}_0$.

## Explanations

### L1 human

Weak König's lemma lets one prove theorems about all sets more easily.
But for a statement about numbers, or about all sets one at a time with no further set quantifiers, it adds nothing.
Every such statement that $\mathsf{WKL}_0$ proves has a proof in the weaker system $\mathsf{RCA}_0$.

### L2 human

The proof is by models: every countable model of $\mathsf{RCA}_0$ has more sets added to it so that it satisfies $\mathsf{WKL}_0$, with the same numbers.
An arithmetic statement about a fixed set does not change when sets are added.
A trap is to think that the added sets are definable in the old model: they are not, and the proof needs a model-theoretic construction.
