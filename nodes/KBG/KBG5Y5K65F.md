---
tag: KBG5Y5K65F
kind: example
name: Exclusive or alone is not functionally complete
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: ug1
not_instance_of:
  - target: 1NNYWRN6B8
    note: exclusive or is a binary connective, but it alone does not express negation, so it is not a Sheffer connective
uses: [1NNYWRN6B8, PTMR3P9J6C, TDZVCWYJ9F, QS0XVAN9BG]
sources:
  - url: https://en.wikipedia.org/wiki/Functional_completeness
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Sheffer_stroke
    locator: lead section
---

## Example

A factory makes only XOR gates, and we ask whether it can build a NOT gate from them.
The [[exclusive or|PTMR3P9J6C]] $p \oplus q$ is true when exactly one of $p$, $q$ is true.
We show that no formula built from variables with $\oplus$ alone has the truth table of $\neg p$, so $\oplus$ alone is not [[functionally complete|TDZVCWYJ9F]], unlike the [[Sheffer stroke|1NNYWRN6B8]].

1. Fix the assignment that makes every variable false.
2. Claim: every formula built from variables with $\oplus$ alone is F under this assignment.
3. A variable is F under the assignment, so the claim holds for variables.
4. Suppose $\varphi$ and $\psi$ are built with $\oplus$ alone and are both F under the assignment.
   Then $\varphi \oplus \psi$ has the value $\mathrm{F} \oplus \mathrm{F} = \mathrm{F}$.
5. By steps 3 and 4 and induction on the construction of formulas, the claim holds for every such formula.
6. The formula $\neg p$ is T at $p$ = F, so no formula built with $\oplus$ alone has the truth table of $\neg p$.

So the factory cannot build a NOT gate, and $\oplus$ alone is not functionally complete.

## Remarks

### Connectives that keep a value

A connective that keeps a truth value cannot produce a negation.
Here $\oplus$ keeps F, because $\mathrm{F} \oplus \mathrm{F} = \mathrm{F}$.
In the same way, $\land$, $\lor$, $\to$ and $\leftrightarrow$ keep T, since each gives T on the input TT, so none of them alone can express $\neg p$.
The Sheffer stroke and the Peirce arrow escape both obstacles, because $\mathrm{T} \uparrow \mathrm{T} = \mathrm{F}$ and $\mathrm{F} \downarrow \mathrm{F} = \mathrm{T}$.

### Adding a constant

With the constant $\top$ added, $\neg p \equiv p \oplus \top$, so negation becomes expressible.
The set $\{\oplus, \top\}$ is still not functionally complete.
With 1 for T and 0 for F, every formula in it computes a sum modulo $2$ of variables and constants, and $p \land q$ is not such a sum.
The set $\{\oplus, \land, \top\}$ is functionally complete, and its formulas are the polynomials of a [[Boolean ring|0RCV1ZFP8G]].

## Explanations

### L1 human

The exclusive or says "exactly one of the two".
If every input is false, then no input is true, so "exactly one" is false.
Combining false results with exclusive or again gives false.
So a formula of exclusive ors can never be true when all its inputs are false.
But "not $p$" is true when $p$ is false, so exclusive or alone can never say "not".

### L2 human

Show in the same way that $\{\land, \lor\}$ is not functionally complete.

1. Fix the assignment that makes every variable true.
2. A variable is T under it.
3. If $\varphi$ and $\psi$ are T, then $\varphi \land \psi$ and $\varphi \lor \psi$ are T.
4. By induction, every formula built with $\land$ and $\lor$ is T under this assignment.
5. The formula $\neg p$ is F at $p$ = T, so it is not expressible.

To prove that a set of connectives is not complete, find a property that all of them keep and that $\neg$ or another connective breaks.
Watch out: the argument proves incompleteness but gives no help in proving completeness, which needs explicit formulas as in [[the stroke example|S3KJ52G2SF]].
