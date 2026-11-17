---
tag: JXBSN6E2X5
kind: definition
name: Opposite structure
msc: [08A02, 20A05]
topics: [BAZT8JJ70S]
audience: ug1
defines: D33V8HE0KY
uses: [0M418FE7BB, G5S1M9]
formal:
  - system: lean4
    library: mathlib
    decl: MulOpposite
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Opposite_group
    locator: lead section
---

## Definition

Let $\cdot$ be a [[binary operation|0M418FE7BB]] on a set $S$.
The *opposite* of $(S, \cdot)$ is the pair $(S, \ast)$, where $a \ast b = b \cdot a$ for all $a, b \in S$.
For a [[group|G5S1M9]] $G$, the opposite $(G, \ast)$ is the *opposite group* $G^{\mathrm{op}}$.
For a structure with several operations, such as a ring, the opposite structure reverses the chosen multiplication and keeps all other operations and constants.

## Notation

Common notations are $S^{\mathrm{op}}$ and $S^{\circ}$.
Some texts write $a^{\mathrm{op}}$ for the element $a$ viewed in $S^{\mathrm{op}}$, so that $a^{\mathrm{op}} b^{\mathrm{op}} = (ba)^{\mathrm{op}}$.
In Mathlib, `MulOpposite α` is the opposite of a type `α` with a multiplication, and the maps `MulOpposite.op` and `MulOpposite.unop` pass between `α` and its opposite.

## Remarks

If $G$ is a group, then $G^{\mathrm{op}}$ is a group with the same identity and the same inverses.
Associativity holds, since $(a \ast b) \ast c = c(ba)$ and $a \ast (b \ast c) = (cb)a$, and these are equal in $G$.
The map $x \mapsto x^{-1}$ is an [[isomorphism|08MG7H8JW5]] from $G$ to $G^{\mathrm{op}}$, because $(xy)^{-1} = y^{-1} x^{-1} = x^{-1} \ast y^{-1}$.
The opposite of the opposite is the original structure.
The operation of $S^{\mathrm{op}}$ is equal to the operation of $S$ exactly when the operation is [[commutative|099E72KTF8]].
For the ring of real $2 \times 2$ matrices, the opposite multiplication differs from the usual one, because the matrices do not all commute.
The transpose $A \mapsto A^T$ is still an isomorphism from this ring to its [[opposite ring|M8Q24XB0AF]], because $(AB)^T = B^T A^T$.
The concept page [[opposite structure|D33V8HE0KY]] gives the examples, the non-examples, the proofs and the link with right actions.

## Explanations

### L1 human

The opposite structure keeps the same elements and reads each product backwards.
If the old rule combines $a$ and $b$ to $a \cdot b$, the new rule combines them to $b \cdot a$.
For addition of numbers nothing changes, because $2 + 3 = 3 + 2$.
For composition of motions or for products of matrices, the new rule is different, because the order matters there.

### L2 human

We compute in the opposite of the set of $2 \times 2$ real matrices under multiplication.

1. Let $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$.
2. The usual product is $AB = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$.
3. The opposite product is $A \ast B = BA = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$.
4. These differ, so the opposite operation is not the usual one.

The typical use is to turn a statement about products in the order $ba$ into a statement about products in the order $ab$.
A trap is to think that the opposite is a new set: it has the same elements, and only the operation changes.
