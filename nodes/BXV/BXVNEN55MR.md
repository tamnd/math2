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

Formulas of [[intuitionistic propositional logic|Q11N8X99FK]] $\mathsf{IPC}$ are built from variables and $\bot$ with $\wedge$, $\vee$ and $\to$, and $\neg A$ abbreviates $A \to \bot$.
The *Gödel-McKinsey-Tarski translation* $T$ sends them to [[modal formulas|C3RZY20ETK]]:

- $T(p) = \square p$ and $T(\bot) = \bot$;
- $T(A \wedge B) = T(A) \wedge T(B)$ and $T(A \vee B) = T(A) \vee T(B)$;
- $T(A \to B) = \square(T(A) \to T(B))$.

**Theorem.** For every intuitionistic formula $A$,
$$\mathsf{IPC} \vdash A \iff \mathsf{S4} \vdash T(A).$$

The direction from left to right is *soundness* of the translation, and the direction from right to left is *faithfulness*.
The proof is in [[the proof of the Gödel-McKinsey-Tarski theorem|6BAQBFVMBR]].

## Remarks

### Why each hypothesis is needed

1. The box on variables is needed for soundness. Without it, the axiom $p \to (q \to p)$ becomes $\square(p \to \square(q \to p))$, which fails in the $\mathsf{S4}$ model $w \leq v$ with $p$ true only at $w$ and $q$ true at $v$.
2. The box on implications is needed for faithfulness. Without it, $p \vee \neg p$ becomes $\square p \vee \neg \square p$, a tautology, though $\mathsf{IPC} \nvdash p \vee \neg p$.
3. $\mathsf{S4}$ cannot be weakened to $\mathsf{T}$, since soundness uses $\square p \to \square \square p$. It cannot be strengthened to $\mathsf{S5}$, since $\mathsf{S5} \vdash \square p \vee \square \neg \square p$, which is $T(p \vee \neg p)$.

### Consequences

1. Decidability of $\mathsf{S4}$ gives decidability of $\mathsf{IPC}$, and complexity bounds transfer along $T$.
2. Every model of $\mathsf{S4}$ gives a model of $\mathsf{IPC}$: topological spaces give the open-set semantics, preorders give Kripke semantics, and interior algebras give Heyting algebras of open elements.
3. Intuitionistic implication is read as "necessarily, if ... then ...", and intuitionistic truth as "provably true" or "stably true".

### Converse

The theorem is an equivalence, so both directions hold.
The translation is not onto, even up to equivalence.
Every translation satisfies $\mathsf{S4} \vdash T(A) \to \square T(A)$, by the lemma in the proof.
So the formula $p$ is not equivalent in $\mathsf{S4}$ to any $T(A)$.

### Generalizations

1. A normal extension $M$ of $\mathsf{S4}$ is a *modal companion* of a superintuitionistic logic $L$ if $L = \set{A : M \vdash T(A)}$.
2. Every superintuitionistic logic $L$ has a least modal companion $\tau L = \mathsf{S4} \oplus \set{T(A) : A \in L}$ and a greatest one $\sigma L = \mathsf{Grz} \oplus \set{T(A) : A \in L}$, and its modal companions form the interval $[\tau L, \sigma L]$ of the [[lattice of normal modal logics|EZ011FT3GT]].
3. For example, $\mathsf{S4}$, $\mathsf{S4.2}$, $\mathsf{S4.3}$ and $\mathsf{S5}$ are the least modal companions of $\mathsf{IPC}$, $\mathsf{KC}$, $\mathsf{LC}$ and classical logic, and $\mathsf{Grz}$ is the greatest companion of $\mathsf{IPC}$; see the [[Blok-Esakia theorem|BB9TA5Q9PN]].
4. The translation extends to intuitionistic predicate logic and quantified $\mathsf{S4}$, with $T(\forall x A) = \square \forall x \, T(A)$.

## History

Kurt Gödel defined the translation in 1933, in "Eine Interpretation des intuitionistischen Aussagenkalküls", reading $\square$ as provability, and proved soundness.
He conjectured faithfulness.
McKinsey and Tarski proved faithfulness in 1948, in "Some theorems about the sentential calculi of Lewis and Heyting", using their algebraic and topological methods.
The theory of modal companions was developed in the 1970s, by Esakia, Blok, Maksimova, Rybakov and others.

## Explanations

### L1 human

Intuitionistic logic accepts a statement only when there is a proof of it.
Modal logic $\mathsf{S4}$ has a word "necessarily" that can be read as "it is proved".
The translation puts "necessarily" in front of each basic statement and each "if ... then", and then intuitionistic logic becomes a part of $\mathsf{S4}$.
A law is intuitionistically valid exactly when its translation is a law of $\mathsf{S4}$.

### L2 human

1. Translate $p \to \neg \neg p$. First $T(\neg p) = \square(\square p \to \bot) = \square \neg \square p$.
2. Then $T(\neg \neg p) = \square \neg \square \neg \square p$, and $T(p \to \neg \neg p) = \square(\square p \to \square \neg \square \neg \square p)$.
3. In $\mathsf{S4}$, $\square p \to \square \square p$ and $\square \square p \to \square \neg \square \neg \square p$, since $\square p \to \neg \square \neg \square p$ by reflexivity. So the translation is a theorem, as $\mathsf{IPC} \vdash p \to \neg \neg p$.
4. Translate $\neg \neg p \to p$. The result is $\square(\square \neg \square \neg \square p \to \square p)$, which fails in the model $w \leq v$ with $p$ true only at $v$. This matches $\mathsf{IPC} \nvdash \neg \neg p \to p$.

The typical use is to transfer results between intuitionistic and modal logics.
A trap: the translation of $\neg A$ is $\square \neg T(A)$, not $\neg T(A)$.

### L3 human

Algebraically, the open elements $\set{a : \square a = a}$ of an interior algebra form a Heyting algebra, and every Heyting algebra arises in this way; the translation is the syntactic form of this construction.
Through it, the lattice of superintuitionistic logics maps into $\mathrm{NExt}(\mathsf{S4})$ by $\tau$ and $\sigma$, and the map $\sigma$ is an isomorphism onto $\mathrm{NExt}(\mathsf{Grz})$ by the Blok-Esakia theorem.
The same idea, a modal operator that marks stable or provable truth, underlies the Artemov logic of proofs, where $\mathsf{S4}$ is itself embedded into a logic of explicit proofs.
