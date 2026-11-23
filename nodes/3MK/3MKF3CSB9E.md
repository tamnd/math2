---
tag: 3MKF3CSB9E
kind: example
name: A satisfiable set without a Herbrand model
msc: ["03B10"]
topics: [NJDME6F845]
audience: ug2
not_instance_of:
  - target: HKW429DSDK
    note: the model ({0, 1}, c = 0, P = {1}) of the set is not a Herbrand structure, and no Herbrand structure is a model, because the sentence with an existential quantifier is not universal
uses: [JAKSE2A1D4, B9C9NTWHZJ, 1WTCZB4DVB]
sources:
  - url: https://en.wikipedia.org/wiki/Herbrand_structure
    locator: lead section
---

## Example

Let $L = \{ c, P \}$, with a constant symbol $c$ and a unary relation symbol $P$.
Let
$$\Sigma = \{ \exists x \, P(x), \ \neg P(c) \}.$$
The set says "something has $P$, but the thing called $c$ does not".
We show that $\Sigma$ has a model but no [[Herbrand model|JAKSE2A1D4]].

1. Let $\mathcal{M}$ have domain $\{ 0, 1 \}$, $c^{\mathcal{M}} = 0$ and $P^{\mathcal{M}} = \{ 1 \}$.
2. The assignment $x \mapsto 1$ satisfies $P(x)$, so $\mathcal{M} \models \exists x \, P(x)$, by the clause for $\exists$ of [[satisfaction|1WTCZB4DVB]].
3. The value of $c$ is $0 \notin P^{\mathcal{M}}$, so $\mathcal{M} \models \neg P(c)$.
   So $\mathcal{M}$ is a model of $\Sigma$.
4. The Herbrand universe of $L$ is $\{ c \}$, because $L$ has no function symbols.
5. Let $\mathcal{H}$ be a Herbrand structure with $\mathcal{H} \models \neg P(c)$.
   Its domain is $\{ c \}$, and $c \notin P^{\mathcal{H}}$, so $P^{\mathcal{H}} = \emptyset$.
6. Then no element satisfies $P(x)$, and $\mathcal{H} \not\models \exists x \, P(x)$.
7. So no Herbrand structure is a model of $\Sigma$.

The condition that fails is that every sentence of $\Sigma$ is universal, which the [[theorem on Herbrand models|B9C9NTWHZJ]] requires.

## Remarks

The example shows that the hypothesis "universal" in the theorem cannot be dropped.
The witness $1$ of $\exists x \, P(x)$ in $\mathcal{M}$ is not the value of any closed term, so a structure made of names cannot copy it.

Skolemization repairs the situation: replace $\exists x \, P(x)$ by $P(d)$ for a new constant $d$.
The new set $\{ P(d), \neg P(c) \}$ is universal, and its Herbrand universe is $\{ c, d \}$.
Of the four choices of $P$ on $\{ c, d \}$, the sets $\emptyset$ and $\{ c \}$ fail $P(d)$, the set $\{ c, d \}$ fails $\neg P(c)$, and $\{ d \}$ satisfies both.
So the Skolemized set has exactly one Herbrand model.

Equality gives a second failure of the same kind: $\{ c = d \}$ has a one-element model, but no Herbrand model, because distinct terms are distinct elements.

## Explanations

### L1 human

The rules say "something has $P$" and "the thing called $c$ does not have $P$".
A world of names that only knows the name $c$ cannot satisfy both rules.
A world with one extra object, which has no name, can.

### L2 human

The typical use is to explain why theorem provers first Skolemize existential quantifiers.
After Skolemization the extra object gets the name $d$, and the search over Herbrand structures succeeds with $P = \{ d \}$.
Watch out: Skolemization keeps satisfiability but not equivalence.
The sentence $P(d)$ implies $\exists x \, P(x)$, but $\exists x \, P(x)$ does not imply $P(d)$, since a structure may give $d$ a value outside $P$.
