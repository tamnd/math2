---
tag: X9WYNYE29C
kind: statement
role: theorem
name: Gödel's first incompleteness theorem
aliases: [godels-incompleteness-theorems]
msc: ["03F40", "03F30"]
topics: [HXHHWY3328]
audience: grad
uses: [3K1AKGXF8A, 0QFT7Z76N5, MFJXPAF0R0, 92SWXST1ZM, DKFGQTRYZE, TN9G24VABN, 655K8Y7VS8, 3PRW76471J, NB2BCZR40F, ~08020cc1, 319P85G2C1]
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

Let $T$ be a [[first-order theory|92SWXST1ZM]] in the language $\set{0, S, +, \cdot}$ with these two properties.

- $T$ contains [[Robinson arithmetic|3K1AKGXF8A]] $\mathsf{Q}$: every axiom of $\mathsf{Q}$ is a theorem of $T$.
- The set of theorems of $T$ is [[computably enumerable|TN9G24VABN]]; equivalently, $T$ has a decidable set of axioms.

Let $\mathrm{Prov}_T$ be the standard [[provability predicate|NB2BCZR40F]] of $T$, for a fixed [[Gödel numbering|MFJXPAF0R0]].
By the [[diagonal lemma|3PRW76471J]], there is a [[sentence|DKFGQTRYZE]] $G_T$, the Gödel sentence of $T$, with $\mathsf{Q} \vdash G_T \leftrightarrow \neg \mathrm{Prov}_T(\ulcorner G_T \urcorner)$.

1. If $T$ is consistent, then $T \nvdash G_T$. Also $G_T$ is $\mathsf{Q}$-equivalent to a $\Pi_1$ sentence, and $G_T$ is true in $\N$.
2. If $T$ is [[ω-consistent|~08020cc1]], or only $1$-consistent, then also $T \nvdash \neg G_T$. So $T$ is not [[negation complete|319P85G2C1]].
3. If $T$ is only consistent, $T$ is still not negation complete, by [[Rosser's theorem|~71fdf6fd]].

In short: no consistent theory with a computably enumerable set of theorems that contains $\mathsf{Q}$ decides every sentence of arithmetic.

## Remarks

### Why each hypothesis is needed

1. Without "contains $\mathsf{Q}$": [[Presburger arithmetic|B66JYY3K58]], in the language $\set{0, S, +}$, is consistent, computably axiomatized and complete. The theory of [[real closed fields|DDY3Q3PJ6W]] is another such theory.
2. Without "computably enumerable": true arithmetic, the set of all sentences true in $\N$, contains $\mathsf{Q}$, is consistent and is complete. It [[has no decidable axiom set|~a7addafc]].
3. Without consistency: the inconsistent theory proves every sentence, so it is negation complete.
4. Part 2 needs more than consistency. The theory $T := \mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ is [[consistent but ω-inconsistent|~0977deea]], and it proves $\neg \mathrm{Con}(T)$. Since $T \vdash G_T \leftrightarrow \mathrm{Con}(T)$ by the proof of the second theorem, $T \vdash \neg G_T$. Rosser's sentence avoids this.

### Consequences

1. Every consistent c.e. extension of $\mathsf{Q}$ is incomplete; in particular $\mathsf{PA}$, $\mathsf{ZFC}$ through its arithmetic, and their c.e. extensions are incomplete.
2. If $T$ is $\Sigma_1$-sound, some true $\Pi_1$ sentence is not provable in $T$. The sentence $G_T$ is one.
3. Every consistent extension of $\mathsf{Q}$ is undecidable, by a refinement of the same argument. Since $\mathsf{Q}$ has finitely many axioms, this gives [[Church's theorem|VA6BNNY2YC]] on the undecidability of first-order validity.
4. The proof of part 1 can be formalized in $T \supseteq \mathsf{PA}$, which gives [[Gödel's second incompleteness theorem|~c79a35b5]].
5. True arithmetic is not computably axiomatizable, and [[arithmetical truth is not definable|YRV6SYK2BY]].

### Converse

The converse "every incomplete theory contains $\mathsf{Q}$" is false: the empty theory in the language $\set{0, S, +, \cdot}$ is incomplete, since it proves neither $0 = S0$ nor its negation.
Also, incompleteness of $T$ does not imply that $T$ is computably enumerable or consistent.
A partial converse is the [[completeness theorem|WQ1ZE255SF]] view: $T \nvdash \varphi$ exactly when $T + \neg \varphi$ has a model, so incompleteness means that $T$ has models that disagree on some sentence, here $\N$ and a [[non-standard model|1QWN5CV4CG]].

### Generalizations

1. The theorem holds for every consistent c.e. theory in any language that interprets $\mathsf{Q}$, for example $\mathsf{ZFC}$ and second-order arithmetic.
2. The unprovable sentence can be chosen of the form "a Diophantine equation has no solution", by the theorem of Matiyasevich, Robinson, Davis and Putnam.
3. [[Kolmogorov complexity|8PY3K6NCKF]] gives Chaitin's form: for a constant $c$ depending on $T$, $T$ proves no sentence "$C(\underline{x}) > \underline{c}$", although all but finitely many $x$ satisfy it.
4. Natural combinatorial sentences independent of $\mathsf{PA}$ include [[Goodstein's theorem|XQMNJF241J]] and the [[Paris-Harrington theorem|509ZWA0R26]].

Three proofs are given: [[the diagonal proof|~3b604178]] of Gödel, [[the proof by the halting problem|~6463c0bc]] and [[Chaitin's proof by Kolmogorov complexity|~403741ce]].

## History

Gödel announced the theorem at a conference in Königsberg in September 1930.
He published it in 1931 in the paper "Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I", with $\omega$-consistency as the hypothesis of part 2.
Rosser proved in 1936 that consistency alone is enough, with a modified sentence.
The proof by the halting problem uses Turing's analysis of computation of 1936, and Chaitin gave the proof by Kolmogorov complexity in 1974.

## Explanations

### L1 human

Choose any list of axioms for whole-number arithmetic that a computer can check, and that never proves a falsehood.
Then some statement about whole numbers is true but has no proof from these axioms.
The statement can be of a simple kind: "this equation has no solution in whole numbers".
Adding the statement as a new axiom does not help, since the new list has its own unprovable truth.
So arithmetic can never be captured completely by one checkable list of axioms.

### L2 human

1. Fix $T = \mathsf{PA}$ and build $G$ with $\mathsf{Q} \vdash G \leftrightarrow \neg \mathrm{Prov}_{\mathsf{PA}}(\ulcorner G \urcorner)$.
2. If $\mathsf{PA} \vdash G$, a real proof with code $p$ exists, and $\mathsf{PA} \vdash \mathrm{Prov}_{\mathsf{PA}}(\ulcorner G \urcorner)$. With step 1, $\mathsf{PA} \vdash \neg G$, so $\mathsf{PA}$ would be inconsistent.
3. So $\mathsf{PA} \nvdash G$, and $G$, which says "$G$ is not provable", is true.
4. If $\mathsf{PA} \vdash \neg G$, then $\mathsf{PA} \vdash \mathrm{Prov}_{\mathsf{PA}}(\ulcorner G \urcorner)$, a false $\Sigma_1$ sentence by step 3. This cannot happen, since $\mathsf{PA}$ is true in $\N$.

The typical use is to show that a given theory cannot settle every question in its language, and to find candidate independent statements.
A trap: "$G_T$ is true" needs the consistency of $T$, which is an assumption from outside $T$; the theorem itself is a statement about $T$ and gives no true sentence that is unprovable in every theory.

### L3 human

The theorem says that the set of theorems of a consistent c.e. extension of $\mathsf{Q}$ is a computably enumerable set that cannot be all of the true sentences, since truth is not even definable.
In computability terms, the theorems of $T$ and the refutable sentences of $T$ form a pair of disjoint c.e. sets that no decidable set separates, which gives essential undecidability.
The proof is an instance of diagonalization, the same pattern as Cantor's theorem, the halting problem and [[Lawvere's fixed point theorem|N84M16W19X]].
Later sub-areas use it for the independence of natural statements, for [[provability logic|WJK0YA4GP2]] and for the ordinal analysis of theories.
