---
tag: BJZ2BKEV4F
kind: example
name: Probability bounds for modus ponens
aliases: [probability-bounds-for-modus-ponens]
msc: ["03B48", "90C05"]
topics: [WZP584JQ06]
audience: grad
instance_of: [Z2WRGJDRQT]
uses: [0Y0MQYST0M, 0DAX8PMAJ4, VNMXB0J2KA]
sources:
  - url: https://plato.stanford.edu/entries/logic-probability/
    locator: 2.2 Adams' Probability Logic; 2.3 Further Generalizations
---

## Example

Take the premises $p$ and $p \to q$ of [[modus ponens|0Y0MQYST0M]], where $\to$ is the material conditional.
Let $P$ be a [[probability function|Z2WRGJDRQT]] with $P(p) = a$ and $P(p \to q) = b$.
We show that $a + b \ge 1$ and $a + b - 1 \le P(q) \le b$, and that both bounds are reached.

1. The valuations of $(p, q)$ are $(1,1)$, $(1,0)$, $(0,1)$ and $(0,0)$. Let $x_1, x_2, x_3, x_4$ be the probabilities of the formulas $p \land q$, $p \land \neg q$, $\neg p \land q$ and $\neg p \land \neg q$.
2. These four formulas exclude each other in pairs, and their disjunction is a tautology. So $x_i \ge 0$ and $x_1 + x_2 + x_3 + x_4 = 1$, by additivity.
3. Every formula in $p$ and $q$ is equivalent to the disjunction of the formulas of step 1 for the valuations that make it true. So its probability is the sum of the matching $x_i$.
4. $p$ is true at $(1,1)$ and $(1,0)$, so $a = x_1 + x_2$.
5. $p \to q$ is false only at $(1,0)$, so $b = x_1 + x_3 + x_4 = 1 - x_2$, and $x_2 = 1 - b$.
6. From steps 4 and 5, $x_1 = a + b - 1$. Since $x_1 \ge 0$, this gives $a + b \ge 1$.
7. From step 2, $x_3 + x_4 = 1 - x_1 - x_2 = 1 - a$, so $x_3$ can be any number in $[0, 1 - a]$.
8. $q$ is true at $(1,1)$ and $(0,1)$, so $P(q) = x_1 + x_3 = a + b - 1 + x_3$.
9. With $x_3 = 0$ we get $P(q) = a + b - 1$, and with $x_3 = 1 - a$ we get $P(q) = b$.
10. So the set of possible values of $P(q)$ is exactly $[a + b - 1, b]$.

With numbers: $a = 0.9$ and $b = 0.8$ give $x_1 = 0.7$, $x_2 = 0.2$ and $x_3 + x_4 = 0.1$, so $0.7 \le P(q) \le 0.8$.

## Remarks

The example is a small [[linear program|VNMXB0J2KA]]: the unknowns are the $x_i$, and the constraints and the goal are linear.
SEP reports that Hailperin and Nilsson computed such optimal bounds in general with linear programming.
The lower bound agrees with the theorem of Adams in SEP: $U(q) \le U(p) + U(p \to q)$, since $1 - (a + b - 1) = (1 - a) + (1 - b)$.
So in this example the uncertainty bound of Adams is reached.

Change the parameters to see the effect.
If $a = 1$, then the interval is the single point $b$, and $P(q) = b$.
If $b = 1$, then $P(q) \in [a, 1]$, so a certain conditional passes the probability of $p$ on to $q$ as a lower bound.
If $a + b < 1$, then no probability function has these values, by step 6.

## Explanations

### L1 human

Suppose "it rains" has chance $0.9$, and "if it rains, the street is wet" has chance $0.8$.
Then "the street is wet" has a chance of at least $0.7$ and at most $0.8$.
The lower number comes from the worst case, where the two doubts never overlap.
The upper number comes from the best case, where the street is wet whenever the rule holds and it does not rain.

### L2 human

1. Name the four cases of $p$ and $q$, and give them unknown weights.
2. Write each given probability as a sum of weights.
3. Solve for as many weights as possible.
4. Write the probability of the conclusion as a sum of weights, and find its smallest and largest value.

The typical use is in expert systems, where rules hold only with some probability.
A trap: $P(p \to q)$ is not the conditional probability $P(q \mid p)$.
With $a = 0.9$ and $b = 0.8$ we have $P(q \mid p) = x_1 / a = \tfrac{7}{9}$, which is not $0.8$.
