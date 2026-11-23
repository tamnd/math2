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

Weak König's lemma lets us prove many new theorems of analysis, but it never lets us prove a new statement of the form "for every set $X$, an arithmetical property of $X$ holds".

A sentence of $L_2$ is $\Pi^1_1$ when it has the form $\forall X\, \theta(X)$ with $\theta$ arithmetical, that is, with no set quantifiers.

**Theorem.** For every $\Pi^1_1$ sentence $\sigma$ of $L_2$, if [[WKL0|K5YPW1NTHZ]] proves $\sigma$, then [[RCA0|DNXCKXZZ08]] proves $\sigma$.

In particular, $\mathsf{WKL}_0$ is a [[conservative extension|N238J43XNE]] of $\mathsf{RCA}_0$ for arithmetical sentences.

## Remarks

### Why the class of sentences matters

The class $\Pi^1_1$ cannot be replaced by $\Pi^1_2$.
Weak König's lemma is itself a $\Pi^1_2$ sentence, "for every tree $T$ there is a path $f$", and $\mathsf{WKL}_0$ proves it.
But $\mathsf{RCA}_0$ does not prove it, because it fails in the $\omega$-model of the computable sets, where the separation tree has no path.
So conservation stops exactly at the level of the new axiom.

### What it gives you

The arithmetical theorems of $\mathsf{WKL}_0$ are those of $\mathsf{RCA}_0$, and both have the first-order part $\mathrm{I}\Sigma_1$.
For example, suppose that a proof in $\mathsf{WKL}_0$ uses the maximum of a continuous function on $[0, 1]$ to show that some equation has a solution in natural numbers.
The theorem says that a proof in $\mathsf{RCA}_0$ also exists, even though $\mathsf{RCA}_0$ cannot prove that the maximum exists.

$\mathsf{WKL}_0$ is consistent if $\mathsf{RCA}_0$ is.
The sentence $0 = 1$ is arithmetical, so a proof of it in $\mathsf{WKL}_0$ would give a proof of it in $\mathsf{RCA}_0$.
Together with Parsons's theorem that $\mathrm{I}\Sigma_1$ is $\Pi^0_2$-conservative over primitive recursive arithmetic, the theorem gives that $\mathsf{WKL}_0$ is [[Π⁰₂-conservative over primitive recursive arithmetic|V609D9SZ05]].

### The converse

The converse holds at once: $\mathsf{WKL}_0$ contains $\mathsf{RCA}_0$, so it proves every theorem of $\mathsf{RCA}_0$.
The interesting fact is that the inclusion of theorems is an equality for $\Pi^1_1$ sentences and strict for $\Pi^1_2$ sentences.

### Generalizations and limits

The same forcing argument shows that $\mathsf{WKL}_0$ plus $\Sigma^0_n$ induction is $\Pi^1_1$-conservative over $\mathsf{RCA}_0$ plus $\Sigma^0_n$ induction, for each $n \ge 1$.
The next system up behaves differently.
$\mathsf{ACA}_0$ is not $\Pi^1_1$-conservative over $\mathsf{RCA}_0$, because it proves the consistency of $\mathrm{I}\Sigma_1$, an arithmetical sentence that $\mathrm{I}\Sigma_1$ does not prove.

### Watch out

The theorem is about sentences with one universal set quantifier in front.
A $\Pi^1_1$ sentence such as "every infinite binary tree $T$ has a node of length $5$" is covered.
The sentence "every infinite binary tree has a path" begins with $\forall T\, \exists f$, so it is $\Pi^1_2$, and it is not covered.
Count the set quantifiers before you apply the theorem.

## History

Leo Harrington proved the theorem by a forcing argument.
He did not publish the proof himself.
Stephen Simpson's book *Subsystems of Second Order Arithmetic* (1999, second edition 2009) presents it.

## Explanations

### L1 human

Weak König's lemma lets us prove more theorems about infinite objects, such as the fact that a continuous function on $[0, 1]$ has a largest value.
But for a statement about numbers, it adds nothing.
Every such statement that $\mathsf{WKL}_0$ proves already has a proof in the weaker system $\mathsf{RCA}_0$.
The extra principle is a convenience, not a source of new facts about numbers.

### L2 human

The [[proof|H5M7W75JCM]] uses models.
Suppose that $\mathsf{RCA}_0$ does not prove $\forall X\, \theta(X)$.
Then some countable model of $\mathsf{RCA}_0$ has a set $A$ with $\neg \theta(A)$.
We add paths through trees to that model, keeping its numbers fixed, until weak König's lemma holds.
The formula $\neg \theta(A)$ talks only about numbers and the old set $A$, so it is still true, and $\mathsf{WKL}_0$ does not prove $\forall X\, \theta(X)$ either.
The trap is to think that the added sets are definable in the old model: they are not, and adding them while keeping $\Sigma^0_1$ induction is the hard step.

### L3 human

Conservation results of this kind are the backbone of [[partial realizations of Hilbert's program|Z26S516BKH]]: a theorem of $\mathsf{WKL}_0$ about numbers has a finitistic justification.
Later proof-theoretic work turns every $\mathsf{WKL}_0$ proof of a $\Pi^1_1$ sentence directly into an $\mathsf{RCA}_0$ proof, without passing through models.
The same question for [[Ramsey's theorem for pairs|ZT5KV6KJ3E]] is much harder, and its answer depends on the induction available in the base theory.
