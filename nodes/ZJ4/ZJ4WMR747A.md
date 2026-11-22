---
tag: ZJ4WMR747A
kind: example
name: The Cantor set is a pathological set
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: ug2
instance_of: [WMBZPYPN2D]
uses: [0BXNDZFQME, 0W7FBYS1F1, VQQM4Y550T, 0XCH8QVDCQ, WMBZPYPN2D]
sources:
  - url: https://en.wikipedia.org/wiki/Cantor_set
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Pathological_(mathematics)
    locator: lead section
---

## Example

Let $C_0 = [0, 1]$, and let $C_{n+1}$ be the set that we get from $C_n$ when we remove the open middle third of each of its closed intervals.
So $C_1 = [0, \tfrac{1}{3}] \cup [\tfrac{2}{3}, 1]$, and $C_2$ has the four intervals $[0, \tfrac{1}{9}]$, $[\tfrac{2}{9}, \tfrac{1}{3}]$, $[\tfrac{2}{3}, \tfrac{7}{9}]$ and $[\tfrac{8}{9}, 1]$.
The [[Cantor set|0BXNDZFQME]] is $C = \bigcap_{n \ge 0} C_n$.
We check two properties that together defeat the intuition that a set with many points must take up some length, so $C$ is [[pathological|WMBZPYPN2D]].

1. The set $C_n$ is a union of $2^n$ closed intervals, each of length $3^{-n}$, so its total length is
   $$2^n \cdot 3^{-n} = \left(\tfrac{2}{3}\right)^n.$$
2. Since $C \subseteq C_n$ for every $n$, and $(2/3)^n \to 0$, the set $C$ has length $0$.
   In the language of measure, $C$ is a [[null set|VQQM4Y550T]].
3. A number $x \in [0, 1]$ lies in $C$ exactly when it has a base $3$ expansion $x = \sum_{n \ge 1} d_n 3^{-n}$ with every digit $d_n \in \{0, 2\}$.
   For example, $\tfrac{1}{4} = 0.0202\ldots_3$, so $\tfrac{1}{4} \in C$.
4. The map
   $$\sum_{n \ge 1} d_n 3^{-n} \longmapsto \sum_{n \ge 1} \frac{d_n}{2} \, 2^{-n}$$
   sends $C$ onto $[0, 1]$, because every number in $[0, 1]$ has a base $2$ expansion.
   So $C$ has at least as many points as $[0, 1]$.
5. Hence $C$ is [[uncountable|0W7FBYS1F1]], since $[0, 1]$ is uncountable by [[Cantor's diagonal argument|0XCH8QVDCQ]].

The set $C$ is as large as $[0, 1]$ in the number of its points and as small as a single point in length, so it is a standard pathological set.

## Remarks

Each interval of $C_n$ has length $3^{-n}$, and $C \subseteq C_n$, so $C$ contains no interval of positive length.
Most of its points are not end points of removed intervals, as $\tfrac{1}{4}$ shows: the end points have finite base $3$ expansions, and $\tfrac{1}{4}$ does not.

The set is pathological only as a subset of the real line.
In topology it is a standard model: every nonempty compact metric space is a continuous image of the Cantor set.
If you remove the middle fifth instead of the middle third, you get another Cantor set with length $0$; if you remove shorter and shorter middle parts, you can keep positive total length and still contain no interval.

## Explanations

### L1 human

Start with a line segment and remove its middle third.
Then remove the middle third of each of the two pieces that remain, and keep going for ever.
The total length that remains goes to $0$.
But infinitely many points remain, and there are as many of them as points in the whole segment.
This surprises most people, so mathematicians call the Cantor set pathological.

### L2 human

To check that a point is in $C$, write it in base $3$.
For $\tfrac{1}{4}$, the expansion $0.020202\ldots_3$ is a geometric series:
$$\sum_{k \ge 1} 2 \cdot 9^{-k} = 2 \cdot \frac{1/9}{1 - 1/9} = \frac{2}{8} = \frac{1}{4}.$$
Every digit is $0$ or $2$, so $\tfrac{1}{4} \in C$.
The point $\tfrac{1}{2} = 0.111\ldots_3$ lies in the first removed interval $(\tfrac{1}{3}, \tfrac{2}{3})$, so $\tfrac{1}{2} \notin C$.
Watch out for numbers with two expansions: $\tfrac{1}{3} = 0.1_3 = 0.0222\ldots_3$, and $\tfrac{1}{3} \in C$ because one of its expansions uses only $0$ and $2$.
