---
tag: 2V7A0TMQN4
kind: proof
name: Proof that compositional truth proves the consistency of PA
msc: ["03F25", "03A05"]
topics: [6Q4JJ2MMV8]
audience: grad
proves: W4MSCKSG3D
uses: [HACXBCM7SS, MFJXPAF0R0, 1MGMQX43B8, 4A84VHDTHV, 4NBAX3VRQ7, EDRV3N0SA3]
methods: [0ASJVEFA9J]
sources:
  - url: https://plato.stanford.edu/entries/truth-axiomatic/
    locator: "Axiomatic Theories of Truth, 3.3 Compositional truth"
  - book: isbn:9780521115810
---

## Proof

Part 1 of the [[statement|W4MSCKSG3D]] is cited and not proved here.
We prove parts 2 and 3, in the notation of the statement.
All reasoning below is inside $\mathsf{CT}$, unless a step says otherwise.

### Setup

1. The language $\mathcal{L}_0$ has $0$, $S$, $=$, and ternary predicates $\mathrm{Add}$, $\mathrm{Mult}$. So every closed term is a numeral $S \cdots S0$.
2. $\mathsf{PA}$ has finitely many *basic axioms* for $0$, $S$, $\mathrm{Add}$, $\mathrm{Mult}$, and the induction axioms.
3. For a formula $\varphi$ and a variable $x$, the *induction axiom* is $\varphi_x[0] \to (\forall x\, (\varphi \to \varphi_x[Sx]) \to \forall x\, \varphi)$.
4. The [[Hilbert system|1MGMQX43B8]] has these logical axioms: $\neg A \vee A$; $A_x[t] \to \exists x\, A$; $x = x$; and the equality axioms.
5. The equality axioms are $x = y \to Sx = Sy$, and $\bar x = \bar y \to (P \bar x \to P \bar y)$ for $P$ among $=$, $\mathrm{Add}$, $\mathrm{Mult}$.
6. The rules are expansion, contraction, associativity, cut and $\exists$-introduction.
7. Expansion infers $B \vee A$ from $A$. Contraction infers $A$ from $A \vee A$.
8. Associativity infers $(A \vee B) \vee C$ from $A \vee (B \vee C)$. Cut infers $B \vee C$ from $A \vee B$ and $\neg A \vee C$.
9. $\exists$-introduction infers $\exists x\, A \to B$ from $A \to B$, if $x$ is not free in $B$.
10. A $\mathsf{PA}$ proof is a finite sequence of formulas. Each line is an axiom, or follows from earlier lines by a rule.
11. $\mathrm{Prf}_{\mathsf{PA}}(d, z)$ formalizes "$d$ is a proof with last line $z$", using a [[Gödel numbering|MFJXPAF0R0]]. $\mathrm{Prov}_{\mathsf{PA}}(z) := \exists d\, \mathrm{Prf}_{\mathsf{PA}}(d, z)$.
12. An *assignment for $z$* is a finite map $s$ from variables to numbers. Every free variable of $z$ must be in its domain.
13. $z[s]$ is the sentence that results from $z$ when each free $v$ is replaced by the numeral $\dot{s}(v)$.
14. $\mathrm{Tall}(z) := \forall s\, (s \text{ is an assignment for } z \to T(z[s]))$. It says that $z$ is true under all assignments.
15. $\mathrm{Tall}$ contains $T$. So an induction on a formula with $\mathrm{Tall}$ is an induction for $\mathcal{L}_T$.

### Lemma 0 (syntax)

*Statement.* $\mathsf{PA}$ proves the following facts, for all formulas, variables, terms and assignments.

1. $z[s]$ is a sentence, and it depends only on the values of $s$ at the free variables of $z$.
2. $(\neg A)[s] = \neg (A[s])$ and $(A \vee B)[s] = A[s] \vee B[s]$.
3. $(\exists x\, A)[s] = \exists x\, (A[s^-])$, where $s^-$ is $s$ without $x$ in its domain.
4. $(A[s^-])_x[\dot m] = A[s^-(x \mapsto m)]$ for every number $m$.
5. If $t$ is substitutable for $x$ in $A$, then $(A_x[t])[s] = A[s(x \mapsto m)]$, where $m$ is the value of the numeral $t[s]$.
6. $S\dot n$ and $\dot{(n+1)}$ are the same term.
7. Let $\varepsilon$ be an identity or equality axiom with variables $v_1, \ldots, v_k$. Then $\varepsilon[s] = \varepsilon_0(\dot a_1, \ldots, \dot a_k)$, with $a_i = s(v_i)$.
8. In step 7, $\varepsilon_0(x_1, \ldots, x_k)$ is one fixed formula for each symbol, so there are finitely many.
9. $\forall a\, \forall b\, (\mathrm{Tr}_0(\ulcorner \dot a = \dot b \urcorner) \leftrightarrow a = b)$, and similar facts hold for $\mathrm{Add}$ and $\mathrm{Mult}$.

*Proof.*

1. Each fact is a property of primitive recursive operations on codes.
2. Each fact follows by induction on the length of a formula or term, inside $\mathsf{PA}$.
3. These inductions use only arithmetical formulas, so $\mathsf{PA}$ proves them.

### Lemma 1 (Tarski biconditionals)

*Statement.* For each arithmetical formula $\varphi(x_1, \ldots, x_k)$, $\mathsf{CT}^- \vdash \forall \bar x\, (T(\ulcorner \varphi(\dot x_1, \ldots, \dot x_k) \urcorner) \leftrightarrow \varphi(\bar x))$.

*Proof.* We use [[induction on the formula|EDRV3N0SA3]] $\varphi$, outside the theory.
Each $\varphi$ gets its own proof.

1. Atomic case. Every term is $S^j 0$ or $S^j x_i$. So $\varphi(\dot{\bar x})$ is an equation or predicate between numerals.
2. Axiom 1 gives $T(\varphi(\dot{\bar x})) \leftrightarrow \mathrm{Tr}_0(\varphi(\dot{\bar x}))$. Lemma 0, step 9, gives $\leftrightarrow \varphi(\bar x)$.
3. Negation. Axiom 2 and Lemma 0 give $T(\ulcorner \neg \psi(\dot{\bar x}) \urcorner) \leftrightarrow \neg T(\ulcorner \psi(\dot{\bar x}) \urcorner)$.
4. The induction hypothesis for $\psi$ gives $\leftrightarrow \neg \psi(\bar x)$.
5. Disjunction. Axiom 3 and the induction hypothesis for both disjuncts give the case $\psi \vee \chi$.
6. Existential case $\exists y\, \psi(y, \bar x)$. Axiom 4 and Lemma 0, step 4, give $T(\ulcorner \exists y\, \psi(y, \dot{\bar x}) \urcorner) \leftrightarrow \exists m\, T(\ulcorner \psi(\dot m, \dot{\bar x}) \urcorner)$.
7. The induction hypothesis for $\psi(y, \bar x)$ gives $\leftrightarrow \exists m\, \psi(m, \bar x)$.
8. No step uses induction for $\mathcal{L}_T$. So each instance is a theorem of $\mathsf{CT}^-$.

### Lemma 2 (logical axioms)

*Statement.* $\mathsf{CT} \vdash \forall z\, (z \text{ is a logical axiom} \to \mathrm{Tall}(z))$.

*Proof.* Let $z$ be a logical axiom and $s$ an assignment for $z$.

1. Case $\neg A \vee A$. By Lemma 0, $z[s] = \neg (A[s]) \vee A[s]$.
2. By axioms 2 and 3, $T(z[s]) \leftrightarrow (\neg T(A[s]) \vee T(A[s]))$. The right side is an instance of excluded middle.
3. Case $\neg A_x[t] \vee \exists x\, A$. Let $m$ be the value of $t[s]$, and $B := A[s^-]$.
4. By Lemma 0, steps 3 to 5, $z[s] = \neg B_x[\dot m] \vee \exists x\, B$.
5. If $T(B_x[\dot m])$, then $T(\exists x\, B)$ by axiom 4 with witness $m$.
6. So $\neg T(B_x[\dot m]) \vee T(\exists x\, B)$ holds. By axioms 2 and 3, $T(z[s])$.
7. Identity and equality axioms. By Lemma 0, step 7, $T(z[s]) \leftrightarrow T(\varepsilon_0(\dot{\bar a}))$.
8. Each $\varepsilon_0(\bar x)$ is logically valid, so $\mathsf{PA} \vdash \forall \bar x\, \varepsilon_0(\bar x)$.
9. Lemma 1 for $\varepsilon_0$ gives $\forall \bar a\, T(\varepsilon_0(\dot{\bar a}))$. There are finitely many $\varepsilon_0$, so one proof covers all cases.

### Lemma 3 (rules)

*Statement.* $\mathsf{CT}$ proves that each rule preserves $\mathrm{Tall}$: if the premises are $\mathrm{Tall}$, then so is the conclusion.

*Proof.* Let $s$ be an assignment for the conclusion.
We extend $s$ by the value $0$ on the other free variables of the premises.

1. By Lemma 0, step 1, the extension does not change the conclusion under $s$.
2. Expansion. $T(A[s])$ holds. By axiom 3, $T(B[s] \vee A[s])$, which is $T((B \vee A)[s])$ by Lemma 0.
3. Contraction. By axiom 3, $T(A[s] \vee A[s])$ gives $T(A[s]) \vee T(A[s])$, so $T(A[s])$.
4. Associativity. By axiom 3 twice, both sides are equivalent to $T(A[s]) \vee T(B[s]) \vee T(C[s])$.
5. Cut. We have $T(A[s]) \vee T(B[s])$, and $\neg T(A[s]) \vee T(C[s])$ by axioms 2 and 3.
6. Case $T(A[s])$ gives $T(C[s])$. Case $\neg T(A[s])$ gives $T(B[s])$. In both cases $T((B \vee C)[s])$.
7. $\exists$-introduction. The premise is $\neg A \vee B$, with $x$ not free in $B$. Assume $T((\exists x\, A)[s])$.
8. By Lemma 0, step 3, and axiom 4, there is $m$ with $T(A[s^-(x \mapsto m)])$.
9. The premise is $\mathrm{Tall}$, so $\neg T(A[s^-(x \mapsto m)]) \vee T(B[s^-(x \mapsto m)])$.
10. So $T(B[s^-(x \mapsto m)])$. This is $T(B[s])$ by Lemma 0, step 1, since $x$ is not free in $B$.
11. So $\neg T((\exists x\, A)[s]) \vee T(B[s])$, and $T(z[s])$ by axioms 2 and 3.

### Lemma 4 (axioms of PA)

*Statement.* $\mathsf{CT} \vdash \forall z\, (z \text{ is an axiom of } \mathsf{PA} \to \mathrm{Tall}(z))$.

*Proof.*

1. Basic axioms. Let $\beta(\bar x)$ be one of them. Then $\mathsf{PA} \vdash \forall \bar x\, \beta(\bar x)$.
2. Lemma 1 gives $\forall \bar a\, T(\beta(\dot{\bar a}))$. With Lemma 0, this is $\mathrm{Tall}(\ulcorner \beta \urcorner)$.
3. Induction axioms. Let $z$ be the induction axiom for $\varphi$ and $x$, and $s$ an assignment for $z$.
4. Let $\psi := \varphi[s^-]$, a formula with at most $x$ free. Write $\psi(\dot n)$ for $\psi_x[\dot n]$.
5. $\forall x\, \chi$ abbreviates $\neg \exists x\, \neg \chi$. By axioms 2 and 4, $T(\forall x\, \chi) \leftrightarrow \forall n\, T(\chi_x[\dot n])$.
6. By Lemma 0, step 6, $(\psi \to \psi_x[Sx])_x[\dot n]$ is $\psi(\dot n) \to \psi(\dot{(n+1)})$.
7. By steps 5 and 6, and axioms 2 and 3, $T(z[s])$ is equivalent to the following:
$$T(\psi(\dot 0)) \to \big(\forall n\, (T(\psi(\dot n)) \to T(\psi(\dot{(n+1)}))) \to \forall n\, T(\psi(\dot n))\big).$$
8. This is an instance of the induction axiom for the $\mathcal{L}_T$ formula $T(p_x[\dot n])$, in $n$, with parameter $p := \psi$.
9. $\mathsf{CT}$ has this axiom, so $T(z[s])$ holds. One axiom covers all $\psi$, since $p$ is a variable.

### Lemma 5 (global reflection)

*Statement.* $\mathsf{CT} \vdash \forall d\, \forall z\, (\mathrm{Prf}_{\mathsf{PA}}(d, z) \to \mathrm{Tall}(z))$.

*Proof.* Let $d$ be a proof with lines $d_0, \ldots, d_{l-1}$.

1. Let $\Phi(i) := \forall j < i\, (j < l \to \mathrm{Tall}(d_j))$. This formula contains $T$.
2. $\Phi(0)$ holds, since no $j$ is below $0$.
3. Assume $\Phi(i)$ and $i < l$. If $d_i$ is a logical axiom, $\mathrm{Tall}(d_i)$ by Lemma 2.
4. If $d_i$ is an axiom of $\mathsf{PA}$, then $\mathrm{Tall}(d_i)$ by Lemma 4.
5. Otherwise $d_i$ follows by a rule from lines $d_j$ with $j < i$. These are $\mathrm{Tall}$ by $\Phi(i)$.
6. So $\mathrm{Tall}(d_i)$ by Lemma 3, and $\Phi(i + 1)$ holds.
7. By induction for $\mathcal{L}_T$ on $i$, $\Phi(l)$ holds. So $\mathrm{Tall}(d_{l-1})$, and $d_{l-1} = z$.
8. If $z$ is a sentence, the empty assignment gives $T(z)$. This is part 2 of the statement.

### Part 3 (consistency)

1. Assume $\mathrm{Prov}_{\mathsf{PA}}(\ulcorner 0 = S0 \urcorner)$. By Lemma 5 and step 8 there, $T(\ulcorner 0 = S0 \urcorner)$.
2. Lemma 1 for the sentence $0 = S0$ gives $0 = S0$.
3. The basic axiom $\forall x\, (Sx \neq 0)$ of $\mathsf{PA}$ gives $S0 \neq 0$, a contradiction.
4. So $\mathsf{CT} \vdash \neg \mathrm{Prov}_{\mathsf{PA}}(\ulcorner 0 = S0 \urcorner)$, which is $\mathrm{Con}(\mathsf{PA})$.

## Idea

Truth is a model of arithmetic that lives inside the theory.
The proof is the [[soundness theorem|4A84VHDTHV]] for this model: axioms are true, and rules keep truth.
The induction along a proof is about $\mathrm{Tall}$, which contains $T$, so it needs induction for $\mathcal{L}_T$.
This is why $\mathsf{CT}^-$ cannot carry out the argument.

## Variants

1. With satisfaction in place of truth, the same proof works for a language with no name for each object, such as set theory.
2. The SEP entry describes the result as the formalized soundness theorem, or global reflection principle, for $\mathsf{PA}$.
3. With function symbols for $+$ and $\cdot$, axiom 1 needs the values of closed terms, and Lemma 0, step 5, uses term evaluation.
