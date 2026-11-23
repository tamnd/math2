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

Two worlds that see each other form a loop, and a loop is enough to break the axiom of [[Grzegorczyk logic|2Q8E4GQF3B]].
Let $W = \{a, b\}$ with $R = W \times W$, so each world sees itself and the other.
The relation is reflexive and transitive, so the frame validates $\mathsf{S4}$, but it is not antisymmetric.
We show that the frame refutes the axiom below:

$$\square(\square(p \to \square p) \to p) \to p.$$

1. Let $p$ be true at $a$ only.
2. Every world sees $b$, and $b \not\models p$, so $\square p$ is false at $a$ and at $b$.
3. At $a$, $p$ is true and $\square p$ is false, so $a \not\models p \to \square p$.
4. Every world sees $a$, so $\square(p \to \square p)$ is false at $a$ and at $b$.
5. Hence $\square(p \to \square p) \to p$ is true at $a$ and at $b$.
   Since $b$ sees only $a$ and $b$, we get $b \models \square(\square(p \to \square p) \to p)$.
6. Since $b \not\models p$, the axiom fails at $b$.

## Remarks

The example shows that $\mathsf{S4} \nvdash \square(\square(p \to \square p) \to p) \to p$, so $\mathsf{S4}$ is a proper part of $\mathsf{Grz}$.
The failure is at $b$, where $p$ is false.
At $a$ the axiom holds, because its conclusion $p$ is true there.

The argument does not need the frame to have only two worlds.
Take any frame in which two different worlds $a$ and $b$ see each other, and let $p$ be false exactly at $b$.
Then $a$ sees $b$, so $p \to \square p$ fails at $a$, and $b$ sees $a$, so $\square(p \to \square p)$ fails at $b$.
Every other successor of $b$ makes $p$ true, so $b \models \square(\square(p \to \square p) \to p)$ while $b \not\models p$.
So every frame of $\mathsf{Grz}$ is antisymmetric.

Compare [[S4 is not the provability logic of PA|AXB7DEGR2D]].
$\mathsf{S4}$ is too weak to be the logic of strong provability, and too strong to be the logic of provability.

## Explanations

### L1 human

Two points that see each other form a loop.
Grzegorczyk logic forbids such loops.
With $p$ true at one point only, the axiom fails at the other point.

### L2 human

The example separates $\mathsf{Grz}$ from $\mathsf{S4}$.
A formula that fails only on frames with clusters is a theorem of $\mathsf{Grz}$ but not of $\mathsf{S4}$, and the Grz axiom is such a formula.
Watch out for where the failure is.
The axiom holds at $a$, where $p$ is true, and it fails at $b$.
If you check only the world where $p$ is true, you find no failure.

### L3 human

A cluster is a set of worlds that all see each other.
$\mathsf{S4}$ frames may have clusters, and the frames of $\mathsf{Grz}$ are exactly the $\mathsf{S4}$ frames with no proper clusters and no infinite strictly ascending chains.
In the same way, Löb's axiom excludes all loops, even a single reflexive point, and this is why $\mathsf{GL}$ frames are irreflexive.
