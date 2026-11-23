---
tag: DBTXYQQCD0
kind: example
name: Kelly's proof of the Sylvester-Gallai theorem
msc: ["00A35", "52C10"]
topics: [1BTHSHST4M]
audience: ug1
instance_of: [A4RJYP79A7]
uses: [A4RJYP79A7, T3GGJN70P2, MD3MRG90W4, 0XW7V9ZZ05, 0HGVCWQGY3]
sources:
  - url: https://en.wikipedia.org/wiki/Sylvester%E2%80%93Gallai_theorem
    locator: Proofs
  - url: https://en.wikipedia.org/wiki/Sylvester%E2%80%93Gallai_theorem
    locator: History
  - url: https://en.wikipedia.org/wiki/Proofs_from_THE_BOOK
    locator: Outline
---

## Example

The [[Sylvester-Gallai theorem|T3GGJN70P2]] says: let $S$ be a finite set of points in the [[Euclidean plane|0XW7V9ZZ05]], not all on one line; then some line contains exactly two points of $S$.
Such a line is called an ordinary line.
Kelly's proof is a standard example of a [[proof from the Book|A4RJYP79A7]], and we give it in full before we check it against the criteria.
Let $\mathcal{L}$ be the set of lines that contain at least two points of $S$.

1. If $S$ has $n$ points, then $\mathcal{L}$ has at most $\frac{n(n - 1)}{2}$ lines, so $\mathcal{L}$ is finite.
2. Consider the pairs $(p, \ell)$ with $p \in S$, $\ell \in \mathcal{L}$ and $p \notin \ell$.
   Such a pair exists: take two points $a, b$ of $S$, and some point of $S$ is off the line $ab$, because the points are not all on one line.
3. There are finitely many pairs, and in each the distance from $p$ to $\ell$ is positive.
   Choose a pair $(p, \ell)$ with the least distance, and call this distance $h > 0$.
4. Suppose $\ell$ contains at least three points of $S$; we derive a contradiction.
   Choose coordinates with $\ell$ as the $x$-axis and $p = (0, h)$, so that the foot of the perpendicular from $p$ is $(0, 0)$.
5. Of three points of $S$ on $\ell$, two have $x$-coordinates of the same sign, counting $0$ as both signs, by the [[pigeonhole principle|0HGVCWQGY3]].
   After a reflection in the $y$-axis if needed, these two points are $b = (\beta, 0)$ and $c = (\gamma, 0)$ with $0 \le \beta < \gamma$.
6. Let $m$ be the line through $p$ and $c$, so $m \in \mathcal{L}$.
   The line $m$ meets the $x$-axis only at $c$, and $b \ne c$, so $b \notin m$ and $(b, m)$ is one of the pairs.
7. The line $m$ passes through $(0, h)$ and $(\gamma, 0)$, so its equation is $h x + \gamma y - h \gamma = 0$, and the distance from $b$ to $m$ is
   $$\frac{|h \beta - h \gamma|}{\sqrt{h^2 + \gamma^2}} = \frac{h (\gamma - \beta)}{\sqrt{\gamma^2 + h^2}}.$$
8. Since $\beta \ge 0$, we have $\gamma - \beta \le \gamma$, and since $h > 0$, we have $\gamma < \sqrt{\gamma^2 + h^2}$.
   So the distance from $b$ to $m$ is less than $h$, which contradicts the choice in step 3.
9. So $\ell$ contains exactly two points of $S$, and $\ell$ is an ordinary line.

Now we check the proof against the criteria of a Book proof.
It is correct, since each step above gives its reason.
It is brief: the core is the choice in step 3 and the estimate in steps 7 and 8.
It turns on one idea, the [[extremal choice|MD3MRG90W4]] of the closest pair, and it needs only the distance from a point to a line.
And it explains the result: a line with three points always yields a closer pair, so the closest pair must use an ordinary line.

## Remarks

The example shows the usual shape of an extremal proof.
We choose an object that is least in some measure, and we show that a bad property would give a smaller one.
The finiteness of $S$ in step 3 ensures that a least distance exists.
For the integer lattice $\mathbb{Z}^2$, every line through two points holds infinitely many, and no pair has a least distance, so the argument cannot start.

James Joseph Sylvester posed the problem in 1893, and Tibor Gallai published a proof in 1944.
Aigner and Ziegler give Kelly's proof in their chapter on lines in the plane, and present it as the best proof of the theorem.
Donald Coxeter objected that Kelly's proof uses distance, which is not part of the statement, since the statement uses only points, lines and the order of points on a line.
Coxeter gave a proof from the axioms of order alone.
So whether a proof is from the Book can depend on what the reader takes as the natural setting of the theorem.

## Explanations

### L1 human

Put a few dots on paper, not all on one straight line.
The theorem says that some straight line passes through exactly two of the dots.
Here is the trick.
Among all pairs of a dot and a line through two other dots, pick the pair where the dot is closest to the line.
If that line held three dots, two of them would sit on the same side of the point straight below our dot.
A line from our dot to the farther of those two would pass closer to the nearer one, and that gives a closer pair, which is impossible.
So the line holds only two dots.

### L2 human

We run steps 5 to 8 once, with $S = \{(0, 0), (1, 0), (3, 0), (0, 2)\}$.
Take $p = (0, 2)$ and $\ell$ the $x$-axis, which holds three points of $S$, so $h = 2$.
The points $b = (1, 0)$ and $c = (3, 0)$ lie on the same side of the foot $(0, 0)$, with $\beta = 1$ and $\gamma = 3$.
The line $m$ through $(0, 2)$ and $(3, 0)$ has the equation $2x + 3y - 6 = 0$, and the distance from $b$ to $m$ is
$$\frac{|2 \cdot 1 - 6|}{\sqrt{4 + 9}} = \frac{4}{\sqrt{13}} \approx 1.11,$$
which is less than $2$.
The line $m$ holds no other point of $S$, since $(0, 0)$ gives $-6$ and $(1, 0)$ gives $-4$, so here $m$ is already an ordinary line.
The typical use of the example is to show the extremal principle at work in geometry.
Watch out at step 5: the two points must lie on the same side of the foot, or the new distance need not be smaller.
