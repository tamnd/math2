---
tag: DH9RQ61GVD
kind: statement
role: theorem
name: Rosser's theorem
aliases: [godel-rosser-theorem]
msc: ["03F40", "03F30"]
topics: [HXHHWY3328]
audience: grad
uses: [3K1AKGXF8A, 92SWXST1ZM, TN9G24VABN, VM8TQ70CVJ, 3PRW76471J, NB2BCZR40F, Z0H1KA8ZHT, 319P85G2C1]
about: [92SWXST1ZM, 319P85G2C1]
history:
  first_stated: "Rosser, 1936, Extensions of some theorems of Gödel and Church"
sources:
  - url: https://en.wikipedia.org/wiki/Rosser%27s_trick
    locator: lead section
  - book: isbn:9780521857840
  - book: isbn:9780521701464
---

## Statement

Let $T$ be a [[consistent|VM8TQ70CVJ]] [[first-order theory|92SWXST1ZM]] in the language $\set{0, S, +, \cdot}$.
Assume that $T$ contains [[Robinson arithmetic|3K1AKGXF8A]] $\mathsf{Q}$ and that the set of theorems of $T$ is [[computably enumerable|TN9G24VABN]].
Let $\mathrm{Prov}^{R}_T$ be the [[Rosser provability predicate|Z0H1KA8ZHT]] of $T$.
By the [[diagonal lemma|3PRW76471J]], there is a sentence $R_T$, a Rosser sentence of $T$, with $\mathsf{Q} \vdash R_T \leftrightarrow \neg \mathrm{Prov}^{R}_T(\ulcorner R_T \urcorner)$.

Then $T \nvdash R_T$ and $T \nvdash \neg R_T$.
So $T$ is not [[negation complete|319P85G2C1]].

In short: every consistent theory with a computably enumerable set of theorems that contains $\mathsf{Q}$ is incomplete.
The proof is in [[the proof of Rosser's theorem|CZZAA0WXS3]].

## Remarks

### Why each hypothesis is needed

1. Consistency: an inconsistent theory proves every sentence, so it is negation complete.
2. Containing $\mathsf{Q}$: [[Presburger arithmetic|4W0E9G7PPV]] is consistent, computably axiomatized and complete.
3. Computable enumerability: true arithmetic contains $\mathsf{Q}$, is consistent and is complete.

### Consequences

1. Part 3 of [[Gödel's first incompleteness theorem|X9WYNYE29C]] follows: $\omega$-consistency is not needed for incompleteness.
2. $\mathsf{Q}$ is essentially incomplete: every consistent c.e. extension of $\mathsf{Q}$ in the same language is incomplete. The proof uses no induction axiom.
3. $R_T$ is true in $\N$. No number codes a proof of $R_T$, so $\neg \mathrm{Prov}^{R}_T(\ulcorner R_T \urcorner)$ holds in $\N$, and $\N$ is a model of $\mathsf{Q}$.
4. The theory $T + \neg R_T$ is consistent, although it proves a false sentence.

### Converse

The converse "every incomplete theory contains $\mathsf{Q}$" is false, as for the first theorem: the empty theory in the language $\set{0, S, +, \cdot}$ is incomplete.

### Generalizations

1. The result holds for every consistent c.e. theory that interprets $\mathsf{Q}$, such as $\mathsf{ZFC}$.
2. The sets of codes of theorems and of refutable sentences of $\mathsf{Q}$ are disjoint c.e. sets that no decidable set separates. This gives the undecidability of every consistent extension of $\mathsf{Q}$.
3. Rosser sentences depend on the order of proofs in the coding. Guaspari and Solovay showed that different Rosser sentences of $\mathsf{PA}$ need not be provably equivalent.

## History

Gödel proved incompleteness in 1931 under the hypothesis of $\omega$-consistency.
Rosser proved in 1936, in the paper "Extensions of some theorems of Gödel and Church", that consistency is enough.
His device of comparing a proof with a shorter proof of the negation is called Rosser's trick.

## Explanations

### L1 human

Gödel's sentence says "I am not provable".
Rosser's sentence says "if I am provable, then my negation has a shorter proof".
If the theory proved the sentence, it could check the short proofs one by one and refute the sentence.
If it proved the negation, it could check that no shorter proof of the sentence exists, and prove the sentence.
Either way the theory would contradict itself, so a consistent theory proves neither.

### L2 human

1. Order proofs by their codes, and compare the first proof of $R_T$ with the first proof of $\neg R_T$.
2. $R_T$ says: every proof of $R_T$ is preceded by a proof of $\neg R_T$.
3. A proof of $R_T$ with code $p$ makes $T$ check the finitely many codes $\le p$ and refute $R_T$.
4. A proof of $\neg R_T$ with code $q$ makes $T$ prove $R_T$: below $q$ there is no proof of $R_T$, and above $q$ the proof $q$ comes first.

The typical use is to get incompleteness from consistency alone, for example for $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$.
A trap: the Rosser predicate does not satisfy all derivability conditions, so the proof of the second theorem does not carry over to it.

### L3 human

The trick turns a test of one proof into a race between two searches, a proof of $R_T$ and a proof of $\neg R_T$.
The same pattern proves that the theorems and the refutable sentences of $\mathsf{Q}$ are effectively inseparable c.e. sets.
In [[provability logic|WJK0YA4GP2]], Rosser sentences are studied in an extension of $\mathsf{GL}$ with a relation for the order of proofs.
