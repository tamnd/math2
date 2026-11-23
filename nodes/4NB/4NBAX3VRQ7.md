---
tag: 4NBAX3VRQ7
kind: concept
name: Consistency statement
aliases: [con-t, arithmetized-consistency]
msc: ["03F40", "03F30"]
topics: [HXHHWY3328]
audience: grad
uses: [NB2BCZR40F, VM8TQ70CVJ, 92SWXST1ZM, 3K1AKGXF8A, MPSCREYC3M]
sources:
  - url: https://en.wikipedia.org/wiki/Gödel's_incompleteness_theorems
    locator: Second incompleteness theorem
  - book: isbn:9780521857840
  - book: isbn:9780521701464
---

## Summary

The consistency statement of a theory is the sentence of arithmetic that says "no number codes a proof of $0 = 1$ in this theory".
It turns the claim "$T$ is consistent" into a claim about numbers, which $T$ itself can then try to prove.
For a theory $T$ with provability predicate $\mathrm{Prov}_T$ it is the sentence
$$\mathrm{Con}(T) := \neg \mathrm{Prov}_T(\ulcorner 0 = S0 \urcorner).$$
It is true in $\mathbb{N}$ exactly when $T$ is [[consistent|VM8TQ70CVJ]].
When the axioms of $T$ are given by a $\Sigma_1$ formula, $\mathrm{Con}(T)$ is a $\Pi_1$ sentence, and it depends on that formula and not only on the set of axioms.

## Motivation

Hilbert wanted proofs that the axiom systems of mathematics do not lead to a contradiction.
At first this is a claim about proofs, not about numbers.
With [[Gödel numbering|MFJXPAF0R0]], proofs become numbers and the relation "$y$ codes a proof of $x$" becomes a formula, so the claim becomes a sentence of arithmetic.
Then one can ask which theories prove it.

[[Gödel's second incompleteness theorem|4PZM5GJTR5]] answers the question for the theory itself: a consistent $T$ that contains $\mathsf{PA}$ does not prove $\mathrm{Con}(T)$.
Stronger theories can prove it, so consistency statements measure strength: $S$ is stronger than $T$ when $S \vdash \mathrm{Con}(T)$.
They return in the [[reflection principles|NB485KFXKV]] and in the [[Turing and Feferman progressions|F7Z4BV2KHD]], which add consistency statements again and again.

## Notation

Let the axioms of $T$ be defined in $\mathbb{N}$ by a formula $\alpha(x)$, usually $\Sigma_1$.
The [[provability predicate|NB2BCZR40F]] $\mathrm{Prov}_\alpha(x) = \exists y \, \mathrm{Prf}_\alpha(y, x)$ is built from $\alpha$, and $\mathrm{Con}_\alpha := \neg \mathrm{Prov}_\alpha(\ulcorner 0 = S0 \urcorner)$.
For the standard formula one writes $\mathrm{Con}(T)$ or $\mathrm{Con}_T$.
Some books use $\neg \mathrm{Prov}_T(\ulcorner \bot \urcorner)$ for a fixed refutable sentence $\bot$, and these choices are provably equivalent in $\mathsf{PA}$.
The notation $\mathrm{Con}(T)$ hides $\alpha$, and that is the trap: two formulas for the same axioms can give consistency statements with different provability.

## Remarks

### A first consistency statement

Take $T = \mathsf{PA}$ and its standard axiom formula.
The formula $\mathrm{Prf}_{\mathsf{PA}}(y, x)$ is $\Sigma_1$, of the form $\exists z \, \delta(y, x, z)$ with $\delta$ bounded.
So we can rewrite the consistency statement as
$$\mathrm{Con}(\mathsf{PA}) \equiv \forall y \, \forall z \, \neg \delta(y, \ulcorner 0 = S0 \urcorner, z),$$
which is $\Pi_1$.
For each pair of numbers $m$ and $n$, the instance $\neg \delta(\underline{m}, \ulcorner 0 = S0 \urcorner, \underline{n})$ is a true bounded sentence, so $\mathsf{PA}$ proves it.
Only the universal sentence escapes $\mathsf{PA}$, as [[the example on Con(PA)|23M4TSTPN8]] works out.

### Stronger theories can prove it

[[ZFC proves Con(PA)|1KSQAD4BWM]]: it builds the set $\omega$, checks that all axioms of $\mathsf{PA}$ hold there, and applies soundness.
So the second theorem does not say that consistency statements are unprovable in general.
It says that a theory does not prove its own.
For example, $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$ proves $\mathrm{Con}(\mathsf{PA})$ in one line, but if it is consistent, it does not prove $\mathrm{Con}(\mathsf{PA} + \mathrm{Con}(\mathsf{PA}))$.

### Two formulas for the same axioms

The [[Rosser provability predicate|Z0H1KA8ZHT]] gives the Rosser consistency statement $\neg \mathrm{Prov}^{R}_T(\ulcorner 0 = S0 \urcorner)$.
When $T$ is consistent it is true, yet $T$ proves it, so it is not a consistency statement in the sense of the second theorem.

Feferman's formula goes further and changes only the axiom formula.
Let $\alpha^*(x)$ say "$\alpha(x)$, and the axioms with codes at most $x$ form a consistent set".
Since $\mathsf{PA}$ is consistent, $\alpha^*$ defines exactly the axioms of $\mathsf{PA}$ in $\mathbb{N}$.
Still $\mathsf{PA} \vdash \mathrm{Con}_{\alpha^*}$, and $\alpha^*$ is $\Pi_1$, not $\Sigma_1$.
So the consistency statement belongs to a presentation of the theory, not to its set of axioms.

### The rules you can use

If $\alpha$ is $\Sigma_1$, then $\mathrm{Prov}_\alpha$ is $\Sigma_1$, so $\mathrm{Con}_\alpha$ is $\Pi_1$.
If $\alpha$ defines the axioms of $T$ in $\mathbb{N}$, then $\mathrm{Con}_\alpha$ is true exactly when $T$ is consistent, because $\mathrm{Prf}_\alpha$ defines the real proof relation.
$\mathsf{PA}$ proves that $\mathrm{Con}(T)$ is equivalent to "no sentence is provable together with its negation" and to "some sentence is not provable", by formalizing the usual proofs of these equivalences.
If $T$ is $\Sigma_1$-sound, then $T \nvdash \neg \mathrm{Con}(T)$, because $\neg \mathrm{Con}(T)$ is a false $\Sigma_1$ sentence.
Over $\mathsf{PA}$, $\mathrm{Con}(T)$ is equivalent to reflection for $\Pi_1$ sentences, as [[this example|JHGJ6APMRF]] shows.

### Finite consistency statements

The sentence $\mathrm{Con}_n(T)$ says that no proof of $0 = S0$ has code at most $n$.
If $T$ is consistent, $\mathsf{Q}$ proves each $\mathrm{Con}_n(T)$ by checking the finitely many candidates.
For each $k \le n$ it refutes $\mathrm{Prf}_T(\underline{k}, \ulcorner 0 = S0 \urcorner)$, because $\mathrm{Prf}_T$ represents a decidable relation, and $\mathsf{Q}$ proves that every $y \le \underline{n}$ is one of $\underline{0}, \ldots, \underline{n}$.
Pudlák studied how the length of the shortest proof of $\mathrm{Con}_n(T)$ in $T$ grows with $n$.
The theory $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ proves every $\mathrm{Con}_n(\mathsf{PA})$ together with $\neg \mathrm{Con}(\mathsf{PA})$, and it is [[consistent but ω-inconsistent|FK06QR6A44]].

### History

Gödel stated the second incompleteness theorem for the arithmetized consistency statement in his 1931 paper.
Feferman showed in 1960, in "Arithmetization of metamathematics in a general setting", that the theorem depends on the formula that defines the axioms, and he gave the formula $\alpha^*$.

### Watch out

Do not read $\mathrm{Con}(T)$ as a property of the set of axioms alone.
Feferman's $\alpha^*$ and the standard $\alpha$ define the same set, and only the second gives an unprovable consistency statement.
Do not read "$T \nvdash \mathrm{Con}(T)$" as doubt about $T$ either: $\mathrm{Con}(\mathsf{PA})$ is true and provable in $\mathsf{ZFC}$.

### Try it

Is $\mathrm{Con}_{100}(\mathsf{PA})$ provable in $\mathsf{PA}$?
Yes: $\mathsf{PA}$ is consistent, so $\mathsf{Q}$ already proves it by the 101 checks for $k = 0, \ldots, 100$ described above, and $\mathsf{PA}$ contains $\mathsf{Q}$.

Does $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$ prove its own consistency statement?
Not if it is consistent, because it is a theory with a $\Sigma_1$ axiom formula that contains $\mathsf{PA}$, and the second theorem applies.

## Explanations

### L1 human

Write every proof from some axioms as a number, the way a computer stores a file.
Then "the axioms never prove $0 = 1$" becomes a statement about numbers: no number is the code of a proof of $0 = 1$.
This statement is the consistency statement of the axioms.
You can check it for the numbers $0$, $1$, $2$ and so on, one at a time, but Gödel showed that the axioms themselves cannot prove it for all numbers at once.

### L2 human

We build $\mathrm{Con}(T)$ in three steps.
First fix a formula $\alpha(x)$ for "$x$ is the code of an axiom".
Then build $\mathrm{Prf}_\alpha(y, x)$, "$y$ codes a finite list of formulas, each an axiom, a logical axiom or the result of a rule, whose last entry has code $x$".
Last, put
$$\mathrm{Con}_\alpha := \neg \exists y \, \mathrm{Prf}_\alpha(y, \ulcorner 0 = S0 \urcorner).$$
The typical use is as a measure of strength, because $S$ is stronger than $T$ when $S \vdash \mathrm{Con}(T)$.
Watch out: with an unusual $\alpha$, such as Feferman's $\alpha^*$, the consistency statement can be provable, so the choice of $\alpha$ is a part of the statement.

### L3 human

Consistency statements order theories by consistency strength.
Natural theories, from fragments of arithmetic to set theory with large cardinals, are observed to fall into a linear order in this way, although no general reason for this is known.
Over $\mathsf{PA}$, $\mathrm{Con}(T)$ is the weakest of the [[reflection principles|NB485KFXKV]]: it is the $\Pi_1$ part of the claim that $T$ is sound.
Ordinal analysis, which began with [[Gentzen's consistency proof|QPV0HNP22S]], proves consistency statements by induction along ordinal notations.
