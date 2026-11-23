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

Löb's axiom makes axiom 4 redundant, gives a rule for proving formulas, and holds exactly on the frames that are transitive and have no infinite forward path.

Modal formulas are built from propositional variables $p, q, \dots$ and $\bot$ with $\to$ and $\square$.
We use $\neg \varphi := \varphi \to \bot$, $\top := \neg \bot$, $\lozenge \varphi := \neg \square \neg \varphi$, and the other connectives as abbreviations.
The [[modal logic|C3RZY20ETK]] $\mathsf{K}$ has all tautologies and the axiom K, which is $\square(p \to q) \to (\square p \to \square q)$.
Its rules are modus ponens, the [[necessitation rule|G989VP2NGP]] (from $\varphi$ infer $\square \varphi$) and uniform substitution.
Löb's axiom is the following formula:
$$\mathrm{L}: \quad \square(\square p \to p) \to \square p.$$
The logic $\mathsf{GL}$ of [[provability logic|WJK0YA4GP2]] is $\mathsf{K}$ with the extra axiom $\mathrm{L}$, as in its [[definition|61THBNS8WE]].
A frame $(W, R)$ is a nonempty set $W$ with a relation $R$, and a formula is valid on it when it is true at every world under every valuation, as in [[Kripke semantics|NGHWZ9Y7ZV]].
The relation $R$ is conversely well-founded when every nonempty $X \subseteq W$ has an $R$-maximal element, that is, some $x \in X$ such that no $y \in X$ has $x R y$.

1. Axiom 4 follows from Löb's axiom: $\mathsf{K} + \mathrm{L} \vdash \square p \to \square \square p$.
   Hence $\mathsf{GL}$ is also $\mathsf{K4}$ with the extra axiom $\mathrm{L}$.
2. Löb's rule: for every formula $\varphi$, if $\mathsf{GL} \vdash \square \varphi \to \varphi$, then $\mathsf{GL} \vdash \varphi$.
3. Frame condition: $\mathrm{L}$ is valid on a frame $(W, R)$ if and only if $R$ is [[transitive|0GJZW9JFZQ]] and conversely [[well-founded|0DQPNJNPYK]].

The proof is in [[the proof of the properties of Löb's axiom|17C5DRFAW7]].

## Remarks

### The second incompleteness theorem as an instance

Substitute $\bot$ for $p$ in Löb's axiom.
Since $\square \bot \to \bot$ is the formula $\neg \square \bot$, the instance reads as follows:
$$\square \neg \square \bot \to \square \bot.$$
Under the arithmetical reading, $\neg \square \bot$ is the consistency statement, so the instance says "if $T$ proves its own consistency, then $T$ is inconsistent".
That is the [[second incompleteness theorem|4PZM5GJTR5]], and its contrapositive is worked out in [[the formalized second incompleteness theorem in GL|3K967QR766]].
In general, under the arithmetical reading $\mathrm{L}$ is the formalized [[Löb's theorem|3HD30YG3DG]], $\mathsf{PA} \vdash \square(\square \varphi \to \varphi) \to \square \varphi$ for every sentence $\varphi$.

### A frame where Löb's axiom holds

Take the chain with worlds $1, 2, 3$ and arrows $1 R 2$, $1 R 3$ and $2 R 3$, and let $p$ be true only at $3$.
World $3$ has no successors, so $\square p$ is true there, and $\square p \to p$ is true because $p$ is true at $3$.
World $2$ sees only $3$, so $\square p$ is true at $2$ while $p$ is false, and $\square p \to p$ fails at $2$.
At world $1$, the premise $\square(\square p \to p)$ fails because $1$ sees $2$, so $\mathrm{L}$ holds at $1$.
At world $2$, the premise holds, since $2$ sees only $3$, and the conclusion $\square p$ holds too.
Check: the frame is transitive and finite without loops, so part 3 says $\mathrm{L}$ holds under every valuation, as here.

### Why each hypothesis is needed

Transitivity is needed in part 3.
Take $W = \{ a, b, c \}$ with $a R b$ and $b R c$ only, which has no cycles and so is conversely well-founded.
Put $p$ true only at $a$.
Then $b \not\models \square p$, so $b \models \square p \to p$ and $a \models \square(\square p \to p)$, while $a \not\models \square p$.

Converse well-foundedness is needed too.
Take one world $a$ with $a R a$ and $p$ false at $a$.
Then $\square p$ is false at $a$, so $\square p \to p$ is true at $a$ and $a \models \square(\square p \to p)$, while $a \not\models \square p$.

### Watch out

Irreflexivity is not a substitute for converse well-foundedness.
On $(\mathbb{N}, <)$, which is transitive and irreflexive, put $p$ false everywhere.
Every $n$ has a successor, so $\square p$ is false everywhere, $\square p \to p$ is true everywhere, and $\mathrm{L}$ fails at every $n$.
Löb's rule has a trap of its own: it needs $\square \varphi \to \varphi$ as a theorem, and the formula being true at one world gives nothing.

### What it gives you

Without Löb's axiom, $\mathsf{K} \nvdash \square p \to \square \square p$.
In the frame $a R b R c$ above with $p$ true only at $b$, we get $a \models \square p$ and $b \not\models \square p$, so $a \not\models \square \square p$.
So part 1 is a real gain.

$\mathsf{GL}$ does not prove $\square p \to p$.
On one world with an empty relation and $p$ false, $\square p$ is true and $p$ is false, and this frame validates $\mathsf{GL}$ by part 3.
Worse, adding $\square p \to p$ to $\mathsf{GL}$ gives an inconsistent logic, because the instance $\square \bot \to \bot$ and Löb's rule give $\bot$.

Every frame that validates $\mathrm{L}$ is irreflexive, since a world $w$ with $w R w$ makes $\{ w \}$ a set without a maximal element.
By part 3 and the [[Kripke completeness of GL|1DMFNR7FZT]], $\mathsf{GL}$ is the logic of the transitive conversely well-founded frames, and also of the finite transitive irreflexive frames.

### The converse

The converse of part 1 is false: $\mathsf{K4} \nvdash \mathrm{L}$.
The one-world reflexive frame is transitive, so it validates axiom 4, and it refutes $\mathrm{L}$ as shown above.
The converse of part 2 holds: if $\mathsf{GL} \vdash \varphi$, then $\mathsf{GL} \vdash \square \varphi \to \varphi$ by propositional logic.

### Generalizations

In [[Grzegorczyk logic|2Q8E4GQF3B]] the axiom $\square(\square(p \to \square p) \to p) \to p$ plays the same role for reflexive frames.
In [[Japaridze's polymodal logic GLP|3EDRQJJHMT]] each of the operators $[n]$ satisfies Löb's axiom.

## History

Löb proved the formalized form of his theorem for arithmetic in 1955, in answer to a question of Henkin.
Segerberg proved in 1971 that $\mathsf{GL}$ is complete for the finite transitive irreflexive frames.
Solovay showed in 1976 that $\mathsf{GL}$ is exactly the provability logic of $\mathsf{PA}$.

## Explanations

### L1 human

Think of $\square p$ as "$p$ can be proved".
Löb's axiom says: if it can be proved that "a proof of $p$ would make $p$ true", then $p$ can be proved.
A theory that proves its own trustworthiness about $p$ has, in fact, already proved $p$.
In pictures, the axiom holds on diagrams of arrows that never loop back and never go on forever, such as $1 \to 2 \to 3$.

### L2 human

The typical use of Löb's axiom is Löb's rule: to prove $\varphi$, prove that $\square \varphi$ implies $\varphi$.
Here is the rule at work on [[Henkin's sentence|HJD67H8CXN]], a sentence $H$ with $T \vdash H \leftrightarrow \square H$.
One half of the equivalence is $T \vdash \square H \to H$.
That is exactly the premise of Löb's rule, so $T \vdash H$.
Check: the argument never asked whether $H$ is true, only that $T$ proves "if $H$ is provable, then $H$".
So Löb's rule turns a conditional promise of soundness into an outright proof.

### L3 human

Löb's axiom is the modal form of induction along a conversely well-founded relation: if a property holds at a world whenever it holds at all later worlds, then it holds everywhere above.
This explains part 3, and it explains why $\mathsf{GL}$ is not compact and has no completeness proof by the canonical model, as the [[Kripke completeness of GL|1DMFNR7FZT]] shows.
Algebraically, the axiom defines the [[Magari algebras|YTA4C8QCB0]] among the [[Boolean algebras|0XADJKM699]] with an operator, and it is the axiom behind the [[de Jongh-Sambin fixed-point theorem|TDDX1NHG8D]].
