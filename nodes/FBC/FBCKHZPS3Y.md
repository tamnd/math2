---
tag: FBCKHZPS3Y
kind: example
name: The "if" of a definition is not a one-way conditional
msc: ["97E40"]
topics: [WMY13MXY3W]
audience: school
not_instance_of:
  - target: FA6YZGR2SS
    note: in a definition the word "if" means "if and only if", so the sentence is not a one-way conditional
uses: [FA6YZGR2SS, 0S6GMNJ62Y]
sources:
  - url: https://en.wikipedia.org/wiki/If_and_only_if
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Definition
    locator: lead section
---

## Example

A textbook writes: "an integer $n$ is even if $n = 2k$ for some integer $k$".
The word "if" suggests a one-way [[conditional statement|FA6YZGR2SS]].
We show that the sentence is not used as a one-way conditional, but as a [[biconditional|0S6GMNJ62Y]].

1. Read as a one-way conditional, the sentence says only: if $n = 2k$ for some integer $k$, then $n$ is even.
2. The sentence is the only place where the book defines "even". So on the one-way reading, the book never says which integers are not even.
3. On that reading, we could not prove that $3$ is not even. The hypothesis "$3 = 2k$" fails, and a conditional says nothing when its hypothesis fails.
4. The same books also use the converse: if $n$ is even, then $n = 2k$ for some integer $k$. For example, the proof that the square of an even number is even starts with "write $n = 2k$".
5. So the sentence is used as "$n$ is even if and only if $n = 2k$ for some integer $k$". It is a definition, and the word "if" in it means "if and only if".

## Remarks

This convention is old and very common, and many books state it once, near the start.
Some authors write "iff" or "exactly when" in definitions to avoid it.
The convention holds only in definitions.
In a theorem, "if" is one-way: "a function is continuous if it is differentiable" does not claim the converse, and the converse is false.

A sign of a definition is a word in italic or bold type, or a phrase such as "is called" or "we say that".
When these signs are present, a reader should read "if" as "if and only if".

## Explanations

### L1 human

A book says "a number is called even if it can be split into two equal whole parts".
This sentence tells us exactly which numbers are even.
So it also tells us that a number that cannot be split in this way, such as $7$, is not even.
That is why the "if" in a definition works in both directions.

### L2 human

We use the definition "a subset $U$ of $\mathbb{R}$ is open if for each $a \in U$ there is $r > 0$ with $(a - r, a + r) \subseteq U$" to show that $[0, 1)$ is not open.

1. We need the direction "if $U$ is open, then the condition holds". This is the converse of the one-way reading, and the definition gives it.
2. For $U = [0, 1)$ and $a = 0$, take any $r > 0$. The number $-r/2$ lies in $(0 - r, 0 + r)$, but $-r/2 < 0$, so $-r/2 \notin U$.
3. So the condition fails at $a = 0$, and by step 1, $U$ is not open.

The typical use of the converse direction of a definition is in a proof that an object does not have a property.

A trap: a student who reads the definition as one-way cannot do step 3.
The student then thinks that the definition is not strong enough, but the definition is a biconditional.
