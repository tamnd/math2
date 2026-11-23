---
tag: NQR665PX9T
kind: example
name: Infinitely often versus eventually always in LTL
msc: ["03B44", "68Q60"]
topics: [CQM9SRN8PM]
audience: grad
instance_of: [RMJ56ZPA63]
uses: [8S64VZ6A1S, RMJ56ZPA63]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_temporal_logic
    locator: section Semantics
  - book: isbn:9780262026499
    locator: Baier and Katoen, Principles of Model Checking, chapter 5
---

## Example

In [[linear temporal logic|RMJ56ZPA63]] over $AP = \{p\}$, we compare recurrence and persistence:
$$GFp \ (\text{"$p$ infinitely often"}) \qquad\text{and}\qquad FGp \ (\text{"$p$ from some point on"}).$$
We show that $FGp \to GFp$ is valid and that its converse is not.

1. By [[the definition|8S64VZ6A1S]], $w \models GFp$ if and only if for every $i$ there is a $j \ge i$ with $p \in w_j$.
   So $GFp$ says that the set $\{j : p \in w_j\}$ is infinite.
2. In the same way, $w \models FGp$ if and only if there is an $i$ with $p \in w_j$ for all $j \ge i$.
   So $FGp$ says that the complement of that set is finite.
3. Take $w = (\emptyset\,\{p\})^\omega$, with $p$ exactly at the odd positions.
   The odd numbers form an infinite set, so $w \models GFp$.
4. The even numbers form an infinite set too, so $p$ fails at arbitrarily late positions, and $w \not\models FGp$.
   So $GFp \to FGp$ is not valid.
5. Conversely, let $w \models FGp$ with witness $i$.
   For any $k$, the position $\max(i, k) \ge k$ has $p$, so $w \models GFp$.
   Hence $FGp \to GFp$ is valid, and $FGp$ is strictly stronger.

## Remarks

Negation swaps the two shapes.
From $\neg G \equiv F\neg$ and $\neg F \equiv G\neg$ we get $\neg GFp \equiv FG\neg p$: "not infinitely often $p$" means "from some point on, never $p$".

The two shapes are the acceptance conditions of automata on infinite words.
Recurrence $GFp$ is the condition of a [[Büchi automaton|92DM43HQZT]], that some accepting state is visited infinitely often, and persistence $FGp$ is the dual co-Büchi condition.
Fairness assumptions are usually written in these forms, for example $GF\,\mathit{enabled} \to GF\,\mathit{taken}$.

## Explanations

### L1 human

"The light blinks forever" makes $GF\,\mathit{on}$ true, because the light comes on again and again.
It does not make $FG\,\mathit{on}$ true, because the light never stays on for good.
A light that flickers for a while and then stays on makes both true.

### L2 human

Three words show the three possible outcomes.
On $\emptyset\,\emptyset\,\{p\}^\omega$, both formulas hold, with witness $i = 2$ for $FGp$.
On $\{p\}\,\{p\}\,\emptyset^\omega$, both fail, because after position $1$ there is no $p$.
On $(\emptyset\,\{p\})^\omega$, only $GFp$ holds.
Watch out: $GFp$ and $FGp$ differ, but repeated operators of one kind collapse, $GGp \equiv Gp$ and $FFp \equiv Fp$.
