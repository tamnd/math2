---
tag: W33WAE1XTC
kind: statement
role: theorem
name: Normalization theorem for natural deduction
msc: ["03F05"]
topics: [R10RMQCJQX]
audience: grad
uses: [PAQ4ZX2TX1, ZMVBAY7ZZD, Z2NXKDK06G]
about: [6KT3BJZ7D1, GYMQHR3PXF]
proofs: [ZGZC1FDWD5]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_deduction
    locator: Proofs and type theory
  - url: https://en.wikipedia.org/wiki/Normalization_property_(abstract_rewriting)
    locator: lead section
history:
  first_stated: "1965"
  notes: "Dag Prawitz proved normalization for natural deduction in his book Natural Deduction."
---

## Statement

The theorem says that every natural deduction derivation can be freed of detours, an introduction directly followed by an elimination, and that the result uses only pieces of its conclusion and assumptions.

We work in the implicational fragment of [[natural deduction|PAQ4ZX2TX1]], whose formulas are built from propositional variables by $\to$.
A derivation is a finite tree of formula occurrences built by two rules.
The rule ${\to}$I infers $A \to B$ from a derivation of $B$ and discharges any number of occurrences of the assumption $A$ that carry a label $u$.
The rule ${\to}$E infers $B$ from a derivation of $A \to B$, the *major premise*, and a derivation of $A$, the *minor premise*.
The leaves are assumptions, open or discharged, and a derivation of $A$ from $\Gamma$ has conclusion $A$ and all open assumptions in the finite set $\Gamma$.

A *detour* is an occurrence of a formula $A \to B$ that is the conclusion of ${\to}$I and the major premise of ${\to}$E.
Its *degree* is the number of occurrences of $\to$ in $A \to B$, and a derivation is *normal* if it has no detour.
A *reduction step* takes a detour, where ${\to}$I turns a derivation $D_1$ of $B$ into $A \to B$ and ${\to}$E applies it to a derivation $D_2$ of $A$.
It replaces this part by $D_1$ with each assumption $A$ labeled $u$ replaced by a copy of $D_2$.

1. **Weak normalization.** Every derivation of $A$ from $\Gamma$ turns into a normal derivation of $A$ from $\Gamma$ by finitely many reduction steps.
2. **Subformula property.** In a normal derivation of $A$ from $\Gamma$, every formula is a subformula of $A$ or of a formula in $\Gamma$.
3. **Strong normalization.** There is no infinite sequence of reduction steps that starts from a derivation.

## Remarks

### A detour and its removal

Here is a derivation of $q$ from $p \to (p \to q)$, $r \to p$ and $r$ with one detour, on $p \to q$.
$$\dfrac{\dfrac{\dfrac{\dfrac{p \to (p \to q) \qquad [p]^u}{p \to q}\,{\to}\mathrm{E} \qquad [p]^u}{q}\,{\to}\mathrm{E}}{p \to q}\,{\to}\mathrm{I}^u \qquad \dfrac{r \to p \qquad r}{p}\,{\to}\mathrm{E}}{q}\,{\to}\mathrm{E}$$
The left branch proves the general fact "from $p$ we get $q$", and the last step uses it once, for the $p$ that the right branch derives.
The reduction does the argument directly for that $p$: we put a copy of the right branch in place of each assumption $[p]^u$.
$$\dfrac{\dfrac{p \to (p \to q) \qquad \dfrac{r \to p \qquad r}{p}\,{\to}\mathrm{E}}{p \to q}\,{\to}\mathrm{E} \qquad \dfrac{r \to p \qquad r}{p}\,{\to}\mathrm{E}}{q}\,{\to}\mathrm{E}$$
Check: every major premise is now an assumption or the conclusion of ${\to}$E, so the derivation is normal, and its open assumptions are the same three formulas.
Notice the price: the derivation of $p$ now appears twice, because $u$ labeled two assumptions.

### Why each hypothesis is needed

The restriction to $\to$ keeps part 2 in its simple form.
With $\vee$ and $\exists$ a normal derivation needs extra *permutative* reductions, and with classical rules the property holds only in a restricted form.

A detour needs both rules on the same formula occurrence.
An ${\to}$E whose major premise is an assumption is no detour and cannot be removed: the derivation of $q$ from $p \to q$ and $p$ by one ${\to}$E is already normal.

Part 2 needs normality.
Discharge $p$ to get $p \to p$, then apply it to an open assumption $p$: this derivation of $p$ from $p$ contains $p \to p$, which is not a subformula of $p$.

### What it gives you

The fragment is consistent: no normal derivation of a variable $p$ from no assumptions exists.
Such a derivation cannot end with ${\to}$I, since $p$ is not an implication, and by part 2 and its proof it cannot end with ${\to}$E without an open assumption.

Part 2 bounds proof search to subformulas of the goal and the assumptions, and this is the base of decision procedures for the fragment.
Under the [[Curry-Howard correspondence|A77FER1Q5H]] a derivation is a typed program and a reduction step is a [[beta reduction|Y9B9CVY6SJ]].
Then part 3 is the [[strong normalization of the simply typed lambda calculus|V2Z855MFPC]]: every typed program terminates, whatever order of evaluation we choose.

### The converse

Reduction never changes what is derivable: a step keeps the conclusion and adds no open assumptions.
The converse of part 2 fails, since a derivation with the subformula property need not be normal.
From the assumption $p$ labeled $u$, ${\to}$I gives $p \to p$, and ${\to}$E with a new assumption $p$ labeled $v$ gives $p$.
Then ${\to}$I discharges $v$ and gives $p \to p$ from no assumptions.
This derivation has a detour on $p \to p$, yet every formula in it is $p$ or $p \to p$.

### Relation to cut elimination

Natural deduction and the sequent calculus translate into each other.
A detour corresponds to a cut, and a normal derivation goes to a cut-free one, so normalization is the natural deduction form of the [[cut-elimination theorem|AYRZ98Y0NW]].
The match is not one-to-one, because a sequent derivation records an order of rule applications that natural deduction leaves open.

### Generalizations

Prawitz proved weak normalization for full intuitionistic natural deduction, with permutative reductions for $\vee$ and $\exists$, and for a classical system without $\vee$ and $\exists$.
Strong normalization holds for full intuitionistic natural deduction as well.
For second-order natural deduction, the form of System F, strong normalization is Girard's theorem, proved with reducibility candidates.

### Watch out

A reduction step can make a derivation larger and can create new detours, so "fewer detours each step" is false.
In the example above the derivation grew.
If a discharged assumption $[A]^u$ had been the major premise of an ${\to}$E, and the copied branch had ended with ${\to}$I, the copy would have created a new detour on $A$.
The proof handles this by always reducing a detour of the largest degree whose minor premise contains no other such detour.

## History

Gentzen introduced natural deduction in his paper of 1934 and 1935, but he published the normal form result only for the sequent calculus.
Jan von Plato later found an unpublished proof of normalization for intuitionistic natural deduction in Gentzen's manuscripts.
Dag Prawitz proved normalization for natural deduction in his book *Natural Deduction* of 1965.
Prawitz later proved strong normalization, and Tait's computability method of 1967 had already given strong normalization for the simply typed lambda calculus.

## Explanations

### L1 human

In a proof, a detour is a step where we prove a general rule "if $A$ then $B$" and use it at once for one particular $A$.
We can always remove such a step by doing the argument directly for that $A$.
The theorem says that removing detours one at a time always ends.
The final proof uses only pieces of what it proves and of what it assumes.

### L2 human

We normalize a tiny derivation of $q$ from the assumption $q$.
From the assumption $q$ labeled $u$, ${\to}$I gives $q \to q$ and discharges $u$.
With a second assumption $q$, ${\to}$E gives $q$, and $q \to q$ is a detour of degree $1$.
The reduction step puts the derivation of the minor premise, here the bare assumption $q$, in place of the assumption labeled $u$.
The result is the one-node derivation $q$, which is normal.

The typical use is to normalize first and then argue about the last rule of a normal derivation.
Watch out: a reduction step can copy the minor premise many times, so the size of a derivation can grow while its detours are removed.

### L3 human

Weak normalization is a statement about one strategy, and strong normalization is a statement about all of them.
Under Curry-Howard, part 3 says that every simply typed lambda term has only finite reduction sequences, and the usual proof uses Tait's computability predicates.
A normal derivation has a clear shape on each branch: from an assumption, a run of eliminations, then a run of introductions.
That shape gives the subformula property, and it underlies [[proof-theoretic semantics|K97KZB5R7N]], where normal derivations justify the meaning of the rules.
