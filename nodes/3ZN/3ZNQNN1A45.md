---
tag: 3ZNQNN1A45
kind: definition
name: Exchange
msc: ["03F05", "03B47"]
topics: [98QF5J4W16]
audience: grad
defines: YAFD18WYJ8
uses: [PZX9J3VEMT, S9Z6PKTXAS]
sources:
  - url: https://en.wikipedia.org/wiki/Structural_rule
    locator: Common structural rules
  - url: https://plato.stanford.edu/entries/logic-substructural/
    locator: 1.2 Commutativity
    note: Restall, Substructural Logics, Stanford Encyclopedia of Philosophy, revision of 2024-08-15
  - book: isbn:9780444521415
    note: Galatos, Jipsen, Kowalski and Ono, Residuated Lattices
---

## Definition

Let $\Gamma$, $\Gamma'$, $\Delta$ and $\Delta'$ be finite lists of formulas and $A$, $B$ formulas.
*Exchange* is any of the following structural rules.

1. Left exchange: from $\Gamma, A, B, \Gamma' \Rightarrow \Delta$ infer $\Gamma, B, A, \Gamma' \Rightarrow \Delta$.
2. Right exchange: from $\Gamma \Rightarrow \Delta, A, B, \Delta'$ infer $\Gamma \Rightarrow \Delta, B, A, \Delta'$.

A calculus *has exchange* if these rules are rules of the calculus.
Repeated exchange gives every permutation of the antecedent, since adjacent transpositions generate the symmetric group.
So in a calculus with exchange, the antecedent and the succedent can be read as multisets.

## Notation

In [[LK|PZX9J3VEMT]] the rules are named XL and XR.
In the full Lambek calculus, $\mathsf{FL}_e$ is $\mathsf{FL}$ with left exchange.
In Hilbert systems, the axiom $(A \to (B \to C)) \to (B \to (A \to C))$ plays the role of exchange.

## Remarks

### Commutativity of fusion

Interpret a sequent $A_1, \dots, A_n \Rightarrow C$ of the full Lambek calculus in a [[residuated lattice|S9Z6PKTXAS]] as $a_1 \cdot \ldots \cdot a_n \leq c$.
Claim: left exchange preserves validity in every interpretation in the lattice if and only if fusion is commutative.

1. Assume $x \cdot y = y \cdot x$ for all $x, y$.
   Let $g$ and $g'$ be the products of $\Gamma$ and $\Gamma'$, and let $g \cdot a \cdot b \cdot g' \leq c$.
2. By commutativity, $g \cdot b \cdot a \cdot g' = g \cdot a \cdot b \cdot g' \leq c$.
3. Conversely, the sequent $A, B \Rightarrow A \cdot B$ follows from two axioms by the right rule for fusion, and it is valid.
4. Left exchange gives $B, A \Rightarrow A \cdot B$.
   If exchange preserves validity, then $b \cdot a \leq a \cdot b$ for all values $a$ and $b$.
5. Exchanging the roles of $a$ and $b$ gives $a \cdot b \leq b \cdot a$, so $a \cdot b = b \cdot a$.

### The two residuals

In a residuated lattice, $x \backslash y$ is the largest $z$ with $x \cdot z \leq y$, and $y / x$ is the largest $z$ with $z \cdot x \leq y$.
If fusion is commutative, then $x \cdot z \leq y$ if and only if $z \cdot x \leq y$, so $x \backslash y = y / x$.
For this reason a logic with exchange has one implication, and a logic without exchange has two.

## Explanations

### L1 human

Exchange lets us swap two neighboring facts in a list of hypotheses.
With enough swaps, we can put the facts in any order.
In the algebra of a logic, the rule says that $x$ times $y$ equals $y$ times $x$.

### L2 human

We check exchange in the residuated lattice of languages over the alphabet $\set{a, b}$, ordered by inclusion, with concatenation as fusion.

1. Let $A$ have value $\set{a}$, let $B$ have value $\set{b}$, and let $C$ have value $\set{ab}$.
2. The sequent $A, B \Rightarrow C$ says $\set{a} \cdot \set{b} \subseteq \set{ab}$, which is true.
3. Exchange gives $B, A \Rightarrow C$, which says $\set{ba} \subseteq \set{ab}$.
   This is false.
4. So exchange is not sound in this lattice, because concatenation of words is not commutative.

The typical use is to recognize a non-commutative logic from its algebras.
A trap: a lattice with commutative meet can still have a non-commutative fusion, as here.
