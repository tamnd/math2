---
tag: F75D6CZ5EC
kind: example
name: An infinite Hintikka set over the terms 0, s(0), s(s(0)), …
msc: ["03B10", "03F03"]
topics: [TTCRX3NFNY]
audience: ug2
instance_of: [RJNDEG07R1]
uses: [RJNDEG07R1, 2A6QP78XN3, 6D3WA7N2W4, 2BVB7YDEV4, 983GZBQYT4]
sources:
  - url: https://en.wikipedia.org/wiki/Hintikka_set
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Herbrand_structure
    locator: lead section
---

## Example

Let $L$ be the language with one constant symbol $0$, one unary function symbol $s$ and one binary relation symbol $R$.
The closed [[terms|6D3WA7N2W4]] of $L$ are $0, s(0), s(s(0)), \dots$, and this set $T_L$ is the [[Herbrand universe|2BVB7YDEV4]] of $L$.
For each closed term $t$, the term $s(t)$ is a different string from $t$, because it is longer.
Let
$$H = \{ \forall x\, \exists y\, R(x,y),\ \forall x\, \neg R(x,x) \} \cup \{ \exists y\, R(t,y),\ R(t, s(t)),\ \neg R(t,t) : t \in T_L \}.$$
We check the five conditions of a [[Hintikka set|RJNDEG07R1]].

1. Condition 1: the atoms in $H$ are the sentences $R(t, s(t))$, and the negated atoms are the sentences $\neg R(u,u)$.
   A clash would need $R(u,u) = R(t, s(t))$, so $u = t$ and $u = s(t)$, and then $t = s(t)$, which is impossible since $s(t)$ is longer.
2. Conditions 2 and 3: $H$ has no $\alpha$ sentence and no $\beta$ sentence.
   The sentences $\neg R(t,t)$ are negated atoms, not $\alpha$ sentences.
3. Condition 4: the $\gamma$ sentences are $\forall x\, \exists y\, R(x,y)$ and $\forall x\, \neg R(x,x)$.
   Their instances at a closed term $t$ are $\exists y\, R(t,y)$ and $\neg R(t,t)$, and both are in $H$ for every $t$.
4. Condition 5: the $\delta$ sentences are the sentences $\exists y\, R(t,y)$.
   For each of them the instance at the closed term $s(t)$ is $R(t, s(t))$, which is in $H$.

So $H$ is an infinite Hintikka set for $L$.
[[Hintikka's lemma|2A6QP78XN3]] gives the [[structure|983GZBQYT4]] $\mathcal{M}$ with domain $T_L$, $s^{\mathcal{M}}(t) = s(t)$, and $R^{\mathcal{M}} = \{ (t, s(t)) : t \in T_L \}$.
If we write $n$ for the term with $n$ copies of $s$ in front of $0$, then $\mathcal{M}$ is isomorphic to the natural numbers with $R$ the relation $y = x + 1$.
Check: each element has an $R$-successor, and no element is $R$-related to itself, as $H$ requires.

## Remarks

### Why it must be infinite

A Hintikka set that contains a $\gamma$ sentence is infinite whenever the language has a function symbol.
Condition 4 asks for an instance at each of the infinitely many closed terms.

### Other models of the same set

The model of the lemma is infinite here, but $H$ also has finite models.
Take the domain $\{ 0, 1 \}$, let $s$ swap $0$ and $1$, and let $R = \{ (0,1), (1,0) \}$.
Every member of $H$ is true there, since a term $t$ and the term $s(t)$ always get different values.
So the lemma gives one model, the term model, and not the only one.
If we add $R(0,0)$ to $H$, condition 1 fails, because $\neg R(0,0) \in H$.

## Explanations

### L1 human

Start with the number $0$ and the rule "add one".
The list of facts says that every number is related to some number, and that no number is related to itself.
For each number $n$ the list names the related number: it is $n + 1$.
The list never says that a number is related to itself, so there is no clash.
The world that the list describes is the counting numbers, with each number related to the next.

### L2 human

The check of condition 5 needs a witness term for each $\delta$ sentence, and here the witness of $\exists y\, R(t,y)$ is $s(t)$.

1. Take $t = 0$: the sentence $\exists y\, R(0,y)$ is in $H$, and its witness instance $R(0, s(0))$ is in $H$.
2. Take $t = s(0)$: the witness instance of $\exists y\, R(s(0), y)$ is $R(s(0), s(s(0)))$, which is in $H$.

The typical use of such a set is a term model in which a function symbol supplies the witnesses, as in the Skolem normal form of a theory.
Watch out for the choice of witness: the witness $t$ itself would give $R(t,t)$, which clashes with $\neg R(t,t)$.
