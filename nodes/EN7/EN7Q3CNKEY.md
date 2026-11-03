---
tag: EN7Q3CNKEY
kind: statement
role: theorem
name: Principle of induction for subsets of the nonnegative integers
msc: [03F30]
uses: [0ASJVEFA9J, 0MWKJ44V5A]
about: [0ASJVEFA9J]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_background_formal-num-sys.ptx#L61
    locator: source/s_background_formal-num-sys.ptx:61
---

## Statement

Let $M$ be a subset of the set of nonnegative integers.
Then $M$ is the whole set of nonnegative integers if and only if two conditions hold.
First, $0$ lies in $M$.
Second, for every nonnegative integer $k$, if $k$ lies in $M$, then $k+1$ lies in $M$.

## Remarks

This is the set form of [[induction|0ASJVEFA9J]] on the [[natural numbers|0MWKJ44V5A]].
Apply it to the set of numbers $n$ for which a property $P(n)$ holds.
The direction from the two conditions to $M$ being everything is the useful one.
The other direction is immediate, since the whole set contains $0$ and is closed under adding $1$.
