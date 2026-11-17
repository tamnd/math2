---
tag: ~b4da6e0a
kind: example
name: A sequent derivation of the drinker paradox
msc: ["03F05", "03B10"]
topics: [TTCRX3NFNY]
audience: grad
instance_of: [W72CA3R9MP]
uses: [PZX9J3VEMT]
sources:
  - url: https://en.wikipedia.org/wiki/Sequent_calculus
    locator: Example derivations
  - url: https://en.wikipedia.org/wiki/Drinker_paradox
    locator: lead section
---

## Example

We derive the sequent $\Rightarrow \exists x\, (D(x) \to \forall y\, D(y))$ in LK, with the rules of the [[definition|PZX9J3VEMT]].
Here $D$ is a unary relation symbol, and $a$ and $b$ are distinct variables.
Let $E$ abbreviate the conclusion $\exists x\, (D(x) \to \forall y\, D(y))$.
We leave the exchange rule implicit.

1. $D(b) \Rightarrow D(b)$. Axiom.
2. $D(b) \Rightarrow D(b), \forall y\, D(y)$. WR from step 1.
3. $\Rightarrow D(b), D(b) \to \forall y\, D(y)$. ${\to}$R from step 2, with $A = D(b)$, $B = \forall y\, D(y)$ and $\Delta = D(b)$.
4. $\Rightarrow D(b), E$. ${\exists}$R from step 3, with the term $t = b$: $(D(x) \to \forall y\, D(y))[b/x] = D(b) \to \forall y\, D(y)$.
5. $\Rightarrow \forall y\, D(y), E$. ${\forall}$R from step 4, with eigenvariable $b$: $b$ is not free in $E$, in $\forall y\, D(y)$, or in the empty antecedent.
6. $D(a) \Rightarrow \forall y\, D(y), E$. WL from step 5.
7. $\Rightarrow D(a) \to \forall y\, D(y), E$. ${\to}$R from step 6.
8. $\Rightarrow E, E$. ${\exists}$R from step 7, with the term $t = a$.
9. $\Rightarrow E$. CR from step 8.

Each step uses one rule of LK, and the eigenvariable condition holds at step 5, so this is a derivation of $\Rightarrow E$.
It uses no cut, and every formula in it is a subformula of $E$ up to the terms $a$ and $b$.

## Remarks

The formula is the drinker paradox: in every nonempty bar there is a person such that, if this person drinks, then everybody drinks.
The derivation needs two copies of $E$ at step 8, so it uses contraction on the right, and it has two formulas in the succedent from step 2 on.
So it is not an LJ derivation, and the formula is not intuitionistically valid: no intuitionistic proof can pick the person.
Informally, step 5 covers the case "everybody drinks" with any person $a$, and steps 1 to 4 cover the case where the person $b$ does not drink.
If the variable $a$ is replaced by $b$ in steps 6 to 8, the derivation stays correct, because the eigenvariable condition is checked only at step 5.

## Explanations

### L1 human

The drinker paradox says: in a bar with at least one person, there is someone such that, if they drink, everybody drinks.
If everybody drinks, any person works.
If somebody does not drink, pick that person: the "if" part is false, so the sentence is true.
The derivation follows these two cases, and it keeps both possible answers on the right side until the end.

### L2 human

To find the derivation, search backward from $\Rightarrow E$.

1. ${\exists}$R needs a term, but neither choice works alone, so first copy $E$ with CR.
2. Use one copy with a variable $a$: ${\to}$R moves $D(a)$ to the left and leaves $\forall y\, D(y)$ on the right.
3. ${\forall}$R on $\forall y\, D(y)$ needs a new eigenvariable $b$, and it leaves $D(b)$ on the right.
4. Use the second copy of $E$ with the term $b$: ${\to}$R puts $D(b)$ on the left, and the axiom $D(b) \Rightarrow D(b)$ closes the branch.

This pattern, where a quantifier is used twice with different terms, is typical for valid formulas with $\exists$ in front.
A trap is to apply WL before ${\forall}$R with $b = a$: then $a$ is free in the antecedent $D(a)$, and the eigenvariable condition fails.
