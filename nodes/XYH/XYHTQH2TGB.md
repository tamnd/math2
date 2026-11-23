---
tag: XYHTQH2TGB
kind: proof
name: Gödel's diagonal proof of the first incompleteness theorem
msc: ["03F40"]
topics: [HXHHWY3328]
audience: grad
proves: X9WYNYE29C
uses: [3PRW76471J, NB2BCZR40F, 6M12VR1GT6, 4S29X1GTV4, 3K1AKGXF8A]
methods: [0J0XBKG64S, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_sketch_for_G%C3%B6del%27s_first_incompleteness_theorem
    locator: lead section
  - book: isbn:9780521857840
  - book: isbn:9780521701464
---

## Proof

The liar sentence "this sentence is false" leads to a paradox.
Replace "false" by "not provable", and the paradox becomes a theorem: the sentence "this sentence is not provable" cannot be proved by a consistent theory.
The proof makes this sentence inside arithmetic and checks both halves.

Let $T$ satisfy the hypotheses of the theorem.
If $T$ is given only by a computably enumerable set of theorems, Craig's trick replaces its axioms by a decidable set with the same theorems.

1. By [[arithmetization of syntax|6M12VR1GT6]], the relation "$y$ codes a proof in $T$ of the formula with code $x$" is decidable.
   Let $\mathrm{Prf}_T(y, x)$ be a $\Sigma_1$ formula that represents it in $\mathsf{Q}$.
2. Let $\mathrm{Prov}_T(x) := \exists y \, \mathrm{Prf}_T(y, x)$, the [[provability predicate|NB2BCZR40F]].
3. Apply the [[diagonal lemma|3PRW76471J]] to $\neg \mathrm{Prov}_T(x)$.
   It gives a sentence $G$ with $\mathsf{Q} \vdash G \leftrightarrow \neg \mathrm{Prov}_T(\ulcorner G \urcorner)$, and $T$ proves the same equivalence since $T \supseteq \mathsf{Q}$.

### Part 1: a consistent $T$ does not prove $G$

4. Assume $T \vdash G$, and let $p$ be the code of a proof of $G$ in $T$.
5. Then $p$ codes a proof of $G$, so $\mathsf{Q} \vdash \mathrm{Prf}_T(\underline{p}, \ulcorner G \urcorner)$ by representability.
6. By the rule for $\exists$, $T \vdash \mathrm{Prov}_T(\ulcorner G \urcorner)$.
7. By step 3, $T \vdash \neg G$, and with step 4, $T$ is inconsistent.
8. So if $T$ is consistent, then $T \nvdash G$, and no number codes a proof of $G$ in $T$.

### $G$ is $\Pi_1$ and true

9. $\mathrm{Prf}_T$ has the form $\exists z \, \delta(y, x, z)$ with $\delta$ in $\Delta_0$.
   So $\neg \mathrm{Prov}_T(\ulcorner G \urcorner)$ is logically equivalent to the $\Pi_1$ sentence $\forall y \, \forall z \, \neg \delta(y, \ulcorner G \urcorner, z)$, and by step 3 $G$ is $\mathsf{Q}$-equivalent to it.
10. $\mathbb{N}$ is a model of $\mathsf{Q}$, and $\mathrm{Prf}_T$ represents the proof relation, so $\mathrm{Prf}_T$ defines the proof relation in $\mathbb{N}$.
11. By steps 8 and 10, $\mathbb{N} \models \neg \mathrm{Prov}_T(\ulcorner G \urcorner)$.
12. The equivalence of step 3 holds in the model $\mathbb{N}$ of $\mathsf{Q}$, so with step 11, $\mathbb{N} \models G$.

### Part 2: an $\omega$-consistent $T$ does not refute $G$

13. Assume that $T$ is [[ω-consistent|4S29X1GTV4]].
    Then $T$ is consistent, so step 8 applies.
14. Assume, for a contradiction, that $T \vdash \neg G$.
    By step 3, $T \vdash \exists y \, \mathrm{Prf}_T(y, \ulcorner G \urcorner)$.
15. Let $n \in \mathbb{N}$.
    By step 8, $n$ does not code a proof of $G$, so $T \vdash \neg \mathrm{Prf}_T(\underline{n}, \ulcorner G \urcorner)$ by representability.
16. Steps 14 and 15 show that $\mathrm{Prf}_T(y, \ulcorner G \urcorner)$ witnesses the $\omega$-inconsistency of $T$, against step 13.
17. If $T$ is only $1$-consistent, step 14 already gives a contradiction, since $\mathrm{Prov}_T(\ulcorner G \urcorner)$ is a $\Sigma_1$ sentence that is false by step 11.
18. So $T \nvdash \neg G$, and with step 8, $T$ is not negation complete.

Part 3 of the statement, incompleteness under consistency alone, is proved in [[Rosser's theorem|DH9RQ61GVD]].

## Idea

The sentence $G$ says "I am not provable in $T$".
If $T$ proved $G$, then $T$ would check the proof and prove "$G$ is provable", which is $\neg G$.
If $T$ proved $\neg G$, it would claim a proof of $G$ that no actual number codes, and $\omega$-consistency forbids such empty existence claims.
So $G$ is undecided, and it is true because it is unprovable.

Watch out: the two halves use different hypotheses.
Part 1 needs only consistency, while part 2 needs $\omega$-consistency, and [[PA + ¬Con(PA)|FK06QR6A44]] shows that consistency is not enough for part 2 with this sentence.

## Variants

Gödel's 1931 proof worked in a type theory based on Principia Mathematica.
It built the self-referential sentence directly for the one formula it needed, without a general diagonal lemma.
[[Rosser's theorem|DH9RQ61GVD]] replaces $\neg \mathrm{Prov}_T$ by the Rosser formula and needs only consistency in part 2.
Other routes avoid explicit self-reference: the [[computability proof|ZR9D1N70KY]] uses the halting problem, and [[Chaitin's proof|77EMTE7X9V]] uses Kolmogorov complexity.
