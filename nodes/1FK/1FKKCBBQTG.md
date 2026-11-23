---
tag: 1FKKCBBQTG
kind: example
name: The negation of 2 < x ≤ 5
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
instance_of: [029JBBF693]
uses: [029JBBF693, 025YZN3VJW, 09PKJKA6J0]
sources:
  - url: https://en.wikipedia.org/wiki/Negation
    locator: lead section
  - url: https://en.wikipedia.org/wiki/De_Morgan%27s_laws
    locator: lead section
---

## Example

For a real number $x$, let $S$ be the statement "$2 < x \le 5$".
We find the [[negation|029JBBF693]] of $S$ and check it on five values of $x$.

1. The chain $2 < x \le 5$ is a [[conjunction|025YZN3VJW]] $p \land q$, with $p$ for "$2 < x$" and $q$ for "$x \le 5$".
2. By [[De Morgan's law|09PKJKA6J0]], $\neg(p \land q) \equiv \neg p \lor \neg q$.
3. The negation of "$2 < x$" is "$x \le 2$", and the negation of "$x \le 5$" is "$x > 5$".
4. So $\neg S$ is "$x \le 2$ or $x > 5$".
5. We check five values, including the two boundary points:

| $x$ | $2 < x$ | $x \le 5$ | $S$ | $x \le 2$ | $x > 5$ | $\neg S$ |
|---|---|---|---|---|---|---|
| $0$ | F | T | F | T | F | T |
| $2$ | F | T | F | T | F | T |
| $3$ | T | T | T | F | F | F |
| $5$ | T | T | T | F | F | F |
| $7$ | T | F | F | F | T | T |

6. In every row $S$ and $\neg S$ have opposite truth values, as the definition of negation requires.

## Remarks

Negating a compound statement takes two steps: find its logical form, then negate by the laws.
In the language of sets, $S$ describes the interval $(2, 5]$, and $\neg S$ describes its [[complement|0RKF1ZT5JJ]] $(-\infty, 2] \cup (5, \infty)$ in $\mathbb{R}$.

The boundary values $x = 2$ and $x = 5$ test the choice of strict and non-strict inequalities.
The wrong guess "$x < 2$ or $x > 5$" is F at $x = 2$, where $S$ is also F, so it is not the negation.
If $S$ were "$2 \le x \le 5$", the negation would be "$x < 2$ or $x > 5$".

## Explanations

### L1 human

The claim "$x$ is bigger than $2$ and at most $5$" says that $x$ lies in a window from $2$ to $5$.
The claim fails when $x$ is outside the window.
That happens when $x$ is at most $2$, or when $x$ is bigger than $5$.
So the negation is "$x$ is at most $2$ or $x$ is bigger than $5$", and for $x = 7$ the claim is false and the negation is true.

### L2 human

Negate "$-1 \le y < 4$ and $y \ne 0$" for a real number $y$.
The form is $a \land b \land c$, with $a$ for "$-1 \le y$", $b$ for "$y < 4$" and $c$ for "$y \ne 0$".
De Morgan's law, used twice, gives $\neg a \lor \neg b \lor \neg c$, which reads "$y < -1$ or $y \ge 4$ or $y = 0$".
Check $y = 0$: the statement is F because $c$ is F, and the negation is T because "$y = 0$" is T.
A proof by contradiction starts with exactly this kind of negation.
Watch out: the negation of "$y \ne 0$" is "$y = 0$", so the negation of a condition with $\ne$ contains an equation.
