---
tag: F1GYSA9TW0
kind: example
name: Every number has a larger one, but no number is larger than all
msc: ["00A35", "97E30"]
topics: [T6QQ749DM5]
audience: school
instance_of: [CRW82NARQV]
uses: [CRW82NARQV, 0FYQMKFE77, 0MWKJ44V5A]
sources:
  - url: https://en.wikipedia.org/wiki/Quantifier_shift
    locator: Examples
---

## Example

Here is a two-line "proof" that one of the [[natural numbers|0MWKJ44V5A]] is larger than all of them; spot the flaw.

> Every natural number $x$ has a larger natural number $y$, for instance $y = x + 1$.
> So there is a natural number $y$ that is larger than every natural number $x$.

In symbols, the argument goes from $\forall x \, \exists y \, (y > x)$ to $\exists y \, \forall x \, (y > x)$.
We check each half.

1. The premise is true: for a given $x$, the number $y = x + 1$ is natural and $y > x$.
2. The conclusion is false. If some $y_0$ satisfied $y_0 > x$ for every $x$, then $x = y_0$ would give $y_0 > y_0$.
3. True premise and false conclusion mean the inference is invalid.
4. The step that fails swaps $\forall x$ and $\exists y$, which is the [[quantifier shift fallacy|CRW82NARQV]]. The $y$ of step 1 depends on $x$, and no single $y$ serves every $x$.

The correct conclusion keeps the order: every natural number has a larger one, and no natural number is larger than all.

## Remarks

The [[order of quantifiers|0FYQMKFE77]] changes the meaning even though the predicate $y > x$ stays the same.
Changing the domain shows how fragile the premise is.
On the finite set $\{1, 2, 3\}$ the premise itself is false, since $3$ has no larger element in the set.
With $y \ge x$ in place of $y > x$ on a finite set, both orders are true, and $y$ is the largest element.

## Explanations

### L1 human

For every number we can find a bigger one: add $1$.
No number is bigger than every number, since it would have to be bigger than itself.
The first sentence lets the bigger number change with the given number.
The second asks for one number that works for all, which is a much stronger claim.

### L2 human

We decide which order holds for the predicate $x + y = 0$ on the integers.
The statement $\forall x \, \exists y \, (x + y = 0)$ is true: for each $x$, take $y = -x$.
The statement $\exists y \, \forall x \, (x + y = 0)$ is false: a single $y_0$ would need $0 + y_0 = 0$ and $1 + y_0 = 0$, so $y_0 = 0$ and $y_0 = -1$ at once.
So passing from the first to the second is a quantifier shift.

The typical use of this test is to try two values of $x$ and see whether one $y$ can serve both.
Watch out for reading "there is a $y$ such that for every $x$" as "for every $x$ there is a $y$" because both phrases appear in one sentence.
