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

**Setup.**
We use the clauses of the [[Dialectica interpretation|ZREF8MTYNW]] and the terms of [[system T|A4WR995XZP]].
We write $A^D = \exists x\, \forall y\, A_D(x, y)$, $B^D = \exists u\, \forall v\, B_D(u, v)$ and $C^D = \exists w\, \forall s\, C_D(w, s)$.
By the clause for $\to$, $(A \to B)^D = \exists U, Y\, \forall x, v\, (A_D(x, Y x v) \to B_D(U x, v))$.
We say that terms $U, Y$ *verify* $A \to B$ when T proves $A_D(x, Y x v) \to B_D(U x, v)$.
We say that terms $t$ *verify* $A$ when T proves $A_D(t, y)$.
We use three facts about T.

1. Decidability: for each quantifier-free $P$, T proves $P \vee \neg P$, since equality of numbers is decided by a term of T.
2. Definition by cases: for each quantifier-free $P$ and terms $s, r$ of the same type, a term $\mathrm{if}\ P\ \mathrm{then}\ s\ \mathrm{else}\ r$ equals $s$ under $P$ and $r$ under $\neg P$. It is built from $R_\sigma$.
3. Zero terms: each type $\sigma$ has a closed term $O^\sigma$, namely $O^0 = 0$ and $O^{\sigma \to \tau} = \lambda z.\, O^\tau$.

T also allows substitution of terms for free variables in its theorems, and it proves the propositional tautologies.

**The logical system.**
We use a [[Hilbert system|1MGMQX43B8]] for intuitionistic predicate logic with these axioms and rules.
It derives the same formulas as intuitionistic natural deduction.

- Axioms: $A \to A \wedge A$, $A \vee A \to A$, $A \to A \vee B$, $A \wedge B \to A$, $A \vee B \to B \vee A$, $A \wedge B \to B \wedge A$, $\bot \to A$, $\forall z\, A \to A[t/z]$ and $A[t/z] \to \exists z\, A$.
- Rules: modus ponens; syllogism (from $A \to B$ and $B \to C$ infer $A \to C$); exportation (from $A \wedge B \to C$ infer $A \to (B \to C)$); importation, the converse of exportation.
- More rules: expansion (from $A \to B$ infer $C \vee A \to C \vee B$); from $B \to A$ infer $B \to \forall z\, A$, and from $A \to B$ infer $\exists z\, A \to B$, if $z$ is not free in $B$.
- Equality axioms: $x = x$, and $x = x' \to (P(x) \to P(x'))$ for atomic $P$.

We show by induction on derivations: for every theorem of HA there are terms that verify it.

**Propositional axioms.**

1. $A \to A \wedge A$: we need $U x = (x, x)$ and $Y x y_1 y_2$ with $A_D(x, Y x y_1 y_2) \to A_D(x, y_1) \wedge A_D(x, y_2)$.
2. Let $Y x y_1 y_2 = \mathrm{if}\ A_D(x, y_1)\ \mathrm{then}\ y_2\ \mathrm{else}\ y_1$.
3. If $A_D(x, y_1)$ holds, then $Y = y_2$, so the premise is $A_D(x, y_2)$, and both conjuncts hold.
4. If $A_D(x, y_1)$ fails, then $Y = y_1$, so the premise $A_D(x, y_1)$ is false and the implication holds.
5. $A \vee A \to A$: the premise has witness $(z, x_1, x_2)$ and challenge $(y_1, y_2)$.
6. Let $U = \mathrm{if}\ z = 0\ \mathrm{then}\ x_1\ \mathrm{else}\ x_2$, and send the challenge $y$ to $(y, y)$.
7. If $z = 0$, the premise gives $A_D(x_1, y)$, which is $A_D(U, y)$. If $z \ne 0$, it gives $A_D(x_2, y)$, which is $A_D(U, y)$.
8. $A \to A \vee B$: let $U x = (0, x, O)$, and send the challenge $(y, v)$ to $y$.
9. The conclusion is $(0 = 0 \to A_D(x, y)) \wedge (0 \ne 0 \to B_D(O, v))$, and both conjuncts follow from $A_D(x, y)$.
10. $A \wedge B \to A$: let $U (x, u) = x$, and send $y$ to $(y, O)$. Then $A_D(x, y) \wedge B_D(u, O) \to A_D(x, y)$.
11. $A \wedge B \to B \wedge A$: swap the witnesses and the challenges. The matrix is a propositional tautology.
12. $A \vee B \to B \vee A$: let $U (z, x, u) = (\mathrm{if}\ z = 0\ \mathrm{then}\ 1\ \mathrm{else}\ 0, u, x)$, and swap the challenges.
13. If $z = 0$, the new flag is $1$ and the premise gives $A_D(x, y)$, as the conclusion needs. The case $z \ne 0$ is symmetric.
14. $\bot \to A$: $\bot^D = \bot$ with empty tuples. Let $U = O$; then $\bot \to A_D(O, y)$ holds in T.

**Quantifier axioms.**

1. $\forall z\, A(z) \to A(t)$: the premise has witness $f$ and challenge $(z, y)$, with matrix $A_D(f z, y, z)$.
2. Let $U f = f\, t$, and send $y$ to $(t, y)$. Then the matrix is $A_D(f t, y, t) \to A_D(f t, y, t)$.
3. $A(t) \to \exists z\, A(z)$: let $U x = (t, x)$, and send $y$ to $y$. The matrix is again $P \to P$.

**Rules.**

1. Modus ponens: let $t$ verify $A$, and $U, Y$ verify $A \to B$.
2. Substituting $t$ for $x$ in the second, and $Y t v$ for $y$ in the first, gives $A_D(t, Y t v)$ and then $B_D(U t, v)$.
3. So $U t$ verifies $B$.
4. Syllogism: let $U_1, Y_1$ verify $A \to B$ and $U_2, Y_2$ verify $B \to C$.
5. Substitution gives $A_D(x, Y_1 x (Y_2 (U_1 x) s)) \to B_D(U_1 x, Y_2 (U_1 x) s)$.
6. It also gives $B_D(U_1 x, Y_2 (U_1 x) s) \to C_D(U_2 (U_1 x), s)$.
7. So $U x = U_2 (U_1 x)$ and $Y x s = Y_1 x (Y_2 (U_1 x) s)$ verify $A \to C$.
8. Exportation: let $U, Y_1, Y_2$ verify $A \wedge B \to C$, that is, $A_D(x, Y_1 x u s) \wedge B_D(u, Y_2 x u s) \to C_D(U x u, s)$.
9. The formula $(A \to (B \to C))^D$ asks for $G$ and $H$ with $A_D(x, H x u s) \to (B_D(u, (G x)_2 u s) \to C_D((G x)_1 u, s))$.
10. Here $G x$ is a witness of $B \to C$, a pair of functionals. Let $G x = (\lambda u.\, U x u, \lambda u\, s.\, Y_2 x u s)$ and $H = Y_1$.
11. The required formula follows from the premise by the tautology $(P \wedge Q \to R) \to (P \to (Q \to R))$.
12. Importation: the same terms, read backwards, verify $A \wedge B \to C$, by the converse tautology.
13. Expansion: let $U, Y$ verify $A \to B$. The witness of $C \vee A$ is $(z, w, x)$, and the challenge of $C \vee B$ is $(s, v)$.
14. Let $U' (z, w, x) = (z, w, U x)$, and send $(s, v)$ to $(s, Y x v)$.
15. Then $(z = 0 \to C_D(w, s)) \wedge (z \ne 0 \to A_D(x, Y x v))$ implies the same with $B_D(U x, v)$, by the premise.
16. The rule for $\forall$: let $U, Y$ verify $B \to A(z)$, with $z$ not free in $B$. The terms may contain $z$.
17. Let $U' u = \lambda z.\, U u$ and $Y' u z y = Y u y$. By beta reduction, they verify $B \to \forall z\, A(z)$.
18. The rule for $\exists$: let $U, Y$ verify $A(z) \to B$, with $z$ not free in $B$.
19. Let $U' (z, x) = U x$ and $Y' (z, x) v = Y x v$, where $z$ is now an input. They verify $\exists z\, A(z) \to B$.

**Non-logical axioms.**

1. The equality axioms and the axioms $S x \ne 0$, $S x = S y \to x = y$ and the defining equations of $+$ and $\cdot$ are quantifier-free.
2. For quantifier-free $A$, $A^D = A$ with empty tuples, and T proves these axioms. So the empty tuple verifies them.

**The induction axiom.**
Let $A(n)^D = \exists x\, \forall y\, A_D(x, y, n)$.
The axiom is $A(0) \wedge \forall n\, (A(n) \to A(S n)) \to \forall n\, A(n)$.
Its witness inputs are $x_0$ for $A(0)$, and $U, Y$ for the step, with matrix $A_D(x, Y n x y, n) \to A_D(U n x, y, S n)$.
Its challenge inputs are $n$ and $y$ for the conclusion.
So we need terms $X$, $y_0'$, $k$, $x'$, $y'$ in these inputs such that T proves
$$A_D(x_0, y_0', 0) \wedge \bigl(A_D(x', Y k x' y', k) \to A_D(U k x', y', S k)\bigr) \to A_D(X n, y, n).$$

1. Witness: $X = \lambda n.\, R\, x_0\, U\, n$, so $X 0 = x_0$ and $X (S k) = U k (X k)$.
2. Backward chain: let $y_n = y$ and $y_k = Y k (X k) y_{k + 1}$ for $k < n$. This is a primitive recursion on $n - k$, so a term of T defines it.
3. Write $P(k)$ for the quantifier-free formula $A_D(X k, y_k, k)$, for $k \le n$.
4. Let $k$ be the least $k < n$ with $P(k) \wedge \neg P(k + 1)$, and $k = 0$ if there is none. A bounded search term of T defines it.
5. Choose $y_0' = y_0$, $x' = X k$ and $y' = y_{k + 1}$.
6. By definition, $Y k (X k) y_{k + 1} = y_k$ and $U k (X k) = X (k + 1)$. So the second conjunct is $P(k) \to P(k + 1)$.
7. Case $P(n)$: the conclusion $A_D(X n, y, n)$ is $P(n)$, so the implication holds.
8. Case $\neg P(n)$ and $\neg P(0)$: the first conjunct is $P(0)$, which is false, so the implication holds.
9. Case $\neg P(n)$ and $P(0)$: quantifier-free induction on $n$ in T shows that some $k < n$ has $P(k) \wedge \neg P(k + 1)$.
10. For the least such $k$, the second conjunct $P(k) \to P(k + 1)$ is false, so the implication holds.
11. By decidability, the three cases cover all possibilities. So the terms verify the induction axiom.

**Conclusion of part 1.**
Every axiom of HA is verified, and every rule preserves verification.
By induction on the derivation, every theorem $A$ of HA is verified by terms $t$ with free variables among those of $A$.

**Part 2.**

1. Let PA prove $\forall n\, \exists m\, \varphi(n, m)$ with $\varphi$ quantifier-free.
2. The [[Gödel-Gentzen theorem|WC4TDGEWZR]] and Lemma F5 of the [[conservativity proof|ANXVZG97MG]] give $\mathsf{HA} \vdash \forall n\, \neg \neg \exists m\, \varphi(n, m)$.
3. By the clauses, $(\exists m\, \varphi)^D = \exists m\, \varphi$, and $(\neg \exists m\, \varphi)^D = \forall m\, \neg \varphi$, with empty witness.
4. So $(\neg \neg \exists m\, \varphi)^D = \exists m\, \neg \neg \varphi(n, m)$, and the clause for $\forall$ gives $\exists f\, \forall n\, \neg \neg \varphi(n, f n)$.
5. Part 1 gives a closed term $t$ with $\mathsf{T} \vdash \neg \neg \varphi(n, t\, n)$.
6. By decidability, T proves $\varphi(n, t\, n)$.

This proves the [[soundness theorem|6QFRG42QQR]].

## Idea

Each axiom is verified by explicit terms, and each rule combines the terms of its premises.
Information flows in two directions: witnesses go forward, from premises to conclusions, and challenges go backward.
Contraction $A \to A \wedge A$ is the only place where a choice between two challenges is needed, and it uses decidability.
The induction axiom is verified by recursion forward for the witnesses and by recursion backward for the challenges, with a search for the first failure.

## Variants

- With the induction rule instead of the axiom, the verification is a single recursion, without the search.
- Natural deduction gives a proof with one case for each introduction and elimination rule; the case of ${\to}\mathrm{I}$ with several discharged copies of $A$ again needs definition by cases.
- The Diller-Nahm variant collects finitely many challenges instead of choosing one, and so it avoids definition by cases; it needs finite sequences in T.
- Kohlenbach's monotone interpretation proves only that some majorant of the witness exists, which simplifies the verification of contraction.
