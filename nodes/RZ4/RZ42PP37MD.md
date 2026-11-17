---
tag: RZ42PP37MD
kind: statement
role: theorem
name: Robinson arithmetic is essentially undecidable
aliases: [essential-undecidability-of-q, essential-undecidability-of-robinson-arithmetic]
msc: ["03B25", "03F30", "03D35"]
topics: [E4AVTNWE9E]
audience: grad
about: [3K1AKGXF8A, 9JDDFN8PT7]
uses: [3K1AKGXF8A, 9JDDFN8PT7, HWC687ES0Q, VM8TQ70CVJ, PPGD5KW8JC]
history:
  first_stated: "1953"
  notes: Proved by Alfred Tarski, Andrzej Mostowski and Raphael Robinson in the book Undecidable Theories (1953).
sources:
  - url: https://en.wikipedia.org/wiki/Robinson_arithmetic
    locator: lead section
  - url: https://builds.openlogicproject.org/
    locator: Undecidability
  - book: isbn:9780521701464
---

## Statement

Let $L_A = \set{0, S, +, \cdot}$ be the signature of arithmetic, and let $\mathsf{Q}$ be [[Robinson arithmetic|3K1AKGXF8A]], the theory in $L_A$ axiomatized by its seven axioms.
Let $T$ be a [[consistent|VM8TQ70CVJ]] theory in $L_A$ with $\mathsf{Q} \subseteq T$.
Then $T$ is not a [[decidable theory|HWC687ES0Q]].
In other words, $\mathsf{Q}$ is [[essentially undecidable|9JDDFN8PT7]].

## Remarks

### Why each hypothesis is needed

- Consistency is needed. The inconsistent theory, the set of all $L_A$-sentences, contains $\mathsf{Q}$ and is decidable.
- The axioms of $\mathsf{Q}$ are needed. The theory of the one-element structure, with $S$, $+$ and $\cdot$ all constant, is consistent and decidable, and it does not contain axiom 1, $S x \ne 0$.
- The signature matters only through the axioms: a theory in a larger signature that contains $\mathsf{Q}$ is undecidable as well, since its $L_A$-part is a consistent extension of $\mathsf{Q}$.

### Consequences

1. True arithmetic $\operatorname{Th}(\N, 0, S, +, \cdot)$ is undecidable, and so is [[Peano arithmetic|EYKECP4YKP]].
2. $\mathsf{Q}$ has no consistent complete axiomatizable extension. This is the Gödel-Rosser incompleteness theorem for $\mathsf{Q}$, by the theorem on [[complete axiomatizable theories|HZ7A7B2ERA]].
3. Since $\mathsf{Q}$ is finitely axiomatized, the set of valid $L_A$-sentences is undecidable. This is [[Church's theorem|VA6BNNY2YC]] for the signature of arithmetic.
4. By the [[transfer theorem|FMB2C20G8W]], every theory that interprets $\mathsf{Q}$ is essentially undecidable.

### Converse

The converse fails: an undecidable theory need not contain $\mathsf{Q}$.
The empty theory in a signature with one binary relation symbol is undecidable, by Church's theorem, and it contains no arithmetic.

### Generalizations

- The same proof works for every consistent theory in which all computable relations are representable, for example Robinson's theory $\mathsf{R}$.
- The theorems of $\mathsf{Q}$ and the sentences refutable in $\mathsf{Q}$ form two computably inseparable sets.

## History

Tarski, Mostowski and Robinson proved the theorem in their book Undecidable Theories of 1953.
Raphael Robinson had introduced the theory $\mathsf{Q}$ in 1950 as a finitely axiomatized theory in which all computable functions are representable.
The diagonal argument goes back to Gödel's incompleteness proof of 1931 and to Church's and Turing's undecidability proofs of 1936.

## Explanations

### L1 human

Imagine a computer that, for every statement about whole numbers with plus and times, decides whether it follows from some list of rules.
The list contains seven basic facts about counting, and it contains no contradiction.
The theorem says that such a computer cannot exist, whatever extra rules the list contains.
The proof feeds the computer a statement that talks about the computer's own answers, in the way of the liar paradox.

### L2 human

We follow the diagonal argument on a toy scale.

1. Number all formulas with one free variable as $\varphi_0, \varphi_1, \varphi_2, \ldots$.
2. Suppose a decision procedure for $T$ exists. Then the set $D$ of $n$ with $\varphi_n(\bar{n}) \notin T$ is computable.
3. By representability, some formula $\varphi_d$ is proved by $\mathsf{Q}$ at exactly the numerals of members of $D$, and refuted at the others.
4. If $d \in D$, then $T$ proves $\varphi_d(\bar{d})$, so $d \notin D$. If $d \notin D$, then $T$ proves both $\varphi_d(\bar{d})$ and its negation.
5. Both cases are impossible, so no decision procedure exists.

The typical use is as the starting point of undecidability proofs by interpretation.
A trap is to forget the role of consistency: it is used only in the second case of step 4.

### L3 human

The theorem shows that undecidability already lives in a very weak, finitely axiomatized theory that has no induction at all.
The heavy part is the representability of computable relations in $\mathsf{Q}$, which belongs to the theory of incompleteness; the diagonal step itself is short.
Through interpretations, $\mathsf{Q}$ is the common source of the undecidability of arithmetic, of the theory of rings and of the theory of fields.
