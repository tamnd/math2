---
tag: J1HQ8MMQ8C
kind: example
name: A strictly decreasing real quantity does not force termination
msc: ["00A35", "26A18"]
topics: [GB14W4SYPK]
audience: school
not_instance_of:
  - target: TP3GC5J08D
    note: x decreases at each step of halving, but the positive real numbers are not well-ordered, so the decrease never forces a stop
uses: [TP3GC5J08D, 01BX15HSRR]
sources:
  - url: https://en.wikipedia.org/wiki/Well-order
    locator: lead section
---

## Example

Start with the number $x_0 = 1$.
A move replaces the current number $x$ by $x/2$, and a move is allowed whenever $x > 0$.
We check why the quantity $x$ does not give a [[monovariant|TP3GC5J08D]] proof that the process stops.

1. After $k$ moves the number is $x_k = 1/2^k$.
2. Each $x_k$ is positive, so a move is allowed from each state, and the process never stops.
3. Each move changes $x$ into $x/2 < x$. So $x$ strictly decreases at each move.
4. The values $x_k$ are bounded below by $0$. So $x$ decreases at each move and is bounded below, and still the process goes on for ever.
5. The condition that fails is the one on the values. The set $\set{1, 1/2, 1/4, \dots}$ has no least element, so it is not well-ordered, and the [[well-ordering principle|01BX15HSRR]] does not apply.
6. The decrease at the move $k + 1$ is $x_k/2 = 1/2^{k+1}$. It tends to $0$, so there is no fixed amount by which each move lowers $x$.

## Remarks

The monovariant method needs a decrease that cannot go on for ever.
Two ways give it: values in the natural numbers or in another well-ordered set, or a decrease of at least a fixed amount $\delta > 0$ together with a lower bound.
Halving fails both, as steps 5 and 6 show.

A small change of the rules makes the method work.
Allow a move only when $x \ge 1/1000$.
A move from $x_k = 1/2^k$ is then allowed only when $2^k \le 1000$, that is when $k \le 9$, since $2^9 = 512 < 1000 < 1024 = 2^{10}$.
So the process stops after exactly $10$ moves, at $x_{10} = 1/1024$.
Equivalently, the value $\floor{\log_2(1/x)}$ is a natural number that increases by $1$ at each move and is bounded above.

## Explanations

### L1 human

Halve a cake again and again.
The piece gets smaller at each step, and it never reaches $0$.
So a quantity that keeps going down does not prove that a process stops.
Whole numbers are different: a whole number that goes down and stays at least $0$ must stop.
The piece of cake is not a whole number, and this is why the argument fails.

### L2 human

We compare two quantities that both decrease at each move of a process.

1. The count of inversions in a list, as in the [[sort by swaps of neighbours|MGMET02ZZS]]: a natural number that drops by $1$ at each swap. It cannot drop more than its start value times, so the process stops.
2. The number $x$ under halving: a positive real number that drops at each move. Its values $1, 1/2, 1/4, \dots$ form an infinite decreasing sequence, so nothing stops the process.
3. The difference is the set of values: the natural numbers are well-ordered, and the positive real numbers are not.

The typical use of this example is a test for a proposed monovariant: ask whether its values can form an infinite decreasing sequence.
A trap is to check only that the quantity is bounded below; a bound below without a fixed step is not enough.
