---
tag: XBVPYJ1NEB
kind: example
name: Chameleons of three colours cannot all become one colour
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
When two chameleons of different colours meet, both change to the third colour.
No other change of colour happens.
We show with an [[invariant|8NQ190278Y]] that the chameleons can never all have the same colour.

1. A state is a triple $(r, g, b)$ of the numbers of red, green and blue chameleons. The start is $(13, 15, 17)$.
2. A meeting of a red and a green chameleon changes $(r, g, b)$ into $(r - 1, g - 1, b + 2)$. A red and blue meeting gives $(r - 1, g + 2, b - 1)$. A green and blue meeting gives $(r + 2, g - 1, b - 1)$.
3. We compute the change of $r - g$ in each case. The three meetings change $r - g$ by $0$, $-3$ and $+3$.
4. So $r - g$ [[modulo|0WAY5WX8NY]] $3$ does not change. By the same computation, $g - b$ and $r - b$ modulo $3$ do not change. These three residues are invariants.
5. At the start, $r - g = -2 \equiv 1$, $g - b = -2 \equiv 1$ and $r - b = -4 \equiv 2 \pmod 3$. None of the three differences is divisible by $3$.
6. If all chameleons are red, then $g = b = 0$, so $g - b \equiv 0 \pmod 3$. If all are green, then $r - b \equiv 0$. If all are blue, then $r - g \equiv 0$.
7. In each case of step 6, one of the three differences is divisible by $3$. This contradicts steps 4 and 5. So the chameleons never all have the same colour.

## Remarks

The example shows an invariant with values modulo $3$, a typical choice when a move changes the counts by $1$ and $2$.
Each single count changes at each meeting, and only the differences modulo $3$ stay fixed.

A change of one count changes the answer.
With $13$ red, $16$ green and $17$ blue chameleons, the difference $r - g = -3$ is divisible by $3$.
Then $13$ red and green meetings give $(0, 3, 43)$, one green and blue meeting gives $(2, 2, 42)$, and two red and green meetings give $(0, 0, 46)$.
So all chameleons can become blue.
The invariant did not rule this out, and the explicit sequence of meetings proves that it is possible.

## Explanations

### L1 human

Chameleons of three colours live on an island, and two chameleons of different colours that meet both take the third colour.
We want to know whether one day they can all have the same colour.
Look at the difference between the number of red and the number of green chameleons.
Each meeting changes this difference by $0$, $3$ or $-3$, so its remainder after division by $3$ never changes.
With $13$ red, $15$ green and $17$ blue, no difference is a multiple of $3$, but a single colour needs one difference equal to $0$.
So the island never becomes one colour.

### L2 human

We test a smaller island with $2$ red, $1$ green and $0$ blue chameleons.

1. The differences at the start are $r - g = 1$, $g - b = 1$ and $r - b = 2$. None is divisible by $3$.
2. By the invariant, the chameleons never all have one colour.
3. We check by hand. The only possible meeting is red and green, which gives $(1, 0, 2)$.
4. From $(1, 0, 2)$, the only possible meeting is red and blue, which gives $(0, 2, 1)$.
5. From $(0, 2, 1)$, the only possible meeting is green and blue, which gives $(2, 1, 0)$, the start.
6. So the reachable states are exactly $(2, 1, 0)$, $(1, 0, 2)$ and $(0, 2, 1)$, and none of them has one colour.

The typical use is to replace the search of step 3 to 6, which is short here but long for large counts, by the computation of step 1.
A trap is to use $r - g$ itself instead of its residue: it changes by $3$ at some meetings, so it is not an invariant.
