---
tag: BH8WMN52AF
kind: example
name: Adding the converse schema to classical propositional logic
msc: ["03B05"]
topics: [H8QZY0RZXZ]
audience: grad
instance_of: [WK2P0E82B4]
uses: [WK2P0E82B4, R1122T076S, 1MGMQX43B8, 0Y0MQYST0M]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_system
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Completeness_(logic)
    locator: Syntactical completeness
---

## Example

Let $\mathsf{H}$ be the [[Hilbert system|1MGMQX43B8]] for classical propositional logic with modus ponens and the schemas
$$\text{(A1) } \varphi \to (\psi \to \varphi), \qquad \text{(A2) } (\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi)), \qquad \text{(A3) } (\lnot\varphi \to \lnot\psi) \to (\psi \to \varphi),$$
as in the [[Post completeness theorem|R1122T076S]].
Let $A = (p \to q) \to (q \to p)$, the converse schema.
We show that $A$ is not a theorem of $\mathsf{H}$, but every formula $B$ is a theorem of $\mathsf{H} + A$.
This is an instance of [[Post completeness|WK2P0E82B4]].

First, $A$ is not a theorem.

1. Take the valuation $p = \mathsf{F}$, $q = \mathsf{T}$.
   Then $p \to q = \mathsf{T}$ and $q \to p = \mathsf{F}$.
2. So $A = (\mathsf{T} \to \mathsf{F}) = \mathsf{F}$, and $A$ is not a tautology.
3. By the soundness of $\mathsf{H}$, $A$ is not a theorem of $\mathsf{H}$.

Second, every formula is a theorem of $\mathsf{H} + A$.
Let $B$ be any formula and $r$ a variable.

4. $(r \to ((r \to r) \to r)) \to ((r \to (r \to r)) \to (r \to r))$, an instance of A2 with $\varphi = r$, $\psi = r \to r$, $\chi = r$.
5. $r \to ((r \to r) \to r)$, an instance of A1 with $\varphi = r$, $\psi = r \to r$.
6. $(r \to (r \to r)) \to (r \to r)$, by [[modus ponens|0Y0MQYST0M]] from lines 5 and 4.
7. $r \to (r \to r)$, an instance of A1 with $\varphi = r$, $\psi = r$.
8. $r \to r$, by modus ponens from lines 7 and 6.
9. $(r \to r) \to (B \to (r \to r))$, an instance of A1 with $\varphi = r \to r$, $\psi = B$.
10. $B \to (r \to r)$, by modus ponens from lines 8 and 9.
11. $(B \to (r \to r)) \to ((r \to r) \to B)$, the instance of $A$ with $p = B$ and $q = r \to r$.
    It is an axiom of $\mathsf{H} + A$.
12. $(r \to r) \to B$, by modus ponens from lines 10 and 11.
13. $B$, by modus ponens from lines 8 and 12.

Lines 4 to 13 form a derivation of $B$ in $\mathsf{H} + A$.
So $\mathsf{H} + A$ is Post inconsistent.

## Remarks

The derivation uses A3 nowhere, so the same collapse happens in the implicational part of the system.
The choice of instance in line 11 follows the general proof.
The falsifying valuation of step 1 makes $q$ true, so $q$ becomes the always true formula $r \to r$.
The general proof would put the always false formula $\lnot(r \to r)$ for $p$ and then use explosion, but here $B$ itself does the job.

If $A$ is changed to the tautology $(p \to q) \to (\lnot q \to \lnot p)$, the contrapositive, nothing collapses, because every instance is already a theorem.
If only the single formula $(p \to q) \to (q \to p)$ is added, without its instances, the system stays Post consistent.
Take the valuation with $p$ and $q$ true and another variable $s$ false.
It makes every axiom true, modus ponens keeps truth, and $s$ is false, so $s$ is not derivable.

## Explanations

### L1 human

"If $p$ implies $q$, then $q$ implies $p$" is a common mistake, and here we see how bad it is as a law of logic.
Suppose it is accepted for all statements, and take $q$ to be a statement that is always true, such as "if it rains, it rains".
Every statement $B$ implies an always true statement.
The mistaken law then turns this into "the always true statement implies $B$", and so $B$ follows.
Since $B$ was arbitrary, everything follows.

### L2 human

Lines 4 to 8 are the standard derivation of $r \to r$ in the Hilbert system, and they are worth checking once.

1. Line 4 is A2 with $\varphi = r$, $\psi = r \to r$, $\chi = r$.
   The schema $(\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi))$ becomes exactly line 4.
2. Line 5 is A1 with $\psi = r \to r$, giving $r \to ((r \to r) \to r)$.
3. Line 6 removes the antecedent of line 4 with line 5.
4. Line 7 is A1 with $\psi = r$, and line 8 removes the antecedent of line 6.

The typical use of this pattern is to test a proposed new axiom: if it is not a tautology, the system with it is trivial.
A trap is to put the always true formula in place of $p$.
The instance $((r \to r) \to B) \to (B \to (r \to r))$ has a conclusion that is already a theorem, so it gives nothing new.
