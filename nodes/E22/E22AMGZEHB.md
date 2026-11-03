---
tag: E22AMGZEHB
kind: statement
role: lemma
name: Hotelling's lemma
msc: [91B38, 91B24]
uses: [0ABK9V9Y64, 0K57YG3BB8]
sources:
  - url: https://en.wikipedia.org/wiki/Hotelling%27s_lemma
same_as:
  wikidata: Q139965
  wikipedia: Hotelling's lemma
---

## Statement

Let $Y \subseteq \R^n$ be a nonempty production set: a vector $y \in Y$ is a production plan, with positive entries for outputs and negative entries for inputs.
For a price vector $p \in \R^n$, let the profit function be $\pi(p) = \sup \set{p \cdot y : y \in Y}$.
Let $\bar p$ be a price vector such that $\pi$ is finite near $\bar p$ and [[differentiable|0K57YG3BB8]] at $\bar p$.
Let $\bar y \in Y$ be a profit-maximizing plan at $\bar p$, so that $\bar p \cdot \bar y = \pi(\bar p)$.
Then
$$\nabla \pi(\bar p) = \bar y,$$
that is, $\partial \pi / \partial p_i (\bar p) = \bar y_i$ for every good $i$.
In particular, the profit-maximizing plan at $\bar p$ is unique.

## Remarks

For every $p$, the plan $\bar y$ is still available, so $\pi(p) \ge p \cdot \bar y$, with equality at $p = \bar p$.
So $p \mapsto \pi(p) - p \cdot \bar y$ has a minimum at $\bar p$, and its [[gradient|0ABK9V9Y64]] vanishes there.
This is a case of the [[envelope theorem|WK7MKDWRFF]].
Conversely, under standard conditions, if the profit-maximizing plan at $\bar p$ is unique, then $\pi$ is differentiable at $\bar p$.

Example: a firm turns an input $x \ge 0$ into output $\sqrt{x}$, with output price $p$ and input price $w$.
Maximizing $p \sqrt{x} - w x$ gives $x = p^2 / (4 w^2)$, output $p / (2w)$ and profit $\pi(p, w) = p^2 / (4 w)$.
Then $\partial \pi / \partial p = p / (2w)$ is the output and $\partial \pi / \partial w = - p^2 / (4 w^2)$ is minus the input, as the lemma says.

## Explanations

### L1 human

The profit function says how much a firm can earn at given prices.
Hotelling's lemma says that if the price of the product goes up a little, profit goes up by that change times the amount the firm sells.
If the price of an input goes up, profit goes down by the change times the amount of input used.
So supply and input demand can be read off the profit function by differentiating.

### L2 human

The lemma is the producer counterpart of [[Shephard's lemma|T968JGCJHC]].
Since $\pi$ is a supremum of linear functions of $p$, it is convex, so its Hessian is positive semidefinite where it exists.
By the lemma this Hessian is the matrix of price derivatives of supply, which gives the law of supply: a plan responds to its own price in the same direction.
The symmetry of the Hessian gives reciprocity relations between cross-price effects.
