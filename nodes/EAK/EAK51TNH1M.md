---
tag: EAK51TNH1M
kind: proof
name: Proof of the correctness of the standard translation
msc: ["03B45", "03C80"]
topics: [SKY7AQFG1V]
audience: grad
proves: 1HQ1W36J4V
uses: [YW6YGBMVQY, NGHWZ9Y7ZV, 6BQ71KQ6QT, 086QKPF0A6, G6X7SZSNC5, 12MQ2NJ29A]
methods: [12MQ2NJ29A, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Standard_translation
    locator: lead section
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds, chapter on frame definability
---

## Proof

We prove the four parts of [[the correctness of the standard translation|1HQ1W36J4V]]: parts 1 and 2 by induction on formulas, and parts 3 and 4 by unfolding the definitions of truth.

Fix a [[Kripke model|NGHWZ9Y7ZV]] $\mathfrak{M} = (W, R, V)$, read as a first-order structure with $P_i$ interpreted as $V(p_i)$.
For $z \in \{ x, y \}$, write $\mathfrak{M} \models \mathrm{ST}_z(\varphi)[z \mapsto w]$ for truth under an assignment that sends $z$ to $w$.

### Part 1: the variables

1. We use [[structural induction|12MQ2NJ29A]] on $\varphi$, for $\mathrm{ST}_x$ and $\mathrm{ST}_y$ together.
   The claim for $\mathrm{ST}_x(\varphi)$ is that its free variables are among $\{ x \}$ and all its variables are among $\{ x, y \}$.
2. For $p$ the translation is $P(x)$, and for $\bot$ it is $\bot$, so the claim holds.
3. For $\varphi \to \psi$, the free variables of an implication are those of its two sides, so the claim follows from the hypothesis for $\varphi$ and $\psi$.
4. For $\square\varphi$, the hypothesis for $\mathrm{ST}_y$ says that $\mathrm{ST}_y(\varphi)$ has free variables among $\{ y \}$ and variables among $\{ x, y \}$.
   In $\forall y\,(R(x, y) \to \mathrm{ST}_y(\varphi))$ the quantifier binds $y$, and the only new free variable is the $x$ of $R(x, y)$.
   So the claim holds, and the case of $\mathrm{ST}_y$ is the same with $x$ and $y$ exchanged.
5. By part 1 and the coincidence lemma of [[first-order logic|086QKPF0A6]], the truth of $\mathrm{ST}_z(\varphi)$ depends only on the value of $z$.
   So the notation $[z \mapsto w]$ is well defined.

### Part 2: local truth

6. We use structural induction on $\varphi$ again.
   The claim is that for all $w \in W$ and $z \in \{ x, y \}$, $\mathfrak{M}, w \models \varphi$ holds if and only if $\mathfrak{M} \models \mathrm{ST}_z(\varphi)[z \mapsto w]$.
7. For $p_i$, the left side means $w \in V(p_i)$.
   The right side $P_i(z)[z \mapsto w]$ also means $w \in V(p_i)$, because $P_i$ is interpreted as $V(p_i)$.
   This is where the choice of interpretation is used.
8. For $\bot$, both sides are false at every $w$.
9. For $\varphi \to \psi$, both sides are true exactly when the left part fails or the right part holds, and the hypothesis matches the parts.
10. For $\square\varphi$ and $z = x$, the formula $\forall y\,(R(x, y) \to \mathrm{ST}_y(\varphi))$ holds at $w$ if and only if $\mathrm{ST}_y(\varphi)[y \mapsto v]$ holds for every $v \in W$ with $(w, v) \in R$.
11. By the hypothesis for $\varphi$ with $z = y$, this holds if and only if $\mathfrak{M}, v \models \varphi$ for every $v$ with $w R v$.
    By the box clause of [[Kripke semantics|6BQ71KQ6QT]], this means $\mathfrak{M}, w \models \square\varphi$.
    This is where the induction for $\mathrm{ST}_y$ feeds the step for $\mathrm{ST}_x$.
12. The case $z = y$ is the same with $x$ and $y$ exchanged, which proves part 2.

### Parts 3 and 4: models and frames

13. $\mathfrak{M} \models \varphi$ means $\mathfrak{M}, w \models \varphi$ for every $w \in W$.
    By part 2, this means $\mathfrak{M} \models \mathrm{ST}_x(\varphi)[x \mapsto w]$ for every $w$, which is the meaning of $\mathfrak{M} \models \forall x\, \mathrm{ST}_x(\varphi)$.
14. $\mathfrak{F} \models \varphi$ means $(\mathfrak{F}, V) \models \varphi$ for every valuation $V$.
    Only the values $V(p_1), \dots, V(p_n)$ matter, because the truth of $\varphi$ depends only on its own variables.
15. The choices of $V(p_1), \dots, V(p_n)$ correspond exactly to the choices of subsets of $W$ for $P_1, \dots, P_n$.
    By part 3 for each $V$, $\mathfrak{F} \models \varphi$ holds if and only if $\forall x\, \mathrm{ST}_x(\varphi)$ holds for every choice of the $P_i$.
16. By the semantics of monadic [[second-order logic|G6X7SZSNC5]], this is the meaning of $\mathfrak{F} \models \forall P_1 \dots \forall P_n\, \forall x\, \mathrm{ST}_x(\varphi)$.

## Idea

Each clause of the translation copies a clause of the Kripke truth definition, so the induction is a clause-by-clause match.
The only care is in the box step, where the hypothesis is used for the other variable.

## Variants

With a new variable at each box, the same induction works with the claim that the free variable is the one given.
Part 1 then gives $d + 1$ variables for a formula of modal depth $d$.

One can also take $\lozenge$ as primitive, with the clause $\exists y\,(R(x, y) \wedge \mathrm{ST}_y(\varphi))$.
Its step in part 2 is the dual of steps 10 and 11.
