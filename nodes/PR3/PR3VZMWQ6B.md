---
tag: PR3VZMWQ6B
kind: example
name: From exists-for-all to for-all-exists is a valid inference
msc: ["00A35", "97E30"]
topics: [T6QQ749DM5]
audience: ug1
not_instance_of:
  - target: CRW82NARQV
    note: the inference goes from the stronger order to the weaker order, and it is valid
uses: [CRW82NARQV, 0FYQMKFE77]
sources:
  - url: https://en.wikipedia.org/wiki/Quantifier_shift
    locator: Definition
---

## Example

This inference also swaps two quantifiers; decide whether it is valid before you read on.

> Let $S$ be a set of real numbers, and suppose some real $M$ satisfies $s \le M$ for every $s \in S$.
> So for every $s \in S$ there is a real $y$ with $s \le y$.

In symbols it goes from $\exists M \, \forall s \in S \, (s \le M)$ to $\forall s \in S \, \exists y \, (s \le y)$.
It is valid, and here is the proof.

1. Fix $M$ as in the premise.
2. Let $s \in S$ be arbitrary, and take $y = M$. By the premise, $s \le y$.
3. Since $s$ was arbitrary, every $s \in S$ has such a $y$, which is the conclusion.

The conclusion asks only for some $y$ for each $s$, and one $y$ that serves every $s$ certainly qualifies.
So the step loses information but makes no error, and it is not the [[quantifier shift fallacy|CRW82NARQV]], which runs the other way.

## Remarks

One direction of the swap is always valid: $\exists y \, \forall x \, P(x, y)$ implies $\forall x \, \exists y \, P(x, y)$, by the same three steps with $P$ in place of $\le$.
So the [[order of quantifiers|0FYQMKFE77]] "exists, then for all" gives the stronger statement.
Here the loss is total: the conclusion holds for every set $S$, with $y = s$, while the premise says that $S$ is bounded above.

## Explanations

### L1 human

If one key opens every door in a house, then every door can be opened by some key.
We just use the same key each time.
The opposite step is the dangerous one: if every door has a key, there need not be one key for all the doors.

### L2 human

We use the valid direction to show that a uniformly continuous function $f$ on a set $S$ is continuous at every point.
Uniform continuity says that for each $\varepsilon > 0$ some $\delta > 0$ works for all $a, x \in S$: if $|x - a| < \delta$, then $|f(x) - f(a)| < \varepsilon$.
Fix a point $a \in S$ and $\varepsilon > 0$, and take the $\delta$ that uniform continuity gives for this $\varepsilon$.
That $\delta$ works at $a$, since it works at every point, so $f$ is continuous at $a$.

The typical use of this direction is to get a pointwise property from a uniform one.
Watch out for the converse, from continuity to uniform continuity, which needs a further argument such as compactness.
