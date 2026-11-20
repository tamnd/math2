---
tag: JSAH84Y9G2
kind: statement
role: theorem
name: Cut elimination for the full Lambek calculus
msc: ["03F05", "03B47"]
topics: [98QF5J4W16]
audience: research
uses: [Q47701D0E1, DAMGTSY6VV, Z2NXKDK06G]
about: [V5XVVN16GS, HGVMPZ2DXA]
proofs: [5EP05PDM29]
sources:
  - url: https://plato.stanford.edu/entries/logic-substructural/
    locator: 3. Proof Theory
    note: Restall, Substructural Logics, Stanford Encyclopedia of Philosophy, revision of 2024-08-15
  - url: https://en.wikipedia.org/wiki/Cut-elimination_theorem
    locator: Cut elimination
  - book: isbn:9780444521415
    note: Galatos, Jipsen, Kowalski and Ono, Residuated Lattices
---

## Statement

Let $\mathsf{X}$ be one of the calculi $\mathsf{FL}$, $\mathsf{FL}_e$, $\mathsf{FL}_w$ and $\mathsf{FL}_{ew}$ of the [[full Lambek calculus|Q47701D0E1]].
The *size* of a sequent is the number of occurrences of atoms, constants and connectives in it.

1. Every sequent derivable in $\mathsf{X}$ has a derivation in $\mathsf{X}$ without the [[cut rule|DAMGTSY6VV]].
2. In a cut-free derivation, every formula is a subformula of a formula of the end sequent.
   This is the [[subformula property|Z2NXKDK06G]].
3. There is an algorithm that decides, for each sequent, whether it is derivable in $\mathsf{X}$.

## Remarks

### Why each hypothesis is needed

The proof uses that $\mathsf{X}$ has no contraction.
If the right premise of a cut ends with contraction on the cut formula $A$, then moving the cut up gives two cuts on $A$, and the second cut has a premise of unknown height.
Gentzen met this problem for LK and solved it with the mix rule, which cuts all copies of $A$ at once.
The restriction to the four calculi is a restriction of this proof, and it does not say that the other extensions lack cut elimination.

### Consequences

1. Disjunction property: if $\Rightarrow A \vee B$ is derivable in $\mathsf{X}$, then $\Rightarrow A$ or $\Rightarrow B$ is derivable.
   In a cut-free derivation the empty sequent never occurs, since no axiom and no rule other than cut has it as conclusion.
   So the last rule is ${\vee}\mathrm{R}$, as every other rule needs a formula on the left or the empty sequent above.
2. Conservativity: a sequent in the connectives $\cdot$, $\backslash$, $/$ is derivable in $\mathsf{FL}$ only by rules for these connectives, by the subformula property.
   So $\mathsf{FL}$ is conservative over its implicational and multiplicative fragments.
3. Non-derivability can be shown by a finite search, as in [[fusion is commutative in FLe|SSHRBKVCK6]] and [[the non-example for contraction|P9WRDJWAXF]].

### Converse

The converse of part 1 holds: a cut-free derivation is a derivation.
So cut is admissible: adding it does not change the set of derivable sequents.

### Generalizations

The same proof works for the Lambek calculus, which has the rules for $\cdot$, $\backslash$ and $/$ restricted to nonempty antecedents.
With contraction, cut elimination needs a different induction, as for LK.

## History

The Wikipedia article on the cut-elimination theorem attributes the theorem for LK and LJ to Gentzen, in his paper of 1934 to 1935.
The proof for $\mathsf{FL}$ follows Gentzen's pattern, and it is shorter, since without contraction no mix rule is needed.

## Explanations

### L1 human

A cut is a step that proves a lemma and then uses it.
The theorem says that in these logics every lemma can be removed from a proof.
The proof without lemmas uses only pieces of the statement that it proves.
So a computer can search for such a proof among finitely many candidates.

### L2 human

We remove a cut on $A \cdot B$ from a small derivation in $\mathsf{FL}$.

1. The left premise is $A, B \Rightarrow A \cdot B$, from the axioms $A \Rightarrow A$ and $B \Rightarrow B$ by ${\cdot}\mathrm{R}$.
2. The right premise is $A \cdot B \Rightarrow A \cdot B$, from $A, B \Rightarrow A \cdot B$ by ${\cdot}\mathrm{L}$.
3. The cut gives $A, B \Rightarrow A \cdot B$.
4. The reduction replaces the cut by two cuts on $B$ and on $A$, both against axioms, which disappear.
5. The result is the derivation of step 1, which has no cut.

The typical use is to prove that a sequent is not derivable, by a search through cut-free derivations.
A trap: the search terminates only because no rule makes a premise larger than its conclusion, which fails with contraction.

### L3 human

Cut elimination for $\mathsf{FL}$ gives the decidability of the equational theory of residuated lattices, by the [[algebraic completeness|Q47701D0E1]] of $\mathsf{FL}$.
The method of the proof, a double induction on the cut formula and the heights, is the standard method for all the calculi of this sub-area.
For [[linear logic|2P2184B6HE]], the [[cut elimination for MLL|SYMW99C0EV]] has the same structure, with one-sided sequents.
