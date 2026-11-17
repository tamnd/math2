---
tag: GA3VNQQBPB
kind: example
name: The two-element cluster is not a frame of Grz
msc: ["03B45"]
topics: [3E7M66WW6Q]
audience: research
not_instance_of:
  - target: 2Q8E4GQF3B
    note: "The two-element cluster validates S4 but refutes the Grz axiom at the world where p is false."
uses: [2Q8E4GQF3B, NGHWZ9Y7ZV, 0QV2JS9RJ3, AXB7DEGR2D]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
---

## Example

Let $W = \set{a, b}$ with $R = W \times W$: each world sees itself and the other.
The relation is reflexive and transitive, so the frame validates $\mathsf{S4}$, but it is not antisymmetric.
We show that it refutes the axiom $\square(\square(p \to \square p) \to p) \to p$ of [[Grzegorczyk logic|2Q8E4GQF3B]].

1. Let $p$ be true at $a$ only.
2. $b \not\models p$ and $b$ is a successor of every world, so $\square p$ is false at $a$ and at $b$.
3. At $a$, $p$ is true and $\square p$ is false, so $a \not\models p \to \square p$.
4. Every world sees $a$, so $\square(p \to \square p)$ is false at $a$ and at $b$.
5. Hence $\square(p \to \square p) \to p$ is true at $a$ and at $b$, and $b \models \square(\square(p \to \square p) \to p)$.
6. Since $b \not\models p$, the axiom fails at $b$.

## Remarks

So $\mathsf{S4} \nvdash \square(\square(p \to \square p) \to p) \to p$, and $\mathsf{S4}$ is a proper part of $\mathsf{Grz}$.
The same argument, with $p$ false exactly at $b$, works on every frame with two different worlds $a$, $b$ that see each other, so every frame of $\mathsf{Grz}$ is antisymmetric.
Compare [[S4 is not the provability logic of PA|AXB7DEGR2D]]: $\mathsf{S4}$ is too weak to be the logic of strong provability and too strong to be the logic of provability.

## Explanations

### L1 human

Two points that see each other form a loop.
Grzegorczyk logic forbids such loops, and this example shows how: with $p$ true at one point only, the axiom fails at the other point.

### L2 human

The typical use is to separate $\mathsf{Grz}$ from $\mathsf{S4}$: a formula that fails only on frames with clusters is a theorem of $\mathsf{Grz}$ but not of $\mathsf{S4}$.
A trap: the axiom holds at $a$, where $p$ is true; the failure is at $b$.
