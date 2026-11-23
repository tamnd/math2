---
tag: WFK9VE30Y0
kind: example
name: A cut-free derivation of Peirce's law
msc: ["03F05"]
topics: [R10RMQCJQX]
audience: ug2
instance_of: [Z2NXKDK06G]
uses: [PZX9J3VEMT, GMSZ75D5WE]
sources:
  - url: https://en.wikipedia.org/wiki/Peirce%27s_law
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Structural_proof_theory
    locator: Analytic proof
---

## Example

We derive [[Peirce's law|GMSZ75D5WE]] $\Rightarrow ((p \to q) \to p) \to p$ in LK without cut, for propositional variables $p$ and $q$.
Then we check that every formula of the derivation is a subformula of the law, so the derivation has the [[subformula property|Z2NXKDK06G]].

1. The sequent $p \Rightarrow p$ is an axiom.
2. The rule WR gives $p \Rightarrow p, q$.
3. The rule ${\to}$R, with active formulas $p$ on the left and $q$ on the right and with $\Delta = p$, gives $\Rightarrow p, p \to q$.
4. The sequent $p \Rightarrow p$ is again an axiom.
5. The rule ${\to}$L, with left premise from step 3 (active formula $p \to q$) and right premise from step 4 (active formula $p$), gives $(p \to q) \to p \Rightarrow p, p$.
6. The rule CR gives $(p \to q) \to p \Rightarrow p$.
7. The rule ${\to}$R gives $\Rightarrow ((p \to q) \to p) \to p$.

Now the check.

8. The subformulas of the law are $((p \to q) \to p) \to p$, $(p \to q) \to p$, $p \to q$, $p$ and $q$.
9. The formulas in steps 1 to 7 are $p$, $q$, $p \to q$, $(p \to q) \to p$ and the law itself.
   Each one is in the list of step 8.

## Remarks

The derivation is in LK but not in LJ, because steps 2, 3, 5 and 6 have two formulas in the succedent.
That is no accident: Peirce's law is not valid in [[intuitionistic logic|Q11N8X99FK]], so LJ has no derivation of it at all.

The contraction in step 6 is the heart of the derivation.
The formula $p$ is used twice on the right, once to close the axiom of step 4 and once to feed the ${\to}$R of step 3.
Classical logic lets a cut-free derivation keep a second copy of a conclusion in reserve, and LJ forbids exactly that.

The variable $q$ enters only by weakening in step 2.
So the derivation stays correct when $q$ is replaced by any formula, and it then shows each instance of the law with the same shape.

## Explanations

### L1 human

Peirce's law is a statement about two statements $p$ and $q$ that is true in classical logic.
The derivation above proves it using only pieces of the law itself.
No outside lemma appears, and each line is built from the lines above it.

### L2 human

To check the property, list the subformulas of the end formula, then list the formulas that occur in the derivation.
Here the second list is contained in the first, so the derivation has the property.
Watch out for $q$: it occurs alone only in step 2, and it is a subformula because it is a part of $p \to q$.
