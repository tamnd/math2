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

1. Give the site $x$ the weight $w(x) = x(m + 1 - x)$. Then $w(0) = w(m + 1) = 0$, and $w(x) > 0$ for each inner site.
2. Let $c(x)$ be the number of chips on the site $x$, and let $W = \sum_x c(x) w(x)$. Then $W$ is an integer and $W \ge 0$.
3. A firing at $x$ changes $W$ by $w(x - 1) + w(x + 1) - 2w(x)$.
4. We expand: $w(x - 1) + w(x + 1) = (x - 1)(m + 2 - x) + (x + 1)(m - x) = 2xm + 2x - 2x^2 - 2$, and $2w(x) = 2xm + 2x - 2x^2$.
5. So each firing changes $W$ by exactly $-2$, whatever inner site fires.
6. After $k$ firings, $W = W_0 - 2k$, where $W_0$ is the value at the start. Since $W \ge 0$, we get $k \le W_0/2$. So every sequence of firings stops.
7. For $m = 3$ with $4$ chips on site $2$, the weights of the sites $0$ to $4$ are $0, 3, 4, 3, 0$, and $W_0 = 4 \cdot 4 = 16$. So at most $8$ firings can happen.
8. We fire the sites $2, 2, 1, 3, 2$ in this order. The chips on the sites $0$ to $4$ go through $(0, 1, 2, 1, 0)$, $(0, 2, 0, 2, 0)$, $(1, 0, 1, 2, 0)$, $(1, 0, 2, 0, 1)$ and $(1, 1, 0, 1, 1)$, and $W$ goes through $14, 12, 10, 8, 6$.
9. In the state $(1, 1, 0, 1, 1)$ no inner site has $2$ chips, so the process stops after $5$ firings.

## Remarks

The example shows a monovariant built for the problem: the weight $w$ is chosen so that each firing lowers $W$ by the same amount.
The simpler count of chips on inner sites is not a monovariant here, since a firing at the site $2$ keeps all chips on inner sites.

The firing order $2, 2, 3, 1, 2$ also stops after $5$ firings at the state $(1, 1, 0, 1, 1)$.
That both orders give the same final state and the same number of firings is a general fact about chip-firing, but the monovariant does not prove it.
The monovariant proves only that each order stops.

Without sinks, the method fails.
On a cycle of $3$ sites with $2, 1, 1$ chips, the firings go on for ever, and the [[abelian sandpile model|N33S3095R5]] uses sinks for this reason.

## Explanations

### L1 human

Chips sit on a row of boxes, and the two end boxes are bins.
A box with at least $2$ chips may pass $1$ chip to each neighbour.
Give each box a score: boxes near the middle score high, and the bins score $0$.
Add up the scores of all chips.
Each pass lowers this total by exactly $2$, and the total can never go below $0$.
So the passing must stop.

### L2 human

We check the claim of step 5 on a firing at the site $1$, next to the sink, for $m = 3$.

1. The weights are $w(0) = 0$, $w(1) = 3$ and $w(2) = 4$.
2. A firing at the site $1$ removes $2$ chips of weight $3$, so $W$ drops by $6$.
3. It puts $1$ chip on the sink $0$, of weight $0$, and $1$ chip on the site $2$, of weight $4$. So $W$ rises by $4$.
4. The total change is $-6 + 4 = -2$, as in step 5.
5. In the run of step 8, the third firing is at the site $1$, and $W$ goes from $12$ to $10$.

The typical use is a weight that is zero at the places where the process loses material and largest far from them.
A trap is a weight that is constant, such as the number of chips: a firing keeps the total number of chips, so it changes nothing and proves nothing.
