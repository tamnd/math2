---
tag: 2XAK5BWA8G
kind: example
name: Jensen's inequality for midpoint convex functions by forward-backward induction
msc: ["00A35", "26A51"]
topics: [EEH2F76CYQ]
audience: ug2
instance_of: [QC9FKGZH1V]
uses: [1TQ1JQXEWP, 0RWMRTPC87, 0Q1D85B8G6, QC9FKGZH1V]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_function
    locator: Functions of one variable
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Forward-backward induction
---

## Example

Let $I$ be an [[interval|0Q1D85B8G6]] of real numbers, and let $f \colon I \to \mathbb{R}$ be [[midpoint convex|1TQ1JQXEWP]]: for all $x, y \in I$,
$$f\left(\frac{x + y}{2}\right) \le \frac{f(x) + f(y)}{2}.$$
We prove the finite form of [[Jensen's inequality|0RWMRTPC87]] with equal weights by [[forward-backward induction|QC9FKGZH1V]].
For each $n \ge 1$, let $P(n)$ be the statement: for all $x_1, \ldots, x_n \in I$,
$$f\left(\frac{x_1 + \cdots + x_n}{n}\right) \le \frac{f(x_1) + \cdots + f(x_n)}{n}.$$

1. The mean of points of $I$ lies in $I$.
   The mean lies between the smallest and the largest of the points, and an interval contains every number between two of its points.
   So the left side of $P(n)$ is defined.
2. $P(1)$ says $f(x_1) \le f(x_1)$, which holds, and $P(2)$ is the definition of midpoint convexity.
3. Forward step: assume $P(n)$, and let $x_1, \ldots, x_{2n} \in I$.
   Let $B$ be the mean of $x_1, \ldots, x_n$ and $C$ the mean of $x_{n+1}, \ldots, x_{2n}$, which lie in $I$ by step 1.
4. Let $S_1 = f(x_1) + \cdots + f(x_n)$ and $S_2 = f(x_{n+1}) + \cdots + f(x_{2n})$.
   By $P(n)$ for each half, $f(B) \le S_1/n$ and $f(C) \le S_2/n$.
5. The mean of all $2n$ points is $\frac{B + C}{2}$.
   Apply $P(2)$ to $B$ and $C$, and then step 4:
   $$f\left(\frac{B + C}{2}\right) \le \frac{f(B) + f(C)}{2} \le \frac{S_1/n + S_2/n}{2} = \frac{S_1 + S_2}{2n}.$$
   This is $P(2n)$.
6. By induction on $k$, steps 2 to 5 give $P(2^k)$ for every $k \ge 0$.
7. Backward step: let $n \ge 2$ and assume $P(n)$.
   Let $x_1, \ldots, x_{n-1} \in I$ have mean $m$, and let $S = f(x_1) + \cdots + f(x_{n-1})$.
   By step 1, $m \in I$, so we may put $x_n = m$.
8. The mean of $x_1, \ldots, x_n$ is $\frac{(n - 1)m + m}{n} = m$, so $P(n)$ gives $f(m) \le \frac{S + f(m)}{n}$.
9. Multiply by $n$ and subtract $f(m)$ to get $(n - 1) f(m) \le S$.
   Divide by $n - 1 > 0$ to get $f(m) \le \frac{S}{n - 1}$, which is $P(n - 1)$.
10. Steps 6 and 9 give $P(n)$ for every $n \ge 1$, by the validity of forward-backward induction.

Check with $f(x) = x^2$ on $\mathbb{R}$ and the points $1, 2, 6$: the result says $f(3) = 9 \le \frac{1 + 4 + 36}{3} = \frac{41}{3}$.
The backward step gets this from the case $n = 4$ for $1, 2, 6, 3$, where $9 \le \frac{50}{4}$, so $4 \cdot 9 \le 50$, and subtracting $9$ gives $3 \cdot 9 \le 41$.

## Remarks

Step 1 is what lets the backward step work, because the extra point $m$ must lie in the domain of $f$.
On a set that is not an interval, such as $[0, 1] \cup [2, 3]$, the mean of $0$ and $3$ is $1.5$, which lies outside the set.

Rational weights follow by repetition.
If $k_1, \ldots, k_r$ are positive integers with sum $N$, apply $P(N)$ to the list in which $x_i$ appears $k_i$ times:
$$f\left(\sum_{i = 1}^{r} \frac{k_i}{N} x_i\right) \le \sum_{i = 1}^{r} \frac{k_i}{N} f(x_i).$$
If $f$ is also continuous, a limit over rational weights gives $f(tx + (1 - t)y) \le t f(x) + (1 - t) f(y)$ for every real $t \in [0, 1]$.
So a continuous midpoint convex function is [[convex|07Q7CNM5WF]].

The function $f(x) = -\ln x$ is convex on the positive reals.
For it, the result says $\ln \frac{x_1 + \cdots + x_n}{n} \ge \frac{\ln x_1 + \cdots + \ln x_n}{n}$, and exponentiation gives the [[AM-GM inequality|HM1J3JN5YG]] for positive numbers.

## Explanations

### L1 human

A function is midpoint convex if its value at the midpoint of two points is at most the average of its values at the two points.
The graph of $x^2$ has this property, because it bends upward.
We want the same for any number of points: the value at the average point is at most the average of the values.
For $2$ points this is the definition.
Two groups of points combine into a larger group, which gives $4$, $8$ and $16$ points.
To go down by one point, we add the average point to the list, which does not change the average.

### L2 human

Follow the forward step for $f(x) = x^2$ and the four points $0, 2, 4, 10$.
The first half $0, 2$ has mean $B = 1$, and $f(1) = 1 \le \frac{0 + 4}{2} = 2$.
The second half $4, 10$ has mean $C = 7$, and $f(7) = 49 \le \frac{16 + 100}{2} = 58$.
The mean of all four points is $\frac{1 + 7}{2} = 4$, and $P(2)$ for $B$ and $C$ gives
$$f(4) = 16 \le \frac{f(1) + f(7)}{2} = \frac{1 + 49}{2} = 25 \le \frac{2 + 58}{2} = 30.$$
Check: $30 = \frac{0 + 4 + 16 + 100}{4}$ is the mean of the four values.
The result is the usual way to get an inequality between averages from a property of $f$ at two points only.
Watch out for the domain: on a set that is not an interval, the mean point can fall outside it.
