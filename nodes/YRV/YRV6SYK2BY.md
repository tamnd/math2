---
tag: YRV6SYK2BY
kind: statement
role: theorem
name: Tarski's undefinability theorem
msc: ["03F40", "03C62"]
topics: [HXHHWY3328]
audience: grad
uses: [MFJXPAF0R0, HYJ10AF6RT, DKFGQTRYZE, 0MWKJ44V5A, WP27CABPA4, 3K1AKGXF8A, 3PRW76471J, VM8TQ70CVJ]
about: [MFJXPAF0R0]
history:
  first_stated: "Tarski, 1933, monograph The Concept of Truth in the Languages of the Deductive Sciences"
  notes: "Gödel also found the result in 1930 and described it in a 1931 letter to von Neumann, but did not publish it."
sources:
  - url: https://en.wikipedia.org/wiki/Tarski's_undefinability_theorem
    locator: History; General form
  - book: isbn:9780521857840
  - book: isbn:9780521701464
same_as:
  wikidata: Q574902
  wikipedia: Tarski's undefinability theorem
---

## Statement

Let $\mathcal{N} = (\N, 0, S, +, \cdot)$ be the [[standard model|WP27CABPA4]] of arithmetic on the [[natural numbers|0MWKJ44V5A]], and fix a [[Gödel numbering|MFJXPAF0R0]] of the [[formulas|HYJ10AF6RT]] of the language of arithmetic.

1. Semantic form. There is no formula $\mathrm{True}(x)$ with one free variable such that, for every [[sentence|DKFGQTRYZE]] $\varphi$, $\mathcal{N} \models \mathrm{True}(\ulcorner \varphi \urcorner) \iff \mathcal{N} \models \varphi$. So the set of codes of sentences true in $\mathcal{N}$ is not definable in $\mathcal{N}$.
2. Syntactic form. Let $T$ be a [[consistent|VM8TQ70CVJ]] theory that contains [[Robinson arithmetic|3K1AKGXF8A]]. There is no formula $\mathrm{Tr}(x)$ such that $T \vdash \mathrm{Tr}(\ulcorner \varphi \urcorner) \leftrightarrow \varphi$ for every sentence $\varphi$.

The proof is in [[the proof of Tarski's theorem|M6M7T09E36]].

## Remarks

### Why each hypothesis is needed

1. Full truth: for each $n$, the set of true $\Sigma_n$ sentences is definable in $\mathcal{N}$, by a [[partial truth predicate|Y2MF1EZAM7]]. Only truth for all sentences at once is not definable.
2. Definability in the same structure: in [[ZFC|0HE5WDQ9FJ]], truth in $\mathcal{N}$ is definable, by recursion on formulas. The theorem forbids only a definition in the language of $\mathcal{N}$ itself.
3. Consistency in the syntactic form: an inconsistent $T$ proves every biconditional $\mathrm{Tr}(\ulcorner \varphi \urcorner) \leftrightarrow \varphi$.

### Consequences

1. The set of true arithmetic sentences is not arithmetical: it is not $\Sigma_n$ for any $n$ in the [[arithmetical hierarchy|7CVJCQKY41]].
2. Provability in a theory with c.e. axioms is $\Sigma_1$-definable, and truth is not definable. So, for a sound c.e. theory $T$, some true sentence is unprovable in $T$. This gives a short proof of a form of [[the first incompleteness theorem|X9WYNYE29C]].
3. The theorem is a precise form of the [[liar paradox|~005ac188]]: a truth predicate would allow the sentence "this sentence is not true".

### Converse

The converse "every set that is not definable in $\mathcal{N}$ is the set of true sentences" is false: there are uncountably many subsets of $\N$ and only countably many definable ones.
Truth in $\mathcal{N}$ becomes definable in a stronger language, such as second-order arithmetic or set theory.

### Generalizations

1. The semantic form holds for every model $M$ of $\mathsf{Q}$: no formula defines in $M$ the set of codes of sentences true in $M$.
2. A [[Tarskian hierarchy|Z6MCGB0ZFX]] of languages, each with a truth predicate for the one below it, avoids the paradox.
3. Axiomatic theories of truth add a new predicate symbol with restricted axioms, and they study which restrictions are consistent.

## History

Tarski stated and proved the theorem in 1933, in his monograph on the concept of truth in the languages of the deductive sciences, written in Polish.
Gödel found the result in 1930, while working on the incompleteness theorems, and described it in a 1931 letter to von Neumann, but did not publish it.

## Explanations

### L1 human

Arithmetic can talk about its own formulas through codes, but it cannot define which of them are true.
Any attempt runs into the sentence "this sentence is not true".
So the notion of arithmetical truth lies outside arithmetic itself.

### L2 human

1. Assume a formula $\mathrm{True}(x)$ defines truth.
2. The diagonal lemma gives $\lambda$ with $\lambda \leftrightarrow \neg \mathrm{True}(\ulcorner \lambda \urcorner)$ true in $\mathcal{N}$.
3. Then $\lambda$ is true exactly when it is not true.

The typical use is to separate truth from provability: provability is definable, truth is not.
A trap: the theorem is about one language; truth for arithmetic is definable in set theory.

### L3 human

The theorem says that a model cannot define its own satisfaction relation for all formulas, while it can for formulas of bounded complexity.
It is the semantic counterpart of the [[first incompleteness theorem|X9WYNYE29C]], and both are diagonal arguments, as in [[Lawvere's fixed point theorem|N84M16W19X]].
In the arithmetical hierarchy, truth for $\Sigma_n$ sentences is $\Sigma_n$-complete, and full truth lies above every level.
