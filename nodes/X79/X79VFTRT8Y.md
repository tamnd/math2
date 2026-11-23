---
tag: X79VFTRT8Y
kind: proof
name: Proof of the soundness of the Dialectica interpretation
msc: ["03F10", "03F25", "03F30"]
topics: [8XY7JYZKFW]
audience: grad
proves: 6QFRG42QQR
uses: [ZREF8MTYNW, A4WR995XZP, 1MGMQX43B8, RXHJPVMPJH, WC4TDGEWZR, ANXVZG97MG]
methods: [12MQ2NJ29A, 0WCP0PVET6, 0NTF6DMVAP, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Dialectica_interpretation
    locator: Proof translation (soundness)
  - url: https://en.wikipedia.org/wiki/Dialectica_interpretation
    locator: Induction
---

## Proof

We fix a Hilbert-style system for HA, give explicit terms of T for each axiom, and show that each rule turns terms for its premises into terms for its conclusion.

### Setup

We use the clauses of the [[Dialectica interpretation|ZREF8MTYNW]] and the terms of [[system T|A4WR995XZP]].
We write $A^D = \exists x\, \forall y\, A_D(x, y)$, $B^D = \exists u\, \forall v\, B_D(u, v)$ and $C^D = \exists w\, \forall s\, C_D(w, s)$.
Terms $t$ *verify* $A$ when T proves $A_D(t, y)$, with $y$ free.
Terms $U, Y$ *verify* $A \to B$ when T proves $A_D(x, Y x v) \to B_D(U x, v)$.
We use three facts about T.

1. Decidability: for each quantifier-free $P$, T proves $P \vee \neg P$, because equality of numbers is decided by a term of T.
2. Definition by cases: for quantifier-free $P$ and terms $s, r$ of one type, a term $\mathrm{if}\ P\ \mathrm{then}\ s\ \mathrm{else}\ r$ equals $s$ under $P$ and $r$ under $\neg P$.
   It is built from a recursor applied to the characteristic term of $P$.
3. Zero terms: each type $\sigma$ has a closed term $O^\sigma$, with $O^{\mathbb{N}} = 0$ and $O^{\sigma \to \tau} = \lambda z.\, O^\tau$.

T also allows substitution of terms for free variables in its theorems, and it proves every propositional tautology.

### The logical system

We use a [[Hilbert system|1MGMQX43B8]] for intuitionistic predicate logic, which derives the same formulas as intuitionistic natural deduction.
Its axioms are $A \to A \wedge A$, $A \vee A \to A$, $A \to A \vee B$, $A \wedge B \to A$, $A \vee B \to B \vee A$, $A \wedge B \to B \wedge A$, $\bot \to A$, $\forall z\, A \to A[t/z]$ and $A[t/z] \to \exists z\, A$.
Its rules are modus ponens and syllogism (from $A \to B$ and $B \to C$ infer $A \to C$).
Further rules are exportation (from $A \wedge B \to C$ infer $A \to (B \to C)$) and its converse, importation.
Expansion infers $C \vee A \to C \vee B$ from $A \to B$.
The quantifier rules infer $B \to \forall z\, A$ from $B \to A$, and $\exists z\, A \to B$ from $A \to B$, when $z$ is not free in $B$.
The equality axioms are $x = x$ and $x = x' \to (P(x) \to P(x'))$ for atomic $P$.
We show, by induction on derivations, that every theorem of HA is verified by some terms.

### Contraction and the disjunction axioms

1. For $A \to A \wedge A$ we take $U x = (x, x)$ and $Y x y_1 y_2 = \mathrm{if}\ A_D(x, y_1)\ \mathrm{then}\ y_2\ \mathrm{else}\ y_1$.
   We must prove $A_D(x, Y x y_1 y_2) \to A_D(x, y_1) \wedge A_D(x, y_2)$.
2. If $A_D(x, y_1)$ holds, then $Y = y_2$, so the premise is $A_D(x, y_2)$, and both conjuncts hold.
   If $A_D(x, y_1)$ fails, then $Y = y_1$, so the premise is false and the implication holds.
3. For $A \vee A \to A$ the premise has witness $(z, x_1, x_2)$.
   We take $U = \mathrm{if}\ z = 0\ \mathrm{then}\ x_1\ \mathrm{else}\ x_2$ and send the challenge $y$ to $(y, y)$.
   If $z = 0$ the premise gives $A_D(x_1, y)$, and if $z \ne 0$ it gives $A_D(x_2, y)$; in both cases this is $A_D(U, y)$.
4. For $A \to A \vee B$ we take $U x = (0, x, O)$ and send $(y, v)$ to $y$.
   The conclusion $(0 = 0 \to A_D(x, y)) \wedge (0 \ne 0 \to B_D(O, v))$ follows from $A_D(x, y)$.
5. For $A \vee B \to B \vee A$ we take $U(z, x, u) = (\mathrm{if}\ z = 0\ \mathrm{then}\ 1\ \mathrm{else}\ 0,\ u,\ x)$ and swap the two challenges.
   If $z = 0$, the new flag is $1$ and the premise gives $A_D(x, y)$, which the conclusion needs; the case $z \ne 0$ is symmetric.

### The other logical axioms

1. For $A \wedge B \to A$ we take $U(x, u) = x$ and send $y$ to $(y, O)$, so the matrix is $A_D(x, y) \wedge B_D(u, O) \to A_D(x, y)$.
2. For $A \wedge B \to B \wedge A$ we swap the witnesses and the challenges, and the matrix is a tautology.
3. For $\bot \to A$ we take $U = O$, since $\bot^D = \bot$ and $\bot \to A_D(O, y)$ is a tautology.
4. For $\forall z\, A(z) \to A(t)$ the premise has witness $f$ and challenge $(z, y)$, with matrix $A_D(f z, y, z)$.
   We take $U f = f\, t$ and send $y$ to $(t, y)$, and the matrix becomes $A_D(f t, y, t) \to A_D(f t, y, t)$.
5. For $A(t) \to \exists z\, A(z)$ we take $U x = (t, x)$ and send $y$ to $y$, and the matrix is again of the form $P \to P$.
6. The equality axioms and the axioms $S x \ne 0$, $S x = S y \to x = y$ and the equations for $+$ and $\cdot$ are quantifier-free.
   They are their own interpretations, T proves them, and the empty tuple verifies them.

### Modus ponens and syllogism

1. Modus ponens: let $t$ verify $A$, and let $U, Y$ verify $A \to B$.
2. Substituting $t$ for $x$ gives $A_D(t, Y t v) \to B_D(U t, v)$, and substituting $Y t v$ for $y$ in the first gives $A_D(t, Y t v)$.
   So T proves $B_D(U t, v)$, and $U t$ verifies $B$.
3. Syllogism: let $U_1, Y_1$ verify $A \to B$ and $U_2, Y_2$ verify $B \to C$.
4. Substitution in the first gives this implication:
   $$A_D(x, Y_1 x (Y_2 (U_1 x) s)) \to B_D(U_1 x, Y_2 (U_1 x) s).$$
5. Substitution in the second gives $B_D(U_1 x, Y_2 (U_1 x) s) \to C_D(U_2 (U_1 x), s)$.
6. So $U x = U_2 (U_1 x)$ and $Y x s = Y_1 x (Y_2 (U_1 x) s)$ verify $A \to C$.

### The other rules

1. Exportation: let $U, Y_1, Y_2$ verify $A \wedge B \to C$, so T proves $A_D(x, Y_1 x u s) \wedge B_D(u, Y_2 x u s) \to C_D(U x u, s)$.
2. A witness of $A \to (B \to C)$ is a pair $G, H$, where $G x$ is itself a witness of $B \to C$.
   We take $G x = (\lambda u.\, U x u,\ \lambda u\, s.\, Y_2 x u s)$ and $H = Y_1$.
3. The required matrix $A_D(x, Y_1 x u s) \to (B_D(u, Y_2 x u s) \to C_D(U x u, s))$ follows by the tautology $(P \wedge Q \to R) \to (P \to (Q \to R))$.
   Importation uses the same terms read backward and the converse tautology.
4. Expansion: let $U, Y$ verify $A \to B$.
   We send the witness $(z, w, x)$ of $C \vee A$ to $(z, w, U x)$, and the challenge $(s, v)$ of $C \vee B$ to $(s, Y x v)$.
   The premise $A_D(x, Y x v) \to B_D(U x, v)$ turns the matrix of $C \vee A$ into the matrix of $C \vee B$.
5. The rule for $\forall$: let $U, Y$ verify $B \to A(z)$, with $z$ not free in $B$; the terms may contain $z$.
   Then $U' u = \lambda z.\, U u$ and $Y' u z y = Y u y$ verify $B \to \forall z\, A(z)$, by beta reduction.
6. The rule for $\exists$: let $U, Y$ verify $A(z) \to B$, with $z$ not free in $B$.
   Then $U'(z, x) = U x$ and $Y'(z, x) v = Y x v$ verify $\exists z\, A(z) \to B$, with $z$ now an input.

### The induction axiom: the terms

Let $A(n)^D = \exists x\, \forall y\, A_D(x, y, n)$, and consider $A(0) \wedge \forall n\, (A(n) \to A(S n)) \to \forall n\, A(n)$.
The witness of the premise is $x_0$ for $A(0)$ and $U, Y$ for the step, whose matrix is $A_D(x, Y n x y, n) \to A_D(U n x, y, S n)$.
The challenge of the conclusion is a pair $n, y$.
We need terms $X$, $y_0'$, $k$, $x'$, $y'$ in these inputs such that T proves the following:
$$A_D(x_0, y_0', 0) \wedge \bigl(A_D(x', Y k x' y', k) \to A_D(U k x', y', S k)\bigr) \to A_D(X n, y, n).$$

1. The witness goes forward: $X = \lambda n.\, R\, x_0\, U\, n$, so $X 0 = x_0$ and $X (S k) = U k (X k)$.
2. The challenges go backward: $y_n = y$ and $y_k = Y k (X k) y_{k + 1}$ for $k < n$.
   This is a primitive recursion on $n - k$, so a term of T defines it.
3. Write $P(k)$ for the quantifier-free formula $A_D(X k, y_k, k)$, for $k \le n$.
4. Let $k$ be the least $k < n$ with $P(k) \wedge \neg P(k + 1)$, and $k = 0$ if there is none.
   A bounded search, which is a term of T, finds it.
5. We choose $y_0' = y_0$, $x' = X k$ and $y' = y_{k + 1}$.

### The induction axiom: the check

1. By steps 1 and 2 of the terms, $Y k (X k) y_{k + 1} = y_k$ and $U k (X k) = X (k + 1)$.
   So the second conjunct is $P(k) \to P(k + 1)$, and the first conjunct is $P(0)$.
2. The conclusion $A_D(X n, y, n)$ is $P(n)$, because $y_n = y$.
3. Case $P(n)$: the conclusion holds, so the implication holds.
4. Case $\neg P(n)$ and $\neg P(0)$: the first conjunct is false, so the implication holds.
5. Case $\neg P(n)$ and $P(0)$: quantifier-free induction in T shows that some $k < n$ has $P(k) \wedge \neg P(k + 1)$.
   For the least such $k$ the second conjunct is false, so the implication holds.
6. By decidability these three cases cover all possibilities, so the terms verify the induction axiom.

### Conclusion

Every axiom of HA is verified, and every rule preserves verification.
By induction on the derivation, every theorem $A$ of HA is verified by terms $t$ whose free variables are among those of $A$, which is part 1.

For part 2, let PA prove $\forall n\, \exists m\, \varphi(n, m)$ with $\varphi$ quantifier-free.

1. The [[Gödel-Gentzen theorem|WC4TDGEWZR]] and Lemma F5 of the [[conservativity proof|ANXVZG97MG]] give $\mathsf{HA} \vdash \forall n\, \neg \neg \exists m\, \varphi(n, m)$.
2. By the clauses, $(\neg \exists m\, \varphi)^D = \forall m\, \neg \varphi$ with an empty witness, so $(\neg \neg \exists m\, \varphi)^D = \exists m\, \neg \neg \varphi$.
3. The clause for $\forall$ gives $\exists f\, \forall n\, \neg \neg \varphi(n, f n)$, and part 1 gives a closed term $t$ with $\mathsf{T} \vdash \neg \neg \varphi(n, t\, n)$.
4. By decidability of $\varphi$, T proves $\varphi(n, t\, n)$.

This proves the [[soundness theorem|6QFRG42QQR]].

## Idea

Witnesses go forward, from premises to conclusions, and challenges go backward, from conclusions to premises.
Each axiom gets explicit terms, and each rule composes the terms of its premises, the way a compiler composes the code of subprograms.
Contraction is the one place where a single challenge must be chosen from two, and it uses decidability to pick the one that fails.
Induction is verified by a forward recursion for the witnesses, a backward recursion for the challenges, and a search for the first place where the step fails.

## Variants

A proof with natural deduction instead of a Hilbert system has one case for each introduction and elimination rule.
There, the rule ${\to}\mathrm{I}$ with several discharged copies of $A$ plays the role of contraction and again needs a definition by cases.
The Diller-Nahm variant of the interpretation collects a finite list of challenges instead of choosing one, so it needs no definition by cases, but it needs finite sequences in T.
Kohlenbach's monotone interpretation asks only for majorants of the witnesses, and its soundness proof follows the same plan.
