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

Let $S$ be a set of real numbers, and assume that there is a real number $M$ with $s \le M$ for every $s \in S$.
We conclude that for every $s \in S$ there is a real number $y$ with $s \le y$.
In symbols, the inference passes from $\exists M \, \forall s \in S \, (s \le M)$ to $\forall s \in S \, \exists y \, (s \le y)$.

We check that the inference is valid.

1. Assume the premise, and fix $M$ with $s \le M$ for every $s \in S$.
2. Let $s \in S$ be arbitrary.
3. Take $y = M$. By step 1, $s \le y$.
4. Since $s$ was arbitrary, every $s \in S$ has such a $y$. This is the conclusion.
5. The same $y$ serves every $s$, and the conclusion asks only for some $y$ for each $s$. So the step loses information but makes no error.

So the inference is not an instance of the [[quantifier shift fallacy|CRW82NARQV]], which goes in the other direction.

## Remarks

The example shows that one direction of the exchange is always valid: $\exists y \, \forall x \, P(x, y)$ implies $\forall x \, \exists y \, P(x, y)$, by the same four steps with $P$ in place of $\le$.
The [[order of quantifiers|0FYQMKFE77]] makes the first statement stronger.
The conclusion of the example holds for every set $S$, with $y = s$, so here the conclusion is weaker than the premise "$S$ is bounded above".

## Explanations

### L1 human

If one key opens every door in a house, then every door can be opened by some key.
We just use the same key each time.
The opposite step is the dangerous one: if every door has a key, there need not be one key for all doors.

### L2 human

We use the valid direction in analysis.

1. A uniformly continuous function $f$ on a set $S$ satisfies: for each $\varepsilon > 0$ there is $\delta > 0$ such that for all $a, x \in S$ with $|x - a| < \delta$ we have $|f(x) - f(a)| < \varepsilon$.
2. Fix $a \in S$ and $\varepsilon > 0$. Take the $\delta$ of step 1 for this $\varepsilon$.
3. That $\delta$ works for the given $a$, since it works for all points.
4. So $f$ is continuous at $a$, and since $a$ was arbitrary, $f$ is continuous on $S$.

The typical use of this direction is to show that a uniform property implies the pointwise property.
A trap is to use the converse, from continuity to uniform continuity, without a further argument such as compactness.
