---
tag: VGS1GCM047
kind: definition
name: Contraction
msc: ["03F05", "03B47"]
topics: [98QF5J4W16]
audience: grad
defines: V0MZVC2XA9
uses: [PZX9J3VEMT, S9Z6PKTXAS]
sources:
  - url: https://en.wikipedia.org/wiki/Structural_rule
    locator: Common structural rules
  - url: https://plato.stanford.edu/entries/logic-substructural/
    locator: 1.4 Contraction
    note: Restall, Substructural Logics, Stanford Encyclopedia of Philosophy, revision of 2024-08-15
  - book: isbn:9780444521415
    note: Galatos, Jipsen, Kowalski and Ono, Residuated Lattices
---

## Definition

Let $\Gamma$, $\Gamma'$ and $\Delta$ be finite lists of formulas and $A$ a formula.
*Contraction* is any of the following structural rules.

1. Left contraction, for two-sided sequents: from $\Gamma, A, A, \Gamma' \Rightarrow \Delta$ infer $\Gamma, A, \Gamma' \Rightarrow \Delta$.
2. Right contraction, for two-sided sequents: from $\Gamma \Rightarrow \Delta, A, A$ infer $\Gamma \Rightarrow \Delta, A$.
3. Contraction for one-sided sequents: from $\vdash \Gamma, A, A$ infer $\vdash \Gamma, A$.

A calculus *has contraction* if these rules are rules of the calculus, and contraction is *admissible* if adding them does not change the set of derivable sequents.
In the calculus [[LK|PZX9J3VEMT]] the rules are CL and CR.
The two copies of $A$ must be next to each other; with exchange this is no restriction.

## Notation

In linear logic, contraction is allowed only for formulas $?A$ in one-sided sequents, and the rule is named $?C$.
In the full Lambek calculus, $\mathsf{FL}_c$ is $\mathsf{FL}$ with left contraction.
In Hilbert systems, the axiom $(A \to (A \to B)) \to (A \to B)$ plays the role of contraction.

## Remarks

### Square-increasing algebras

Interpret a sequent $A_1, \dots, A_n \Rightarrow C$ of the full Lambek calculus in a [[residuated lattice|S9Z6PKTXAS]] as $a_1 \cdot \ldots \cdot a_n \leq c$, where the empty product is $1$.
The lattice is *square-increasing* if $x \leq x \cdot x$ for all $x$.
Claim: left contraction preserves validity in every interpretation in the lattice if and only if the lattice is square-increasing.

1. Assume $x \leq x \cdot x$ for all $x$.
   Let $g$ and $g'$ be the products of $\Gamma$ and $\Gamma'$, and let $g \cdot a \cdot a \cdot g' \leq c$.
2. Fusion is monotone in each argument, and $a \leq a \cdot a$.
   So $g \cdot a \cdot g' \leq g \cdot a \cdot a \cdot g' \leq c$.
3. Conversely, the sequent $A, A \Rightarrow A \cdot A$ follows from two axioms by the right rule for fusion.
   It is valid, since it says $a \cdot a \leq a \cdot a$.
4. Left contraction turns it into $A \Rightarrow A \cdot A$.
   If contraction preserves validity, then $a \leq a \cdot a$ for every value $a$ of $A$.

### Examples and non-examples

In a Heyting algebra, fusion is meet, and $x \leq x \wedge x$ holds, so contraction is sound.
In the residuated lattice $(\mathbb{Z}, \leq, +, 0)$, the inequality $x \leq x + x$ fails for $x = -1$, so contraction is not sound.
Contraction drives [[Curry's paradox|40Q1NK471S]], and linear logic keeps it for $?$-formulas, see [[controlled contraction|9ZMEDB2YP4]].

## Explanations

### L1 human

Contraction is the rule "two copies of a fact are as good as one copy".
If we know that it rains, then knowing it twice adds nothing.
For resources the rule is false: two tickets are not one ticket.

### L2 human

We check contraction in the residuated lattice $(\mathbb{Z}, \leq, +, 0)$, where fusion is addition and the unit is $0$.

1. Take $A$ with value $-1$ and $C$ with value $-2$.
2. The sequent $A, A \Rightarrow C$ says $(-1) + (-1) \leq -2$, which is true.
3. Contraction gives $A \Rightarrow C$, which says $-1 \leq -2$.
   This is false.
4. So contraction fails, and the reason is that $-1 \leq -2$ fails, that is, $x \leq x + x$ fails at $x = -1$.
5. For values $x \geq 0$ the inequality $x \leq x + x$ holds, so the failure needs a negative value.

The typical use is to read off from an algebra whether a substructural logic has contraction.
A trap: weakening and contraction are independent, and $\mathbb{Z}$ refutes both, with $x = 5$ for weakening and $x = -1$ for contraction.
