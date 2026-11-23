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

We define the normal modal logics as sets of formulas, and $\mathsf{K}$ as the smallest of them.

A *normal modal logic* is a set $\Lambda$ of [[modal formulas|G8VGTW9P4F]] with these five properties.

1. $\Lambda$ contains every substitution instance of a [[tautology|05006AJ7DZ]].
2. $\Lambda$ contains the axiom $\mathrm{K}$, the formula $\square(p \to q) \to (\square p \to \square q)$.
3. Modus ponens: if $\varphi \in \Lambda$ and $\varphi \to \psi \in \Lambda$, then $\psi \in \Lambda$.
4. Necessitation: if $\varphi \in \Lambda$, then $\square\varphi \in \Lambda$.
5. Uniform substitution: if $\varphi \in \Lambda$ and $\sigma$ is a substitution, then $\varphi^\sigma \in \Lambda$.

The logic $\mathsf{K}$ is the intersection of all normal modal logics, which is the smallest normal modal logic.
For a set $\Gamma$ of formulas, $\mathsf{K}\Gamma$ is the smallest normal modal logic that contains $\Gamma$.

## Notation

We write $\Lambda \vdash \varphi$ for $\varphi \in \Lambda$.
As a [[Hilbert system|1MGMQX43B8]], $\mathsf{K}\Gamma$ has as axioms all tautology instances, all instances of $\mathrm{K}$ and all instances of the formulas in $\Gamma$.
Its [[rules of inference|QPD3X471Q1]] are [[modus ponens|0Y0MQYST0M]] and necessitation.
With instances as axioms, uniform substitution becomes an admissible rule of this system, and $\mathsf{K}\Gamma$ is its set of theorems.
The name $\mathsf{K}$ honors Kripke, and the axiom $\mathrm{K}$ is also called the distribution axiom.

## Remarks

### Reading the conditions

Conditions 1, 3 and 5 make $\Lambda$ a modal logic, so they keep classical reasoning and make theorems into schemas.
Condition 2 lets the box pass through an implication, and condition 4 says that every theorem is necessary.
Together, 2 and 4 make the box act as "true at every alternative", which is why every [[Kripke frame|NGHWZ9Y7ZV]] validates a normal logic of this kind.
The intersection of normal logics is again normal, because each condition survives intersection, so $\mathsf{K}$ and $\mathsf{K}\Gamma$ exist.

### The derived rules

Three derived rules carry most of the work in derivations.
Rule RM says that $\Lambda \vdash \varphi \to \psi$ gives $\Lambda \vdash \square\varphi \to \square\psi$: apply necessitation, then an instance of $\mathrm{K}$ and modus ponens.
Rule RE says that $\Lambda \vdash \varphi \leftrightarrow \psi$ gives $\Lambda \vdash \square\varphi \leftrightarrow \square\psi$: apply RM in both directions.
Rule RK says that $\Lambda \vdash (\varphi_1 \wedge \dots \wedge \varphi_n) \to \psi$ gives $\Lambda \vdash (\square\varphi_1 \wedge \dots \wedge \square\varphi_n) \to \square\psi$.
For $n = 0$ it is necessitation, and each step from $n$ to $n + 1$ uses $\mathrm{K}$ once.

The dual rule for the diamond follows: $\Lambda \vdash \varphi \to \psi$ gives $\Lambda \vdash \lozenge\varphi \to \lozenge\psi$, by RM on $\neg\psi \to \neg\varphi$ and contraposition.
By RE and induction on formulas, we may replace a subformula by a provably equivalent one anywhere inside a formula.

### A non-example and the semantics

The set of tautology instances satisfies conditions 1, 3 and 5, and it fails condition 2, since $\mathrm{K}$ is not a tautology when $\square(p \to q)$, $\square p$ and $\square q$ are read as three letters.
$\mathsf{K}$ is the set of formulas valid on all frames: [[soundness of normal modal logics|E87G6ZTMTN]] gives one inclusion, and [[completeness of K, T, D, K4, S4, B and S5|FXTCKYR3AQ]] gives the other.
The concept page [[normal modal logic|D1TJYZZDCY]] has the examples, including [[box over conjunction|S860E9DNXA]] and [[the trivial and verum logics|5PZCVXYXDD]].

## Explanations

### L1 human

The logic $\mathsf{K}$ is the weakest reasonable set of laws for "necessarily".
It has the laws of ordinary logic and one extra law: if "$p$ implies $q$" is necessary and $p$ is necessary, then $q$ is necessary.
It also has the rule that each proved law is necessary.
It says nothing more, for example nothing about whether necessary things are true.

### L2 human

We derive $(\lozenge p \wedge \square q) \to \lozenge(p \wedge q)$ in $\mathsf{K}$.
The formula $(q \wedge \neg(p \wedge q)) \to \neg p$ is a tautology, since $q$ and $\neg(p \wedge q)$ together rule out $p$.
Rule RK with $n = 2$ gives the following theorem:
$$(\square q \wedge \square\neg(p \wedge q)) \to \square\neg p.$$
Propositional reasoning turns it into $(\square q \wedge \neg\square\neg p) \to \neg\square\neg(p \wedge q)$.
By the definition of $\lozenge$, this is $(\square q \wedge \lozenge p) \to \lozenge(p \wedge q)$.
The typical use of RK is to move a propositional law under the box.
Watch out: RK needs a theorem as its premise, and it does not apply to a formula that holds only in one model.

### L3 human

The rules RM, RE and RK say that $\square$ acts as a map that preserves finite meets on the Lindenbaum algebra of $\Lambda$.
In a Gentzen system for $\mathsf{K}$, the rule that adds a box to every formula of a sequent at once plays the role of RK.
Cut elimination for that system gives the subformula property, and with it a decision procedure.
