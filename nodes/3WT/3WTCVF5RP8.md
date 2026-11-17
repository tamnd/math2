---
tag: 3WTCVF5RP8
kind: example
name: Cosets of a line through the origin in the plane
msc: ["20A05"]
topics: [1VHQWXC64D]
audience: ug1
instance_of: [564VVAQTNR, 03DEH43F4H, 0NE1DK7H4T]
uses: [G5S1M9, 0X1JXT47GA, 082GHNPJ53, 564VVAQTNR, 03DEH43F4H, 0NE1DK7H4T, 0DTXBQPA2S, 08QMKTWF9T]
sources:
  - url: https://en.wikipedia.org/wiki/Coset
    locator: Examples
  - book: isbn:9781305657960
    locator: Chapter 7
---

## Example

Let $G = (\mathbb{R}^2, +)$ be the plane with vector addition.
This is a [[group|G5S1M9]] with identity $(0, 0)$, and it is [[abelian|082GHNPJ53]].
Let $L = \{(t, 2t) : t \in \mathbb{R}\}$ be the line $y = 2x$ through the origin.

1. The set $L$ is a [[subgroup|0X1JXT47GA]]. It contains $(0, 0)$ for $t = 0$. The sum $(s, 2s) + (t, 2t) = (s + t, 2(s + t))$ is in $L$. The negative of $(t, 2t)$ is $(-t, 2(-t))$, which is in $L$.
2. Let $v = (a, b) \in \mathbb{R}^2$. The [[left coset|03DEH43F4H]] of $v$ is $v + L = \{(a + t, b + 2t) : t \in \mathbb{R}\}$.
3. A point $(x, y)$ is in $v + L$ if and only if $y - 2x = b - 2a$. For the forward direction, $x = a + t$ and $y = b + 2t$ give $y - 2x = b - 2a$. For the reverse direction, put $t = x - a$. Then $y = 2x + (b - 2a) = b + 2t$.
4. Thus $v + L$ is the line $y = 2x + c$ with $c = b - 2a$. This line is parallel to $L$ and passes through $v$.
5. The group is abelian, so $v + L = L + v$. Each left coset is also a [[right coset|0NE1DK7H4T]].
6. Each point $(x, y)$ lies on exactly one line $y = 2x + c$, namely the one with $c = y - 2x$. So the cosets form a [[partition|08QMKTWF9T]] of the plane.
7. The cosets are in bijection with $\mathbb{R}$ by $v + L \mapsto c$. Thus the [[index|0DTXBQPA2S]] $[G : L]$ is the cardinality of $\mathbb{R}$, which is infinite.

## Remarks

The example shows the picture behind the word coset.
The cosets of $L$ are copies of $L$ moved by a vector, and they fill the plane without overlap.
The map $(x, y) \mapsto y - 2x$ is a homomorphism from $\mathbb{R}^2$ to $(\mathbb{R}, +)$ with kernel $L$.
Each coset is the set of points where this map has a fixed value.
If we replace $L$ by a line that does not pass through the origin, then it is not a subgroup, because it does not contain $(0, 0)$.
If we replace $L$ by the subgroup $\{(0, 0)\}$, then each coset is a single point.

## Explanations

### L1 human

Draw the line $y = 2x$ on squared paper.
Slide the whole line up by $1$ unit.
You get the line $y = 2x + 1$, which is parallel to the first line.
Each parallel line that you get by sliding is a coset.
Each point of the paper lies on exactly one of these lines.

### L2 human

We find the coset of $L$ that contains the point $v = (3, 1)$.

1. We compute $c = 1 - 2 \cdot 3 = -5$.
2. By step 3 of the example, the coset $v + L$ is the line $y = 2x - 5$.
3. We check one more point. For $t = 1$, the point $(3 + 1, 1 + 2) = (4, 3)$ is in $v + L$, and $3 = 2 \cdot 4 - 5$.
4. The point $(0, -5)$ is also on this line. So $(3, 1) + L = (0, -5) + L$, and $(3, 1) - (0, -5) = (3, 6)$ is in $L$.

The typical use is to see a quotient group as a picture.
The set of these lines is the group $\mathbb{R}^2 / L$, and the map $v + L \mapsto c$ is an isomorphism onto $(\mathbb{R}, +)$.
A trap is to think that the other lines are subgroups too.
The line $y = 2x - 5$ does not contain $(0, 0)$, so it is a coset but not a subgroup.
