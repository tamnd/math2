---
tag: XBVPYJ1NEB
kind: example
name: Chameleons of three colors cannot all become one color
aliases: [chameleons-of-three-colours-cannot-all-become-one-colour]
msc: ["00A35", "05A99"]
topics: [GB14W4SYPK]
audience: school
instance_of: [8NQ190278Y]
uses: [8NQ190278Y, 0WAY5WX8NY]
sources:
  - url: https://en.wikipedia.org/wiki/Invariant_(mathematics)
    locator: lead section
---

## Example

An island has $13$ red, $15$ green and $17$ blue chameleons.
When two chameleons of different colors meet, both change to the third color.
No other change of color happens.
We show with an [[invariant|8NQ190278Y]] that the chameleons can never all have the same color.

1. A state is a triple $(r, g, b)$ of the numbers of red, green and blue chameleons, and the start is $(13, 15, 17)$.
2. The three kinds of meeting change the state as follows:
   $$\begin{aligned} \text{red and green:}\ & (r, g, b) \mapsto (r - 1, g - 1, b + 2), \\ \text{red and blue:}\ & (r, g, b) \mapsto (r - 1, g + 2, b - 1), \\ \text{green and blue:}\ & (r, g, b) \mapsto (r + 2, g - 1, b - 1). \end{aligned}$$
3. The three meetings change $r - g$ by $0$, by $-1 - 2 = -3$ and by $2 + 1 = 3$.
   Each change is a multiple of $3$, so $r - g$ [[modulo|0WAY5WX8NY]] $3$ never changes.
4. The same computation shows that $g - b$ and $r - b$ modulo $3$ never change.
   So the three residues are invariants.
5. At the start, $r - g = -2 \equiv 1$, $g - b = -2 \equiv 1$ and $r - b = -4 \equiv 2 \pmod 3$.
   None of the three differences is a multiple of $3$.
6. If all chameleons are red, then $g = b = 0$, so $g - b = 0$.
   If all are green, then $r - b = 0$, and if all are blue, then $r - g = 0$.
7. In each case of step 6, one difference is a multiple of $3$, which contradicts steps 4 and 5.
   So the chameleons never all have the same color.

## Remarks

The example shows an invariant with values modulo $3$.
That modulus is the natural choice here, because a meeting changes the three counts by $-1$, $-1$ and $+2$, and these three numbers are equal modulo $3$.
Each single count changes at every meeting, and only the differences modulo $3$ stay fixed.

A change of one count changes the answer.
With $13$ red, $16$ green and $17$ blue chameleons, the difference $r - g = -3$ is a multiple of $3$, so the invariant no longer rules out an all-blue island.
Then a construction finishes the job:
$$(13, 16, 17) \xrightarrow{13 \text{ red-green}} (0, 3, 43) \xrightarrow{1 \text{ green-blue}} (2, 2, 42) \xrightarrow{2 \text{ red-green}} (0, 0, 46).$$
Check: each state has total $46$, and the last one is all blue.
The invariant only said that the target was not ruled out; the explicit meetings prove that it is reachable.

## Explanations

### L1 human

Chameleons of three colors live on an island, and two chameleons of different colors that meet both take the third color.
Can they one day all have the same color?
Look at the number of red chameleons minus the number of green ones.
Each meeting changes this difference by $0$, $3$ or $-3$, so its remainder after division by $3$ never changes.
With $13$ red, $15$ green and $17$ blue, no difference is a multiple of $3$, but one color everywhere makes one difference equal to $0$.
So the island never becomes one color.

### L2 human

We test the invariant on a small island with $2$ red, $1$ green and $0$ blue chameleons, where we can also follow every move by hand.
The differences at the start are $r - g = 1$, $g - b = 1$ and $r - b = 2$, and none is a multiple of $3$, so the invariant says that one color is impossible.

Now we check by hand.
From $(2, 1, 0)$ the only possible meeting is red and green, and it gives $(1, 0, 2)$.
From $(1, 0, 2)$ the only possible meeting is red and blue, and it gives $(0, 2, 1)$.
From $(0, 2, 1)$ the only possible meeting is green and blue, and it gives $(2, 1, 0)$, the start again.
So the reachable states are exactly $(2, 1, 0)$, $(1, 0, 2)$ and $(0, 2, 1)$, and none of them has one color.

For large counts the search by hand is long, and the invariant replaces it by one computation.
Watch out: $r - g$ itself is not an invariant, because it changes by $3$ at some meetings; only its residue modulo $3$ stays fixed.
