---
tag: PHWAN904PT
kind: definition
name: Magari algebra
msc: ["03G25", "03F45"]
topics: [3E7M66WW6Q]
audience: research
defines: YTA4C8QCB0
uses: [0XADJKM699, WJK0YA4GP2, QC9M3Q8B8Q, S4QJ395PA5, 05006AJ7DZ, G989VP2NGP, HACXBCM7SS, F6H4STF9RG, 3HD30YG3DG, 3PRW76471J, TDDX1NHG8D]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_algebra
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Provability_logic
    locator: Examples
---

## Definition

A Magari algebra is a Boolean algebra with a box operation that obeys the laws of provability in arithmetic.

Let $(B, \wedge, \vee, \neg, 0, 1)$ be a [[Boolean algebra|0XADJKM699]].
Write $a \to b$ for $\neg a \vee b$, $a \leftrightarrow b$ for $(a \to b) \wedge (b \to a)$, and $a \le b$ for $a \wedge b = a$.
A *Magari algebra*, or *diagonalizable algebra*, is a pair $(B, \square)$ where $\square \colon B \to B$ is a map with the following three properties for all $x, y \in B$.

1. $\square 1 = 1$.
2. $\square (x \wedge y) = \square x \wedge \square y$.
3. $\square (\square x \to x) = \square x$.

Property 3 is the *Löb law*.

## Notation

We write $\lozenge x$ for $\neg \square \neg x$ and $\boxdot x$ for $x \wedge \square x$.
Magari wrote $\tau$ for the operation $\square$.
A formula $\varphi$ of modal logic is *valid* in $(B, \square)$ when it takes the value $1$ under every assignment of elements of $B$ to its variables.

## Remarks

### Reading the three properties

Read $\square x$ as "$x$ is provable".
Property 1 says that the true statement is provable.
Property 2 says that a conjunction is provable exactly when both parts are.
Property 3 is Löb's theorem: proving "if $x$ is provable, then $x$" is the same as proving $x$.

On $B = \{0, 1\}$ the map $\square x = 1$ satisfies all three, since every side of every law is $1$; see [[the two-element Magari algebra|BB0SVFTESA]].
The identity map satisfies properties 1 and 2 but not 3.
At $x = 0$ the left side of property 3 is $\square(\neg 0) = 1$ and the right side is $0$; see [[the identity operator is not a Magari operator|F3YQMQHKYR]].
So property 3 is the one that separates provability from truth.

### Two facts about Boolean algebras

The proofs below use two facts that hold in every Boolean algebra, for all $a, b, x$.

- (F1) $a \le b$ if and only if $a \to b = 1$.
- (F2) $x \wedge a \le b$ if and only if $x \le a \to b$.

Proof of (F1).

1. Assume $a \le b$.
   Since $y \mapsto \neg a \vee y$ preserves $\le$, we get $\neg a \vee b \ge \neg a \vee a = 1$, so $a \to b = 1$.
2. Conversely, assume $\neg a \vee b = 1$.
   Then $a = a \wedge (\neg a \vee b) = (a \wedge \neg a) \vee (a \wedge b) = a \wedge b$, so $a \le b$.

Proof of (F2).

1. Assume $x \wedge a \le b$.
   Then $x = (x \wedge a) \vee (x \wedge \neg a) \le b \vee \neg a = a \to b$.
2. Assume $x \le a \to b$.
   Then $x \wedge a \le (\neg a \vee b) \wedge a = (\neg a \wedge a) \vee (b \wedge a) = b \wedge a \le b$.

### Monotonicity and the inequality form of the Löb law

**Lemma 1.** If $(B, \square)$ satisfies properties 1 and 2, then $x \le y$ implies $\square x \le \square y$.

1. Assume $x \le y$, so $x = x \wedge y$.
2. Property 2 gives $\square x = \square(x \wedge y) = \square x \wedge \square y$.
3. By the definition of $\le$, this says $\square x \le \square y$.

**Lemma 2.** If $(B, \square)$ satisfies properties 1 and 2, then property 3 holds if and only if $\square(\square x \to x) \le \square x$ for all $x$.

1. Property 3 implies the inequality, because $c = c$ implies $c \le c$.
2. For the converse, first $x \le \square x \to x$.
   Indeed $x \wedge (\neg \square x \vee x) = (x \wedge \neg \square x) \vee x = x$ by absorption.
3. Lemma 1 turns step 2 into $\square x \le \square(\square x \to x)$.
4. Together with the assumed inequality, antisymmetry of $\le$ gives $\square(\square x \to x) = \square x$.

Lemma 2 explains why some authors state the Löb law as an inequality.

### The law of axiom 4

**Proposition.** Every Magari algebra satisfies $\square x \le \square \square x$ for all $x$.

In the modal logic $\mathsf{K}$, axiom 4, $\square p \to \square \square p$, follows from Löb's axiom by the substitution $p := p \wedge \square p$.
The following steps are the algebraic form of that derivation.

1. Fix $x$ and put $y = x \wedge \square x$.
2. Property 2 gives $\square y = \square x \wedge \square \square x$, so $\square y \le \square x$.
3. Hence $x \wedge \square y \le x \wedge \square x = y$.
4. Fact (F2) turns step 3 into $x \le \square y \to y$.
5. Lemma 1 turns step 4 into $\square x \le \square(\square y \to y)$.
6. Property 3 at $y$ gives $\square(\square y \to y) = \square y$, so $\square x \le \square y$.
7. By step 2, $\square y = \square x \wedge \square \square x \le \square \square x$, so $\square x \le \square \square x$.

### Algebraic completeness of GL

The formulas of modal logic are built from propositional variables, $\bot$, $\to$ and $\square$, and the other connectives are abbreviations.
The logic $\mathsf{GL}$ of [[provability logic|WJK0YA4GP2]] has three kinds of axioms.
They are all instances of [[tautologies|05006AJ7DZ]], all instances of $\mathrm{K}\colon \square(\varphi \to \psi) \to (\square \varphi \to \square \psi)$, and all instances of Löb's axiom $\square(\square \varphi \to \varphi) \to \square \varphi$.
Its rules are modus ponens and [[necessitation|G989VP2NGP]], which infers $\square \varphi$ from $\varphi$.

An assignment $v$ into $(B, \square)$ maps the variables to $B$.
It extends to all formulas by $v(\bot) = 0$, $v(\varphi \to \psi) = v(\varphi) \to v(\psi)$ and $v(\square \varphi) = \square v(\varphi)$.

**Theorem.** For every modal formula $\varphi$, $\mathsf{GL} \vdash \varphi$ if and only if $\varphi$ is valid in every Magari algebra.

Soundness says that every theorem takes the value $1$ everywhere, and it comes from checking each axiom and rule.
Completeness needs a single algebra in which every non-theorem fails, and the Lindenbaum-Tarski algebra of $\mathsf{GL}$ is that algebra.
The next three subsections give the two halves.

### Soundness

We show by induction on the length of a derivation that every theorem $\varphi$ of $\mathsf{GL}$ has $v(\varphi) = 1$ for every Magari algebra and every assignment $v$.

1. Let $\varphi = \theta(\psi_1, \dots, \psi_k)$ be an instance of a tautology $\theta(q_1, \dots, q_k)$.
   Then $v(\varphi) = \theta^B(b_1, \dots, b_k)$ with $b_i = v(\psi_i)$, the Boolean term $\theta$ computed in $B$.
2. By [[Stone's representation theorem|S4QJ395PA5]], there is an injective homomorphism of Boolean algebras $h \colon B \to \mathcal{P}(X)$ for some set $X$.
3. In $\mathcal{P}(X)$ the operations act point by point.
   So a point $s$ lies in $\theta^{\mathcal{P}(X)}(C_1, \dots, C_k)$ exactly when the truth table of $\theta$ gives "true" at the values "$s \in C_i$".
4. Since $\theta$ is a tautology, every point lies there, so $h(\theta^B(b_1, \dots, b_k)) = X = h(1)$.
   Injectivity gives $\theta^B(b_1, \dots, b_k) = 1$.
5. For an instance of $\mathrm{K}$, put $a = v(\varphi)$ and $b = v(\psi)$.
   Property 2 gives $\square(a \to b) \wedge \square a = \square((\neg a \vee b) \wedge a) = \square(a \wedge b)$.
6. Lemma 1 gives $\square(a \wedge b) \le \square b$, and (F2) then gives $\square(a \to b) \le \square a \to \square b$.
   By (F1) the value of the axiom is $1$.
7. For an instance of Löb's axiom, property 3 gives $\square(\square a \to a) \le \square a$, and (F1) gives the value $1$.
8. Modus ponens: if $v(\varphi) = 1$ and $v(\varphi \to \psi) = 1$, then $v(\psi) = \neg 1 \vee v(\psi) = v(\varphi \to \psi) = 1$.
9. Necessitation: if $v(\varphi) = 1$, then $v(\square \varphi) = \square 1 = 1$ by property 1.

### Completeness: the Lindenbaum-Tarski algebra

We build one Magari algebra in which every non-theorem fails.

1. For formulas $\varphi, \psi$ put $\varphi \equiv \psi$ when $\mathsf{GL} \vdash \varphi \leftrightarrow \psi$.
   Tautologies and modus ponens show that $\equiv$ is an equivalence relation.
2. If $\varphi \equiv \varphi'$ and $\psi \equiv \psi'$, then $(\varphi \to \psi) \equiv (\varphi' \to \psi')$, by a tautology and modus ponens.
3. If $\varphi \equiv \psi$, then $\mathsf{GL} \vdash \varphi \to \psi$, necessitation gives $\square(\varphi \to \psi)$, and $\mathrm{K}$ gives $\square \varphi \to \square \psi$.
   The same argument with $\psi \to \varphi$ gives $\square \varphi \equiv \square \psi$.
4. Let $L$ be the set of classes $[\varphi]$, with $0 = [\bot]$ and $[\varphi] \to [\psi] = [\varphi \to \psi]$.
   The operations $\neg, \wedge, \vee$ have their usual definitions from $\to$ and $\bot$, and step 2 shows that all are well defined.
5. Each equation $s = t$ of the axioms of Boolean algebras gives a tautology $s \leftrightarrow t$, which $\mathsf{GL}$ proves.
   So $L$ is a Boolean algebra, the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]] of $\mathsf{GL}$.
6. In $L$, $[\varphi] = 1$ if and only if $\mathsf{GL} \vdash \varphi$.
   The reason is that $\varphi \leftrightarrow (\bot \to \bot)$ is a tautological consequence of $\varphi$, and conversely.
7. Put $\square [\varphi] = [\square \varphi]$, which is well defined by step 3.

### Completeness: the box and the failing assignment

8. Property 1: $\mathsf{GL} \vdash \bot \to \bot$, necessitation gives $\mathsf{GL} \vdash \square(\bot \to \bot)$, and step 6 gives $\square 1 = 1$.
9. Property 2, one half: the tautologies $\varphi \wedge \psi \to \varphi$ and $\varphi \wedge \psi \to \psi$ with necessitation and $\mathrm{K}$ give $\square(\varphi \wedge \psi) \to \square \varphi \wedge \square \psi$.
10. Property 2, other half: the tautology $\varphi \to (\psi \to \varphi \wedge \psi)$ with necessitation and two uses of $\mathrm{K}$ gives $\square \varphi \to (\square \psi \to \square(\varphi \wedge \psi))$.
11. Property 3: Löb's axiom, step 6 and (F1) give $\square(\square[\varphi] \to [\varphi]) \le \square[\varphi]$.
    Lemma 2 gives equality, so $(L, \square)$ is a Magari algebra.
12. Let $v_0(p) = [p]$ for each variable $p$.
    Induction on formulas gives $v_0(\psi) = [\psi]$ for every $\psi$, since both sides follow the same rules for $\bot$, $\to$ and $\square$.
13. If $\mathsf{GL} \nvdash \varphi$, then $v_0(\varphi) = [\varphi] \ne 1$ by step 6.
    So $\varphi$ is not valid in the Magari algebra $(L, \square)$.

### The algebra of Peano arithmetic

Let $\mathsf{PA}$ be [[Peano arithmetic|HACXBCM7SS]], and write $\square \sigma$ for $\mathrm{Prov}_{\mathsf{PA}}(\ulcorner \sigma \urcorner)$.
Let $L_{\mathsf{PA}}$ be the Lindenbaum-Tarski algebra of the sentences of $\mathsf{PA}$, with $[\sigma] = [\tau]$ when $\mathsf{PA} \vdash \sigma \leftrightarrow \tau$.
We use two of the [[derivability conditions|F6H4STF9RG]].
(D1) says that $\mathsf{PA} \vdash \sigma$ implies $\mathsf{PA} \vdash \square \sigma$, and (D2) says that $\mathsf{PA} \vdash \square(\sigma \to \tau) \to (\square \sigma \to \square \tau)$.

**Proposition.** The map $\square[\sigma] = [\square \sigma]$ makes $L_{\mathsf{PA}}$ a Magari algebra.

1. The map is well defined.
   From $\mathsf{PA} \vdash \sigma \to \tau$, (D1) gives $\mathsf{PA} \vdash \square(\sigma \to \tau)$, and (D2) gives $\mathsf{PA} \vdash \square \sigma \to \square \tau$.
2. Property 1: $\mathsf{PA}$ proves $0 = 0$, so (D1) gives $\mathsf{PA} \vdash \square(0 = 0)$, and $[\square(0 = 0)] = [0 = 0] = 1$.
3. Property 2: steps 9 and 10 of the completeness proof work in $\mathsf{PA}$, with (D1) in place of necessitation and (D2) in place of $\mathrm{K}$.
4. Property 3: the formalized form of [[Löb's theorem|3HD30YG3DG]] is $\mathsf{PA} \vdash \square(\square \sigma \to \sigma) \to \square \sigma$.
   This gives the inequality, and Lemma 2 gives equality.

The [[diagonal lemma|3PRW76471J]] gives a sentence $G$ with $\mathsf{PA} \vdash G \leftrightarrow \neg \square G$.
In $L_{\mathsf{PA}}$ this says $[G] = \neg \square [G]$, so $[G]$ is a fixed point of $x \mapsto \neg \square x$.
The name "diagonalizable algebra" comes from these fixed points.

### Fixed points in every Magari algebra

A term $t(x, y_1, \dots, y_n)$ is *modalized in* $x$ when every occurrence of $x$ lies inside the scope of $\square$.

**Proposition.** Let $t$ be modalized in $x$, and let $b_1, \dots, b_n \in B$.
There is exactly one $d \in B$ with $d = t(d, b_1, \dots, b_n)$, and $d$ is the value of a term in $b_1, \dots, b_n$ alone.

1. Read $t$ as a modal formula $A(p, q_1, \dots, q_n)$, modalized in $p$.
2. The [[de Jongh-Sambin fixed-point theorem|TDDX1NHG8D]] gives a formula $D(q_1, \dots, q_n)$ without $p$ with $\mathsf{GL} \vdash D \leftrightarrow A(D, q_1, \dots, q_n)$.
3. Its uniqueness part gives $\mathsf{GL} \vdash \boxdot(p \leftrightarrow A(p, \vec{q})) \wedge \boxdot(r \leftrightarrow A(r, \vec{q})) \to (p \leftrightarrow r)$.
4. Existence: take $v(q_i) = b_i$ and $d = v(D)$.
   Soundness and step 2 give $(d \leftrightarrow t(d, \vec{b})) = 1$, and (F1) in both directions gives $d = t(d, \vec{b})$.
5. Uniqueness: let $d$ and $e$ be fixed points, and take $v(p) = d$, $v(r) = e$, $v(q_i) = b_i$.
6. Then $v(p \leftrightarrow A(p, \vec{q})) = 1$ by (F1), and $\boxdot 1 = 1 \wedge \square 1 = 1$ by property 1.
   The same holds for $r$.
7. Soundness and step 3 give $v(p \leftrightarrow r) = 1$, so $d = e$ by (F1).

For $t(x) = \neg \square x$ the fixed point is $\neg \square 0$, the algebraic form of the consistency statement.
Check: $\neg \square(\neg \square 0) = \neg \square 0$ because the Löb law at $0$ gives $\square(\neg \square 0) = \square 0$.

### Watch out

The Löb law is an equation between two elements, not the statement $\square x \to x = 1$.
By (F1) the second statement is $\square x \le x$, and at $x = 0$ it gives $\square 0 = 0$.
Property 3 at $0$ then reads $1 = \square 1 = \square(\square 0 \to 0) = \square 0 = 0$, so only the one-element algebra satisfies it.

## Explanations

### L1 human

A Boolean algebra is a system of "statements" with "and", "or" and "not".
A Magari algebra adds one more operation, which we read as "it is provable that".
The operation must follow three rules.
The statement "true" is provable.
"$x$ and $y$" is provable exactly when $x$ is provable and $y$ is provable.
The third rule is Löb's rule: proving "if $x$ is provable, then $x$ holds" is the same as proving $x$.

### L2 human

We check the law of axiom 4 in a small case.

1. Take the subsets of $W = \{0, 1, 2\}$ with the order $0 < 1 < 2$, and let $\square X$ be the set of $w$ such that every $v > w$ lies in $X$.
2. For $X = \emptyset$ we get $\square \emptyset = \{2\}$, since only $2$ has no larger element.
3. Then $\square \square \emptyset = \square \{2\} = \{1, 2\}$.
   The points $1$ and $2$ have all larger elements in $\{2\}$, but $0$ has $1 > 0$ and $1 \notin \{2\}$.
4. So $\square \emptyset = \{2\} \subseteq \{1, 2\} = \square \square \emptyset$, as the proposition says.

The typical use of the definition is the completeness theorem: to show that $\mathsf{GL}$ does not prove a formula, find one Magari algebra where the formula fails.
The trap is to read the inclusion in step 4 as an equality; here $\square \square \emptyset$ is strictly larger than $\square \emptyset$.

### L3 human

The three properties are equations, so the Magari algebras form a variety of Boolean algebras with operators.
In the language of abstract algebraic logic, the theorem above makes this variety the equivalent algebraic semantics of $\mathsf{GL}$.
The algebraic completeness proof needs only one algebra, the Lindenbaum-Tarski algebra of $\mathsf{GL}$.
Kripke completeness of $\mathsf{GL}$ is harder, because the canonical model method fails for $\mathsf{GL}$ and the proof must go through finite frames; see [[Kripke completeness of GL|1DMFNR7FZT]].
