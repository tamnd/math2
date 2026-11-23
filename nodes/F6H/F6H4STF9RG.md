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

The derivability conditions say that a strong enough theory knows three basic facts about its own provability predicate: theorems are provable, provability is closed under modus ponens, and provable things are provably provable.

Let $T$ be a theory in the language of arithmetic that contains [[first-order Peano arithmetic|MPSCREYC3M]] $\mathsf{PA}$.
Let the axioms of $T$ be given by a $\Sigma_1$ formula $\mathrm{Ax}_T(x)$ that defines a decidable set in $\mathbb{N}$.
Let $\mathrm{Prov}_T(x) := \exists y \, \mathrm{Prf}_T(y, x)$ be the standard [[provability predicate|NB2BCZR40F]] built from $\mathrm{Ax}_T$ by [[arithmetization of syntax|6M12VR1GT6]].
For a sentence $\varphi$, write $\square \varphi$ for $\mathrm{Prov}_T(\ulcorner \varphi \urcorner)$.
Then for all sentences $\varphi$ and $\psi$ the following hold.

1. (D1) If $T \vdash \varphi$, then $T \vdash \square \varphi$.
2. (D2) $T \vdash \square (\varphi \to \psi) \to (\square \varphi \to \square \psi)$.
3. (D3) $T \vdash \square \varphi \to \square \square \varphi$.

In addition, $T$ proves formalized $\Sigma_1$-completeness: $T \vdash \sigma \to \square \sigma$ for every $\Sigma_1$ sentence $\sigma$.
D3 is the case $\sigma = \square \varphi$.

## Remarks

### A first run of the three conditions

$\mathsf{PA}$ proves $0 + 0 = 0$.
D1 turns this into $\mathsf{PA} \vdash \square (0 + 0 = 0)$, and [[Robinson arithmetic proves that 0 + 0 = 0 is provable|SVMC76P884]] carries out exactly this step.
D3 then gives $\mathsf{PA} \vdash \square \square (0 + 0 = 0)$: $\mathsf{PA}$ proves that it can prove that it proves $0 + 0 = 0$.
D2 lets us chain such facts.
From $\square (0 + 0 = 0 \to 0 = 0 + 0)$ and $\square (0 + 0 = 0)$, it gives $\square (0 = 0 + 0)$.
These are small steps, but they are all that the proofs of the [[second incompleteness theorem|4PZM5GJTR5]] and [[Löb's theorem|3HD30YG3DG]] need about provability.

### Why the predicate must be standard

The conditions are about one formula, not about the set of theorems.
The [[Rosser provability predicate|Z0H1KA8ZHT]] defines the same set in $\mathbb{N}$ when $T$ is consistent, and it satisfies D1.
But $T$ proves the consistency statement built from it.
So it must fail D2 or D3, since the three conditions together give the second theorem.

### Why the axiom formula must be $\Sigma_1$

Feferman built a $\Pi_1$ formula $\alpha^*$ that defines the axioms of $\mathsf{PA}$ in $\mathbb{N}$, and for which $\mathsf{PA}$ proves the consistency statement $\mathrm{Con}_{\alpha^*}$.
The predicate built from $\alpha^*$ fails D3, because D1 to D3 would give the second theorem for it.
The proof of D3 below needs $\square \varphi$ to be $\Sigma_1$, and with $\alpha^*$ it is not.

### Why the theory needs induction

D1 holds already in $\mathsf{Q}$, by the same proof.
The proofs of D2 and D3 are inductions on the length of proofs and on the build of $\Sigma_1$ formulas, and they do not work in $\mathsf{Q}$, which has no induction axioms.
The conditions hold in $\mathsf{I}\Sigma_1$, and even in elementary arithmetic, with the same outline.

### Watch out: D1 is a rule

D1 says "if $T$ proves $\varphi$, then $T$ proves $\square \varphi$".
It does not say $T \vdash \varphi \to \square \varphi$, and that implication can fail.
Let $G$ be the sentence with $\mathsf{PA} \vdash G \leftrightarrow \neg \square G$ from the [[diagonal lemma|3PRW76471J]].
If $\mathsf{PA} \vdash G \to \square G$, then $\mathsf{PA} \vdash G \to \bot$, so $\mathsf{PA} \vdash \neg G$, which is equivalent to $\square G$.
Then $\mathsf{PA}$ proves a false $\Sigma_1$ sentence, because $G$ is not provable, and this is impossible for a theory that is true in $\mathbb{N}$.

### The converse of D1

The converse, "if $T \vdash \square \varphi$ then $T \vdash \varphi$", is false in general.
The theory $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ proves $\square (0 = S0)$ for the predicate of $\mathsf{PA}$, and it does not prove $0 = S0$, since it is consistent.
The converse holds when $T$ is $\Sigma_1$-sound, because then $\square \varphi$ is true in $\mathbb{N}$, so $\varphi$ has a real proof.

### The modal reading

Read $\square$ as a modal operator.
D1 is the necessitation rule, D2 is the axiom K, and D3 is the axiom 4 of modal logic.
Add the formalized Löb theorem $\square (\square \varphi \to \varphi) \to \square \varphi$, and the result is the modal logic GL of [[provability logic|WJK0YA4GP2]].
A version with a free variable also holds: $T \vdash \forall x \, (\square \varphi(\dot{x}) \to \square \square \varphi(\dot{x}))$, where $\dot{x}$ is the numeral of $x$.
The conditions also hold for theories in other languages that interpret $\mathsf{PA}$, such as $\mathsf{ZFC}$, through the interpretation.

### Try it

Derive $\square \varphi \wedge \square \psi \to \square (\varphi \wedge \psi)$ from D1 and D2.
Apply D1 to the tautology $\varphi \to (\psi \to \varphi \wedge \psi)$, then use D2 twice.

## History

Hilbert and Bernays proved the second incompleteness theorem in detail in the second volume of their Grundlagen der Mathematik, published in 1939.
They isolated the conditions on the provability predicate that the proof needs, in a more complex form.
Löb stated the three conditions in their present form in 1955, in the paper where he proved [[Löb's theorem|3HD30YG3DG]].

## Explanations

### L1 human

The derivability conditions are three simple rules about the formula "this statement is provable".
First, if a statement has a proof, the theory can prove that it has a proof.
Second, the theory knows that modus ponens works for provable statements.
Third, if something is provable, the theory can prove that it is provably provable.
For example, from a proof of $0 + 0 = 0$ the theory gets "$0 + 0 = 0$ is provable", and from that it gets "it is provable that $0 + 0 = 0$ is provable".

### L2 human

Here is how the conditions combine.
Suppose $T \vdash \varphi \to \psi$ and $T \vdash \varphi$.
D1 gives $T \vdash \square (\varphi \to \psi)$ and $T \vdash \square \varphi$.
D2 and modus ponens then give $T \vdash \square \psi$, and D3 gives $T \vdash \square \square \psi$.
In the proof of the second theorem the same moves run on the Gödel sentence $G$: D1 and D2 turn $G \to \neg \square G$ into $\square G \to \square \neg \square G$, and D3 supplies $\square G \to \square \square G$.
Together these give $\square G \to \square \bot$, which is the key step.

### L3 human

The conditions abstract from the details of arithmetization.
Any formula that satisfies them, together with a fixed point lemma, gives the second theorem and Löb's theorem.
Solovay's completeness theorem shows that GL is exactly the modal logic of the standard predicate of $\mathsf{PA}$.
In type theory, the "later" modality of guarded recursion obeys similar laws, and Löb's rule becomes a rule for recursive definitions.
