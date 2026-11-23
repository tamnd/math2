---
tag: VVY4Y14P0H
kind: example
name: Defining the smallest prime factor assumes that a prime factor exists
msc: ["00A35", "11A41"]
topics: [T6QQ749DM5]
audience: ug1
instance_of: [JPHE53PABT]
uses: [JPHE53PABT, 0VMWPGGG3C, 01BX15HSRR, 0SN0MAEKYX]
sources:
  - url: https://en.wikipedia.org/wiki/Circular_reasoning
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Well-ordering_principle
    locator: lead section
---

## Example

The claim: every integer $n \ge 2$ has a [[prime|0SN0MAEKYX]] factor.
Here is a false proof in three lines; find the gap before you read on.

1. Let $n \ge 2$, and let $p$ be the [[smallest prime factor|0VMWPGGG3C]] of $n$.
2. Then $p$ is prime and $p$ divides $n$.
3. So $n$ has a prime factor.

The gap is in step 1, and it is a [[circle|JPHE53PABT]].
"The smallest prime factor of $n$" exists only if the set of prime factors of $n$ is nonempty, and that set is nonempty exactly when $n$ has a prime factor, which is the claim.
So step 1 assumes the claim, and steps 2 and 3 only restate it.

A correct proof chooses the least element of a set whose nonemptiness we can check.

1. Let $D$ be the set of divisors $d$ of $n$ with $d \ge 2$. It is nonempty, because $n \in D$.
2. By the [[well-ordering principle|01BX15HSRR]], $D$ has a least element $q$.
3. Suppose that $q$ is not prime. Then $q = ab$ with $2 \le a < q$.
4. Then $a$ divides $q$ and $q$ divides $n$, so $a$ divides $n$, and $a \in D$ with $a < q$. This contradicts the choice of $q$.
5. So $q$ is prime and divides $n$, which proves the claim.

## Remarks

The two proofs differ only in the set from which they choose a least element.
The set $D$ is nonempty for a reason we can check, $n \in D$, while the set of prime factors is nonempty only by the claim.
Afterwards the correct proof even justifies the name: every prime factor of $n$ lies in $D$, so it is at least $q$, and $q$ is the smallest prime factor.
The same gap appears with every definite description.
"The least element of $S$", "the limit of $(a_n)$" and "the solution of the equation" each need a proof of existence first.

## Explanations

### L1 human

Imagine a proof that a box holds a red ball which starts with "take the smallest red ball in the box".
That first sentence already assumes that a red ball is there.
The argument never looks inside the box.
A correct argument first shows that a red ball is there, and only then talks about the smallest one.

### L2 human

We run the correct proof on $n = 91$.
The divisors of $91$ that are at least $2$ are $7$, $13$ and $91$, so $D = \{7, 13, 91\}$ and $q = 7$.
The number $7$ has no divisor $a$ with $2 \le a < 7$, so $7$ is prime, as step 5 promises.
Check: $91 = 7 \cdot 13$.

The typical use of this proof shape is any claim "every object has a part with property $P$": take a least part with a weaker property that surely exists, and prove that it has $P$.
Watch out for writing "let $x$ be the least element with property $P$" before any element with property $P$ is known.
