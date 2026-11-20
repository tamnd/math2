---
tag: 6WKWVYFPN1
kind: example
name: Quantifier ranks of the dense order axioms
aliases: [quantifier-ranks-of-dense-order-axioms]
msc: ["03C07", "06A05"]
topics: [N64R1MGDBN]
audience: ug2
instance_of: [FVEVRE5XNZ]
uses: [FVEVRE5XNZ, MQ2KK8P8NT, K4D3S1MBZH, 0FRXBVVR03, V56GXSMWM6, 2W4S2H4VYA]
sources:
  - url: https://en.wikipedia.org/wiki/Quantifier_rank
    locator: Examples
  - book: isbn:9780521587136
    locator: Chapter 3
---

## Example

We compute the [[quantifier ranks|FVEVRE5XNZ]] of the axioms of [[dense linear orders without endpoints|2W4S2H4VYA]], in the signature $\set{<}$.

1. Irreflexivity $\forall x \, \neg(x < x)$ has rank $1$.
2. Transitivity $\forall x \, \forall y \, \forall z \, (x < y \wedge y < z \to x < z)$ has rank $3$.
3. Totality $\forall x \, \forall y \, (x < y \vee x = y \vee y < x)$ has rank $2$.
4. No endpoints, $\forall x \, (\exists y \, (y < x) \wedge \exists y \, (x < y))$, has rank $2$: the two inner quantifiers sit side by side.
5. [[Density|K4D3S1MBZH]], $\forall x \, \forall y \, (x < y \to \exists z \, (x < z \wedge z < y))$, has rank $3$.

So the whole theory is axiomatized by sentences of rank at most $3$.

## Remarks

The ranks show at which level two orders can first be told apart.
The orders $(\Z, <)$ and $(\Q, <)$ satisfy the same sentences of rank at most $2$, but density, of rank $3$, holds in $\Q$ and fails in $\Z$.
So $(\Z, <) \equiv_2 (\Q, <)$ and $(\Z, <) \not\equiv_3 (\Q, <)$; compare [[this example|V56GXSMWM6]].

The first claim follows from the [[Ehrenfeucht-Fraïssé theorem|72BMYXGFA8]], since Duplicator wins the game with $2$ rounds.
In round $1$ any answer works, since neither order has endpoints.
In round $2$ Spoiler picks an element below, equal to or above the first one, and Duplicator copies the relation on the other side.
Only "strictly between two given points" needs a third round, and that is where $\Z$ and $\Q$ differ.

## Explanations

### L1 human

Each axiom of a dense order says how far one must search to check it.
To check that there are no endpoints, we look at one point and then find a point beside it: two steps.
To check density, we look at two points and then find a point between them: three steps.
The integers pass every test with two steps and fail density, which needs three.

### L2 human

We find a rank $3$ sentence true in $(\Q, <)$ and false in $(\Z, <)$, and check that it is the density axiom.

1. Let $\sigma = \forall x \, \forall y \, (x < y \to \exists z \, (x < z \wedge z < y))$.
2. In $\Q$, for $x < y$ take $z = (x + y)/2$, so $\sigma$ holds.
3. In $\Z$, take $x = 0$ and $y = 1$; no integer $z$ satisfies $0 < z < 1$, so $\sigma$ fails.
4. The rank of $\sigma$ is $1 + 1 + 1 = 3$, since the three quantifiers are nested.

The typical use of these computations is to predict how many rounds Spoiler needs in a game.
A trap is to count the three quantifiers of the no-endpoints axiom and to say that its rank is $3$.
