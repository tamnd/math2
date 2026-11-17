---
tag: Y2MF1EZAM7
kind: concept
name: Partial truth predicates
aliases: [partial-truth-definition, sigma-n-truth-predicate]
msc: ["03F30", "03F40"]
topics: [HXHHWY3328]
audience: grad
uses: [YRV6SYK2BY, 7CVJCQKY41, MFJXPAF0R0, WP27CABPA4, 3K1AKGXF8A, MPSCREYC3M]
sources:
  - url: https://en.wikipedia.org/wiki/Tarski's_undefinability_theorem
    locator: General form
  - book: isbn:9780521857840
---

## Summary

A partial truth predicate for a class $\Gamma$ of sentences, such as $\Sigma_n$, is a formula $\mathrm{Tr}_\Gamma(x)$ that is correct about the truth of every sentence in $\Gamma$.
[[Tarski's theorem|YRV6SYK2BY]] forbids a truth predicate for all sentences, but each level $\Sigma_n$ of the [[arithmetical hierarchy|7CVJCQKY41]] has one.
These predicates let a theory reason about the truth of formulas of bounded complexity.

## Motivation

Many arguments about theories need the statement "every theorem of $S$ is true", which needs a truth predicate.
Tarski's theorem rules out a full truth predicate inside arithmetic.
A partial truth predicate gives enough truth for sentences of bounded complexity, and this is often enough, for example to prove the consistency of a fragment of $\mathsf{PA}$.

## Notation

Fix a [[Gödel numbering|MFJXPAF0R0]] and a class $\Gamma$ of sentences, such as $\Delta_0$, $\Sigma_n$ or $\Pi_n$.
A formula $\mathrm{Tr}_\Gamma(x)$ is a partial truth predicate for $\Gamma$ in the [[standard model|WP27CABPA4]] if $\N \models \mathrm{Tr}_\Gamma(\ulcorner \varphi \urcorner) \leftrightarrow \varphi$ for every $\varphi \in \Gamma$.
It is a partial truth predicate for $\Gamma$ in a theory $T$ if $T \vdash \mathrm{Tr}_\Gamma(\ulcorner \varphi \urcorner) \leftrightarrow \varphi$ for every $\varphi \in \Gamma$.
For formulas with free variables one uses a satisfaction formula $\mathrm{Sat}_\Gamma(x, y)$, where $y$ codes an assignment.

## Remarks

### Examples

1. [[A Δ0 truth predicate in Robinson arithmetic|CMZJM97HQ3]]: the decidable set of true $\Delta_0$ sentences is represented in $\mathsf{Q}$, and the representing formula is a truth predicate for $\Delta_0$ in $\mathsf{Q}$.
2. [[Provability in Q is a Σ1 truth predicate|SFEBD4RB0X]] in $\N$: a $\Sigma_1$ sentence is true exactly when $\mathsf{Q}$ proves it.
3. For each $n \ge 1$ there is a $\Sigma_n$ formula $\mathrm{Sat}_{\Sigma_n}$ that is a satisfaction predicate for $\Sigma_n$ formulas in [[Peano arithmetic|MPSCREYC3M]].

### Non-examples

1. [[Provability in Q is not a Π1 truth predicate|G7E1ZT2HST]]: the true $\Pi_1$ sentence $\forall x \, (0 + x = x)$ is not provable in $\mathsf{Q}$.
2. No formula is a truth predicate for all sentences in $\N$, by [[Tarski's theorem|YRV6SYK2BY]].
3. No $\Sigma_n$ formula is a truth predicate for $\Pi_n$ sentences in $\N$, since the set of true $\Pi_n$ sentences is $\Pi_n$-complete and not $\Sigma_n$.

### Basic properties

1. For $n \ge 1$, the set of true $\Sigma_n$ sentences is definable by a $\Sigma_n$ formula, and it is $\Sigma_n$-complete. The definition follows the arithmetical hierarchy: a $\Sigma_{n+1}$ sentence $\exists x \, \pi(x)$ is true when some $x$ makes the $\Pi_n$ formula $\pi$ true.
2. A truth predicate for $\Sigma_n$ gives one for $\Pi_n$: $\pi$ is true exactly when the $\Sigma_n$ sentence equivalent to $\neg \pi$ is not true.
3. With $\mathrm{Sat}_{\Sigma_n}$, the scheme of uniform reflection for $\Sigma_n$ formulas becomes a single sentence.
4. $\mathsf{PA}$ proves the consistency of each finite set of its axioms; the standard proof uses a partial truth predicate together with cut elimination. So, if $\mathsf{PA}$ is consistent, it is not finitely axiomatizable, by the second incompleteness theorem.

### History

Tarski's work of 1933 defined truth for a language in a richer metalanguage and proved that the language itself cannot define it.
Partial truth predicates show that this limit is sharp: for $n \ge 1$, each level $\Sigma_n$ has a truth predicate of the same level.

### Common errors

1. Thinking that a $\Sigma_n$ truth predicate contradicts Tarski's theorem: it covers only $\Sigma_n$ sentences, and the diagonal sentence for it lies outside $\Sigma_n$.
2. Confusing the two notions: a predicate can be correct in $\N$ for every $\Gamma$ sentence without $T$ proving the biconditionals.
3. Expecting a simpler formula: for $n \ge 1$, a truth predicate for $\Sigma_n$ in $\N$ is not $\Pi_n$, since the set of true $\Sigma_n$ sentences is $\Sigma_n$-complete.

## Explanations

### L1 human

Arithmetic cannot define "true" for all of its sentences.
It can define "true" for sentences with a bounded number of quantifier changes, one bound at a time.
This partial notion of truth is enough for many arguments about proofs.

### L2 human

1. Fix $n$ and a coding of $\Sigma_n$ formulas.
2. Define truth for $\Delta_0$ formulas by the decidable evaluation procedure.
3. Add one block of quantifiers at a time: $\exists x \, \pi(x)$ is true when some $x$ makes $\pi$ true.

The typical use is the proof that $\mathsf{PA}$ proves the consistency of each of its finite parts.
A trap: the diagonal sentence of $\neg \mathrm{Tr}_{\Sigma_n}(x)$ is not $\Sigma_n$, so it does not produce a liar paradox.

### L3 human

Partial truth predicates are the arithmetic form of the satisfaction relations used in model theory.
They give the uniform reflection principles, and they underlie the result that $\mathsf{PA}$ is reflexive, that is, proves the consistency of every finite subtheory.
In set theory, for each $n \ge 1$, truth of $\Sigma_n$ formulas in the universe of sets is definable by a $\Sigma_n$ formula, and full truth is not.
