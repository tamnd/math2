---
tag: HWYJG3GCQJ
kind: example
name: The formula ◇□p → □◇p is not a theorem of S4
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
not_instance_of:
  - target: N60RVXSA5W
    note: the formula fails on a preorder, so it is not a theorem of S4
uses: [N60RVXSA5W, 0VABYWJWH9, E87G6ZTMTN, FDFQFWPM4X]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
---

## Example

A road splits at $r$ into two dead ends $a$ and $b$, and each place also sees itself.
This preorder refutes the axioms $.2$ and $.3$, so neither is a theorem of the [[modal logic S4|N60RVXSA5W]].
The model is this:
$$W = \{ r, a, b \}, \quad R = \{ (r, r), (a, a), (b, b), (r, a), (r, b) \}, \quad V(p) = \{ a \}.$$

First we check that the frame is an $\mathsf{S4}$-frame.

1. $R$ is reflexive, because the pairs $(r, r)$, $(a, a)$ and $(b, b)$ are in $R$.
2. $R$ is transitive.
   The only pairs $x R y$ with $x \neq y$ are $(r, a)$ and $(r, b)$, and $a$ and $b$ see only themselves, so a chain $x R y R z$ has $x = y$ or $y = z$, and then $x R z$.
3. So $R$ is a [[preorder|0VABYWJWH9]], and the frame validates $\mathsf{S4}$ by the [[common modal axiom schemata|FDFQFWPM4X]] and [[soundness|E87G6ZTMTN]].

Next we refute $.2$, which is $\lozenge\square p \to \square\lozenge p$.

4. The successor sets are $R[r] = W$, $R[a] = \{ a \}$ and $R[b] = \{ b \}$.
5. $\square p$ is true at $a$, because $a$ sees only $a$ and $p$ is true there.
   So $\lozenge\square p$ is true at $r$.
6. $\lozenge p$ is false at $b$, because $b$ sees only $b$ and $p$ is false there.
   So $\square\lozenge p$ is false at $r$, and $.2$ fails at $r$.

Last we refute $.3$, which is $\square(\square p \to q) \vee \square(\square q \to p)$, with the extra value $V(q) = \{ b \}$.

7. At $a$, $\square p$ is true and $q$ is false, so $\square p \to q$ is false at $a$, and $\square(\square p \to q)$ is false at $r$.
8. At $b$, $\square q$ is true and $p$ is false, so $\square q \to p$ is false at $b$, and $\square(\square q \to p)$ is false at $r$.
9. Both disjuncts fail at $r$, so $.3$ fails at $r$.

## Remarks

The two formulas are the extra axioms of $\mathsf{S4.2}$ and $\mathsf{S4.3}$.
On preorders, $.2$ asks that two successors of a world have a common successor, and here $a$ and $b$ have none.
On preorders, $.3$ asks that two successors of a world be comparable, and here neither $a R b$ nor $b R a$ holds.

What changes if you add the pair $(a, b)$?
The frame becomes the chain $r, a, b$, which is connected and validates both axioms.
In the old valuation, $\square p$ becomes false at $a$, since $a$ now sees $b$, so the countermodel for $.2$ no longer works.

## Explanations

### L1 human

Picture a road that splits at $r$ into two dead ends $a$ and $b$.
At $a$ it is sunny forever, and at $b$ it is never sunny.
Standing at $r$, you can reach a place where it stays sunny.
But you can also reach a place from which sun is never seen again.
So "possibly always sunny" does not give "always possibly sunny".

### L2 human

Read $\square$ as "now and in every future state" for a process that can branch.
Then $\lozenge\square p$ at $r$ says that some branch reaches a state from which $p$ holds forever.
And $\square\lozenge p$ at $r$ says that from every reachable state a $p$-state can still be reached.
The branch through $b$ breaks the second claim, while the branch through $a$ makes the first one true.
This three-world frame is the standard way to separate $\mathsf{S4}$ from $\mathsf{S4.2}$ and $\mathsf{S4.3}$.
Watch out: $\mathsf{S4}$ is valid on every preorder, with or without branching, so no theorem of $\mathsf{S4}$ forces two branches to meet again.
