---
tag: BXVNEN55MR
kind: statement
role: theorem
name: Gödel-McKinsey-Tarski translation
msc: ["03B45", "03B20"]
topics: [SPQVNPZDTB]
audience: research
uses: [Q11N8X99FK, C3RZY20ETK, NGHWZ9Y7ZV, EZ011FT3GT]
about: [Q11N8X99FK, C3RZY20ETK]
proofs: [6BAQBFVMBR]
history:
  first_stated: "Gödel, 1933, Eine Interpretation des intuitionistischen Aussagenkalküls"
  notes: "Gödel stated the embedding and its soundness; McKinsey and Tarski proved faithfulness in 1948."
sources:
  - url: https://en.wikipedia.org/wiki/Modal_companion
    locator: Gödel–McKinsey–Tarski translation
  - url: https://en.wikipedia.org/wiki/Modal_companion
    locator: Modal companions
  - url: https://en.wikipedia.org/wiki/Interior_algebra
    locator: Modal logic
---

## Statement

The law of excluded middle $p \vee \neg p$ translates to the modal formula $\square p \vee \square \neg \square p$.
That formula fails in $\mathsf{S4}$, at the point $w$ of the two-point model $w \leq v$ with $p$ true only at $v$.
This matches the fact that intuitionistic logic does not prove $p \vee \neg p$, and the theorem says that the match is exact.

Formulas of [[intuitionistic propositional logic|Q11N8X99FK]] $\mathsf{IPC}$ are built from variables and $\bot$ with $\wedge$, $\vee$ and $\to$.
We write $\neg A$ for $A \to \bot$.
The *Gödel-McKinsey-Tarski translation* $T$ sends them to [[modal formulas|C3RZY20ETK]]:

- $T(p) = \square p$ and $T(\bot) = \bot$;
- $T(A \wedge B) = T(A) \wedge T(B)$ and $T(A \vee B) = T(A) \vee T(B)$;
- $T(A \to B) = \square(T(A) \to T(B))$.

**Theorem.** For every intuitionistic formula $A$, the following equivalence holds.

$$\mathsf{IPC} \vdash A \iff \mathsf{S4} \vdash T(A).$$

The direction from left to right is *soundness* of the translation, and the direction from right to left is *faithfulness*.
The proof is in [[the proof of the Gödel-McKinsey-Tarski theorem|6BAQBFVMBR]].

## Remarks

### Reading the translation

Intuitionistic truth is truth that persists: once a statement holds at a stage, it holds at every later stage.
In a model of $\mathsf{S4}$, the formula $\square \varphi$ says that $\varphi$ holds now and at every later point.
So the translation puts a box exactly where the intuitionistic clauses quantify over later stages, at variables and at implications.
Conjunction, disjunction and $\bot$ are read pointwise in both semantics and need no box.
For negation this gives $T(\neg A) = \square(T(A) \to \bot)$, which is $\square \neg T(A)$.

### Why each box and why S4

The box on variables is needed for soundness.
Without it, the axiom $p \to (q \to p)$ becomes $\square(p \to \square(q \to p))$.
That formula fails at $w$ in the $\mathsf{S4}$ model $w \leq v$ with $p$ true only at $w$ and $q$ true at $v$.

The box on implications is needed for faithfulness.
Without it, $p \vee \neg p$ becomes $\square p \vee \neg \square p$, a tautology, though $\mathsf{IPC}$ does not prove $p \vee \neg p$.

The logic $\mathsf{S4}$ cannot be weakened to $\mathsf{T}$, since the translation of $p \to (q \to p)$ needs the axiom $\square p \to \square \square p$.
It cannot be strengthened to $\mathsf{S5}$ either.
The axiom $\neg \square p \to \square \neg \square p$ of $\mathsf{S5}$ is equivalent to $\square p \vee \square \neg \square p$, which is $T(p \vee \neg p)$.

### What it gives you

The translation is computed in linear time.
So a decision procedure for $\mathsf{S4}$ decides $\mathsf{IPC}$, and the PSPACE upper bound for $\mathsf{S4}$ holds for $\mathsf{IPC}$ as well.
Every semantics for $\mathsf{S4}$ also gives one for $\mathsf{IPC}$.
Preorders give intuitionistic Kripke models, topological spaces give the open-set semantics, and interior algebras give Heyting algebras of open elements.

### Not every modal formula is a translation

Every translation is stable: $\mathsf{S4} \vdash T(A) \to \square T(A)$, by the lemma in the proof.
The formula $p \to \square p$ is not a theorem of $\mathsf{S4}$.
So the modal formula $p$ is not equivalent in $\mathsf{S4}$ to any $T(A)$, and the translation is not onto, even up to equivalence.

### Modal companions

A normal extension $M$ of $\mathsf{S4}$ is a *modal companion* of a superintuitionistic logic $L$ when $L$ is the set of formulas $A$ with $M \vdash T(A)$.
Every such $L$ has a least companion $\tau L$, which is $\mathsf{S4}$ plus the axioms $T(A)$ for $A \in L$.
It has a greatest companion $\sigma L$, which is $\mathsf{Grz}$ plus the same axioms.
Its companions form the interval $[\tau L, \sigma L]$ of the [[lattice of normal modal logics|EZ011FT3GT]].
For example, $\mathsf{S4}$, $\mathsf{S4.2}$, $\mathsf{S4.3}$ and $\mathsf{S5}$ are the least companions of $\mathsf{IPC}$, $\mathsf{KC}$, $\mathsf{LC}$ and classical logic.
The greatest companion of $\mathsf{IPC}$ is $\mathsf{Grz}$, and the map $\sigma$ is the subject of the [[Blok-Esakia theorem|BB9TA5Q9PN]].
The translation also extends to predicate logic, with $T(\forall x\, A) = \square \forall x\, T(A)$.

### Watch out

The translation of $\neg A$ is $\square \neg T(A)$, not $\neg T(A)$.
The second reading turns $p \vee \neg p$ into a tautology again.
Also, the intuitionistic countermodel must have up-set valuations, while the modal model may have any valuation.
Faithfulness only needs the first kind, so the two semantics agree on the models that matter.

### Try it

1. Compute $T(\neg \neg p)$.
2. Refute $T(((p \to q) \to p) \to p)$, the translation of Peirce's law, in $\mathsf{S4}$.
3. Show that $\mathsf{S5}$ proves $T(p \vee \neg p)$.

Answers.
For 1, $T(\neg p) = \square \neg \square p$, so $T(\neg \neg p) = \square \neg \square \neg \square p$.
For 2, the translation is $\square(\square(\square(\square p \to \square q) \to \square p) \to \square p)$.
Take $w \leq v$ with $p$ true only at $v$ and $q$ false everywhere.
At $v$, $\square p$ is true and $\square q$ false, so $\square(\square p \to \square q)$ is false at $v$ and at $w$.
So $\square(\square p \to \square q) \to \square p$ is true at both points, and its box is true at $w$, while $\square p$ is false at $w$.
For 3, the $\mathsf{S5}$ axiom $\neg \square p \to \square \neg \square p$ gives $\square p \vee \square \neg \square p$ directly.

## History

Kurt Gödel defined the translation in 1933, in "Eine Interpretation des intuitionistischen Aussagenkalküls".
He read $\square$ as provability, stated soundness, and conjectured faithfulness.
McKinsey and Tarski proved faithfulness in 1948, in "Some theorems about the sentential calculi of Lewis and Heyting", with their algebraic and topological methods.
The theory of modal companions grew in the 1970s, in work of Maksimova and Rybakov, Blok, and Esakia.

## Explanations

### L1 human

Intuitionistic logic accepts a statement only when there is a proof of it.
The modal logic $\mathsf{S4}$ has a word "necessarily" that can be read as "it is proved".
The translation puts "necessarily" in front of each basic statement and each "if ... then".
Then intuitionistic logic becomes a part of $\mathsf{S4}$.
A law is intuitionistically valid exactly when its translation is a law of $\mathsf{S4}$.

### L2 human

We translate $p \to \neg \neg p$, which $\mathsf{IPC}$ proves.
Since $T(\neg \neg p) = \square \neg \square \neg \square p$, the translation is $\square(\square p \to \square \neg \square \neg \square p)$.
Axiom T gives $\square \neg \square p \to \neg \square p$, so $\square p \to \neg \square \neg \square p$.
Boxing both sides and using $\square p \to \square \square p$ gives $\square p \to \square \neg \square \neg \square p$, and necessitation finishes the proof.

Now translate $\neg \neg p \to p$, which $\mathsf{IPC}$ does not prove.
The result is $\square(\square \neg \square \neg \square p \to \square p)$.
In the model $w \leq v$ with $p$ true only at $v$, the point $v$ satisfies $\square p$, so both points satisfy $\lozenge \square p$.
So $\square \neg \square \neg \square p$ holds at $w$, while $\square p$ fails at $w$, and the translation fails.

### L3 human

Algebraically, the open elements $a = \square a$ of an interior algebra form a Heyting algebra, and every Heyting algebra arises in this way.
The translation is the syntactic form of this construction.
Through it, the lattice of superintuitionistic logics maps into $\mathrm{NExt}(\mathsf{S4})$ by $\tau$ and $\sigma$.
By the Blok-Esakia theorem, $\sigma$ is an isomorphism onto $\mathrm{NExt}(\mathsf{Grz})$.
The same idea, a box that marks stable or provable truth, reappears in Artemov's logic of proofs, which realizes $\mathsf{S4}$ by explicit proof terms.
