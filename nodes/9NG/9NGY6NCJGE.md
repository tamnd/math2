---
tag: 9NGY6NCJGE
kind: example
name: Dense linear orders are infinitely generic
aliases: [dense-linear-orders-infinitely-generic]
msc: ["03C25", "06A05"]
topics: [1A9JSC5YG8]
audience: research
instance_of: [2TYY0ZP7YQ]
uses: [2W4S2H4VYA, 0FRXBVVR03, YR6HCMABTE, 4C0VH5FDC6, E52RM0KX94]
sources:
  - url: https://en.wikipedia.org/wiki/Existentially_closed_model
    locator: Examples
  - book: isbn:9780387987606
    locator: Chapter 3
---

## Example

Let $T$ be the theory of [[linear orders|0FRXBVVR03]] in $L = \set{<}$.
It is universal, so $T_\forall = T$.
We show that every model $M$ of [[DLO|2W4S2H4VYA]] is infinitely generic for $T$, by induction on sentences $\varphi$ with parameters in $M$ built with $\neg$, $\land$ and $\exists$, for all models of $\mathrm{DLO}$ at once.

1. Atomic sentences, conjunctions and existential quantifiers: as for any structure, $M \Vdash \varphi \iff M \models \varphi$ follows from the definition and the induction hypothesis.
2. If $M \Vdash \neg \varphi$, then $M$ does not force $\varphi$, so $M \not\models \varphi$ by the induction hypothesis.
3. Suppose $M \models \neg \varphi$ and some linear order $N \supseteq M$ forces $\varphi$. The order $N$ embeds into a dense linear order $M'$ without endpoints, for example $N \times \Q$ with the lexicographic order, with $N$ embedded as $N \times \set{0}$.
4. By monotonicity $M' \Vdash \varphi$, so $M' \models \varphi$ by the induction hypothesis.
5. $\mathrm{DLO}$ has [[quantifier elimination|E52RM0KX94]], so it is [[model complete|YR6HCMABTE]], and $M \preceq M'$. So $M \models \varphi$, a contradiction. Hence $M \Vdash \neg \varphi$.

So every model of $\mathrm{DLO}$ is infinitely generic.

## Remarks

Every infinitely generic linear order is e.c., hence dense without endpoints by [[this example|4C0VH5FDC6]].
So the infinitely generic linear orders are exactly the models of $\mathrm{DLO}$, and $T^F = \mathrm{DLO}$.

When the order changes, the result changes: a linear order that is not dense, or has an endpoint, is not e.c., so it is not infinitely generic.
For the order $\set{0, 1}$, the negation clause fails, as the L2 explanation shows.

## Explanations

### L1 human

In a dense order without endpoints, every gap that a larger order could fill is already filled.
So asking "could this become true in a larger order?" gives the same answer as asking "is it true here?".

### L2 human

We check $\varphi = \exists x \, (a < x \land x < b)$ in $M = \Q$ with $a = 0$ and $b = 1$.

1. $\frac 1 2 \in \Q$ lies between $0$ and $1$, so $M \models \varphi$ and $M \Vdash \varphi$.
2. Now take $\neg \varphi$ in the order $\set{0, 1}$, which is not dense. The order $\set{0, \frac 1 2, 1}$ forces $\varphi$, so $\set{0, 1}$ does not force $\neg \varphi$, although $\neg \varphi$ is true in it.

So $\set{0, 1}$ is not infinitely generic, while $\Q$ is.
The typical use of the example is a second model case, where the model companion has quantifier elimination.
A trap is to check only the existential clause: the negation clause is where genericity can fail.
