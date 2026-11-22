---
tag: 4Y6AAEMN20
kind: example
name: The total number of chameleons does not rule out one color
aliases: [the-total-number-of-chameleons-does-not-rule-out-one-colour]
msc: ["00A35", "05A99"]
topics: [GB14W4SYPK]
audience: school
not_instance_of:
  - target: 8NQ190278Y
    note: the total is unchanged by every meeting, but it has the same value 45 at the start and at each one-color state, so it rules out nothing
uses: [8NQ190278Y, XBVPYJ1NEB]
sources:
  - url: https://en.wikipedia.org/wiki/Invariant_(mathematics)
    locator: lead section
---

## Example

We use the island of the [[game of chameleons|XBVPYJ1NEB]]: $13$ red, $15$ green and $17$ blue chameleons, and two chameleons of different colors that meet both take the third color.
We test two quantities, and we check why neither gives an [[invariant proof|8NQ190278Y]] that one color is impossible.

1. Let $T = r + g + b$ be the total number of chameleons.
   A red and green meeting changes $T$ by $-1 - 1 + 2 = 0$, and the other two meetings do the same.
2. So no move changes $T$, and at the start
   $$T = 13 + 15 + 17 = 45.$$
3. The states of one color are $(45, 0, 0)$, $(0, 45, 0)$ and $(0, 0, 45)$, and each of them has $T = 45$.
4. The values of $T$ at the start and at each target are equal.
   So $T$ rules out no target, and the argument gives no conclusion.
5. Let $R = r$ be the number of red chameleons.
   A red and green meeting changes $R$ from $13$ to $12$.
6. So some moves change $R$, and $R$ is not an invariant.
   Its values at the start and at the target prove nothing about reachability.

## Remarks

An invariant proof needs two conditions: no move changes the quantity, and the quantity has different values at the start and at the target.
The total $T$ meets the first condition and fails the second.
The count $R$ fails the first condition.
The residue of $r - g$ modulo $3$ meets both, and it gives the proof in the [[full example|XBVPYJ1NEB]].

The failure of one quantity is not evidence that the target can be reached.
For the counts $13, 15, 17$ the target is impossible, although $T$ says nothing about it.
So when a candidate fails, the right move is to look for a finer quantity, not to conclude.

## Explanations

### L1 human

The number of chameleons on the island never changes, because a meeting only changes colors.
So the total stays the same, which looks like a good start.
But an island of one color also has $45$ chameleons, the same total as at the start.
A quantity that is the same at the start and at the goal cannot show that the goal is impossible.
We need a quantity that differs at the start and at the goal.

### L2 human

We sort three candidate quantities by the two conditions.
The total $T = r + g + b$ is unchanged by each meeting, and it equals $45$ at the start and at each target, so it fails the second condition.
The count $r$ drops from $13$ to $12$ at a red and green meeting, so it fails the first condition.
The residue of $r - g$ modulo $3$ is unchanged by each meeting, and it equals $1$ at the start and $0$ at the all-blue state, so it meets both conditions.

This sorting is the normal way to search for an invariant: list candidates and test both conditions for each.
Watch out: many students check only the first condition, find that the total is fixed, and stop.
