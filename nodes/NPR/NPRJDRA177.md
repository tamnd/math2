---
tag: NPRJDRA177
kind: example
name: Chip-firing on a path with two sinks always stops
msc: ["00A35", "05C57"]
topics: [GB14W4SYPK]
audience: school
instance_of: [TP3GC5J08D]
uses: [TP3GC5J08D, N33S3095R5]
sources:
  - url: https://en.wikipedia.org/wiki/Chip-firing_game
    locator: lead section
---

## Example

Take the sites $0, 1, \dots, m + 1$ on a line, with $m \ge 1$.
The sites $0$ and $m + 1$ are sinks, and the sites $1$ to $m$ are inner sites.
Each site holds a number of chips.
A firing chooses an inner site $x$ with at least $2$ chips, takes $2$ chips from it, and puts $1$ chip on the site $x - 1$ and $1$ chip on the site $x + 1$.
Sinks never fire, so chips that reach a sink stay there.
We show with a [[monovariant|TP3GC5J08D]] that every sequence of firings stops.

1. Give the site $x$ the weight $w(x) = x(m + 1 - x)$.
   Then $w(0) = w(m + 1) = 0$, and $w(x) > 0$ for each inner site.
2. Let $c(x)$ be the number of chips on the site $x$, and let $W = \sum_x c(x) w(x)$.
   Then $W$ is an integer, and $W \ge 0$.
3. A firing at $x$ removes two chips of weight $w(x)$ and adds one chip of weight $w(x - 1)$ and one of weight $w(x + 1)$.
   So it changes $W$ by $w(x - 1) + w(x + 1) - 2w(x)$.
4. We expand both parts:
   $$w(x - 1) + w(x + 1) = (x - 1)(m + 2 - x) + (x + 1)(m - x) = 2xm + 2x - 2x^2 - 2,$$
   $$2w(x) = 2x(m + 1 - x) = 2xm + 2x - 2x^2.$$
5. So each firing changes $W$ by exactly $-2$, whatever inner site fires.
6. After $k$ firings, $W = W_0 - 2k$, where $W_0$ is the value at the start.
   Since $W \ge 0$, we get $k \le W_0/2$, so every sequence of firings stops.

Check with $m = 3$ and $4$ chips on site $2$.
The weights of the sites $0$ to $4$ are $0, 3, 4, 3, 0$, so $W_0 = 4 \cdot 4 = 16$, and at most $8$ firings can happen.
Fire the sites $2, 2, 1, 3, 2$ in this order.
The chips on the sites $0$ to $4$ go through $(0, 1, 2, 1, 0)$, $(0, 2, 0, 2, 0)$, $(1, 0, 1, 2, 0)$, $(1, 0, 2, 0, 1)$ and $(1, 1, 0, 1, 1)$, and $W$ goes through $14, 12, 10, 8, 6$.
In the state $(1, 1, 0, 1, 1)$ no inner site has $2$ chips, so the process stops after $5$ firings.

## Remarks

The weight $w$ is built for the problem: it is $0$ at the sinks, where chips leave the game, and largest in the middle, and its second difference is the constant $-2$.
So each firing lowers $W$ by the same amount.
The simpler count of chips on inner sites is not a monovariant here, since for $m = 3$ a firing at site $2$ keeps every chip on an inner site.

The firing order $2, 2, 3, 1, 2$ also stops after $5$ firings, at the same state $(1, 1, 0, 1, 1)$.
That every order gives the same final state and the same number of firings is a general fact about chip-firing, but the monovariant does not prove it.
The monovariant proves only that each order stops, and the bound $W_0/2 = 8$ is not reached here.

Without sinks the method fails.
On a cycle of $3$ sites with $2, 1, 1$ chips, the firings $(2, 1, 1) \to (0, 2, 2) \to (1, 0, 3) \to (2, 1, 1)$ return to the start, so the game can go on for ever.
The [[abelian sandpile model|N33S3095R5]] has a sink for this reason.

## Explanations

### L1 human

Chips sit on a row of boxes, and the two end boxes are bins.
A box with at least $2$ chips may pass $1$ chip to each neighbor.
Give each box a score: boxes near the middle score high, and the bins score $0$.
Add up the scores of all chips.
Each pass lowers this total by exactly $2$, and the total can never go below $0$.
So the passing must stop.

### L2 human

We check step 5 on a firing at site $1$, next to the sink, for $m = 3$.
The weights are $w(0) = 0$, $w(1) = 3$ and $w(2) = 4$.
The firing removes $2$ chips of weight $3$ and adds one chip of weight $0$ on the sink and one chip of weight $4$ on site $2$, so the change is
$$-2 \cdot 3 + 0 + 4 = -2.$$
In the run above, the third firing is at site $1$, and $W$ goes from $12$ to $10$, as it should.

The method fits every process that loses material at some places: put weight $0$ there and large weights far away.
Watch out: the total number of chips is not a good weight, because no firing changes it, so it proves nothing about termination.
