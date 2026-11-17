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

Let $L$ be the language with one constant symbol $c$, two unary relation symbols $P$ and $Q$, and no function symbols.
The only closed term of $L$ is $c$.
Let $H$ be the set of the six sentences
$$\forall x(P(x) \vee Q(x)),\quad \exists x(P(x) \wedge \neg Q(x)),\quad P(c) \vee Q(c),\quad P(c) \wedge \neg Q(c),\quad P(c),\quad \neg Q(c).$$
We check the five conditions of a [[Hintikka set|RJNDEG07R1]], one sentence at a time.

1. Condition (1). The atomic members of $H$ are $P(c)$, and the negated atomic members are $\neg Q(c)$. The atom $Q(c)$ is not in $H$, so no atom occurs with its negation.
2. Condition (2). The only $\alpha$ sentence is $P(c) \wedge \neg Q(c)$. Its components $P(c)$ and $\neg Q(c)$ are both in $H$.
3. Condition (3). The only $\beta$ sentence is $P(c) \vee Q(c)$. Its component $P(c)$ is in $H$; one component is enough.
4. Condition (4). The only $\gamma$ sentence is $\forall x(P(x) \vee Q(x))$. Its instance for the only closed term $c$ is $P(c) \vee Q(c)$, and this is in $H$.
5. Condition (5). The only $\delta$ sentence is $\exists x(P(x) \wedge \neg Q(x))$. Its instance for $t = c$ is $P(c) \wedge \neg Q(c)$, and this is in $H$.

So $H$ is a Hintikka set for $L$.

[[Hintikka's lemma|2A6QP78XN3]] gives the [[structure|983GZBQYT4]] $\mathcal{M}$ with domain $\{c\}$, $P^{\mathcal{M}} = \{c\}$ (because $P(c) \in H$) and $Q^{\mathcal{M}} = \varnothing$ (because $Q(c) \notin H$).
We check each member: $P(c)$ is true; $\neg Q(c)$ is true; so $P(c) \wedge \neg Q(c)$ and $P(c) \vee Q(c)$ are true; $\forall x(P(x) \vee Q(x))$ is true because its only instance is true; $\exists x(P(x) \wedge \neg Q(x))$ is true with the witness $c$.

## Remarks

The example shows the four rule types at work in one finite set.
It is finite because the language has one closed term, so the $\gamma$ sentence has one instance.

The example changes in an instructive way when the language changes.
If $L$ also has a second constant $d$, then condition (4) asks for $P(d) \vee Q(d)$ and then for $P(d)$ or $Q(d)$, so $H$ is no longer a Hintikka set for this larger language.
After we add $P(d) \vee Q(d)$ and $Q(d)$, the set is again a Hintikka set, and the model has two elements.
If we add $\forall x\, Q(x)$ to $H$, condition (4) asks for $Q(c)$, which clashes with $\neg Q(c)$.
So no Hintikka set for $L$ contains the larger set, and indeed the larger set is unsatisfiable.

## Explanations

### L1 human

Think of a world with one ball, called $c$.
The list says: "every ball is purple or quiet", "some ball is purple and not quiet", and then the simple facts about $c$ that back these claims.
Ball $c$ is purple, and ball $c$ is not quiet.
These simple facts do not contradict each other, so they describe a world, and each statement on the list is true in it.

### L2 human

The check of a Hintikka set goes from the long sentences down to the short ones.

1. Sort the members by type: here one $\alpha$, one $\beta$, one $\gamma$, one $\delta$ and two literals.
2. For each $\alpha$ sentence, find both components in the set.
3. For each $\beta$ sentence, find one component.
4. For each $\gamma$ sentence, find the instance for every closed term of the language.
5. For each $\delta$ sentence, find one instance.
6. Check the literals for a clash.

The trap is step 4: the closed terms are those of the language $L$, not only those that occur in $H$.
