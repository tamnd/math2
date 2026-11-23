---
tag: AXB7DEGR2D
kind: example
name: S4 is not the provability logic of PA
msc: ["03F45", "03B45"]
topics: [3E7M66WW6Q]
audience: research
not_instance_of:
  - target: WJK0YA4GP2
    note: "S4 proves the reflection axiom, whose instance with 0 = S0 realizes as the consistency of PA, which PA does not prove."
uses: [WJK0YA4GP2, 61THBNS8WE, NGHWZ9Y7ZV, 4PZM5GJTR5, 4NBAX3VRQ7, QQ6PZFGGB3]
sources:
  - url: https://en.wikipedia.org/wiki/Provability_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
---

## Example

The logic of necessity is not the logic of provability, and one instance of one axiom shows it.
The modal logic $\mathsf{S4}$ is $\mathsf{K}$ with the axioms $\mathrm{T}$, which is $\square p \to p$, and 4, which is $\square p \to \square \square p$.
It is the logic of the reflexive transitive frames in [[Kripke semantics|NGHWZ9Y7ZV]].
We show that $\mathsf{S4}$ is not the [[provability logic|WJK0YA4GP2]] $\mathrm{PL}(\mathsf{PA})$, and that neither of $\mathsf{S4}$ and $\mathsf{GL}$ contains the other.

1. The axiom $\mathrm{T}$ is in $\mathsf{S4}$, by definition.
2. Take any realization with $p^* = (0 = S0)$.
   Then $(\square p \to p)^*$ is the sentence $\mathrm{Prov}(\ulcorner 0 = S0 \urcorner) \to 0 = S0$.
3. $\mathsf{PA}$ proves $\neg (0 = S0)$.
   So the sentence of step 2 is equivalent in $\mathsf{PA}$ to $\neg \mathrm{Prov}(\ulcorner 0 = S0 \urcorner)$, the [[consistency statement|4NBAX3VRQ7]] $\mathrm{Con}(\mathsf{PA})$.
4. $\mathsf{PA}$ is consistent, so it does not prove $\mathrm{Con}(\mathsf{PA})$, by the [[second incompleteness theorem|4PZM5GJTR5]].
   Hence $\mathrm{T} \notin \mathrm{PL}(\mathsf{PA})$, and $\mathsf{S4} \neq \mathrm{PL}(\mathsf{PA})$.
5. $\mathrm{T} \notin \mathsf{GL}$.
   Take one world with no successors and $p$ false, so that $\square p$ is true and $p$ is false.
   This frame is transitive and has no infinite path, so it validates $\mathsf{GL}$ by [[the frame condition of Löb's axiom|QQ6PZFGGB3]].
6. Löb's axiom is not in $\mathsf{S4}$.
   Take one world $a$ with $a R a$ and $p$ false.
   Then $\square p$ is false at $a$, so $\square p \to p$ is true at $a$, and $\square(\square p \to p)$ is true at $a$ while $\square p$ is false.
   This frame is reflexive and transitive, so it validates $\mathsf{S4}$.

## Remarks

The example shows that reflexivity, the property that makes $\square$ a "necessity" operator, is exactly what provability lacks.
By Löb's theorem, a theory proves $\square \varphi \to \varphi$ only for the sentences $\varphi$ that it already proves.

The two logics do not merely differ, they cannot be joined.
In $\mathsf{GL}$ with the axiom $\mathrm{T}$, the formula $\square \bot \to \bot$ is a theorem, and Löb's rule then gives $\bot$.
Steps 5 and 6 show the same clash on frames: Löb's axiom forbids the loop $a R a$, and $\mathrm{T}$ demands it.

What changes if we change the reading?
If $\square \varphi$ means "$\varphi$ is true and provable", the reflexivity axiom becomes valid.
The logic is then [[Grzegorczyk logic|2Q8E4GQF3B]], an extension of $\mathsf{S4}$.

## Explanations

### L1 human

In ordinary modal logic, "necessarily $p$" implies $p$.
For "provably $p$" this law fails as a provable law.
With $p$ the false statement $0 = 1$, it would say that the system of axioms is consistent, and Gödel showed that the system cannot prove this.
So the logic of provability is a different logic from the logic of necessity.

### L2 human

Pick the axiom $\square p \to p$ of $\mathsf{S4}$ and realize $p$ as $0 = S0$.
The result is equivalent in $\mathsf{PA}$ to $\mathrm{Con}(\mathsf{PA})$.
$\mathsf{PA}$ does not prove it, so the axiom is not a law of provability in $\mathsf{PA}$.
Watch out: the realization of $\square p \to p$ is true in $\mathbb{N}$ for every $p^*$, since $\mathsf{PA}$ is sound.
It fails only as a theorem of $\mathsf{PA}$.
