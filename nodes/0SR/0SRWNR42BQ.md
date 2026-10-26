---
tag: 0SRWNR42BQ
kind: definition
name: Convergents of a continued fraction
msc: [11A55]
defines: 0D474C7ES1
uses: [06XF7BCFFJ]
sources:
  - url: https://en.wikipedia.org/wiki/Simple_continued_fraction
    locator: Infinite continued fractions and convergents
---

## Definition

Let $[a_0; a_1, a_2, \dots]$ be a [[simple continued fraction|06XF7BCFFJ]].
For each $n$ such that $a_n$ exists, the $n$-th convergent is the rational number $\dfrac{p_n}{q_n} = [a_0; a_1, \dots, a_n]$.
Here $p_n$ and $q_n$ are given by $p_{-2} = 0$, $p_{-1} = 1$, $q_{-2} = 1$, $q_{-1} = 0$ and
$$p_n = a_n p_{n-1} + p_{n-2}, \qquad q_n = a_n q_{n-1} + q_{n-2} \quad (n \ge 0).$$

## Remarks

The recurrences give $p_n q_{n-1} - p_{n-1} q_n = (-1)^{n-1}$. So $\gcd(p_n, q_n) = 1$, and the fraction $p_n / q_n$ is in lowest terms.
For $\sqrt{2} = [1; 2, 2, \dots]$, the convergents are $1, \frac{3}{2}, \frac{7}{5}, \frac{17}{12}, \frac{41}{29}, \dots$.
For a general [[continued fraction|0BK6JBK58W]], the same recurrences hold with $p_n = b_n p_{n-1} + a_n p_{n-2}$ and $q_n = b_n q_{n-1} + a_n q_{n-2}$.

## Explanations

### L1 human

The convergents are the fractions that you get when you cut a continued fraction off after finitely many terms.
They approach the value of the continued fraction, alternately from below and from above.
