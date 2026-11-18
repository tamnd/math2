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

We prove [[the correctness of the standard translation|1HQ1W36J4V]].
Fix a [[Kripke model|NGHWZ9Y7ZV]] $\mathfrak{M} = (W, R, V)$, read as a first-order structure with $P_i$ interpreted as $V(p_i)$.
For a variable $z \in \set{x, y}$, write $\mathfrak{M} \models \mathrm{ST}_z(\varphi)[z \mapsto w]$ for truth under any assignment that sends $z$ to $w$.

1. Part 1, by [[structural induction|12MQ2NJ29A]] on $\varphi$, for $\mathrm{ST}_x$ and $\mathrm{ST}_y$ together. The claim for $\mathrm{ST}_x$ is: the free variables are among $\set{x}$, and all variables are among $\set{x, y}$.
2. For $p$ and $\bot$, $\mathrm{ST}_x(p) = P(x)$ and $\bot$ satisfy the claim.
3. For $\varphi \to \psi$, the free variables of an implication are those of its two sides, so the claim follows from the hypothesis for $\varphi$ and $\psi$.
4. For $\square\varphi$, the hypothesis for $\mathrm{ST}_y$ says that $\mathrm{ST}_y(\varphi)$ has free variables among $\set{y}$ and variables among $\set{x, y}$.
5. In $\forall y\,(R(x, y) \to \mathrm{ST}_y(\varphi))$, the quantifier binds $y$, and the only new free variable is the $x$ of $R(x, y)$. So the claim holds. The case of $\mathrm{ST}_y$ is the same with $x$ and $y$ exchanged.
6. By part 1, truth of $\mathrm{ST}_z(\varphi)$ depends only on the value of $z$, by the coincidence lemma of [[first-order logic|086QKPF0A6]]. So the notation $[z \mapsto w]$ is well defined.
7. Part 2, by structural induction on $\varphi$. The claim is: for all $w \in W$ and $z \in \set{x, y}$, $\mathfrak{M}, w \models \varphi$ if and only if $\mathfrak{M} \models \mathrm{ST}_z(\varphi)[z \mapsto w]$.
8. For $p_i$: $\mathfrak{M}, w \models p_i$ means $w \in V(p_i)$, and $\mathfrak{M} \models P_i(z)[z \mapsto w]$ means $w \in V(p_i)$, since $P_i$ is interpreted as $V(p_i)$. Here the interpretation of $P_i$ is used.
9. For $\bot$, both sides are false at every $w$.
10. For $\varphi \to \psi$, both sides are true exactly when the left part fails or the right part holds, and the hypothesis matches the parts.
11. For $\square\varphi$ and $z = x$: $\mathfrak{M} \models \forall y\,(R(x, y) \to \mathrm{ST}_y(\varphi))[x \mapsto w]$ holds if and only if, for every $v \in W$ with $(w, v) \in R$, $\mathfrak{M} \models \mathrm{ST}_y(\varphi)[y \mapsto v]$.
12. By the hypothesis for $\varphi$ with $z = y$, this holds if and only if $\mathfrak{M}, v \models \varphi$ for every $v$ with $w R v$. By the clause of [[Kripke semantics|6BQ71KQ6QT]], this means $\mathfrak{M}, w \models \square\varphi$.
13. The case $z = y$ is the same with $x$ and $y$ exchanged. This proves part 2.
14. Part 3. $\mathfrak{M} \models \varphi$ means $\mathfrak{M}, w \models \varphi$ for every $w \in W$. By part 2, this means $\mathfrak{M} \models \mathrm{ST}_x(\varphi)[x \mapsto w]$ for every $w$, which is the meaning of $\mathfrak{M} \models \forall x\, \mathrm{ST}_x(\varphi)$.
15. Part 4. $\mathfrak{F} \models \varphi$ means $(\mathfrak{F}, V) \models \varphi$ for every valuation $V$. The values $V(p_i)$ of the variables of $\varphi$ are what matter, since the truth of $\varphi$ depends only on them.
16. The choices of $V(p_1), \dots, V(p_n)$ correspond exactly to the choices of subsets of $W$ for $P_1, \dots, P_n$. By part 3 for each $V$, $\mathfrak{F} \models \varphi$ if and only if $\forall x\, \mathrm{ST}_x(\varphi)$ holds for every choice of the $P_i$.
17. By the semantics of monadic [[second-order logic|G6X7SZSNC5]], this is the meaning of $\mathfrak{F} \models \forall P_1 \dots \forall P_n\, \forall x\, \mathrm{ST}_x(\varphi)$.

## Idea

Each clause of the translation copies a clause of the Kripke truth definition, so the induction is a clause-by-clause match.
The only care is in the box step, where the hypothesis is used for the other variable.

## Variants

1. With a new variable at each box, the same induction works with the claim "the free variable is the one given". Part 1 then gives as many variables as the modal depth plus one.
2. One can prove part 2 for $\lozenge$ directly, as a primitive, with the clause $\exists y\,(R(x, y) \wedge \mathrm{ST}_y(\varphi))$; the step is the dual of steps 11 and 12.
