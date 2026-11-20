---
tag: JNYY1WD8SR
kind: definition
name: Weakening
msc: ["03F05", "03B47"]
topics: [98QF5J4W16]
audience: grad
defines: VHRXX0T5XT
uses: [PZX9J3VEMT, S9Z6PKTXAS]
sources:
  - url: https://en.wikipedia.org/wiki/Structural_rule
    locator: Common structural rules
  - url: https://plato.stanford.edu/entries/logic-substructural/
    locator: 1.1 Weakening
    note: Restall, Substructural Logics, Stanford Encyclopedia of Philosophy, revision of 2024-08-15
  - book: isbn:9780444521415
    note: Galatos, Jipsen, Kowalski and Ono, Residuated Lattices
---

## Definition

Let $\Gamma$, $\Gamma'$ and $\Delta$ be finite lists of formulas and $A$, $C$ formulas.
*Weakening* is any of the following structural rules.

1. Left weakening, for two-sided sequents: from $\Gamma, \Gamma' \Rightarrow \Delta$ infer $\Gamma, A, \Gamma' \Rightarrow \Delta$.
2. Right weakening, for two-sided sequents: from $\Gamma \Rightarrow \Delta$ infer $\Gamma \Rightarrow \Delta, A$.
   In a calculus with at most one formula on the right, the rule is: from $\Gamma \Rightarrow$ infer $\Gamma \Rightarrow C$.
3. Weakening for one-sided sequents: from $\vdash \Gamma$ infer $\vdash \Gamma, A$.

A calculus *has weakening* if these rules are rules of the calculus, and weakening is *admissible* if adding them does not change the set of derivable sequents.
In the calculus [[LK|PZX9J3VEMT]] the rules are WL and WR, with $A$ added at the left end or the right end.

## Notation

In linear logic, weakening is allowed only for formulas $?A$ in one-sided sequents, and the rule is named $?W$.
In the full Lambek calculus, $\mathsf{FL}_w$ is $\mathsf{FL}$ with rules 1 and 2.

## Remarks

**Integrality.**
Interpret a sequent $A_1, \dots, A_n \Rightarrow C$ of the full Lambek calculus in a [[residuated lattice|S9Z6PKTXAS]] with an extra constant $0$ as $a_1 \cdot \ldots \cdot a_n \leq c$, where the empty product is $1$.
Interpret $A_1, \dots, A_n \Rightarrow$ (empty right side) as $a_1 \cdot \ldots \cdot a_n \leq 0$.
The lattice is *integral* if $x \leq 1$ for all $x$.
Claim: left weakening preserves validity in every interpretation if and only if the lattice is integral.

1. Assume integrality, and let $g \cdot g' \leq c$, where $g$ and $g'$ are the products of $\Gamma$ and $\Gamma'$.
2. Fusion is monotone in each argument, and $a \leq 1$.
   So $g \cdot a \cdot g' \leq g \cdot 1 \cdot g' = g \cdot g' \leq c$.
3. Conversely, $\Rightarrow 1$ is valid, since $1 \leq 1$.
   Left weakening turns it into $A \Rightarrow 1$.
4. If left weakening preserves validity, then $a \leq 1$ for every value $a$ of $A$, so the lattice is integral.

The same argument with the axiom $0 \Rightarrow$ shows that right weakening preserves validity if and only if $0 \leq x$ for all $x$.

**Examples and non-examples.**
Weakening derives $p \to (q \to p)$ in LJ, see [[the example|M7Z40M37TQ]], and $A \multimap (!B \multimap A)$ in linear logic, see [[the example|K428NVQY1M]].
It is not admissible in linear logic without exponentials, see [[the non-example|V1ZRAX3GBM]].

## Explanations

### L1 human

Weakening is the rule "add a fact you do not need".
If two coins buy a coffee, then two coins and a stone also buy a coffee.
The rule is harmless for truth, but it is wrong for resources that must all be spent.

### L2 human

We check integrality in the residuated lattice $(\mathbb{Z}, \leq, +, 0)$ of the integers, where fusion is addition and the unit is $0$.

1. The logical constant $1$ denotes the unit of fusion, which is the integer $0$.
2. Integrality would say $x \leq 0$ for all integers $x$.
   It fails for $x = 5$.
3. The sequent $\Rightarrow 1$ is valid, since it says $0 \leq 0$.
4. Left weakening gives $A \Rightarrow 1$.
   With $A$ valued $5$, this says $5 \leq 0$, which is false.
5. In the residuated lattice $[0, 1]$ with fusion the real product, the unit is the number $1$ and $x \leq 1$ holds.
   So left weakening is sound there.

The typical use is to read off from an algebra whether a substructural logic has weakening.
A trap: the constant $1$ of the logic is the unit of fusion, which is not always the number $1$.
