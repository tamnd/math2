---
tag: NP9MTQ5QPZ
kind: example
name: The arithmetic mean is not a t-norm
msc: ["03B52"]
topics: [WZP584JQ06]
audience: grad
not_instance_of:
  - target: VR6D8JXX1W
    note: the mean is commutative and monotone, but 1 is not neutral and it is not associative
uses: [BHGCVPAJW0]
sources:
  - url: https://en.wikipedia.org/wiki/T-norm
    locator: Definition
---

## Example

Let $m(x, y) = (x + y)/2$ on $[0, 1]$.
Averaging sounds like a fair way to combine two degrees of truth, so we check the four axioms of a [[t-norm|BHGCVPAJW0]].

1. Commutativity holds, since $(x + y)/2 = (y + x)/2$.
2. Monotonicity holds: if $x \le x'$ and $y \le y'$, then $x + y \le x' + y'$, and halving keeps the order.
3. The unit law fails, since $m(0.4, 1) = 0.7 \ne 0.4$.
4. Associativity fails, as the two groupings of $0, 0, 1$ show.
   $$m(m(0, 0), 1) = m(0, 1) = \tfrac12, \qquad m(0, m(0, 1)) = m(0, \tfrac12) = \tfrac14.$$
5. The law $x * 0 = 0$, which every t-norm obeys, fails too, since $m(1, 0) = \tfrac12$.

So $m$ is not a t-norm.

## Remarks

The failure is not a detail.
As a conjunction, $m$ gives "true and false" the value $\tfrac12$, so it is not even classical on $\{0, 1\}$.
It also breaks the bound $x * y \le \min(x, y)$ that every t-norm obeys, because $m(0.4, 1) = 0.7 > 0.4$.

The mean is an aggregation operator, used to average scores, and in that role it is useful.
What it measures is "how true on average", not "how true are both".
Replace the mean by the geometric mean $\sqrt{xy}$ and the unit law still fails, since $\sqrt{0.25 \cdot 1} = 0.5 \ne 0.25$.

## Explanations

### L1 human

Averaging two degrees sounds like a fair "and", but it fails a basic test.
"$A$ and a fully true statement" should be exactly as true as $A$.
With $A$ true to degree $0.4$, the average gives $0.7$, which is more true than $A$ itself.

### L2 human

To rule out a candidate conjunction quickly, test two axioms first.
Test the unit law with $y = 1$, and test associativity on the values $0$ and $1$.
Here both tests fail at once.
Watch out: commutativity and monotonicity alone do not make a t-norm, and most averaging operators have both.
