---
tag: CJJZX90P2M
kind: example
name: Measuring 6 liters with jugs of 4 and 9 liters, found by working backwards
msc: ["00A35", "00A08"]
topics: [X1NSTVGDNQ]
audience: school
instance_of: [3QTB9S1THS]
uses: [3QTB9S1THS]
sources:
  - url: https://en.wikipedia.org/wiki/Water_pouring_puzzle
    locator: lead section
  - book: isbn:9780691164076
---

## Example

We have a jug that holds exactly $4$ liters, a jug that holds exactly $9$ liters, and an unlimited supply of water.
The jugs have no marks.
A move fills a jug completely, empties a jug completely, or pours one jug into the other until the first is empty or the second is full.
The goal is exactly $6$ liters in the large jug.

We write a state as a pair $(s, \ell)$, where $s$ is the amount in the small jug and $\ell$ the amount in the large jug, and the start is $(0, 0)$.
We use [[working backwards|3QTB9S1THS]]: from the goal, we ask at each stage which state comes just before.

1. The goal is $\ell = 6$.
   A full large jug holds $9 = 6 + 3$ liters, so $6$ liters remain if exactly $3$ liters are poured out of a full large jug.
2. A pour into the small jug stops when the small jug is full.
   So exactly $3$ liters flow when the small jug already holds $4 - 3 = 1$ liter, and the state before is $(1, 9)$.
3. The state $(1, 9)$ comes from $(1, 0)$ by filling the large jug.
4. The state $(1, 0)$ comes from $(0, 1)$ by pouring the large jug into the small jug.
5. A full large jug holds $9 = 4 + 4 + 1$ liters.
   Two pours into the empty small jug, with the small jug emptied in between, leave $1$ liter, so $(0, 1)$ comes from $(0, 9)$.
6. The state $(0, 9)$ comes from the start by filling the large jug, so the backward chain has reached the start.

Now we reverse the chain and check each move forward.

1. Fill the large jug: $(0, 0) \to (0, 9)$.
2. Pour the large jug into the small jug, which moves $4$ liters: $(0, 9) \to (4, 5)$.
3. Empty the small jug: $(4, 5) \to (0, 5)$.
4. Pour the large jug into the small jug: $(0, 5) \to (4, 1)$.
5. Empty the small jug: $(4, 1) \to (0, 1)$.
6. Pour the large jug into the small jug, which moves $1$ liter: $(0, 1) \to (1, 0)$.
7. Fill the large jug: $(1, 0) \to (1, 9)$.
8. Pour the large jug into the small jug, which moves $3$ liters: $(1, 9) \to (4, 6)$.

The large jug holds $6$ liters after $8$ moves.

## Remarks

The forward search from $(0, 0)$ branches at every state, and most branches do not lead to $6$ liters.
The backward search starts from one fact about the goal, $9 - 3 = 6$, and each step reduces the goal to a smaller one, such as "have $1$ liter in the small jug".
A breadth-first search over the $26$ states that can be reached from $(0, 0)$ confirms that $8$ moves is the least possible number.

The answer depends on the sizes of the jugs.
With jugs of $4$ and $9$ liters, the large jug can hold every whole number of liters from $0$ to $9$, which agrees with $\gcd(4, 9) = 1$.
With jugs of $4$ and $6$ liters, the amount $5$ cannot be reached, and [[the backward search for 5 liters with jugs of 4 and 6 liters|33P1SJW98J]] shows why working backwards alone cannot settle that case.

## Explanations

### L1 human

We want $6$ liters, and the big jug holds $9$.
So we need to pour away exactly $3$ liters from a full big jug.
The small jug takes exactly $3$ liters if it already holds $1$ liter.
Now the problem is smaller: how do we get $1$ liter?
A full big jug minus two small jugs leaves $9 - 4 - 4 = 1$ liter.
We found the plan from the end, and then we carry it out from the start.

### L2 human

We use the same method on a smaller case: get $1$ liter with jugs of $3$ and $5$ liters.
We guess that the last move pours a full small jug into the large jug and stops when the large jug is full.
Such a pour leaves $1$ liter when $2$ liters flow, so the large jug held $5 - 2 = 3$ liters, and the state before is $(3, 3)$.
That state comes from $(0, 3)$ by filling the small jug, which comes from $(3, 0)$ by a pour, which comes from the start by filling the small jug.
The forward check is
$$(0, 0) \to (3, 0) \to (0, 3) \to (3, 3) \to (1, 5),$$
so the small jug holds $1$ liter after $4$ moves.

This is the typical use: write the target as a combination of the capacities, such as $6 = 2 \cdot 9 - 3 \cdot 4$ or $1 = 2 \cdot 3 - 5$, and read the moves from it.
Watch out: the guess for the last move could be wrong, and another guess can lead back to a state already met.
Working backwards is a search with a good starting point, not an algorithm that always succeeds.
