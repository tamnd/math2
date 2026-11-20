---
tag: 81EJ8BVE5Q
kind: example
name: A partial model in which excluded middle fails
msc: ["03B50", "03B60"]
topics: [NJB94B39QK]
audience: ug2
instance_of: [F5SP7HQFFS]
uses: [F5SP7HQFFS, 0RYYK8PG4S, 4CBCWZQZ12]
sources:
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: Many-Valued Logic (SEP entry), section 2
  - url: https://en.wikipedia.org/wiki/Three-valued_logic
    locator: Kleene and Priest logics
---

## Example

Let $M$ be the partial model with domain $\set{a, b}$ and one unary predicate $P$, with extension $P^{+} = \set{b}$ and anti-extension $P^{-} = \emptyset$.

1. $Pb$ is $\mathsf{T}$, since $b \in P^{+}$.
2. $Pa$ is $\mathsf{U}$, since $a$ is in neither $P^{+}$ nor $P^{-}$.
3. $\neg Pa$ is $\mathsf{U}$, by the strong Kleene table of $\neg$.
4. $Pa \lor \neg Pa = \max(\mathsf{U}, \mathsf{U}) = \mathsf{U}$.
5. $\forall x\,(Px \lor \neg Px)$ is not $\mathsf{T}$, since it fails at $a$. It is not $\mathsf{F}$ either, since no instance is $\mathsf{F}$. So it is $\mathsf{U}$.

So the [[law of excluded middle|0RYYK8PG4S]] is not valid in [[partial logic|F5SP7HQFFS]].
The atom $Pa$ is a [[truth-value gap|4CBCWZQZ12]].

Now extend $M$ to $N$ by putting $a$ into $P^{-}$.
Then $Pa$ is $\mathsf{F}$, $\neg Pa$ is $\mathsf{T}$, and $Pa \lor \neg Pa$ is $\mathsf{T}$.
The value of $Pb$ is still $\mathsf{T}$: the extension changed only undefined values.

## Remarks

The second half of the example shows monotonicity: adding information turns some $\mathsf{U}$ values into $\mathsf{T}$ or $\mathsf{F}$, and never changes a defined value.
Every partial model can be extended to a total, classical model, by putting each undecided tuple into $P^{+}$ or $P^{-}$.
So every K3-valid inference is classically valid.

## Explanations

### L1 human

Suppose a register lists $b$ as a member and says nothing about $a$.
Then "$a$ is a member or $a$ is not a member" has no definite value from the register.
When the register later records that $a$ is not a member, the statement becomes true.

### L2 human

The key line is $\max(\mathsf{U}, \mathsf{U}) = \mathsf{U}$.
Excluded middle needs one of its disjuncts to be true, and neither is.
A trap is to think that $\neg Pa$ is true because $Pa$ is not true; in partial logic, $\neg Pa$ is true only when $a \in P^{-}$.
