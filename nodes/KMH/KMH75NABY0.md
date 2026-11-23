---
tag: KMH75NABY0
kind: example
name: A finite Hintikka set with all four rule types
msc: ["03B10", "03F03"]
topics: [TTCRX3NFNY]
audience: ug2
instance_of: [RJNDEG07R1]
uses: [RJNDEG07R1, 2A6QP78XN3, 983GZBQYT4]
sources:
  - url: https://en.wikipedia.org/wiki/Hintikka_set
    locator: lead section
---

## Example

Let $L$ be the language with one constant symbol $c$, two unary relation symbols $P$ and $Q$, and no function symbols, so its only closed term is $c$.
Let $H$ be the set of six sentences
$$\forall x(P(x) \vee Q(x)),\quad \exists x(P(x) \wedge \neg Q(x)),\quad P(c) \vee Q(c),\quad P(c) \wedge \neg Q(c),\quad P(c),\quad \neg Q(c).$$
We check the five conditions of a [[Hintikka set|RJNDEG07R1]], one type of sentence at a time.

1. Condition 1: the only atom in $H$ is $P(c)$ and the only negated atom is $\neg Q(c)$, so no atom occurs with its negation.
2. Condition 2: the only $\alpha$ sentence is $P(c) \wedge \neg Q(c)$, and both $P(c)$ and $\neg Q(c)$ are in $H$.
3. Condition 3: the only $\beta$ sentence is $P(c) \vee Q(c)$, and its component $P(c)$ is in $H$.
   One component is enough.
4. Condition 4: the only $\gamma$ sentence is $\forall x(P(x) \vee Q(x))$, and its instance for the only closed term $c$ is $P(c) \vee Q(c)$, which is in $H$.
5. Condition 5: the only $\delta$ sentence is $\exists x(P(x) \wedge \neg Q(x))$, and its instance for $t = c$ is $P(c) \wedge \neg Q(c)$, which is in $H$.

So $H$ is a Hintikka set for $L$.
[[Hintikka's lemma|2A6QP78XN3]] gives the [[structure|983GZBQYT4]] $\mathcal{M}$ with domain $\{ c \}$, $P^{\mathcal{M}} = \{ c \}$ because $P(c) \in H$, and $Q^{\mathcal{M}} = \varnothing$ because $Q(c) \notin H$.
Check each member from the bottom up: $P(c)$ and $\neg Q(c)$ are true, so the conjunction and the disjunction are true, the universal sentence is true because its only instance is, and the existential sentence has the witness $c$.

## Remarks

### Why it is finite

The set shows all four rule types at work in one finite set.
It is finite because the language has one closed term, so the $\gamma$ sentence needs only one instance.

### What changes with the language

If $L$ also has a second constant $d$, condition 4 asks for $P(d) \vee Q(d)$, and condition 3 then asks for $P(d)$ or $Q(d)$.
So $H$ is not a Hintikka set for the larger language.
After we add $P(d) \vee Q(d)$ and $Q(d)$, it is one again, and the model has two elements.

If we add $\forall x\, Q(x)$ to $H$, condition 4 asks for $Q(c)$, which clashes with $\neg Q(c)$.
So no Hintikka set for $L$ contains the larger set, and indeed the larger set is unsatisfiable.

## Explanations

### L1 human

Think of a world with one ball, called $c$.
The list says "every ball is purple or quiet" and "some ball is purple and not quiet", and then it gives the simple facts about $c$ that back these claims.
Ball $c$ is purple, and ball $c$ is not quiet.
These simple facts do not contradict each other, so they describe a world, and each statement on the list is true in it.

### L2 human

The check of a Hintikka set goes from the long sentences down to the short ones.

1. Sort the members by type: here one $\alpha$, one $\beta$, one $\gamma$, one $\delta$ and two literals.
2. For each $\alpha$ sentence, find both components, and for each $\beta$ sentence, find one.
3. For each $\gamma$ sentence, find the instance for every closed term of the language.
4. For each $\delta$ sentence, find one instance.
5. Check the literals for a clash.

Watch out at step 3: the closed terms are those of the language $L$, not only those that occur in $H$.
