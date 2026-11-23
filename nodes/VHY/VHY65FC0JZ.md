---
tag: VHY65FC0JZ
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

We derive the sequent $\Rightarrow \exists x\, (D(x) \to \forall y\, D(y))$ in LK, with the rules of the [[sequent calculus|PZX9J3VEMT]].
In words: in every nonempty bar there is a person such that, if this person drinks, everybody drinks.
Here $D$ is a unary relation symbol, and $a$ and $b$ are distinct variables.
Let $E$ abbreviate the formula $\exists x\, (D(x) \to \forall y\, D(y))$, and leave the exchange rule implicit.

1. $D(b) \Rightarrow D(b)$ is an axiom.
2. $D(b) \Rightarrow D(b), \forall y\, D(y)$ follows by WR from step 1.
3. $\Rightarrow D(b), D(b) \to \forall y\, D(y)$ follows by ${\to}$R from step 2, with $A = D(b)$, $B = \forall y\, D(y)$ and $\Delta = D(b)$.
4. $\Rightarrow D(b), E$ follows by ${\exists}$R from step 3, with the term $b$, since $(D(x) \to \forall y\, D(y))[b/x] = D(b) \to \forall y\, D(y)$.
5. $\Rightarrow \forall y\, D(y), E$ follows by ${\forall}$R from step 4, with eigenvariable $b$.
   The left side is empty, and $b$ is not free in $E$ or in $\forall y\, D(y)$.
6. $D(a) \Rightarrow \forall y\, D(y), E$ follows by WL from step 5.
7. $\Rightarrow D(a) \to \forall y\, D(y), E$ follows by ${\to}$R from step 6.
8. $\Rightarrow E, E$ follows by ${\exists}$R from step 7, with the term $a$.
9. $\Rightarrow E$ follows by CR from step 8.

Each step uses one rule of LK, and the only eigenvariable condition, at step 5, holds.
So this is a derivation of $\Rightarrow E$.
It uses no cut, and every formula in it is a subformula of $E$ up to the variables $a$ and $b$.

## Remarks

### Two cases in one derivation

The formula is the [[drinker paradox|8BMQTZZEWB]], and the derivation follows its informal proof by cases.
Steps 1 to 4 cover the case where the person $b$ does not drink: then "if $b$ drinks, everybody drinks" is true because its premise is false.
Steps 5 to 8 cover the case where everybody drinks: then any person $a$ will do.
The sequent keeps both answers on the right side, and contraction at step 9 merges them.

### Why it is not intuitionistic

From step 2 on there are two formulas on the right, and step 8 needs two copies of $E$.
So the derivation is not an LJ derivation, and in fact the formula is not intuitionistically valid: no intuitionistic proof can name the person.
The formula also needs a nonempty domain; in the empty structure $E$ is false, since nothing exists to be the witness.

### What changes with the variables

If the variable $a$ is replaced by $b$ in steps 6 to 8, the derivation stays correct, because the eigenvariable condition is checked only at step 5.
But if WL with $D(b)$ came before step 5, the left side would contain $b$, and ${\forall}$R with eigenvariable $b$ would break the condition.

## Explanations

### L1 human

The drinker paradox says: in a bar with at least one person, there is someone such that, if they drink, everybody drinks.
If everybody drinks, any person works.
If somebody does not drink, pick that person: the "if" part is false, so the sentence is true.
The derivation follows these two cases, and it keeps both possible answers on the right side until the end.

### L2 human

To find the derivation, search backward from $\Rightarrow E$.

1. ${\exists}$R needs a term, but no single term works, so first copy $E$ with CR.
2. Use one copy with a variable $a$: ${\to}$R moves $D(a)$ to the left and leaves $\forall y\, D(y)$ on the right.
3. Drop $D(a)$ from the left (it is not needed), then apply ${\forall}$R to $\forall y\, D(y)$ with a new eigenvariable $b$, which leaves $D(b)$ on the right.
4. Use the second copy of $E$ with the term $b$: ${\to}$R puts $D(b)$ on the left, and the axiom $D(b) \Rightarrow D(b)$ closes the branch after a weakening.

This pattern, where one existential formula is used twice with different terms, is typical for valid formulas with $\exists$ in front.
Watch out: in step 3 the eigenvariable must differ from $a$ unless $D(a)$ has been dropped, since otherwise $a$ is free on the left.
