---
tag: VF1N6N8ECC
kind: example
name: The operator not X has no least fixed point
msc: ["03F15", "03F35"]
topics: [XTTKZTYDSD]
audience: research
not_instance_of:
  - target: 5VNT564Y2W
    note: the operator is not X-positive, so the closure and minimality axioms hold for the full set but do not describe a fixed point
  - target: 0A7KV2WB7A
    note: the operator reverses inclusion, so it is not monotone
uses: [45GQ3KQVT3, 0A7KV2WB7A, DBD64TH52D]
sources:
  - url: https://en.wikipedia.org/wiki/Theories_of_iterated_inductive_definitions
    locator: ID<sub>1</sub>
  - url: https://en.wikipedia.org/wiki/Least_fixed_point
    locator: lead section
---

## Example

Let $A(X, x) = \neg X(x)$.
As an operator on sets of natural numbers, it sends $S$ to $\Gamma(S) = \mathbb{N} \setminus S$.
We show that the axioms of the [[definition|45GQ3KQVT3]] for this $A$ do not describe a fixed point.

1. Positivity fails, because the only occurrence of $X$ stands under a negation.
2. [[Monotonicity|0A7KV2WB7A]] fails: $\emptyset \subseteq \{ 0 \}$, but $\Gamma(\emptyset) = \mathbb{N}$ is not contained in $\Gamma(\{ 0 \}) = \mathbb{N} \setminus \{ 0 \}$.
3. No fixed point exists: if $\Gamma(S) = S$, then $0 \in S$ holds exactly when $0 \notin S$, which is impossible.
   So there is no [[least fixed point|DBD64TH52D]].
4. The closed sets are the sets with $\Gamma(S) \subseteq S$, that is $\mathbb{N} \setminus S \subseteq S$, and the only such set is $\mathbb{N}$.
5. So both schemes hold with $I = \mathbb{N}$.
   The closure axiom reads $\forall x \, (\neg I(x) \to I(x))$, which forces $I = \mathbb{N}$, and the hypothesis of minimality forces $F$ to hold everywhere, so $I \subseteq F$.
6. But $I = \mathbb{N}$ is not a fixed point, because $A(\mathbb{N}, x)$ is false for every $x$.

So the theory with these axioms is consistent, but the fixed point lemma of $\mathrm{ID}_1$ fails, because its proof uses monotonicity.

## Remarks

Positivity is the condition that makes the axioms of $\mathrm{ID}_1$ mean "least fixed point".
For a positive operator, closure and minimality together prove $A(I_A) = I_A$.
For $\neg X$, minimality only gives the smallest closed set, and here the smallest closed set is not a fixed point.

The iterates $\Gamma(\emptyset) = \mathbb{N}$, $\Gamma(\mathbb{N}) = \emptyset$, $\Gamma(\emptyset) = \mathbb{N}$, and so on, flip back and forth, as the [[stages of a non-monotone operator|ED681VEX1B]] show in more detail.
A negative occurrence is allowed in $\mathrm{ID}_\nu$ only for a predicate of an earlier stage, which is already fixed when the new stage is defined.

## Explanations

### L1 human

Take the rule "a number is in the set if it is not in the set".
If a number is in the set, the rule says it should be out, and if it is out, the rule says it should be in.
So no set follows the rule exactly.
The only set that is closed under the rule is the set of all numbers, and it does not follow the rule exactly either.
Inductive definitions avoid this by forbidding a "not" in front of the set being defined.

### L2 human

We check the closed sets on the two-element set $\{ 0, 1 \}$ instead of $\mathbb{N}$, with $\Gamma(S) = \{ 0, 1 \} \setminus S$.
For $S = \emptyset$, $\{ 0 \}$ and $\{ 1 \}$ we get $\Gamma(S) = \{ 0, 1 \}$, $\{ 1 \}$ and $\{ 0 \}$, and none of these is inside $S$, so none of the three sets is closed.
For $S = \{ 0, 1 \}$ we get $\Gamma(S) = \emptyset \subseteq S$, so it is closed, but $\Gamma(S) \ne S$.

The example explains the positivity condition in a first course on inductive definitions.
Watch out: the least closed set is a fixed point only for monotone operators.
