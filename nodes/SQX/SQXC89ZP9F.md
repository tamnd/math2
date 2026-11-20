---
tag: SQXC89ZP9F
kind: example
name: Disjunction elimination in multiple-conclusion form
msc: ["03B22", "03B05"]
topics: [NJB94B39QK]
audience: ug2
instance_of: [3AJTDAP93H]
uses: [3AJTDAP93H, 0F72FK8EKB, 05RSK4Q657]
sources:
  - url: https://en.wikipedia.org/wiki/Multiple-conclusion_logic
    locator: lead section
---

## Example

Let $\vDash$ be classical [[multiple-conclusion|3AJTDAP93H]] consequence: $\Gamma \vDash \Delta$ if every Boolean valuation that makes all of $\Gamma$ true makes some element of $\Delta$ true.
We show that $p \lor q \vDash p, q$, while $p \lor q \nvDash p$ and $p \lor q \nvDash q$.

1. Let $v$ be a Boolean valuation with $v(p \lor q) = \mathsf{T}$.
2. By the [[truth table|05RSK4Q657]] of [[disjunction|0F72FK8EKB]], $v(p) = \mathsf{T}$ or $v(q) = \mathsf{T}$.
3. So $v$ makes some element of $\set{p, q}$ true, and $p \lor q \vDash p, q$.
4. Let $v(p) = \mathsf{F}$ and $v(q) = \mathsf{T}$. Then $v(p \lor q) = \mathsf{T}$ and $v(p) = \mathsf{F}$, so $p \lor q \nvDash p$.
5. Let $v(p) = \mathsf{T}$ and $v(q) = \mathsf{F}$. Then $v(p \lor q) = \mathsf{T}$ and $v(q) = \mathsf{F}$, so $p \lor q \nvDash q$.

## Remarks

The single-conclusion relation records only $p \lor q \vDash p \lor q$ and its weaker consequences.
As a constraint on arbitrary valuations, it cannot say that the truth of $p \lor q$ forces the truth of one of $p$ and $q$.
The example [[Multiple conclusions fix the classical truth tables|B5TPYADN4W]] makes this precise.
The multiple-conclusion form states exactly this, and it is the semantic form of the left rule for $\lor$ in the sequent calculus LK.
In classical logic, the inference $p \lor q \vDash p, q$ is equivalent to the tautology $(p \lor q) \to (p \lor q)$, so nothing is lost in the formula reading.

## Explanations

### L1 human

If "it is Monday or Tuesday" is true, then one of "it is Monday" and "it is Tuesday" is true.
We do not know which one.
A multiple-conclusion argument says exactly this: at least one conclusion holds.

### L2 human

The conclusion set $\set{p, q}$ is read as a disjunction.
So the inference is valid, while each single-conclusion inference fails at one row of the truth table.
A trap is to read the comma on the right as "and"; then the inference would claim both $p$ and $q$, which is false.
