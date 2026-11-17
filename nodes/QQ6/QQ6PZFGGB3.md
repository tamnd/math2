---
tag: QQ6PZFGGB3
kind: statement
role: theorem
name: Löb's axiom in provability logic
msc: ["03F45", "03B45"]
topics: [3E7M66WW6Q]
audience: research
uses: [WJK0YA4GP2, 61THBNS8WE, C3RZY20ETK, NGHWZ9Y7ZV, G989VP2NGP, 0GJZW9JFZQ, 0DQPNJNPYK, 3HD30YG3DG]
about: [WJK0YA4GP2]
proofs: [17C5DRFAW7]
history:
  first_stated: "Löb, 1955, Solution of a problem of Leon Henkin, Journal of Symbolic Logic (the arithmetical form)"
  notes: "The modal axiom carries the formalized form of Löb's theorem into modal logic."
sources:
  - wikipedia: en:693002@r1343042369
    locator: Löb's theorem, section Löb's theorem in provability logic
    note: adopted
    mention: wikipedia://en/693002#SMBU
    sections: [Statement]
  - url: https://en.wikipedia.org/wiki/Provability_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
  - book: isbn:9780521701464
inventory: [1WWMN5M6CY]
---

## Statement

Modal formulas are built from propositional variables $p, q, \dots$ and $\bot$ with $\to$ and $\square$.
We use $\neg \varphi := \varphi \to \bot$, $\top := \neg \bot$, $\lozenge \varphi := \neg \square \neg \varphi$, and the other connectives as abbreviations.
The [[modal logic|C3RZY20ETK]] $\mathsf{K}$ has all tautologies and the axiom $\mathrm{K}$: $\square(p \to q) \to (\square p \to \square q)$.
Its rules are modus ponens, the [[necessitation rule|G989VP2NGP]] (from $\varphi$ infer $\square \varphi$) and uniform substitution.
Löb's axiom is the formula
$$\mathrm{L}: \quad \square(\square p \to p) \to \square p.$$
The logic $\mathsf{GL}$ of [[provability logic|WJK0YA4GP2]] is $\mathsf{K}$ with the extra axiom $\mathrm{L}$; see its [[definition|61THBNS8WE]].
A frame $(W, R)$ is a nonempty set $W$ with a relation $R$, and a formula is valid on it when it is true at every world under every valuation, as in [[Kripke semantics|NGHWZ9Y7ZV]].
The relation $R$ is conversely well-founded when every nonempty $X \subseteq W$ has an $R$-maximal element: some $x \in X$ such that no $y \in X$ has $x R y$.

1. Axiom 4 follows from Löb's axiom: $\mathsf{K} + \mathrm{L} \vdash \square p \to \square \square p$. Hence $\mathsf{GL}$ is also $\mathsf{K4}$ with the extra axiom $\mathrm{L}$.
2. Löb's rule: for every formula $\varphi$, if $\mathsf{GL} \vdash \square \varphi \to \varphi$, then $\mathsf{GL} \vdash \varphi$.
3. Frame condition: $\mathrm{L}$ is valid on a frame $(W, R)$ if and only if $R$ is [[transitive|0GJZW9JFZQ]] and conversely [[well-founded|0DQPNJNPYK]].

The proof is in [[the proof of the properties of Löb's axiom|17C5DRFAW7]].

## Remarks

### Why each hypothesis is needed

1. Transitivity in part 3. Take $W = \set{a, b, c}$ with $a R b$ and $b R c$ only. The relation is conversely well-founded, since there are no cycles in a finite set. Put $p$ true only at $a$. Then $b \not\models \square p$, so $b \models \square p \to p$ and $a \models \square(\square p \to p)$, while $a \not\models \square p$. So $\mathrm{L}$ fails at $a$.
2. Converse well-foundedness in part 3. Take one world $a$ with $a R a$, and $p$ false at $a$. Then $\square p$ is false at $a$, so $\square p \to p$ is true at $a$ and $a \models \square(\square p \to p)$, while $a \not\models \square p$.
3. Irreflexivity is not enough. On $(\N, <)$, which is transitive and irreflexive, put $p$ false everywhere. Every $n$ has a successor, so $\square p$ is false everywhere, $\square p \to p$ is true everywhere, and $\mathrm{L}$ fails at every $n$.
4. Löb's axiom in part 1. Without it, $\mathsf{K} \nvdash \square p \to \square \square p$: in the frame of item 1 with $p$ true only at $b$, we get $a \models \square p$ and $b \not\models \square p$, so $a \not\models \square \square p$.

### Consequences

1. $\mathsf{GL} \nvdash \square p \to p$. On one world with an empty relation and $p$ false, $\square p$ is true and $p$ is false; this frame validates $\mathsf{GL}$ by part 3.
2. Adding the axiom $\square p \to p$ to $\mathsf{GL}$ gives an inconsistent logic. The instance $\square \bot \to \bot$ and Löb's rule give $\bot$.
3. $\mathsf{GL} \vdash \neg \square \bot \to \neg \square \neg \square \bot$, the modal form of the [[second incompleteness theorem|4PZM5GJTR5]]; see [[the formalized second incompleteness theorem in GL|3K967QR766]].
4. Every frame that validates $\mathrm{L}$ is irreflexive, since a world $w$ with $w R w$ makes $\set{w}$ a set without a maximal element.
5. By part 3 and the [[Kripke completeness of GL|1DMFNR7FZT]], $\mathsf{GL}$ is the logic of the transitive conversely well-founded frames, and also of the finite transitive irreflexive frames.

### Converse

The converse of part 1 is false: $\mathsf{K4} \nvdash \mathrm{L}$.
The one-world reflexive frame is transitive, so it validates axiom 4, and item 2 above shows that it refutes $\mathrm{L}$.
The converse of part 2 holds: if $\mathsf{GL} \vdash \varphi$, then $\mathsf{GL} \vdash \square \varphi \to \varphi$ by propositional logic.

### Generalizations

1. Under the arithmetical reading, $\mathrm{L}$ is the formalized [[Löb's theorem|3HD30YG3DG]]: $\mathsf{PA} \vdash \square(\square \varphi \to \varphi) \to \square \varphi$ for every sentence $\varphi$.
2. In [[Grzegorczyk logic|2Q8E4GQF3B]] the axiom $\square(\square(p \to \square p) \to p) \to p$ plays the same role for reflexive frames.
3. In [[Japaridze's polymodal logic GLP|3EDRQJJHMT]] each of the operators $[n]$ satisfies Löb's axiom.

## History

Löb proved the formalized form of his theorem for arithmetic in 1955.
The modal system $\mathsf{GL}$, named after Gödel and Löb, was studied as a modal logic in the 1970s, when Solovay showed that it is exactly the provability logic of $\mathsf{PA}$.

## Explanations

### L1 human

Think of $\square p$ as "$p$ can be proved".
Löb's axiom says: if it can be proved that "a proof of $p$ would make $p$ true", then $p$ can be proved.
A theory that proves its own trustworthiness about $p$ has, in fact, already proved $p$.
In pictures, the axiom holds on diagrams of arrows that never loop back and never go on forever, such as $1 \to 2 \to 3$.

### L2 human

We check $\mathrm{L}$ at the world $1$ of the chain $1 R 2$, $1 R 3$, $2 R 3$, with $p$ true only at $3$.

1. The world $3$ has no successors, so $3 \models \square p$, and $3 \models \square p \to p$ because $p$ is true at $3$.
2. The world $2$ sees only $3$, so $2 \models \square p$, and $2 \not\models p$. So $2 \not\models \square p \to p$.
3. The world $1$ sees $2$, so $1 \not\models \square(\square p \to p)$, and the implication $\mathrm{L}$ is true at $1$.
4. The world $2$ sees only $3$, where $\square p \to p$ holds, so $2 \models \square(\square p \to p)$, and $2 \models \square p$ by step 2. So $\mathrm{L}$ holds at $2$.

The typical use of Löb's axiom is Löb's rule: to prove $\varphi$, prove that $\square \varphi$ implies $\varphi$.
A trap: Löb's rule needs $\square \varphi \to \varphi$ as a theorem; the formula $\square \varphi \to \varphi$ true at one world gives nothing.

### L3 human

Löb's axiom is the modal form of induction along a conversely well-founded relation: if a property holds at a world whenever it holds at all later worlds, then it holds everywhere above.
This explains part 3, and it explains why $\mathsf{GL}$ is not compact and has no canonical model completeness proof; see the [[Kripke completeness of GL|1DMFNR7FZT]].
Algebraically, the axiom defines the [[Magari algebras|YTA4C8QCB0]] among the [[Boolean algebras|0XADJKM699]] with an operator, and it is the axiom behind the [[de Jongh-Sambin fixed-point theorem|TDDX1NHG8D]].
