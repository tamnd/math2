---
tag: SCV1PRX55T
kind: example
name: Solving x^4 - 13x^2 + 36 = 0 through the auxiliary equation y^2 - 13y + 36 = 0
msc: ["00A35", "12D10"]
topics: [X1NSTVGDNQ]
audience: school
instance_of: [DYSJB93V11]
uses: [DYSJB93V11, 0KYZXYDGQZ]
sources:
  - url: https://en.wikipedia.org/wiki/Quartic_function
    locator: lead section
  - book: isbn:9780691164076
---

## Example

We find all real numbers $x$ with
$$x^4 - 13x^2 + 36 = 0.$$
The equation has degree $4$, and the school methods do not cover it directly, so we look for an [[auxiliary problem|DYSJB93V11]].

1. The unknown appears only through $x^2$, since $x^4 = (x^2)^2$.
2. Put $y = x^2$, and the equation becomes the auxiliary equation $y^2 - 13y + 36 = 0$.
3. The [[quadratic formula|0KYZXYDGQZ]] gives
   $$y = \frac{13 \pm \sqrt{169 - 144}}{2} = \frac{13 \pm 5}{2},$$
   so $y = 9$ or $y = 4$.
4. Check by multiplying out: $(y - 4)(y - 9) = y^2 - 13y + 36$.
5. Return to $x$: we need $x^2 = 4$ or $x^2 = 9$, so $x \in \{-3, -2, 2, 3\}$.
6. Check $x = 3$: $81 - 13 \cdot 9 + 36 = 81 - 117 + 36 = 0$.
   The value $x = 2$ gives $16 - 52 + 36 = 0$, and $-2$ and $-3$ give the same results, since $x^4$ and $x^2$ do not change when $x$ changes sign.

## Remarks

In Pólya's term the reduction is bilateral: the quartic and the auxiliary equation, together with the return step, are equivalent.
A real $x$ solves the quartic exactly when $y = x^2$ is a root of the quadratic, and each root $y \ge 0$ gives back the two solutions $x = \pm \sqrt{y}$.
So no solution is lost and none is added.

The condition $y \ge 0$ matters when the numbers change.
For $x^4 + 3x^2 - 4 = 0$ the auxiliary equation $y^2 + 3y - 4 = 0$ has the roots $1$ and $-4$.
Only $y = 1$ comes from a real $x$, so the real solutions are $x = \pm 1$.

The same substitution $y = x^k$ solves every equation $a x^{2k} + b x^k + c = 0$.

## Explanations

### L1 human

The equation looks hard because of the fourth power.
But $x^4$ is the square of $x^2$.
If we give $x^2$ a new name, $y$, the equation becomes an ordinary quadratic equation in $y$, and $y$ is $4$ or $9$.
Then $x$ is a number whose square is $4$ or $9$, so $x$ is $2$, $-2$, $3$ or $-3$.

### L2 human

We solve $9^x - 4 \cdot 3^x + 3 = 0$ with the same idea.
Since $9^x = (3^x)^2$, the unknown appears only through $3^x$, so we put $y = 3^x$.
The auxiliary equation and its factors are
$$y^2 - 4y + 3 = (y - 1)(y - 3) = 0,$$
so $y = 1$ or $y = 3$.
Return to $x$: $3^x = 1$ gives $x = 0$, and $3^x = 3$ gives $x = 1$.
Check: $1 - 4 + 3 = 0$ and $9 - 12 + 3 = 0$.

The method is to find one expression in the unknown that appears several times and make it the new unknown.
Watch the range of the new unknown: here $y = 3^x > 0$, so a negative root of the auxiliary equation would give no solution.
