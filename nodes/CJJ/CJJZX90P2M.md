---
tag: CJJZX90P2M
kind: example
name: Measuring 6 litres with jugs of 4 and 9 litres, found by working backwards
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

Problem: we have a jug that holds exactly $4$ litres, a jug that holds exactly $9$ litres, and an unlimited supply of water.
The jugs have no marks.
The allowed moves are: fill a jug completely, empty a jug completely, or pour from one jug into the other until the first jug is empty or the second jug is full.
The goal is to have exactly $6$ litres in the large jug.

We write a state as a pair $(s, \ell)$, where $s$ is the amount in the small jug and $\ell$ is the amount in the large jug.
The start is $(0, 0)$.
We use [[working backwards|3QTB9S1THS]]: we start from the goal and ask, at each stage, which state comes just before.

1. Goal: $\ell = 6$. A full large jug holds $9 = 6 + 3$ litres. So $6$ litres remain if we pour exactly $3$ litres out of a full large jug.
2. A pour stops when the small jug is full. So $3$ litres flow from the large jug exactly when the small jug already holds $4 - 3 = 1$ litre. The state before is $(1, 9)$.
3. The state $(1, 9)$ comes from $(1, 0)$ by filling the large jug. New goal: $1$ litre in the small jug and an empty large jug.
4. The state $(1, 0)$ comes from $(0, 1)$ by pouring the large jug into the small jug. New goal: $1$ litre in the large jug.
5. A full large jug holds $9 = 4 + 4 + 1$ litres. Two pours into the empty small jug, with the small jug emptied in between, leave $1$ litre. So $(0, 1)$ comes from $(0, 9)$ by these moves.
6. The state $(0, 9)$ comes from the start $(0, 0)$ by filling the large jug. The backward chain has reached the start.

We now reverse the chain and check each move forward.

1. Fill the large jug: $(0, 0) \to (0, 9)$.
2. Pour the large jug into the small jug: $4$ litres move, $(0, 9) \to (4, 5)$.
3. Empty the small jug: $(4, 5) \to (0, 5)$.
4. Pour the large jug into the small jug: $(0, 5) \to (4, 1)$.
5. Empty the small jug: $(4, 1) \to (0, 1)$.
6. Pour the large jug into the small jug: $1$ litre moves, $(0, 1) \to (1, 0)$.
7. Fill the large jug: $(1, 0) \to (1, 9)$.
8. Pour the large jug into the small jug: $3$ litres fill the small jug, $(1, 9) \to (4, 6)$.

The large jug holds $6$ litres after $8$ moves.

## Remarks

The forward search from $(0, 0)$ has many branches, and most of them do not lead to $6$ litres.
The backward search starts from one fact about the goal, $9 - 3 = 6$, and each step reduces the goal to a smaller one: "have $1$ litre in the small jug".
A breadth-first search over the $26$ states that can be reached from $(0, 0)$ confirms that $8$ moves is the least possible number.

The method depends on the sizes of the jugs.
With jugs of $4$ and $9$ litres, the same search shows that the large jug can hold each whole number of litres from $0$ to $9$; this agrees with $\gcd(4, 9) = 1$.
With jugs of $4$ and $6$ litres, the amount $5$ cannot be reached, and [[the backward search for 5 litres with jugs of 4 and 6 litres|33P1SJW98J]] shows why working backwards alone cannot settle that case.

## Explanations

### L1 human

We want $6$ litres, and the big jug holds $9$.
So we need to pour away exactly $3$ litres from a full big jug.
The small jug takes exactly $3$ litres if it already holds $1$ litre.
Now the problem is smaller: how do we get $1$ litre?
A full big jug minus two small jugs leaves $9 - 4 - 4 = 1$ litre.
We found the plan from the end, and then we carry it out from the start.

### L2 human

We solve a smaller case by the same method: get $1$ litre with jugs of $3$ and $5$ litres.

1. Goal: $1$ litre in the small jug. We guess that the last move is a pour from the small jug into the large jug that stops when the large jug is full.
2. Such a pour leaves $1$ litre when $2$ litres flow from a full small jug. So the large jug held $5 - 2 = 3$ litres before. The state before is $(3, 3)$.
3. The state $(3, 3)$ comes from $(0, 3)$ by filling the small jug.
4. The state $(0, 3)$ comes from $(3, 0)$ by pouring the small jug into the large jug.
5. The state $(3, 0)$ comes from the start $(0, 0)$ by filling the small jug.
6. Forward check: $(0, 0) \to (3, 0) \to (0, 3) \to (3, 3) \to (1, 5)$. The small jug holds $1$ litre after $4$ moves.

The typical use: write the target as a combination of the capacities, such as $6 = 2 \cdot 9 - 3 \cdot 4$ or $1 = 2 \cdot 3 - 5$, and read the moves from it.

A trap: the guess in step 1 could be wrong, and another guess can lead back to a state already met.
Working backwards is a search with a good starting point, not an algorithm that always succeeds.
