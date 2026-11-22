---
tag: 8AR2JJMCPT
kind: example
name: A square root inequality by symmetry
msc: ["00A35", "26D07"]
topics: [958EF46EYJ]
audience: ug1
instance_of: [Y7NE0E6PCV]
uses: [Y7NE0E6PCV, 00S7C68D51]
sources:
  - url: https://en.wikipedia.org/wiki/Without_loss_of_generality
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Square_root
    locator: lead section
---

## Example

Statement: for all real numbers $x \ge 0$ and $y \ge 0$,
$$\left| \sqrt{x} - \sqrt{y} \right| \le \sqrt{|x - y|}.$$
We use [[without loss of generality|Y7NE0E6PCV]].

1. Exchanging $x$ and $y$ keeps the hypotheses $x \ge 0$ and $y \ge 0$.
   It also keeps both sides, since $\left| \sqrt{y} - \sqrt{x} \right| = \left| \sqrt{x} - \sqrt{y} \right|$ and $|y - x| = |x - y|$.
   So we may assume $x \ge y$.
2. The square root is increasing, so $\sqrt{x} \ge \sqrt{y}$.
   The left side is then $\sqrt{x} - \sqrt{y}$, and the right side is $\sqrt{x - y}$.
3. The claim becomes $\sqrt{x} \le \sqrt{y} + \sqrt{x - y}$.
4. Both sides of step 3 are at least $0$, and for numbers $u, v \ge 0$ we have $u \le v$ exactly when $u^2 \le v^2$.
   So it suffices to compare the squares.
5. The square of the right side is
   $$\left( \sqrt{y} + \sqrt{x - y} \right)^2 = y + (x - y) + 2\sqrt{y(x - y)} = x + 2\sqrt{y(x - y)}.$$
6. Since $2\sqrt{y(x - y)} \ge 0$, this is at least $x$, which is the square of the left side.
   So step 3 holds, and the statement is proved.

Check: $x = 9$ and $y = 4$ give $|3 - 2| = 1 \le \sqrt{5} \approx 2.24$.

## Remarks

The wlog step does two jobs at once.
It removes the [[absolute values|00S7C68D51]], whose signs would otherwise need two cases.
It also makes $x - y \ge 0$, so that $\sqrt{x - y}$ is defined in step 2.

Equality holds exactly when $y(x - y) = 0$, that is, when $y = 0$ or $x = y$ in the chosen case.
For $x = 9$ and $y = 0$ both sides are $3$.
Drop the hypotheses $x, y \ge 0$ and the statement has no meaning, since $\sqrt{x}$ is not a real number for $x < 0$.

## Explanations

### L1 human

Take $x = 16$ and $y = 9$.
The square roots are $4$ and $3$, and they differ by $1$.
The numbers themselves differ by $7$, and the square root of $7$ is about $2.6$.
So the difference of the roots, $1$, is at most the root of the difference.
The proof assumes that the first number is the larger one; if it is not, we exchange the names, and both sides stay the same.

### L2 human

Step 4 compares squares, and it is worth checking why that is allowed.
Let $u, v \ge 0$ with $u^2 \le v^2$, and factor:
$$v^2 - u^2 = (v - u)(v + u) \ge 0.$$
If $v + u > 0$, dividing by it gives $v - u \ge 0$, so $u \le v$.
If $v + u = 0$, then $u = v = 0$, so $u \le v$ again.
The typical use is to prove an inequality between square roots by reducing it to one between nonnegative numbers and squaring both sides.
Watch out: squaring keeps the order only for numbers that are at least $0$, since $-3 \le 2$ but $9 > 4$.
