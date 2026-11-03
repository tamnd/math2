---
tag: JKY3NA9V8P
kind: definition
name: Life table
msc: [91G05, 91D20]
defines: PWBQ7GKQGD
uses: [QTM1HZM53Q, 0PNRKMRC55]
sources:
  - url: https://en.wikipedia.org/wiki/Life_table
---

## Definition

Let $T$ be a nonnegative [[random variable|0PNRKMRC55]], the age at death of a newborn, with [[survival function|QTM1HZM53Q]] $S(x) = P(T > x)$.
Fix a number $l_0 > 0$, the *radix*.
The *life table* of $T$ with radix $l_0$ lists, for each integer age $x \ge 0$:

1. the number of survivors $l_x = l_0 S(x)$;
2. the number of deaths $d_x = l_x - l_{x+1}$ between ages $x$ and $x + 1$;
3. the one-year death probability $q_x = d_x / l_x$ and survival probability $p_x = 1 - q_x = l_{x+1}/l_x$, defined when $l_x > 0$.

The *curtate life expectancy* at age $x$ is $e_x = \sum_{k \ge 1} l_{x+k}/l_x$, and the *complete life expectancy* is $\mathring{e}_x = \frac{1}{l_x}\int_x^\infty l_t \, dt$, where $l_t = l_0 S(t)$ for real $t$.

## Remarks

The quantity $q_x$ equals $P(T \le x + 1 \mid T > x)$, the chance that a person alive at age $x$ dies within a year.
Example: with $l_0 = 1000$, $l_1 = 990$ and $l_2 = 985$, one gets $d_0 = 10$, $q_0 = 0.01$, $d_1 = 5$ and $q_1 = 5/990 \approx 0.00505$.
Non-example: a list with $l_1 = 990$ and $l_2 = 995$ is not a life table, since $l_x$ must be nonincreasing because $S$ is.
In actuarial notation, ${}_t p_x = l_{x+t}/l_x$ is the probability of surviving $t$ more years from age $x$.
