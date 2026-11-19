---
tag: 52XCYMK0WW
kind: definition
name: Intuitionistic logic
msc: ["03B20", "03F55"]
topics: [38EQ20GR7M]
audience: grad
defines: Q11N8X99FK
uses: [09K9MWD2QQ, 1MGMQX43B8, 0Y0MQYST0M, 0RYYK8PG4S]
sources:
  - url: https://en.wikipedia.org/wiki/Intuitionistic_logic
  - url: https://en.wikipedia.org/wiki/Intuitionistic_logic
    locator: Hilbert-style calculus
  - url: https://plato.stanford.edu/entries/logic-intuitionistic/
    locator: The formal systems H-IPC and H-IQC
---

## Definition

The formulas of intuitionistic propositional logic are built from propositional variables and $\bot$ with $\wedge$, $\vee$ and $\to$.
The negation $\neg\varphi$ abbreviates $\varphi \to \bot$.
*Intuitionistic propositional logic* $\mathsf{IPC}$ is the set of formulas derivable in the [[Hilbert system|1MGMQX43B8]] with the following axiom schemes, for all formulas $\varphi$, $\psi$, $\chi$.

1. $\varphi \to (\psi \to \varphi)$.
2. $(\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi))$.
3. $\varphi \wedge \psi \to \varphi$ and $\varphi \wedge \psi \to \psi$.
4. $\varphi \to (\psi \to \varphi \wedge \psi)$.
5. $\varphi \to \varphi \vee \psi$ and $\psi \to \varphi \vee \psi$.
6. $(\varphi \to \chi) \to ((\psi \to \chi) \to (\varphi \vee \psi \to \chi))$.
7. $\bot \to \varphi$.

The only rule is [[modus ponens|0Y0MQYST0M]]: from $\varphi$ and $\varphi \to \psi$, derive $\psi$.
For a set $\Gamma$ of formulas, $\Gamma \vdash_{\mathsf{i}} \varphi$ means that $\varphi$ has a derivation from axioms and members of $\Gamma$ by modus ponens.

## Notation

$\mathsf{IPC}$ is also written $\mathsf{Int}$ or $\mathsf{IL}$, and $\vdash_{\mathsf{i}}$ is also written $\vdash_{\mathsf{IPC}}$.
Some authors take $\neg$ as primitive, with the axioms $(\varphi \to \psi) \to ((\varphi \to \neg\psi) \to \neg\varphi)$ and $\neg\varphi \to (\varphi \to \psi)$ in place of axiom 7.
Both choices give the same theorems after the translation $\neg\varphi \mapsto \varphi \to \bot$.

## Remarks

1. Axioms 1 to 6 with modus ponens form positive intuitionistic logic. Axiom 7 is the principle of [[explosion|TTKZGJEEK7]].
2. Dropping axiom 7 gives [[minimal logic|3MBG95617E]]. Adding the [[law of excluded middle|0RYYK8PG4S]] $\varphi \vee \neg\varphi$ gives classical [[propositional logic|09K9MWD2QQ]].
3. The [[deduction theorem|9X08XK5RV2]] holds: $\Gamma, \varphi \vdash_{\mathsf{i}} \psi$ if and only if $\Gamma \vdash_{\mathsf{i}} \varphi \to \psi$. Its proof uses only axioms 1 and 2.
4. $\mathsf{IPC}$ is closed under uniform substitution, since each axiom is a scheme.
5. Intuitionistic predicate logic $\mathsf{IQC}$ adds the quantifier axioms $\forall x \varphi \to \varphi[t/x]$ and $\varphi[t/x] \to \exists x \varphi$, and two rules. From $\psi \to \varphi$ derive $\psi \to \forall x\varphi$, and from $\varphi \to \psi$ derive $\exists x\varphi \to \psi$, when $x$ is not free in $\psi$.
6. The natural deduction system $\mathrm{NJ}$ has the introduction and elimination rules for $\wedge$, $\vee$, $\to$ and the rule "from $\bot$ infer $\varphi$". It has no rule of reductio ad absurdum. The sequent calculus $\mathrm{LJ}$ is $\mathrm{LK}$ with at most one formula on the right of each sequent. Both derive exactly the theorems of $\mathsf{IPC}$.
7. Example: $\varphi \to \neg\neg\varphi$ is derivable. By the deduction theorem it suffices to derive $\bot$ from $\varphi$ and $\varphi \to \bot$, which is one step of modus ponens.
8. Non-example: $p \vee \neg p$ is not derivable for a variable $p$. In the [[Kripke model|35VKJY77TY]] with worlds $u \le v$ and $p$ true only at $v$, neither $p$ nor $\neg p$ holds at $u$; see [[the two-point countermodel|8BKRJ0KPVD]].

## Explanations

### L1 human

The definition lists seven kinds of starting laws and one rule.
The rule says: if $A$ is proved and "if $A$ then $B$" is proved, then $B$ is proved.
The laws are those of ordinary logic, except that "$A$ or not $A$" is not among them and can not be derived.
For example, the law "if $A$ and $B$, then $A$" is axiom 3.

### L2 human

We derive $\varphi \to \varphi$ in the Hilbert system.

1. Axiom 2 with $\psi := \varphi \to \varphi$ and $\chi := \varphi$ gives $(\varphi \to ((\varphi \to \varphi) \to \varphi)) \to ((\varphi \to (\varphi \to \varphi)) \to (\varphi \to \varphi))$.
2. Axiom 1 with $\psi := \varphi \to \varphi$ gives $\varphi \to ((\varphi \to \varphi) \to \varphi)$.
3. Modus ponens on steps 2 and 1 gives $(\varphi \to (\varphi \to \varphi)) \to (\varphi \to \varphi)$.
4. Axiom 1 with $\psi := \varphi$ gives $\varphi \to (\varphi \to \varphi)$.
5. Modus ponens on steps 4 and 3 gives $\varphi \to \varphi$.

The typical use of the Hilbert system is in metatheorems, such as soundness, where few axioms mean few cases.
A trap: derivations in this system are long, so in practice one derives formulas in natural deduction and uses the equivalence of the systems.

### L3 human

The Hilbert system for $\mathsf{IPC}$ is the classical one without excluded middle, and its theorems are exactly the formulas valid in all [[Heyting algebras|NG943XNQWH]].
Every [[intermediate logic|H5NSKEP3P2]] is obtained by adding axiom schemes to this system and closing under modus ponens and substitution.
Proof-theoretic properties, such as cut elimination and the [[disjunction property|YTRVX6F3FX]], are easier to see in $\mathrm{LJ}$, where the single formula on the right blocks the classical derivation of $p \vee \neg p$.
