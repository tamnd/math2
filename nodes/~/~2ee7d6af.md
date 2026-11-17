---
tag: ~2ee7d6af
kind: example
name: A cut-free derivation of Peirce's law
msc: ["03F05"]
topics: [R10RMQCJQX]
audience: ug2
instance_of: [~694ac127]
uses: [PZX9J3VEMT, GMSZ75D5WE]
sources:
  - url: https://en.wikipedia.org/wiki/Peirce%27s_law
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Structural_proof_theory
    locator: Analytic proof
---

## Example

We derive [[Peirce's law|GMSZ75D5WE]] $\Rightarrow ((p \to q) \to p) \to p$ in LK without cut, for propositional variables $p$ and $q$.

1. $p \Rightarrow p$ is an axiom.
2. WR gives $p \Rightarrow p, q$.
3. ${\to}$R, with $A = p$, $\Delta = p$ and $B = q$, gives $\Rightarrow p, p \to q$.
4. $p \Rightarrow p$ is an axiom.
5. ${\to}$L, applied to step 3 with $A = p \to q$ and to step 4 with $B = p$, gives $(p \to q) \to p \Rightarrow p, p$.
6. CR gives $(p \to q) \to p \Rightarrow p$.
7. ${\to}$R gives $\Rightarrow ((p \to q) \to p) \to p$.

We check the subformula property.

8. The subformulas of the end formula are $((p \to q) \to p) \to p$, $(p \to q) \to p$, $p \to q$, $p$ and $q$.
9. The formulas in steps 1 to 7 are $p$, $q$, $p \to q$, $(p \to q) \to p$ and the end formula. Each one is in the list of step 8.

## Remarks

The derivation is in LK but not in LJ: steps 2, 3, 5 and 6 have two formulas in the succedent.
Peirce's law has no LJ derivation, since it is not valid in [[intuitionistic logic|Q11N8X99FK]].
The variable $q$ enters only by weakening, so the derivation stays correct when $q$ is replaced by any formula.
The contraction in step 6 is needed: the cut-free derivation uses the formula $p$ twice on the right.

## Explanations

### L1 human

Peirce's law is a true statement of classical logic about two statements $p$ and $q$.
The derivation above proves it using only pieces of the law itself.
No outside lemma appears, and each line is built from the line above it.

### L2 human

To check the property, list the subformulas of the end formula, then list the formulas that occur in the derivation.
Here the second list is contained in the first, so the derivation has the property.
A trap is to forget $q$: it occurs only in step 2 and inside $p \to q$, and it is a subformula.
