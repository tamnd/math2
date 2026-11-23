---
tag: R496E8BXRB
kind: example
name: There is no empty plurality
msc: ["03A05", "03B16"]
topics: [MDHDYV8QZW]
audience: research
uses: [DZVEFDYYZX, G6X7SZSNC5, 0ECVK59Y03]
not_instance_of:
  - target: DZVEFDYYZX
    note: the empty set is a value of a second-order variable, but some things are always at least one thing
sources:
  - url: https://en.wikipedia.org/wiki/Plural_quantification
    locator: Formal definition
  - url: https://en.wikipedia.org/wiki/Second-order_logic
    locator: lead section
---

## Example

A set can be empty, but "some things" are always at least one thing.
This one difference is where the plural reading of second-order logic needs care.

The monadic second-order sentence $\sigma = \exists X \, \forall x \, \neg X x$ says that there is an empty set of elements.
We show that $\sigma$ is valid in [[second-order logic|G6X7SZSNC5]] with the full semantics.
Then we show that its direct reading as a [[plural quantification|DZVEFDYYZX]] is refutable.
So $\sigma$ is not a plural statement, and Boolos's translation needs a separate clause for the empty case.

1. In the full semantics, $X$ ranges over all subsets of the domain $M$, and the [[empty set|0ECVK59Y03]] is one of them.
   With $X = \emptyset$, the formula $\forall x \, \neg Xx$ is true, so $\sigma$ is true in every structure.
2. The direct plural reading of $\sigma$ is $\sigma_p = \exists xx \, \forall x \, \neg (x \prec xx)$.
   It says that there are some things such that nothing is one of them.
3. Plural logic has the axiom $\forall xx \, \exists y \, (y \prec xx)$: any things include at least one thing.
4. Let $xx$ be some things.
   By step 3 there is a $y$ with $y \prec xx$, so $\forall x \, \neg (x \prec xx)$ fails for $xx$.
   So $\neg \sigma_p$ is provable.
5. Boolos's translation of $\exists X \, \psi$ is $\psi[\emptyset] \lor \exists xx \, \psi[xx]$, where $\psi[\emptyset]$ replaces each atom $Xy$ by $y \neq y$.
   For $\psi = \forall x \, \neg Xx$, the two disjuncts are these:
   $$\forall x \, \neg (x \neq x) \qquad \text{and} \qquad \exists xx \, \forall x \, \neg (x \prec xx).$$
6. The first disjunct is valid, so the translation of $\sigma$ is valid, as $\sigma$ is.
   It is true because of the first disjunct alone, and that disjunct has no plural quantifier.

Check: by step 4 the second disjunct is $\sigma_p$, which is refutable, so the first disjunct carries the whole translation.

## Remarks

The example shows the one point where monadic second-order logic and plural logic differ: sets can be empty, and pluralities cannot.
Ordinary language agrees, since "there are some critics who ..." is false when there are no such critics.
Plural comprehension has the matching hypothesis $\exists y \, \varphi(y)$.
Without it, the instance for $\varphi(y) = (y \neq y)$ would give an empty plurality.

The difference does no harm to expressive power.
A second-order formula can exclude the empty set with $\exists x \, Xx$, and the first disjunct of Boolos's translation brings the empty set back.
For the sentence $\exists X \, \exists x \, Xx$, the roles change: the empty case is false, and only the plural disjunct matters.

## Explanations

### L1 human

In mathematics, the empty set is a set like any other: it is the set with no members.
In ordinary speech, "some things" always means at least one thing.
"There are some apples on the table" is false when the table is empty.
So "there is a set with no members" is true, but "there are some things, and none of them is anything" makes no sense.
When we read sets as "some things", we must treat the empty set separately.

### L2 human

We translate $\tau = \exists X \, (\forall x \, \neg Xx \land \exists y \, \neg Xy)$ with Boolos's rule.

1. Here $\psi = \forall x \, \neg Xx \land \exists y \, \neg Xy$.
2. The first disjunct $\psi[\emptyset]$ is $\forall x \, \neg (x \neq x) \land \exists y \, \neg (y \neq y)$.
   It is true in every structure, because domains are nonempty.
3. The second disjunct $\exists xx \, \psi[xx]$ is refutable, because its first conjunct says that nothing is one of $xx$.
4. So the translation of $\tau$ is valid, as $\tau$ is: the empty set misses some element.

The typical use of the rule is a correct translation of a second-order formula into plural logic.
Watch out: if you drop the first disjunct, valid second-order sentences such as $\tau$ become refutable plural sentences.
