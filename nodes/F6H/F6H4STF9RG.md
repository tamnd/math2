---
tag: F6H4STF9RG
kind: statement
role: theorem
name: Hilbert-Bernays-Löb derivability conditions
aliases: [hilbert-bernays-derivability-conditions]
msc: ["03F40", "03F45"]
topics: [HXHHWY3328]
audience: grad
about: [NB2BCZR40F]
uses: [NB2BCZR40F, 6M12VR1GT6, 0QFT7Z76N5, MPSCREYC3M]
history:
  first_stated: "Hilbert and Bernays, Grundlagen der Mathematik, volume 2, 1939, in a more complex form"
  notes: "Löb gave the three conditions in their present simple form in his 1955 paper that solved Henkin's problem."
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%E2%80%93Bernays_provability_conditions
    locator: lead section
  - url: https://en.wikipedia.org/wiki/L%C3%B6b%27s_theorem
    locator: lead section
  - book: isbn:9780521857840
---

## Statement

Let $T$ be a theory in the language $\set{0, S, +, \cdot}$ that contains [[first-order Peano arithmetic|MPSCREYC3M]] $\mathsf{PA}$.
Let the axioms of $T$ be given by a $\Sigma_1$ formula $\mathrm{Ax}_T(x)$ that defines a decidable set in $\N$.
Let $\mathrm{Prov}_T(x) := \exists y \, \mathrm{Prf}_T(y, x)$ be the standard [[provability predicate|NB2BCZR40F]] built from $\mathrm{Ax}_T$ by [[arithmetization of syntax|6M12VR1GT6]].
For a sentence $\varphi$, write $\square \varphi$ for $\mathrm{Prov}_T(\ulcorner \varphi \urcorner)$.
Then for all sentences $\varphi$ and $\psi$:

- (D1) if $T \vdash \varphi$, then $T \vdash \square \varphi$;
- (D2) $T \vdash \square (\varphi \to \psi) \to (\square \varphi \to \square \psi)$;
- (D3) $T \vdash \square \varphi \to \square \square \varphi$.

In addition, $T$ proves formalized $\Sigma_1$-completeness: $T \vdash \sigma \to \square \sigma$ for every $\Sigma_1$ sentence $\sigma$.
D3 is the case $\sigma = \square \varphi$.

## Remarks

### Why each hypothesis is needed

1. The predicate must be the standard one. The [[Rosser provability predicate|Z0H1KA8ZHT]] defines the same set in $\N$ and satisfies D1. But $T$ proves its consistency statement, so by the proof of the [[second incompleteness theorem|4PZM5GJTR5]] it fails D2 or D3.
2. The axiom formula must be $\Sigma_1$. Feferman built a $\Pi_1$ formula $\alpha^*$ that defines the axioms of $\mathsf{PA}$ in $\N$, with $\mathsf{PA} \vdash \mathrm{Con}_{\alpha^*}$. For the predicate built from $\alpha^*$, D3 fails, since D1 to D3 would give the second theorem.
3. The theory needs induction. The proofs of D2 and D3 use induction on the length of proofs and on the build of $\Sigma_1$ formulas. These proofs do not work in $\mathsf{Q}$; D1 holds there by the same proof.
4. D1 is a rule, not an implication inside $T$. Let $G$ be a sentence with $\mathsf{PA} \vdash G \leftrightarrow \neg \square G$, from the [[diagonal lemma|3PRW76471J]]. If $\mathsf{PA} \vdash G \to \square G$, then $\mathsf{PA} \vdash \neg G$, which fails because $\mathsf{PA}$ is $\Sigma_1$-sound.

### Consequences

1. The [[second incompleteness theorem|4PZM5GJTR5]] follows from D1 to D3 and the [[diagonal lemma|3PRW76471J]].
2. [[Löb's theorem|3HD30YG3DG]] follows in the same way: if $T \vdash \square \varphi \to \varphi$, then $T \vdash \varphi$.
3. Read $\square$ as a modal operator. Then D1 is the necessitation rule, D2 is the axiom K, and D3 is the axiom 4 of modal logic.
4. Together with the formalized Löb theorem $\square (\square \varphi \to \varphi) \to \square \varphi$, these laws give the modal logic GL of [[provability logic|WJK0YA4GP2]].

### Converse

The converse of D1, "if $T \vdash \square \varphi$ then $T \vdash \varphi$", is false in general.
The theory $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ proves $\square (0 = S0)$ for the predicate of $\mathsf{PA}$, and it does not prove $0 = S0$, since it is consistent.
The converse holds when $T$ is $\Sigma_1$-sound, because then $\square \varphi$ is true in $\N$, so $\varphi$ has a real proof.

### Generalizations

1. The three conditions hold already for theories that contain $\mathsf{I}\Sigma_1$, and for some weaker theories, such as elementary arithmetic, with the same outline of proof.
2. They hold for theories in other languages that interpret enough arithmetic, such as $\mathsf{ZFC}$, through the interpretation.
3. A parametrized form holds: $T \vdash \forall x \, (\square \varphi(\dot{x}) \to \square \square \varphi(\dot{x}))$, where $\square \varphi(\dot{x})$ is the provability of $\varphi$ applied to the numeral of $x$.

## History

Hilbert and Bernays proved the second incompleteness theorem in detail in the second volume of their Grundlagen der Mathematik, published in 1939.
They isolated conditions on the provability predicate that the proof needs, in a more complex form.
Löb stated the three conditions in their present form in 1955, in the paper where he proved [[Löb's theorem|3HD30YG3DG]].

## Explanations

### L1 human

The derivability conditions are three simple rules about the formula "this statement is provable".
First: if a statement has a proof, the theory can prove that it has a proof.
Second: the theory knows that modus ponens works for provable statements.
Third: if something is provable, the theory can prove that it is provably provable.
For example, from a proof of $0 + 0 = 0$ the theory gets "$0 + 0 = 0$ is provable", and from that it gets "it is provable that $0 + 0 = 0$ is provable".

### L2 human

1. Suppose $T \vdash \varphi \to \psi$ and $T \vdash \varphi$.
2. D1 gives $T \vdash \square (\varphi \to \psi)$ and $T \vdash \square \varphi$.
3. D2 and modus ponens give $T \vdash \square \psi$.
4. D3 gives $T \vdash \square \square \psi$.

The typical use is the short proof of the second incompleteness theorem, which uses only D1 to D3 and the diagonal lemma.
A trap: D1 says "if $T$ proves $\varphi$, then $T$ proves $\square \varphi$", not "$T$ proves $\varphi \to \square \varphi$".

### L3 human

The conditions abstract from the details of arithmetization: any formula that satisfies them, together with a fixed point lemma, gives the second theorem and Löb's theorem.
In modal terms, a provability predicate with D1 to D3 makes $T$ a model of the logic K4, and the diagonal lemma adds the Löb axiom.
Solovay's completeness theorem shows that GL is exactly the modal logic of the standard predicate of $\mathsf{PA}$.
In type theory, the "later" modality of guarded recursion satisfies the same laws, and Löb's rule becomes a rule for recursive definitions.
