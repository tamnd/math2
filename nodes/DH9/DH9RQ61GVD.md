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

The theory $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ is consistent, and it refutes its own Gödel sentence.
So Gödel's sentence is not undecided in every consistent theory, and Gödel's proof needed $\omega$-consistency for a real reason.
Rosser changed the sentence to "if I am provable, then my negation has an earlier proof", and this sentence is undecided in every consistent theory of this kind.

Let $T$ be a [[consistent|VM8TQ70CVJ]] [[first-order theory|92SWXST1ZM]] in the language $\{0, S, +, \cdot\}$.
Assume that $T$ contains [[Robinson arithmetic|3K1AKGXF8A]] $\mathsf{Q}$ and that the set of theorems of $T$ is [[computably enumerable|TN9G24VABN]].
Let $\mathrm{Prov}^{R}_T$ be the [[Rosser provability predicate|Z0H1KA8ZHT]] of $T$.
By the [[diagonal lemma|3PRW76471J]], there is a sentence $R_T$, a Rosser sentence of $T$, with $\mathsf{Q} \vdash R_T \leftrightarrow \neg \mathrm{Prov}^{R}_T(\ulcorner R_T \urcorner)$.

Then $T \nvdash R_T$ and $T \nvdash \neg R_T$, so $T$ is not [[negation complete|319P85G2C1]].

In one line: every consistent theory that contains $\mathsf{Q}$ and has a computably enumerable set of theorems is incomplete.
The proof is in [[the proof of Rosser's theorem|CZZAA0WXS3]].

## Remarks

### Why each hypothesis is needed

An inconsistent theory proves every sentence, so it is negation complete.
[[Presburger arithmetic|4W0E9G7PPV]] does not contain $\mathsf{Q}$, and it is consistent, computably axiomatized and complete.
True arithmetic contains $\mathsf{Q}$ and is consistent and complete, but its theorems are not computably enumerable.

### Consequences

Part 3 of [[Gödel's first incompleteness theorem|X9WYNYE29C]] follows, so $\omega$-consistency is not needed for incompleteness.

$\mathsf{Q}$ is essentially incomplete: every consistent computably axiomatized extension of $\mathsf{Q}$ in the same language is incomplete.
The proof uses no induction axiom.

$R_T$ is true in $\mathbb{N}$.
No number codes a proof of $R_T$, so $\neg \mathrm{Prov}^{R}_T(\ulcorner R_T \urcorner)$ holds in $\mathbb{N}$, and $\mathbb{N}$ is a model of $\mathsf{Q}$.
So $T + \neg R_T$ is a consistent theory that proves a false sentence.

### Watch out

The Rosser predicate defines the same set as the standard one in $\mathbb{N}$, but it is a different formula.
It fails one of the [[derivability conditions|F6H4STF9RG]], so the proof of the second incompleteness theorem does not carry over to it.
Indeed $T$ proves the Rosser form of its own consistency, as [[the Rosser predicate example|Z0H1KA8ZHT]] shows.

### The converse

Is every incomplete theory an extension of $\mathsf{Q}$?
No, as for the first theorem: the empty theory in the language $\{0, S, +, \cdot\}$ is incomplete.

### Generalizations

The result holds for every consistent computably axiomatized theory that interprets $\mathsf{Q}$, such as $\mathsf{ZFC}$.
The theorems of $\mathsf{Q}$ and the sentences that $\mathsf{Q}$ refutes form two disjoint computably enumerable sets that no decidable set separates.
This gives the undecidability of every consistent extension of $\mathsf{Q}$.
Rosser sentences depend on how proofs are ordered in the coding, and Guaspari and Solovay showed that different Rosser sentences of $\mathsf{PA}$ need not be provably equivalent.

### Try it

Let $T := \mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$.
Does $T$ decide its Rosser sentence $R_T$?
No: $T$ is consistent, and Rosser's theorem needs nothing more.

## History

Gödel proved incompleteness in 1931 under the hypothesis of $\omega$-consistency.
Rosser proved in 1936, in the paper "Extensions of some theorems of Gödel and Church", that consistency is enough.
His device of comparing a proof with an earlier proof of the negation is called Rosser's trick.

## Explanations

### L1 human

Gödel's sentence says "I am not provable".
Rosser's sentence says "if I am provable, then my negation has an earlier proof".
If the theory proved the sentence, it could check the finitely many earlier proofs one by one and refute the sentence.
If it proved the negation, it could check that no earlier proof of the sentence exists, and prove the sentence.
Either way the theory would contradict itself, so a consistent theory proves neither.

### L2 human

Order proofs by their codes, and compare the first proof of $R_T$ with the first proof of $\neg R_T$.
$R_T$ says that every proof of $R_T$ is preceded by a proof of $\neg R_T$.
A proof of $R_T$ with code $p$ lets $T$ check the finitely many codes up to $p$ and refute $R_T$.
A proof of $\neg R_T$ with code $q$ lets $T$ prove $R_T$, since below $q$ there is no proof of $R_T$ and above $q$ the proof $q$ comes first.
Each case needs only finite checks on actual numbers, which is why plain consistency suffices.
Watch out: the checks need $\mathsf{Q}$ to prove that every $y$ is either at most $\underline{q}$ or at least $\underline{q}$, which is fact Q-b in the proof.

### L3 human

The trick turns a test of one proof into a race between two searches, one for a proof of $R_T$ and one for a proof of $\neg R_T$.
The same pattern proves that the theorems and the refutable sentences of $\mathsf{Q}$ are effectively inseparable computably enumerable sets.
In [[provability logic|WJK0YA4GP2]], Rosser sentences are studied in an extension of $\mathsf{GL}$ with a relation for the order of proofs.
