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
We show that the sentence is used as a [[biconditional|0S6GMNJ62Y]] instead.

1. Read as a one-way conditional, the sentence says only this: if $n = 2k$ for some integer $k$, then $n$ is even.
2. The sentence is the only place where the book defines "even".
   So on the one-way reading the book never says which integers are not even.
3. On that reading we could not prove that $3$ is not even.
   The hypothesis "$3 = 2k$ for some integer $k$" fails, and a conditional says nothing when its hypothesis fails.
4. The same books also use the other direction: if $n$ is even, then $n = 2k$ for some integer $k$.
   For example, the proof that the square of an even number is even starts with "write $n = 2k$".
5. So the sentence is used as "$n$ is even if and only if $n = 2k$ for some integer $k$".
   It is a definition, and the word "if" in it means "if and only if".

## Remarks

The convention is old and very common, and many books state it once near the start.
Some authors write "iff" or "exactly when" in definitions to avoid it.
The convention holds only in definitions.
In a theorem "if" is one-way: "a function is continuous if it is differentiable" does not claim the converse, and the converse is false.

A definition shows itself by its typography and its wording.
The new word is in italic or bold type, or the sentence says "is called" or "we say that".
When you see these signs, read "if" as "if and only if".

## Explanations

### L1 human

A book says "a number is called even if it can be split into two equal whole parts".
This sentence tells us exactly which numbers are even.
So it also tells us that a number that cannot be split in this way, such as $7$, is not even.
That is why the "if" of a definition works in both directions.

### L2 human

Use the definition "a subset $U$ of $\mathbb{R}$ is open if for each $a \in U$ there is $r > 0$ with $(a - r, a + r) \subseteq U$" to show that $[0, 1)$ is not open.
The direction we need is "if $U$ is open, then the condition holds", which is exactly the direction that the one-way reading leaves out.
Take $U = [0, 1)$ and $a = 0$, and let $r > 0$ be arbitrary.
The number $-r/2$ lies in $(-r, r)$, but $-r/2 < 0$, so $-r/2 \notin U$.
So the condition fails at $a = 0$, and $U$ is not open.

Proofs that an object does not have a property always use this direction of a definition.
Watch out: a student who reads the definition as one-way gets stuck at the last step and decides that the definition is too weak.
The definition is not too weak; it is a biconditional.
