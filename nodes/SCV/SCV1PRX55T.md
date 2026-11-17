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

Problem: find all real numbers $x$ with
$$x^4 - 13x^2 + 36 = 0.$$
The equation has degree $4$, and we have no general method at hand for it.
We use an [[auxiliary problem|DYSJB93V11]].

1. Look at the unknown: $x$ appears only through $x^2$, since $x^4 = (x^2)^2$.
2. Introduce $y = x^2$. The equation becomes the auxiliary problem $y^2 - 13y + 36 = 0$.
3. Solve the auxiliary problem. The [[quadratic formula|0KYZXYDGQZ]] gives $y = \frac{13 \pm \sqrt{169 - 144}}{2} = \frac{13 \pm 5}{2}$, so $y = 9$ or $y = 4$.
4. Check the factorization: $(y - 4)(y - 9) = y^2 - 13y + 36$.
5. Return to the original unknown: $x^2 = 4$ or $x^2 = 9$.
6. So $x \in \{-3, -2, 2, 3\}$.
7. Check one value: for $x = 3$, $81 - 13 \cdot 9 + 36 = 81 - 117 + 36 = 0$. The values $-3$, $2$ and $-2$ give $0$ in the same way, since $x^4$ and $x^2$ do not change when $x$ changes sign.

## Remarks

The reduction is bilateral, in Pólya's term: the original problem and the auxiliary problem with the return step are equivalent.
A real number $x$ solves the quartic exactly when $y = x^2$ is a root of the quadratic.
Conversely, each root $y \geq 0$ of the quadratic gives the solutions $x = \pm\sqrt{y}$ of the quartic.
So no solution is lost and no false solution is added.

The condition $y \geq 0$ matters when the coefficients change.
For $x^4 + 3x^2 - 4 = 0$, the auxiliary equation $y^2 + 3y - 4 = 0$ has the roots $y = 1$ and $y = -4$.
Only $y = 1$ gives real $x$, so the real solutions are $x = \pm 1$.

The same substitution solves every equation $a x^{2k} + b x^k + c = 0$, with $y = x^k$.

## Explanations

### L1 human

The equation looks hard because of the fourth power.
But $x^4$ is the square of $x^2$.
If we call $x^2$ a new name, $y$, the equation becomes an ordinary quadratic equation in $y$.
That one we can solve: $y$ is $4$ or $9$.
Then $x$ is a number whose square is $4$ or $9$, so $x$ is $2$, $-2$, $3$ or $-3$.

### L2 human

We solve $9^x - 4 \cdot 3^x + 3 = 0$ with the same idea.

1. Look at the unknown: $9^x = (3^x)^2$, so $x$ appears only through $3^x$.
2. Introduce $y = 3^x$. The auxiliary equation is $y^2 - 4y + 3 = 0$.
3. Factor: $(y - 1)(y - 3) = 0$, so $y = 1$ or $y = 3$.
4. Return: $3^x = 1$ gives $x = 0$, and $3^x = 3$ gives $x = 1$.
5. Check: $1 - 4 + 3 = 0$ and $9 - 12 + 3 = 0$.

The typical use: find an expression in the unknown that appears several times, and make it the new unknown.

A trap: the new unknown has a range; here $y = 3^x > 0$, so a negative root of the auxiliary equation would give no solution.
