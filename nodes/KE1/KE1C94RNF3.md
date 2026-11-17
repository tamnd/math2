---
tag: KE1C94RNF3
kind: example
name: A witness from an infinite descent argument by the A-translation
msc: ["03F30", "03F55"]
topics: [8XY7JYZKFW]
audience: grad
instance_of: [6CCK0TT69P]
uses: [6CCK0TT69P, ANXVZG97MG, RXHJPVMPJH, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Friedman_translation
    locator: Application
---

## Example

Let $f$ be a function from $\N$ to $\N$, given by a function symbol of the language.
We work in [[Heyting arithmetic|RXHJPVMPJH]] for this language, with $\le$ and $<$ as decidable relations, and with induction for all formulas.
The goal is $A = \exists y\, (f(y) \le f(y + 1))$: the values of $f$ cannot decrease forever.
We take the classical proof by contradiction and apply the [[A-translation|6CCK0TT69P]] for this $A$.

1. The classical proof assumes $H = \forall y\, \neg (f(y) \le f(y + 1))$, that is, $f(y + 1) < f(y)$ for every $y$.
2. Under $H$, it proves $\forall n\, (f(n) + n \le f(0))$ by [[induction|0ASJVEFA9J]] on $n$, since $f(n + 1) + n + 1 \le f(n) + n$.
3. For $n = f(0) + 1$ this gives $f(n) + f(0) + 1 \le f(0)$, which is false. So the proof derives $\neg H$, a double negation of $A$.
4. By Lemma F4 of the [[proof of conservativity|ANXVZG97MG]], the A-translation of $H$ is equivalent to $\forall y\, (f(y) \le f(y + 1) \to A)$.
5. This translated assumption is provable: from $f(y) \le f(y + 1)$, the rule ${\exists}\mathrm{I}$ gives $A$.
6. The induction formula $f(n) + n \le f(0)$ becomes $f(n) + n \le f(0) \vee A$, by Lemma F4.
7. Base case: $f(0) + 0 \le f(0)$ holds, so the disjunction holds.
8. Step: assume $f(n) + n \le f(0)$. If $f(n) \le f(n + 1)$, we get $A$ with $y = n$.
9. Otherwise $f(n + 1) < f(n)$, so $f(n + 1) + n + 1 \le f(n) + n \le f(0)$. If instead $A$ holds, $A$ still holds.
10. At $n = f(0) + 1$ the first disjunct is false, so $A$ holds.

So the translated proof is an intuitionistic proof of $A$, and it finds a witness $y \le f(0)$.

## Remarks

The translated proof is a search: it checks $n = 0, 1, \dots, f(0)$ in turn and stops at the first $n$ with $f(n) \le f(n + 1)$.
The bound $f(0)$ comes from the classical proof itself, from the length of the descent in step 3.
The bound is sharp: for $c \in \N$ and $f(n) = \max(c - n, 0)$, the first witness is $y = c = f(0)$.
Here HA could prove $A$ directly by a bounded search, but the A-translation finds this search without any insight into the problem.
For a $\Sigma^0_2$ statement, such as the existence of a minimum of $f$, the method does not apply directly; the [[no-counterexample interpretation|4BCD1EM542]] treats such statements.

## Explanations

### L1 human

A list of natural numbers cannot go down forever, since it starts at some number and each step loses at least $1$.
For example, if the list starts at $5$, it can go down at most $5$ times.
So among the first six steps there is a place where the list does not go down.
The A-translation turns the classical "it cannot go down forever" into exactly this search.

### L2 human

We run the translated proof for $f(0) = 3$, $f(1) = 2$, $f(2) = 2$.

1. At $n = 0$: $f(0) + 0 = 3 \le 3$, so the first disjunct holds.
2. Step from $0$: $f(0) = 3 > f(1) = 2$, so we continue with $f(1) + 1 = 3 \le 3$.
3. Step from $1$: $f(1) = 2 \le f(2) = 2$, so we get $A$ with $y = 1$.
4. The witness is $y = 1 \le f(0) = 3$.

The typical use of the method is to extract a bound from a classical proof by contradiction.
A trap is to apply the translation to $H$ in its original form $\forall y\, (f(y) \le f(y + 1) \to \bot)$ and to forget to add $A$ to the atoms.
