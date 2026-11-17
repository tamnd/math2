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

Work in the implicational fragment of [[natural deduction|PAQ4ZX2TX1]].
Formulas are built from propositional variables by $\to$.
A derivation is a finite tree of formula occurrences, built by two rules.

- ${\to}$I: from a derivation of $B$, infer $A \to B$, and discharge any number of occurrences of the assumption $A$ with a label $u$.
- ${\to}$E: from a derivation of $A \to B$, the *major premise*, and a derivation of $A$, the *minor premise*, infer $B$.

The leaves are assumptions, open or discharged.
A derivation of $A$ from $\Gamma$ is a derivation with conclusion $A$ whose open assumptions lie in the finite set $\Gamma$.
A *detour* is an occurrence of a formula $A \to B$ that is the conclusion of ${\to}$I and the major premise of ${\to}$E.
Its *degree* is the number of occurrences of $\to$ in $A \to B$.
A derivation is *normal* if it has no detour.

A *reduction step* replaces a part of a derivation of the following form.
A derivation $D_1$ of $B$, with assumptions $A$ labelled $u$, ends with ${\to}$I to $A \to B$, discharging $u$.
This is the major premise of a ${\to}$E whose minor premise has a derivation $D_2$ of $A$.
The step replaces this part by $D_1$ with each assumption $A$ labelled $u$ replaced by a copy of $D_2$.

1. **Weak normalization.** Every derivation of $A$ from $\Gamma$ turns into a normal derivation of $A$ from $\Gamma$ by finitely many reduction steps.
2. **Subformula property.** In a normal derivation of $A$ from $\Gamma$, every formula is a subformula of $A$ or of a formula in $\Gamma$.
3. **Strong normalization.** There is no infinite sequence of reduction steps starting from a derivation.

## Remarks

### Why each hypothesis is needed

The fragment matters for the simple form of part 2.
With $\wedge$, $\vee$, $\exists$ and $\bot$, normal derivations need extra permutative reductions, and with classical rules the property needs a restricted form.
The definition of a detour needs both rules on the same occurrence.
An ${\to}$E whose major premise is an assumption is no detour, and it cannot be removed: the derivation of $q$ from $p \to q$ and $p$ is normal.
Part 2 needs normality.
The derivation that discharges $p$ to get $p \to p$ and applies it to an assumption $p$ is a derivation of $p$ from $p$ with the formula $p \to p$, which is not a subformula of $p$.

### Consequences

- **Consistency of the fragment.** No normal derivation of a propositional variable $p$ from no assumptions exists, by part 2 and the shape of the last rule. So $p$ is not derivable.
- **Conservativity.** By the generalization to full intuitionistic natural deduction, a derivation of $A$ from $\Gamma$, all implicational, normalizes to one that uses only the rules for $\to$.
- **Proof search.** Part 2 restricts the search for a normal derivation to subformulas of the goal and the assumptions, which is the base of decision procedures for the fragment.
- **Typed programs terminate.** Under the [[Curry-Howard correspondence|A77FER1Q5H]], a reduction step is a [[beta reduction|Y9B9CVY6SJ]], and part 3 is the [[strong normalization of the simply typed lambda calculus|V2Z855MFPC]].

### Converse

Part 1 has a converse in a weak sense: a reduction step keeps the conclusion and does not add open assumptions, so reduction never turns a non-derivable claim into a derivable one.
The converse of part 2 fails: a derivation with the subformula property need not be normal.
From the assumption $p$ labelled $u$, ${\to}$I gives $p \to p$, and ${\to}$E with the assumption $p$ labelled $v$ gives $p$.
Then ${\to}$I discharges $v$ and gives $p \to p$ from no assumptions.
This derivation has a detour on $p \to p$, and every formula in it is $p$ or $p \to p$, both subformulas of the conclusion.

### Generalizations

Prawitz proved weak normalization for full intuitionistic natural deduction, with permutative reductions for $\vee$ and $\exists$, and for a classical system without $\vee$ and $\exists$.
Strong normalization holds for full intuitionistic natural deduction as well.
For the sequent calculus, the corresponding result is the [[cut-elimination theorem|AYRZ98Y0NW]].
For second-order natural deduction, strong normalization is Girard's theorem, proved with reducibility candidates.

## History

Gentzen introduced natural deduction in his paper of 1934 and 1935, but he published the normal form result only for the sequent calculus.
Jan von Plato found an unpublished proof of normalization for intuitionistic natural deduction in Gentzen's manuscripts.
Dag Prawitz proved normalization for natural deduction in his book *Natural Deduction* of 1965.
Prawitz later proved strong normalization.

## Explanations

### L1 human

In a proof, a detour is a step where we prove a general rule "if $A$ then $B$" and use it at once for one $A$.
We can always remove such a step by doing the argument directly for that $A$.
The theorem says that removing detours one at a time always ends.
The final proof uses only pieces of what it proves and of what it assumes.

### L2 human

We normalize a small derivation of $q$ from the assumptions $q$.

1. From the assumption $q$ labelled $u$, ${\to}$I gives $q \to q$ and discharges $u$.
2. With a second assumption $q$, ${\to}$E gives $q$. The formula $q \to q$ is a detour of degree $1$.
3. The reduction step replaces the assumption $q$ labelled $u$ by the derivation of the minor premise, which is the assumption $q$.
4. The result is the one-node derivation $q$, which is normal.

The typical use is to normalize first and then argue about the last rule of a normal derivation.
A trap: a reduction step can copy the minor premise many times, so the number of detours can grow.

### L3 human

Weak normalization is a statement about one strategy, and strong normalization about all of them.
Under Curry-Howard, part 3 says that every simply typed lambda term has only finite reduction sequences, and the usual proof uses Tait's computability predicates.
Normal derivations have a structure of branches: from an assumption, a sequence of eliminations, then a sequence of introductions.
This structure gives the subformula property, and it underlies [[proof-theoretic semantics|K97KZB5R7N]], where normal derivations justify the meaning of the rules.
