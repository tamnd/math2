---
tag: JS8W7PA6JK
kind: definition
name: Normal modal logic K
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
defines: D1TJYZZDCY
uses: [G8VGTW9P4F, 05006AJ7DZ, 0Y0MQYST0M, 1MGMQX43B8, QPD3X471Q1]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_modal_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
---

## Definition

A normal modal logic is a set $\Lambda$ of [[modal formulas|G8VGTW9P4F]] with these five properties.

1. $\Lambda$ contains every substitution instance of a [[tautology|05006AJ7DZ]].
2. $\Lambda$ contains the axiom $\mathrm{K}$: $\square(p \to q) \to (\square p \to \square q)$.
3. Modus ponens: if $\varphi \in \Lambda$ and $\varphi \to \psi \in \Lambda$, then $\psi \in \Lambda$.
4. Necessitation: if $\varphi \in \Lambda$, then $\square\varphi \in \Lambda$.
5. Uniform substitution: if $\varphi \in \Lambda$ and $\sigma$ is a substitution, then $\varphi^\sigma \in \Lambda$.

The logic $\mathsf{K}$ is the intersection of all normal modal logics, the smallest normal modal logic.
For a set $\Gamma$ of formulas, $\mathsf{K}\Gamma$ is the smallest normal modal logic that contains $\Gamma$.

## Notation

We write $\Lambda \vdash \varphi$ for $\varphi \in \Lambda$.
As a [[Hilbert system|1MGMQX43B8]], $\mathsf{K}\Gamma$ has the axioms: all tautology instances, all instances of $\mathrm{K}$ and all instances of the formulas in $\Gamma$.
Its [[rules of inference|QPD3X471Q1]] are [[modus ponens|0Y0MQYST0M]] and necessitation.
With instances as axioms, uniform substitution becomes an admissible rule of this system, and $\mathsf{K}\Gamma$ is its set of theorems.
The name $\mathsf{K}$ honours Kripke, and the axiom $\mathrm{K}$ is also called the distribution axiom.

## Remarks

1. The intersection of normal logics is normal, so $\mathsf{K}$ and $\mathsf{K}\Gamma$ exist.
2. Rule RM: if $\Lambda \vdash \varphi \to \psi$, then $\Lambda \vdash \square\varphi \to \square\psi$; apply necessitation, then an instance of $\mathrm{K}$ and modus ponens.
3. Rule RE: if $\Lambda \vdash \varphi \leftrightarrow \psi$, then $\Lambda \vdash \square\varphi \leftrightarrow \square\psi$; apply RM in both directions.
4. Rule RK: if $\Lambda \vdash (\varphi_1 \wedge \dots \wedge \varphi_n) \to \psi$, then $\Lambda \vdash (\square\varphi_1 \wedge \dots \wedge \square\varphi_n) \to \square\psi$; for $n = 0$ this is necessitation, and the step from $n$ to $n + 1$ uses $\mathrm{K}$ once.
5. Duality: $\Lambda \vdash \square\varphi \leftrightarrow \neg\lozenge\neg\varphi$, since $\neg\lozenge\neg\varphi$ is $\neg\neg\square\neg\neg\varphi$ and RE replaces $\neg\neg\varphi$ by $\varphi$.
6. Dual rule: if $\Lambda \vdash \varphi \to \psi$, then $\Lambda \vdash \lozenge\varphi \to \lozenge\psi$; apply RM to $\neg\psi \to \neg\varphi$ and contrapose.
7. By RE and induction on formulas, provably equivalent subformulas can be replaced inside any formula.
8. $\mathsf{K}$ is the set of formulas valid on all frames. Soundness is [[soundness of normal modal logics|E87G6ZTMTN]] and completeness is [[completeness of K, T, D, K4, S4, B and S5|FXTCKYR3AQ]].
9. Examples are [[the derivation of box over conjunction|S860E9DNXA]] and [[the trivial and verum logics|5PZCVXYXDD]]; the full discussion is in [[normal modal logic|D1TJYZZDCY]].

## Explanations

### L1 human

The logic $\mathsf{K}$ is the weakest reasonable set of laws for "necessarily".
It has the laws of ordinary logic and one extra law: if "$p$ implies $q$" is necessary and $p$ is necessary, then $q$ is necessary.
It also has the rule that each proved law is necessary.
It says nothing more, for example nothing about whether necessary things are true.

### L2 human

We derive $\lozenge p \wedge \square q \to \lozenge(p \wedge q)$ in $\mathsf{K}$.

1. The formula $q \to (\neg(p \wedge q) \to \neg p)$ is a tautology.
2. Rule RK with $n = 2$ applied to $(q \wedge \neg(p \wedge q)) \to \neg p$ gives $(\square q \wedge \square\neg(p \wedge q)) \to \square\neg p$.
3. Propositional reasoning turns this into $(\square q \wedge \neg\square\neg p) \to \neg\square\neg(p \wedge q)$.
4. By the definition of $\lozenge$, this is $(\square q \wedge \lozenge p) \to \lozenge(p \wedge q)$.

The typical use of RK is to move a propositional law under the box.
A trap: RK needs a theorem as its premise; it does not apply to a formula that holds only in one model.

### L3 human

The rules RM, RE and RK say that $\square$ acts as a meet-preserving map on the Lindenbaum algebra of $\Lambda$.
In a Gentzen system for $\mathsf{K}$, the rule that introduces $\square$ on both sides of a sequent at once plays the role of RK.
In this system, cut elimination gives the subformula property.
