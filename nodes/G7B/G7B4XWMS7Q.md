---
tag: G7B4XWMS7Q
kind: problem
name: Identity of proofs
msc: ["03F03", "03F05", "03F52"]
topics: [R10RMQCJQX]
audience: research
uses: [PAQ4ZX2TX1, W33WAE1XTC, AYRZ98Y0NW, A77FER1Q5H]
about: [PAQ4ZX2TX1, W72CA3R9MP]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%27s_twenty-fourth_problem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Proof_net
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Cartesian_closed_category
    locator: lead section
history:
  notes: "Hilbert's notes for a 24th problem, on criteria for the simplicity of proofs, were found by Thiele in 2000; the normalization criterion is due to Prawitz."
---

## Problem

Proof theory has a precise notion of a derivation but no agreed notion of a proof: we do not know when two different-looking derivations are the same proof.
Here is the smallest case.
From the assumption $p \wedge p$, [[natural deduction|PAQ4ZX2TX1]] derives $p$ by $\wedge$E$_1$, and also by $\wedge$E$_2$.
A third derivation takes both parts, joins them by $\wedge$I, and takes the first part again.
Most people say that the first and third are one proof, but are the first and second one proof or two?

The problem asks for a natural equivalence relation on derivations with the same conclusion, in a fixed calculus such as natural deduction or the [[sequent calculus|W72CA3R9MP]], with two properties.
It should identify derivations that differ only by inessential choices, such as the order of two independent rule steps or a detour that a reduction removes.
It should not identify all derivations of one conclusion, since then a proof would carry no more information than the fact that its conclusion is derivable.
It also asks for a canonical representative or a complete invariant of each class.
There is no generally accepted answer, and the answers proposed differ between intuitionistic and classical logic.

## Remarks

### The normalization criterion

The best-studied answer says that two derivations in intuitionistic natural deduction are the same proof when they reduce to the same normal form.
The reductions are the detour reductions together with the expansions that [[harmony|XJSQVK0G71]] supplies.
By the [[normalization theorem|W33WAE1XTC]] every derivation has a normal form, and for implication and conjunction the resulting relation is decidable.

In the opening case, the third derivation has a detour on $p \wedge p$, and one reduction turns it into the first.
The first and second are both normal and different, so they are two proofs.
Under the [[Curry-Howard correspondence|A77FER1Q5H]] they are the [[lambda terms|BD756KR8FM]] $\pi_1 x$ and $\pi_2 x$, the two projections from $p \times p$ to $p$.
In general the relation becomes beta-eta equality of typed terms, and for implication, conjunction and truth the classes are the morphisms of the free [[cartesian closed category|BFBNQ36QS8]] on the atoms.

### Collapse in classical logic

For LK, the same idea identifies too much.
Take any two derivations $\pi_1$ and $\pi_2$ of $\Gamma \Rightarrow \Delta$.
Weaken the first to $\Gamma \Rightarrow \Delta, A$ and the second to $A, \Gamma \Rightarrow \Delta$, and cut on $A$.
The cut can be eliminated in two ways, by deleting either premise, and the results are $\pi_1$ and $\pi_2$ followed by weakenings.
So if a cut-elimination step keeps the proof the same, all derivations of one sequent are one proof, up to weakenings.
This is why cut elimination in LK is not confluent, and why normal forms there are not unique.

### Collapse in categories, continued

The same collapse appears in categorical semantics, by an argument of Joyal.
Let a cartesian closed category have an initial object $0$, and let the canonical map from each $B$ to $(B \Rightarrow 0) \Rightarrow 0$ be an isomorphism.

1. For every object $A$, the product $A \times 0$ is initial, since $A \times (-)$ is a left adjoint and so preserves initial objects.
2. Suppose there is a morphism $f : A \to 0$.
   Then $\langle \mathrm{id}_A, f \rangle : A \to A \times 0$ and the projection $A \times 0 \to A$ are inverse: one composite is $\mathrm{id}_A$ by the product property, and the other is an endomorphism of the initial object $A \times 0$, hence the identity.
3. So such an $A$ is initial, and there is at most one morphism $A \to 0$.
4. Morphisms $A \to B$ correspond to morphisms $A \to (B \Rightarrow 0) \Rightarrow 0$, and so to morphisms $A \times (B \Rightarrow 0) \to 0$, of which there is at most one by step 3.

So the category is a preorder, and all derivations of one sequent get one meaning.

### Other representations

[[Linear logic|2P2184B6HE]] offers [[proof nets|HN6WN1VE39]], introduced by Girard in 1987, graphs that forget the order of independent rule steps.
For the multiplicative fragment without units, two cut-free sequent derivations have the same proof net exactly when one comes from the other by permutations of rules.
The *generality criterion* identifies two derivations when they link the same occurrences of atomic formulas in the conclusion, and Došen compared it with the normalization criterion.
On the opening case the two criteria agree: $\wedge$E$_1$ links the conclusion $p$ to the first $p$ of $p \wedge p$, and $\wedge$E$_2$ to the second.

### Watch out

The normalization criterion does not transfer to LK as it stands.
A student who reasons "cut elimination gives a normal form, so compare normal forms" meets the collapse above, because one derivation with a cut has several cut-free forms.
Any classical answer must give up some step of that argument, either some cut-elimination steps or some structure of a cartesian closed category.

## History

Hilbert considered a 24th problem for his list of 1900, on criteria for the simplicity of proofs, but he did not include it.
Rüdiger Thiele found it in Hilbert's notebooks in 2000, and published an account in the American Mathematical Monthly in 2003.
Prawitz proposed the normalization criterion, which is now called the normalization conjecture.
Lambek connected derivations in intuitionistic logic with morphisms of cartesian closed categories.
Girard introduced proof nets for linear logic in 1987, the year he introduced linear logic.

## Explanations

### L1 human

Two people can prove the same theorem in ways that look different on paper.
Sometimes one proof only writes the steps in another order, and we feel that it is the same proof.
Sometimes the two proofs use different ideas, and we feel that they are different proofs.
The problem is to turn this feeling into an exact rule for formal proofs.
From "$p$ and $p$" we can conclude $p$ by taking the first part or by taking the second part, and the question is whether these are one proof or two.

### L2 human

Compare two derivations of $p \wedge q \to q \wedge p$, as lambda terms.
The first is $\lambda x.\, \langle \pi_2 x, \pi_1 x \rangle$.
The second first swaps and then swaps back and swaps again:
$$\lambda x.\, \bigl(\lambda y.\, \langle \pi_2 y, \pi_1 y \rangle\bigr)\Bigl(\bigl(\lambda z.\, \langle \pi_2 z, \pi_1 z \rangle\bigr)\bigl(\langle \pi_2 x, \pi_1 x \rangle\bigr)\Bigr).$$
Beta reduction of the inner application gives $\langle \pi_1 x, \pi_2 x \rangle$, and the outer one then gives $\langle \pi_2 x, \pi_1 x \rangle$, after the projection reductions $\pi_1 \langle s, t \rangle = s$ and $\pi_2 \langle s, t \rangle = t$.
So the two derivations have the same normal form and are one proof under the normalization criterion.
This is the typical use: decide identity by computing normal forms, which works because intuitionistic normalization is confluent.

### L3 human

The problem asks for the right notion of morphism between formulas, so it is a question of categorical proof theory.
For intuitionistic logic, cartesian closed categories give a stable answer, and the [[Curry-Howard correspondence|A77FER1Q5H]] connects it with the equality of programs.
For classical logic a semantics must give up some structure, to escape Joyal's collapse; proposals include proof nets for classical logic, categories with weaker structure for disjunction, and the atomic flows of [[deep inference|4ZW0SHW2RG]].
[[Focusing|AMMKNENT3R]] restricts the derivations of a sequent to a smaller class, and so removes many inessential permutations.
The question of simple proofs in Hilbert's notes needs an answer to the question of identity first, since a measure of simplicity should not depend on the presentation.
