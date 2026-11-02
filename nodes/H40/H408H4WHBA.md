---
tag: H408H4WHBA
kind: definition
name: Linear logic
msc: [03B47, 03F52]
defines: 2P2184B6HE
uses: [W72CA3R9MP, 09K9MWD2QQ]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_logic
---

## Definition

The formulas of propositional linear logic are built from propositional variables with these connectives and constants.

1. Multiplicatives: the conjunction $A \otimes B$ (tensor), the disjunction "$A$ par $B$", and the units $1$ and $\bot$.
2. Additives: the conjunction $A \mathbin{\&} B$ (with), the disjunction $A \oplus B$ (plus), and the units $\top$ and $0$.
3. Exponentials: $!A$ (of course) and $?A$ (why not).
4. Linear implication: $A \multimap B$.

Linear logic is the set of sequents $\Gamma \vdash \Delta$, with $\Gamma$ and $\Delta$ finite lists of formulas, derivable in Girard's [[sequent calculus|W72CA3R9MP]].
That calculus has the logical rules of each connective and the exchange rule.
It has weakening and contraction only for formulas $!A$ on the left and $?A$ on the right.

## Remarks

The two conjunctions differ in how they treat the context.
The right rule of $\otimes$ derives $\Gamma, \Gamma' \vdash A \otimes B, \Delta, \Delta'$ from $\Gamma \vdash A, \Delta$ and $\Gamma' \vdash B, \Delta'$, so the context is split.
The right rule of $\&$ derives $\Gamma \vdash A \mathbin{\&} B, \Delta$ from $\Gamma \vdash A, \Delta$ and $\Gamma \vdash B, \Delta$, so the context is shared.

Example: $A \vdash A \mathbin{\&} A$ is derivable for a variable $A$: apply the $\&$ rule to two copies of the axiom $A \vdash A$.

Non-example: $A \vdash A \otimes A$ is not derivable for a variable $A$.
By cut elimination, a derivation can be taken cut-free, and then its last rule is the $\otimes$ rule.
That rule would need $A$ for one premise and the empty context for the other, and $\vdash A$ is not derivable.
In classical [[propositional logic|09K9MWD2QQ]], $A \to A \land A$ holds, which shows the role of contraction.

## Explanations

### L1 human

Linear logic counts its hypotheses.
The sequent $A \vdash B$ reads "one copy of $A$ can be turned into one copy of $B$".
The exponential $!A$ marks a hypothesis that may be copied or discarded freely, and so recovers ordinary reasoning when needed.
