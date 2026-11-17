---
tag: MVHPHA20AY
kind: example
name: A transposition and a 3-cycle are not conjugate in S3
msc: ["20B30"]
topics: [E1506A5A55]
audience: ug1
not_instance_of:
  - target: 0DXD4QSZ8A
    note: (1 2) has order 2 and (1 2 3) has order 3, and conjugate elements have the same order
uses: [0515A6D2Y1, 0WE2NHZJ7B, 0ZKPH2BD1T]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugacy_class
    locator: Properties
---

## Example

Let $G = S_3$ be the [[symmetric group|0515A6D2Y1]] on $\{1, 2, 3\}$.
We use [[cycle notation|0ZKPH2BD1T]] and compose permutations from right to left, so $\sigma\tau$ means first $\tau$, then $\sigma$.
We show that $a = (1\,2)$ and $b = (1\,2\,3)$ are not [[conjugate|0DXD4QSZ8A]] in $S_3$.

1. $a^2 = (1\,2)(1\,2) = e$, because the second swap undoes the first swap. Also $a \ne e$. So $a$ has [[order|0WE2NHZJ7B]] $2$.
2. $b^2 = (1\,3\,2)$, because $b^2$ sends $1$ to $3$, $3$ to $2$ and $2$ to $1$. So $b^2 \ne e$.
3. $b^3 = b \, b^2 = (1\,2\,3)(1\,3\,2) = e$, because $(1\,3\,2)$ is the inverse of $(1\,2\,3)$. Also $b \ne e$. So $b$ has order $3$.
4. Conjugate elements have the same order, by the basic properties of [[conjugate elements|0DXD4QSZ8A]].
5. The orders $2$ and $3$ differ. So $a$ and $b$ are not conjugate in $S_3$.

We can also check this directly.
For each $g \in S_3$, the permutation $gag^{-1}$ swaps the two points $g(1)$ and $g(2)$ and fixes the third point.
So each conjugate of $a$ is a transposition, and $b$ is not a transposition.

## Remarks

This example uses an invariant of conjugacy, the order of an element.
The test works in one direction only.
Two elements with the same order need not be conjugate.
For example, in the abelian group $\mathbb{Z}/3\mathbb{Z}$, the elements $1$ and $2$ both have order $3$, but each element is conjugate only to itself.
In $S_3$ the order happens to be a complete test: the conjugacy classes are $\{e\}$, the three transpositions and the two $3$-cycles.

## Explanations

### L1 human

A swap of two cups and a turn of all three cups are different kinds of moves.
If we do a swap twice, every cup is back in its place.
If we do a turn twice, the cups are not back yet.
A renaming of the cups cannot change this fact.
So no renaming turns a swap into a turn.

### L2 human

To show that two elements are conjugate, it is enough to find one $g$ with $gag^{-1} = b$.
To show that two elements are not conjugate, we must exclude every $g$.
For a small group we can try every $g$, but an invariant is faster.
An invariant is a number that does not change under conjugation, such as the order of an element.
If the invariant differs, the elements are not conjugate.
In $S_n$ the full invariant is the cycle type, by the theorem on [[conjugacy classes of symmetric groups|0J438GAC8K]].
