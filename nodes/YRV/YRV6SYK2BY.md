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

The theorem turns the liar sentence "this sentence is not true" into a proof that no formula of arithmetic defines the set of codes of true sentences of arithmetic.

Let $\mathcal{N} = (\mathbb{N}, 0, S, +, \cdot)$ be the [[standard model|WP27CABPA4]] of arithmetic on the [[natural numbers|0MWKJ44V5A]].
Fix a [[Gödel numbering|MFJXPAF0R0]] of the [[formulas|HYJ10AF6RT]] of the language $\{0, S, +, \cdot\}$, and write $\ulcorner \varphi \urcorner$ for the numeral of the code of $\varphi$.

**Theorem (Tarski).**

1. Semantic form.
   There is no formula $\mathrm{True}(x)$ with one free variable such that, for every [[sentence|DKFGQTRYZE]] $\varphi$,
   $$\mathcal{N} \models \mathrm{True}(\ulcorner \varphi \urcorner) \iff \mathcal{N} \models \varphi.$$
   So the set of codes of sentences true in $\mathcal{N}$ is not definable in $\mathcal{N}$.
2. Syntactic form.
   Let $T$ be a [[consistent|VM8TQ70CVJ]] theory that contains [[Robinson arithmetic|3K1AKGXF8A]] $\mathsf{Q}$.
   There is no formula $\mathrm{Tr}(x)$ such that $T \vdash \mathrm{Tr}(\ulcorner \varphi \urcorner) \leftrightarrow \varphi$ for every sentence $\varphi$.

The [[proof of Tarski's theorem|M6M7T09E36]] applies the [[diagonal lemma|3PRW76471J]] to $\neg \mathrm{True}(x)$.

## Remarks

### The liar, in arithmetic

The liar sentence $L$ says "$L$ is not true".
If $L$ is true, then what it says holds, so $L$ is not true.
If $L$ is not true, then what it says holds, so $L$ is true.
In English this is a puzzle, because English has a truth predicate and lets a sentence talk about itself.

Arithmetic lets a sentence talk about itself through codes: the diagonal lemma gives, for each formula $\theta(x)$, a sentence $\lambda$ that $\mathsf{Q}$ proves equivalent to $\theta(\ulcorner \lambda \urcorner)$.
Suppose some formula $\mathrm{True}(x)$ defined truth.
Take $\theta(x) := \neg \mathrm{True}(x)$, and the diagonal lemma builds a liar $\lambda$ inside arithmetic.
Then $\lambda$ is true in $\mathcal{N}$ exactly when $\mathrm{True}(\ulcorner \lambda \urcorner)$ fails, that is, exactly when $\lambda$ is not true.
In arithmetic this is not a puzzle but a contradiction, so the formula $\mathrm{True}(x)$ cannot exist.

### Truth against provability

Gödel's first theorem replaces "true" by "provable" in the liar, and the result is a sentence $G$ that says "$G$ is not provable".
That sentence causes no contradiction, because provability, unlike truth, is definable: $\mathrm{Prov}_T(x)$ is a $\Sigma_1$ formula.
Tarski's theorem explains the difference.
For a theory $T$ with computable axioms whose theorems are all true, the set of theorems is definable and the set of truths is not, so the two sets differ, and some true sentence is unprovable in $T$.
This gives a short proof of a form of [[the first incompleteness theorem|X9WYNYE29C]] for sound theories.

### Why each hypothesis is needed

The theorem is about truth for all sentences at once.
For each $n$, the set of true $\Sigma_n$ sentences is definable in $\mathcal{N}$ by a [[partial truth predicate|Y2MF1EZAM7]].
The liar built from a $\Sigma_n$ truth predicate is not itself a $\Sigma_n$ sentence, so it escapes the predicate.

The theorem forbids a definition in the language of $\mathcal{N}$ itself.
In [[ZFC|0HE5WDQ9FJ]], truth in $\mathcal{N}$ is definable by recursion on formulas.

The syntactic form needs consistency, because an inconsistent $T$ proves every biconditional $\mathrm{Tr}(\ulcorner \varphi \urcorner) \leftrightarrow \varphi$.

### What it gives you

The set of codes of true sentences is not arithmetical: it is not $\Sigma_n$ for any $n$ in the [[arithmetical hierarchy|7CVJCQKY41]].
So [[true arithmetic|DX0KPMH4QZ]] is far from decidable, and it [[has no decidable axiom set|69TTX21TRJ]].
The theorem also shows that a computable numbering cannot sort sentences by their truth value, as [[coding sentences by their truth value|Y4VRPDEV6K]] shows.

### The converse

The converse "every set that is not definable in $\mathcal{N}$ is the set of true sentences" is false.
There are uncountably many subsets of $\mathbb{N}$ and only countably many formulas, so most subsets are not definable.
Truth in $\mathcal{N}$ becomes definable in a stronger language, such as second-order arithmetic or set theory.

### Generalizations

The semantic proof works in every model $M$ of $\mathsf{Q}$: no formula defines in $M$ the set of codes of sentences true in $M$.
A [[Tarskian hierarchy|Z6MCGB0ZFX]] of languages, each with a truth predicate for the one below it, avoids the paradox.
Axiomatic theories of truth add a new predicate symbol with restricted axioms, and they study which restrictions are consistent.

### Watch out

Do not state the theorem as "truth cannot be defined".
Truth for arithmetic is definable, in set theory, and truth for each level $\Sigma_n$ is definable in arithmetic.
What fails is one formula of arithmetic that defines truth for every sentence of arithmetic.

### Try it

Is the set of codes of true $\Delta_0$ sentences definable in $\mathcal{N}$?
Yes: it is decidable, and every decidable set is defined in $\mathcal{N}$ by the formula that represents it in $\mathsf{Q}$.

Why does the argument not show that provability in $\mathsf{PA}$ is undefinable?
The diagonal sentence for $\neg \mathrm{Prov}_{\mathsf{PA}}(x)$ is the Gödel sentence, and it is simply true and unprovable, with no contradiction.

## History

Tarski proved the theorem in his 1933 monograph on the concept of truth in the languages of the deductive sciences, written in Polish, and a German version appeared in 1936.
Gödel found the result in 1930, while working on the incompleteness theorems.
He described it in a 1931 letter to von Neumann, but did not publish it.

## Explanations

### L1 human

Arithmetic can talk about its own sentences, because every sentence has a code number.
Suppose some formula could pick out exactly the codes of the true sentences.
Then arithmetic could build a sentence that says "I am not true", and that sentence would be true exactly when it is false.
So no formula of arithmetic can pick out the true sentences, even though arithmetic can pick out the provable ones.

### L2 human

We run the argument on a supposed truth formula $\mathrm{True}(x)$.
The diagonal lemma gives a sentence $\lambda$ with
$$\mathsf{Q} \vdash \lambda \leftrightarrow \neg \mathrm{True}(\ulcorner \lambda \urcorner).$$
The model $\mathcal{N}$ satisfies $\mathsf{Q}$, so the biconditional is true in $\mathcal{N}$.
By the assumption on $\mathrm{True}$, the right side is true exactly when $\lambda$ is false.
So $\lambda$ is true exactly when $\lambda$ is false, which is impossible.
The typical use is to separate truth from provability: provability is definable by a $\Sigma_1$ formula, truth is not definable at all.
Watch out: the argument is about one language at a time, and truth for arithmetic is definable in set theory.

### L3 human

The theorem says that a structure cannot define its own satisfaction relation for all formulas, while it can for formulas of bounded complexity.
It is the semantic counterpart of the [[first incompleteness theorem|X9WYNYE29C]], and both are diagonal arguments of the same shape as [[Lawvere's fixed point theorem|N84M16W19X]].
In the arithmetical hierarchy, truth for $\Sigma_n$ sentences is $\Sigma_n$-complete, and full truth lies above every level.
The [[liar paradox|KBYY281V8T]], the [[Berry paradox|MYP4A5VRBA]] and Chaitin's form of incompleteness are other faces of the same limit.
