---
tag: X9WYNYE29C
kind: statement
role: theorem
name: Gödel's first incompleteness theorem
aliases: [godels-incompleteness-theorems]
msc: ["03F40", "03F30"]
topics: [HXHHWY3328]
audience: grad
uses: [3K1AKGXF8A, 0QFT7Z76N5, MFJXPAF0R0, 92SWXST1ZM, DKFGQTRYZE, TN9G24VABN, 655K8Y7VS8, 3PRW76471J, NB2BCZR40F, 4S29X1GTV4, 319P85G2C1]
about: [92SWXST1ZM, 655K8Y7VS8, 319P85G2C1]
history:
  first_stated: "Gödel, 1931, Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I"
  notes: "Gödel announced the result at a conference in Königsberg in 1930. Rosser removed the hypothesis of ω-consistency in 1936."
sources:
  - url: https://en.wikipedia.org/wiki/Gödel's_incompleteness_theorems
    locator: First incompleteness theorem
  - book: isbn:9780521857840
  - book: isbn:9780521701464
  - url: https://builds.openlogicproject.org/
    locator: "Part: Incompleteness"
same_as:
  wikidata: Q200787
  wikipedia: Gödel's incompleteness theorems
---

## Statement

Suppose Peano arithmetic is consistent, and let $G$ be a sentence that says "$G$ is not provable in $\mathsf{PA}$".
If $\mathsf{PA}$ proved $G$, it would also prove "$G$ is provable", which is $\neg G$, and it would be inconsistent.
So $G$ has no proof in $\mathsf{PA}$, and that is exactly what $G$ says, so $G$ is true.
The first incompleteness theorem turns this argument into mathematics.

Let $T$ be a [[first-order theory|92SWXST1ZM]] in the language $\{0, S, +, \cdot\}$ with two properties.
First, $T$ contains [[Robinson arithmetic|3K1AKGXF8A]] $\mathsf{Q}$, meaning that every axiom of $\mathsf{Q}$ is a theorem of $T$.
Second, the set of theorems of $T$ is [[computably enumerable|TN9G24VABN]], or equivalently $T$ has a decidable set of axioms.

Let $\mathrm{Prov}_T$ be the standard [[provability predicate|NB2BCZR40F]] of $T$ for a fixed [[Gödel numbering|MFJXPAF0R0]].
By the [[diagonal lemma|3PRW76471J]], there is a [[sentence|DKFGQTRYZE]] $G_T$, the Gödel sentence of $T$, with $\mathsf{Q} \vdash G_T \leftrightarrow \neg \mathrm{Prov}_T(\ulcorner G_T \urcorner)$.

1. If $T$ is consistent, then $T \nvdash G_T$.
   Also $G_T$ is $\mathsf{Q}$-equivalent to a $\Pi_1$ sentence, and $G_T$ is true in $\mathbb{N}$.
2. If $T$ is [[ω-consistent|4S29X1GTV4]], or only $1$-consistent, then also $T \nvdash \neg G_T$, so $T$ is not [[negation complete|319P85G2C1]].
3. If $T$ is only consistent, $T$ is still not negation complete, by [[Rosser's theorem|DH9RQ61GVD]].

In one line: no consistent theory that contains $\mathsf{Q}$ and has a computably enumerable set of theorems decides every sentence of arithmetic.

## Remarks

### Why $G_T$ is true

The truth of $G_T$ is not part of what $T$ proves.
It is an argument made outside $T$, and it uses the consistency of $T$ as a premise.
The sentence $\neg \mathrm{Prov}_T(\ulcorner G_T \urcorner)$ says that no number codes a proof of $G_T$.
Part 1 shows that no number does, so this sentence is true in $\mathbb{N}$, and $G_T$ is true because $\mathsf{Q}$ proves the two equivalent and $\mathbb{N}$ is a model of $\mathsf{Q}$.

$G_T$ is a $\Pi_1$ sentence: "for every $y$, $y$ does not code a proof of $G_T$", where checking one $y$ is a computation.
So the unprovable sentence has the simplest form a sentence can take beyond a bare calculation.
Every false $\Pi_1$ sentence has a counterexample, and $\mathsf{Q}$ refutes it, so a consistent $T \supseteq \mathsf{Q}$ never proves a false $\Pi_1$ sentence.

### Why each hypothesis is needed

Without "contains $\mathsf{Q}$" the theorem fails.
[[Presburger arithmetic|4W0E9G7PPV]], in the language $\{0, S, +\}$, is consistent, computably axiomatized and complete, and so is the theory of [[real closed fields|DDY3Q3PJ6W]].

Without "computably enumerable" it fails too.
True arithmetic, the set of all sentences true in $\mathbb{N}$, contains $\mathsf{Q}$, is consistent and is complete.
It [[has no decidable axiom set|69TTX21TRJ]].

Without consistency it fails, since an inconsistent theory proves every sentence.

Part 2 needs more than consistency.
The theory $T := \mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ is [[consistent but ω-inconsistent|FK06QR6A44]], and it proves $\neg \mathrm{Con}(T)$.
Since $T \vdash G_T \leftrightarrow \mathrm{Con}(T)$, by the proof of the second theorem, $T \vdash \neg G_T$.
Rosser's sentence avoids this problem.

### What the theorem does not say

The theorem is about one theory at a time.
Each $G_T$ is unprovable in $T$, and $T + G_T$ proves it at once.
No sentence is shown to be unprovable in every theory, and no truth is shown to be unknowable.
The theorem also does not say that mathematics is incomplete.
It says that each consistent, computably axiomatized theory containing $\mathsf{Q}$ leaves some arithmetic sentence undecided.

### Consequences

Every consistent computably enumerable extension of $\mathsf{Q}$ is incomplete.
This covers $\mathsf{PA}$, $\mathsf{ZFC}$ through its arithmetic, and all their consistent computably axiomatized extensions.

Every consistent extension of $\mathsf{Q}$ is undecidable, by a refinement of the same argument.
Since $\mathsf{Q}$ has finitely many axioms, this gives [[Church's theorem|VA6BNNY2YC]] that first-order validity is undecidable.

When the proof of part 1 is carried out inside $T \supseteq \mathsf{PA}$, it gives [[Gödel's second incompleteness theorem|4PZM5GJTR5]].
True arithmetic has no computable axiomatization, and [[arithmetical truth is not definable|YRV6SYK2BY]] in arithmetic at all.

### The converse

Is every incomplete theory an extension of $\mathsf{Q}$?
No: the empty theory in the language $\{0, S, +, \cdot\}$ proves neither $0 = S0$ nor its negation.
Incompleteness also does not imply that $T$ is computably enumerable or consistent.

The [[completeness theorem|WQ1ZE255SF]] gives the right reading.
$T \nvdash \varphi$ exactly when $T + \neg \varphi$ has a model.
So incompleteness means that $T$ has models that disagree on some sentence, here $\mathbb{N}$ and a [[non-standard model|1QWN5CV4CG]] of $T + \neg G_T$.

### Generalizations

The theorem holds for every consistent computably axiomatized theory in any language that interprets $\mathsf{Q}$, for example $\mathsf{ZFC}$ and second-order arithmetic.
The undecided sentence can be chosen of the form "this Diophantine equation has no solution", by the theorem of Matiyasevich, Robinson, Davis and Putnam.
[[Kolmogorov complexity|8PY3K6NCKF]] gives Chaitin's form: for a constant $c$ depending on $T$, $T$ proves no sentence "$C(\underline{x}) > \underline{c}$", although all but finitely many $x$ satisfy it.
Natural sentences independent of $\mathsf{PA}$ include [[Goodstein's theorem|XQMNJF241J]] and the [[Paris-Harrington theorem|509ZWA0R26]].

There are three proofs: [[Gödel's diagonal proof|XYHTQH2TGB]], [[the proof by the halting problem|ZR9D1N70KY]] and [[Chaitin's proof by Kolmogorov complexity|77EMTE7X9V]].

### Try it

Let $T := \mathsf{PA} + G_{\mathsf{PA}}$.
Does $T$ prove its own Gödel sentence $G_T$?
No: $T$ is consistent, since $\mathbb{N}$ is a model of it, so part 1 applies to $T$.
Adding $G_{\mathsf{PA}}$ settles one sentence and creates a new undecided one.

## History

Gödel announced the theorem at a conference in Königsberg in September 1930.
He published it in 1931 in the paper "Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I", with $\omega$-consistency as the hypothesis of part 2.
Rosser proved in 1936 that consistency alone is enough, with a modified sentence.
The proof by the halting problem rests on Turing's analysis of computation from 1936, and Chaitin gave the proof by Kolmogorov complexity in 1974.

## Explanations

### L1 human

Choose any list of axioms for whole-number arithmetic that a computer can check and that never proves a falsehood.
Then some statement about whole numbers is true but has no proof from these axioms.
The statement can even be of a simple kind: "this equation has no solution in whole numbers".
Adding the statement as a new axiom does not help, because the new list has its own unprovable statement.
So no single checkable list of true axioms proves every true statement of arithmetic.

### L2 human

We run the argument for $T = \mathsf{PA}$, using that $\mathbb{N}$ is a model of $\mathsf{PA}$.
First build $G$ with $\mathsf{Q} \vdash G \leftrightarrow \neg \mathrm{Prov}_{\mathsf{PA}}(\ulcorner G \urcorner)$.
If $\mathsf{PA} \vdash G$, a proof with some code $p$ exists, and $\mathsf{Q}$ checks it, so $\mathsf{PA} \vdash \mathrm{Prov}_{\mathsf{PA}}(\ulcorner G \urcorner)$.
Then $\mathsf{PA} \vdash \neg G$, and $\mathsf{PA}$ would be inconsistent.
So $\mathsf{PA} \nvdash G$, and $G$, which says "$G$ is not provable", is true.
If $\mathsf{PA} \vdash \neg G$, then $\mathsf{PA}$ proves $\mathrm{Prov}_{\mathsf{PA}}(\ulcorner G \urcorner)$, which is false, and that cannot happen because $\mathsf{PA}$ is true in $\mathbb{N}$.
Watch out: "$G_T$ is true" uses the consistency of $T$, which is a premise from outside $T$.

### L3 human

Read through computability, the theorem says that the theorems of $T$ and the sentences that $T$ refutes form two disjoint computably enumerable sets that no decidable set separates.
This is why every consistent extension of $\mathsf{Q}$ is undecidable, and not only incomplete.
For a theory that is true in $\mathbb{N}$, the theorems form a computably enumerable set of truths, while the set of all truths is not even arithmetically definable.
The proof is a diagonal argument, the same pattern as Cantor's theorem, the halting problem and [[Lawvere's fixed point theorem|N84M16W19X]].
It leads on to the independence of natural statements, to [[provability logic|WJK0YA4GP2]] and to the ordinal analysis of theories.
