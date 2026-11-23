---
tag: 6BAQBFVMBR
kind: proof
name: Proof of the Gödel-McKinsey-Tarski theorem
msc: ["03B45", "03B20"]
topics: [SPQVNPZDTB]
audience: research
proves: BXVNEN55MR
uses: [Q11N8X99FK, NGHWZ9Y7ZV, G989VP2NGP, 0VABYWJWH9]
methods: [0NTF6DMVAP, 12MQ2NJ29A, 0BB5TPGQ1N]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_companion
    locator: Gödel–McKinsey–Tarski translation
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Semantics of intuitionistic logic
---

## Proof

Take the model $w \leq v$ with $p$ true only at $v$.
As an intuitionistic model it refutes $p \vee \neg p$ at $w$, and as a modal model it refutes $T(p \vee \neg p) = \square p \vee \square \neg \square p$ at the same point.
Part B shows that this always happens, and Part A checks the axioms one by one.

### Setup

We write $a, b, c$ for $T(A), T(B), T(C)$.
We use the Hilbert system for $\mathsf{IPC}$ with modus ponens and these axiom schemes:

- (I1) $A \to (B \to A)$, and (I2) $(A \to (B \to C)) \to ((A \to B) \to (A \to C))$;
- (I3) $A \wedge B \to A$, (I4) $A \wedge B \to B$, and (I5) $A \to (B \to A \wedge B)$;
- (I6) $A \to A \vee B$, (I7) $B \to A \vee B$, and (I8) $(A \to C) \to ((B \to C) \to (A \vee B \to C))$;
- (I9) $\bot \to A$.

In $\mathsf{S4}$ we use the axioms K, T: $\square p \to p$ and 4: $\square p \to \square \square p$, with [[necessitation|G989VP2NGP]].
We also use the derived rule (Mon): from $\vdash X \to Y$ infer $\vdash \square X \to \square Y$.
Two results are cited without proof.
(C1) is completeness of $\mathsf{IPC}$ for intuitionistic Kripke models.
(C2) is soundness of $\mathsf{S4}$ for reflexive and transitive frames.

### Part A: soundness

We show that if $\mathsf{IPC} \vdash A$, then $\mathsf{S4} \vdash T(A)$.

1. Lemma: $\mathsf{S4} \vdash a \to \square a$ for every $A$.
   We argue by induction on $A$.
   For $p$ this is axiom 4, and for $\bot$ it is a tautology.
2. For $\wedge$, the hypotheses give $b \wedge c \to \square b \wedge \square c$, and $\square b \wedge \square c \to \square(b \wedge c)$ holds in every normal logic.
3. For $\vee$, use $b \to \square b$ and $\square b \to \square(b \vee c)$, which holds by (Mon), and the same for $c$.
   For $\to$, the translation $\square(b \to c)$ is boxed, and axiom 4 applies.
4. (I3), (I4), (I6), (I7) and (I9) translate to $\square X$ with $X$ a tautology, such as $\square(a \wedge b \to a)$.
   Necessitation proves them.
5. (I1) translates to $\square(a \to \square(b \to a))$.
   Step 1 gives $a \to \square a$, and (Mon) on the tautology $a \to (b \to a)$ gives $\square a \to \square(b \to a)$.
   Chain the two and apply necessitation.
6. (I5) translates to $\square(a \to \square(b \to a \wedge b))$.
   As in step 5, use $a \to \square a$ and (Mon) on $a \to (b \to a \wedge b)$.

### Part A, continued: the axioms I2 and I8, and modus ponens

7. For (I2), let $X = \square(a \to \square(b \to c))$.
   The translation is $\square(X \to \square(\square(a \to b) \to \square(a \to c)))$.
8. By K, $X \wedge \square(a \to b) \to \square((a \to \square(b \to c)) \wedge (a \to b))$.
   With axiom T, the formula $(a \to \square(b \to c)) \wedge (a \to b) \to (a \to c)$ is a theorem.
   So (Mon) gives $X \wedge \square(a \to b) \to \square(a \to c)$.
9. So $\vdash X \to (\square(a \to b) \to \square(a \to c))$, and (Mon) boxes the consequent.
   With $X \to \square X$ from axiom 4 and necessitation, the translation of (I2) is a theorem.
10. For (I8), let $Y = \square(a \to c)$ and $Z = \square(b \to c)$.
    The translation is $\square(Y \to \square(Z \to \square(a \vee b \to c)))$.
11. By K and the tautology $(a \to c) \wedge (b \to c) \to (a \vee b \to c)$, we get $\vdash Y \wedge Z \to \square(a \vee b \to c)$.
    So $\vdash Y \to (Z \to \square(a \vee b \to c))$.
12. By (Mon) and $Y \to \square Y$ from axiom 4, $\vdash Y \to \square(Z \to \square(a \vee b \to c))$.
    Necessitation gives the translation of (I8).
13. For modus ponens, assume $\mathsf{S4} \vdash a$ and $\mathsf{S4} \vdash \square(a \to b)$.
    Axiom T gives $a \to b$, so $\mathsf{S4} \vdash b$.
14. Since $T$ is compositional, an axiom instance translates to a formula of steps 4 to 12, with $a, b, c$ the translations of its parts.
    By induction on the length of an $\mathsf{IPC}$ derivation, $\mathsf{S4} \vdash T(A)$.

### Part B: faithfulness

We show that if $\mathsf{IPC} \nvdash A$, then $\mathsf{S4} \nvdash T(A)$.

15. By (C1), there are an intuitionistic Kripke model $(W, \leq, U)$ and $w \in W$ with $w \nVdash A$.
    Here $\leq$ is a [[preorder|0VABYWJWH9]], and each $U(p)$ is an up-set.
16. Recall the forcing clauses.
    The point $v$ forces $p$ iff $v \in U(p)$, no point forces $\bot$, and $\wedge$ and $\vee$ are pointwise.
    The point $v$ forces $B \to C$ iff every $u \geq v$ that forces $B$ forces $C$.
17. Read $(W, \leq, U)$ as a modal [[Kripke model|NGHWZ9Y7ZV]] with $V(p) = U(p)$.
    We claim that $v \Vdash B$ iff $v \models T(B)$, for every $B$ and $v$.
18. Case $p$: $v \models \square p$ iff every $u \geq v$ is in $U(p)$.
    Since $U(p)$ is an up-set and $v \geq v$, this holds iff $v \in U(p)$.
19. Cases $\bot$, $\wedge$ and $\vee$: the clauses are the same on both sides, and the induction hypothesis applies.
20. Case $B \to C$: $v \models \square(T(B) \to T(C))$ iff every $u \geq v$ with $u \models T(B)$ has $u \models T(C)$.
    By the induction hypothesis, this is the forcing clause of $B \to C$.
21. So $w \not\models T(A)$ in a model on a reflexive and transitive frame.
    By (C2), $\mathsf{S4} \nvdash T(A)$.

## Idea

Soundness checks that the translation of each intuitionistic axiom is a theorem of $\mathsf{S4}$.
The key fact is that translations are stable, $T(A) \to \square T(A)$, which plays the role of persistence in intuitionistic semantics.
Faithfulness compares two semantics on the same preorder.
Intuitionistic forcing with up-set valuations is exactly modal truth of the translation, so a countermodel for $A$ is a countermodel for $T(A)$.

Watch out: step 18 needs the valuation to be an up-set.
With $p$ true only at $w$ in $w \leq v$, the point $w$ satisfies $p$ but not $\square p$, so the claim of step 17 would fail.
Intuitionistic models never have such valuations, so Part B is safe.

## Variants

McKinsey and Tarski proved faithfulness with algebraic and topological semantics.
The open sets of a space form a Heyting algebra, and the translation computes the value of $A$ in this algebra.
A variant of the translation boxes every subformula.
It is equivalent in $\mathsf{S4}$ to the one used here, since step 1 and axiom T give $T(A) \leftrightarrow \square T(A)$.
A proof theoretic version uses cut-free sequent calculi for $\mathsf{IPC}$ and $\mathsf{S4}$ and translates derivations in both directions.
