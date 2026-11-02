---
tag: YRV6SYK2BY
kind: statement
role: theorem
name: Tarski's undefinability theorem
msc: [03F40, 03C62]
uses: [MFJXPAF0R0, HYJ10AF6RT, DKFGQTRYZE, 0MWKJ44V5A]
about: [MFJXPAF0R0]
sources:
  - url: https://en.wikipedia.org/wiki/Tarski's_undefinability_theorem
same_as:
  wikidata: Q574902
  wikipedia: Tarski's undefinability theorem
---

## Statement

Let $\mathcal{N} = (\N, 0, S, +, \cdot)$ be the standard model of arithmetic on the [[natural numbers|0MWKJ44V5A]], and fix a [[Gödel numbering|MFJXPAF0R0]] of the [[formulas|HYJ10AF6RT]] of the language of arithmetic.
There is no formula $\mathrm{True}(x)$ with one free variable such that, for every [[sentence|DKFGQTRYZE]] $\varphi$,
$$\mathcal{N} \models \mathrm{True}(\ulcorner \varphi \urcorner) \iff \mathcal{N} \models \varphi.$$
In other words, the set of codes of sentences true in $\mathcal{N}$ is not definable in $\mathcal{N}$.

## Remarks

Proof idea: suppose $\mathrm{True}(x)$ exists.
The [[diagonal lemma|3PRW76471J]], applied in the theory of all sentences true in $\mathcal{N}$, gives a sentence $\lambda$ with $\mathcal{N} \models \lambda \leftrightarrow \neg \mathrm{True}(\ulcorner \lambda \urcorner)$.
Then $\lambda$ is true exactly when it is not true, a contradiction.
This is a precise form of the liar paradox.

By contrast, for each $n$ the set of true $\Sigma_n$ sentences is definable in $\mathcal{N}$; only full truth is not.
A syntactic form also holds: if $T$ is a consistent theory that contains Robinson arithmetic, there is no formula $\mathrm{True}(x)$ with $T \vdash \mathrm{True}(\ulcorner \varphi \urcorner) \leftrightarrow \varphi$ for every sentence $\varphi$.

## Explanations

### L1 human

Arithmetic can talk about its own formulas through codes, but it cannot define which of them are true.
Any attempt runs into the sentence "this sentence is false".
So the notion of arithmetical truth lies outside arithmetic itself.

### L2 human

Compare with [[Gödel's incompleteness theorems|X9WYNYE29C]]: provability in a computably axiomatized theory is definable in arithmetic, but truth is not.
So truth and provability differ, which gives another proof of the first incompleteness theorem.
In terms of the [[arithmetical hierarchy|7CVJCQKY41]], the set of true sentences is not $\Sigma^0_n$ for any $n$.
