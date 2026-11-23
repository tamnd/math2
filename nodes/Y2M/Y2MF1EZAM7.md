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

Arithmetic cannot define truth for all of its sentences, but it can define truth for the sentences of each fixed complexity.
A partial truth predicate for a class $\Gamma$ of sentences, such as the $\Sigma_n$ sentences, is a formula $\mathrm{Tr}_\Gamma(x)$ that is right about every sentence in $\Gamma$:
$$\mathbb{N} \models \mathrm{Tr}_\Gamma(\ulcorner \varphi \urcorner) \leftrightarrow \varphi \quad \text{for every } \varphi \in \Gamma.$$
[[Tarski's theorem|YRV6SYK2BY]] rules out such a formula for the class of all sentences.
For each $n \ge 1$, however, the class $\Sigma_n$ of the [[arithmetical hierarchy|7CVJCQKY41]] has a partial truth predicate that is itself a $\Sigma_n$ formula.

## Motivation

Many arguments about a theory $S$ need the statement "every theorem of $S$ is true".
Inside arithmetic, that statement needs a truth predicate, and Tarski's theorem forbids a full one.
Partial truth predicates give enough truth for sentences of bounded complexity, and that is often all an argument uses.
For example, a proof that uses only $\Sigma_n$ formulas can be checked with a $\Sigma_n$ truth predicate.

This is how $\mathsf{PA}$ proves the consistency of each finite part of itself, and how the [[reflection principles|NB485KFXKV]] for $\Sigma_n$ sentences become single sentences.
In the model theory of $\mathsf{PA}$, the same formulas define truth for bounded complexity inside non-standard models.

## Notation

Fix a [[Gödel numbering|MFJXPAF0R0]] and a class $\Gamma$ of sentences, such as $\Delta_0$, $\Sigma_n$ or $\Pi_n$.
The formula $\mathrm{Tr}_\Gamma(x)$ is a partial truth predicate for $\Gamma$ in the [[standard model|WP27CABPA4]] when the display in the Summary holds.
It is a partial truth predicate for $\Gamma$ in a theory $T$ when $T \vdash \mathrm{Tr}_\Gamma(\ulcorner \varphi \urcorner) \leftrightarrow \varphi$ for every $\varphi \in \Gamma$, and these biconditionals are called the Tarski biconditionals.
For formulas with free variables one uses a satisfaction formula $\mathrm{Sat}_\Gamma(x, y)$, where $y$ codes an assignment of numbers to the variables.
The two senses differ: a formula can be right in $\mathbb{N}$ without $T$ proving any of the biconditionals.

## Remarks

### A first truth predicate

The bounded sentences, the class $\Delta_0$, are the easiest case.
A $\Delta_0$ sentence such as $\exists x \le 5 \, (x \cdot x = 9)$ can be checked by a finite search: try $x = 0, 1, \ldots, 5$, and $x = 3$ works.
So the set of codes of true $\Delta_0$ sentences is decidable, and a formula that represents it in [[Robinson arithmetic|3K1AKGXF8A]] is a $\Delta_0$ truth predicate even in $\mathsf{Q}$.
[[A Δ0 truth predicate in Robinson arithmetic|CMZJM97HQ3]] carries this out.

### One level up: Σ1 truth

A $\Sigma_1$ sentence $\exists y \, \delta(y)$, with $\delta$ bounded, is true exactly when some number $m$ makes $\delta(\underline{m})$ true.
So a $\Sigma_1$ truth predicate says "there is an $m$ such that the $\Delta_0$ truth predicate holds of the code of $\delta(\underline{m})$".
It is $\Sigma_1$, because it puts one unbounded $\exists$ in front of a decidable condition.
A second route needs no construction: [[provability in Q is a Σ1 truth predicate|SFEBD4RB0X]], because $\mathsf{Q}$ proves exactly the true $\Sigma_1$ sentences.

### Climbing the hierarchy

The same step repeats.
A $\Sigma_{n+1}$ sentence $\exists x \, \pi(x)$, with $\pi$ in $\Pi_n$, is true when some $x$ makes $\pi(x)$ true.
A $\Pi_n$ sentence is true when the $\Sigma_n$ sentence equivalent to its negation is not true.
So a $\Sigma_n$ truth predicate gives a $\Pi_n$ one by negation, and then a $\Sigma_{n+1}$ one by one more $\exists$.
For each $n \ge 1$, the result is a $\Sigma_n$ satisfaction formula $\mathrm{Sat}_{\Sigma_n}$, and its Tarski conditions are provable already in the fragment $\mathsf{I}\Sigma_1$ of [[Peano arithmetic|MPSCREYC3M]].

### What it is not

[[Provability in Q is not a Π1 truth predicate|G7E1ZT2HST]]: the true $\Pi_1$ sentence $\forall x \, (0 + x = x)$ is not provable in $\mathsf{Q}$.
No formula is a truth predicate for all sentences in $\mathbb{N}$, by Tarski's theorem.
No $\Sigma_n$ formula is a truth predicate for $\Pi_n$ sentences in $\mathbb{N}$.
If it were, its conjunction with the decidable formula "$x$ codes a $\Pi_n$ sentence" would define the set of true $\Pi_n$ sentences by a $\Sigma_n$ formula, but that set is $\Pi_n$-complete and so not $\Sigma_n$.

### What it gives you

With $\mathrm{Sat}_{\Sigma_n}$, the scheme of uniform reflection for $\Sigma_n$ formulas becomes a single sentence.
$\mathsf{PA}$ proves the consistency of each finite set of its axioms, by a proof that combines a partial truth predicate with cut elimination.
So, if $\mathsf{PA}$ is consistent, it is [[not finitely axiomatizable|M5WNB181T7]], by the second incompleteness theorem.

### History

Tarski's work of 1933 defined truth for a formal language in a richer metalanguage, and proved that the language itself cannot define it.
Partial truth predicates show that the limit is sharp in arithmetic: for $n \ge 1$, each level $\Sigma_n$ has a truth predicate of the same level.

### Watch out

A $\Sigma_n$ truth predicate does not contradict Tarski's theorem.
Apply the diagonal lemma to $\neg \mathrm{Tr}_{\Sigma_n}(x)$ and you get a liar $\lambda$.
If $\lambda$ were a $\Sigma_n$ sentence, the predicate would be right about it and the liar argument would give a contradiction.
So $\lambda$ is not $\Sigma_n$, the predicate says nothing about it, and no paradox arises.

### Try it

Is $\exists x \le 4 \, (x + x = 7)$ in the set defined by the $\Delta_0$ truth predicate?
No: the sums $x + x$ for $x = 0, \ldots, 4$ are $0, 2, 4, 6, 8$, and none of them is $7$.

What level is the natural truth predicate for $\Pi_2$ sentences?
It is $\Pi_2$: a $\Pi_2$ sentence is true when the $\Sigma_2$ sentence equivalent to its negation is not true, so negate a $\Sigma_2$ predicate.

## Explanations

### L1 human

Arithmetic cannot define "true" for all of its sentences at once.
It can define "true" for the sentences with at most a fixed number of changes between "for all" and "there exists".
For example, "there is a number below $5$ whose square is $9$" is checked by trying $0$ to $5$.
These partial notions of truth are enough for many arguments about proofs.

### L2 human

We build a $\Sigma_1$ truth predicate in two moves.
First, define truth for bounded sentences by the evaluation procedure, which is decidable and so representable in $\mathsf{Q}$.
Second, say that $\exists y \, \delta(y)$ is true when some $m$ makes the bounded sentence $\delta(\underline{m})$ true.
For example, $\exists y \, (y \cdot y = \underline{9})$ is true because the bounded sentence $\underline{3} \cdot \underline{3} = \underline{9}$ is true.
The typical use is the proof that $\mathsf{PA}$ proves the consistency of each of its finite parts.
Watch out: the liar sentence for $\mathrm{Tr}_{\Sigma_n}$ is not $\Sigma_n$, so it produces no paradox.

### L3 human

Partial truth predicates are the arithmetic form of the satisfaction relation of model theory, restricted to bounded complexity.
They give the uniform reflection principles, and they underlie the result that $\mathsf{PA}$ is reflexive, that is, proves the consistency of every finite subtheory.
In set theory the same pattern holds: for each $n \ge 1$, truth of $\Sigma_n$ formulas in the universe of sets is definable by a $\Sigma_n$ formula, and full truth is not.
