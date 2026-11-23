---
tag: VK2A62AQ0F
kind: example
name: The drastic t-norm has no residuum
msc: ["03B52"]
topics: [WZP584JQ06]
audience: grad
instance_of: [VR6D8JXX1W]
not_instance_of:
  - target: PT5PHKJDYM
    note: without a residuum it gives no standard MTL-algebra
illustrates: [D1R4D2HEPP]
uses: [BHGCVPAJW0]
sources:
  - url: https://en.wikipedia.org/wiki/T-norm
    locator: Prominent examples; Residuum
---

## Example

The *drastic t-norm* is defined as follows.

$$x *_D y = \begin{cases} y & \text{if } x = 1, \\ x & \text{if } y = 1, \\ 0 & \text{otherwise.} \end{cases}$$

It is a [[t-norm|BHGCVPAJW0]], and it is the smallest one: every t-norm agrees with it when one argument is $1$, and is at least $0$ elsewhere.
We show that it has no residuum, by looking for the value of $0.5 \Rightarrow 0$.

1. A residuum would need the largest $z$ with $z *_D 0.5 \le 0$, so we compute the set $Z = \{ z : z *_D 0.5 \le 0 \}$.
2. For $z < 1$, neither argument is $1$, so $z *_D 0.5 = 0$, and $z \in Z$.
3. For $z = 1$, we get $1 *_D 0.5 = 0.5 > 0$, so $1 \notin Z$.
4. So $Z = [0, 1)$, and this set has no greatest element.
5. A residuum $r = 0.5 \Rightarrow 0$ would make $Z$ equal to $\{ z : z \le r \} = [0, r]$.
   No closed interval $[0, r]$ equals $[0, 1)$, so no residuum exists.
6. Left-continuity fails at the same place.
   The values $z_n = 1 - \tfrac1n$ increase to $1$, but $z_n *_D 0.5 = 0$ for every $n$, while $1 *_D 0.5 = 0.5$.

So the drastic t-norm is a t-norm without a residuum, as [[the left-continuity statement|D1R4D2HEPP]] predicts.

## Remarks

The example shows that the t-norm axioms alone do not give an implication.
The drastic t-norm is right-continuous, but the residuum needs left-continuity, and here the jump at $z = 1$ comes from the left.
The semantics of [[MTL|PT5PHKJDYM]] uses only left-continuous t-norms, so the drastic t-norm is not one of its standard models.

Change the second argument and the picture stays the same.
For any $x < 1$ and $y < x$, the set $\{ z : z *_D x \le y \}$ is again $[0, 1)$, so $x \Rightarrow y$ is undefined for all such pairs.
When $y \ge x$ the set is all of $[0, 1]$, and when $x = 1$ it is $[0, y]$, so in these cases a maximum exists.

## Explanations

### L1 human

The drastic "and" is zero unless one input is fully true.
Ask for the best value of "if $0.5$ then $0$": the largest $z$ such that "$z$ and $0.5$" is $0$.
Every value below $1$ works, but $1$ itself fails.
So there is no largest value, and the drastic "and" has no matching "if then".

### L2 human

The test for a residuum has three steps.
First, fix $x$ and $y$.
Second, find the set of all $z$ with $z * x \le y$.
Third, check whether that set has a maximum; if it has none, there is no residuum.
Watch out: the drastic t-norm is still a t-norm, and it fails only left-continuity.
