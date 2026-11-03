---
tag: CPNEV9XHM4
kind: statement
role: theorem
name: Balinski–Young theorem
msc: [91B32, 91B12]
uses: [08GR54CKEA]
about: [X1X9TZ8GAR]
sources:
  - url: https://en.wikipedia.org/wiki/Apportionment_paradox
---

## Statement

Let $s$ be the number of states.
For a population vector $p = (p_1, \dots, p_s)$ of positive numbers and a house size $h \ge s$, an *apportionment* is a vector $a = (a_1, \dots, a_s)$ of nonnegative integers with $a_1 + \cdots + a_s = h$.
The *quota* of state $i$ is $q_i = h p_i / (p_1 + \cdots + p_s)$.
An *apportionment method* assigns to each $p$ and each $h \ge s$ a nonempty set $M(p, h)$ of apportionments.
The method:

1. *satisfies quota* if every $a \in M(p, h)$ has $\floor{q_i} \le a_i \le \lceil q_i \rceil$ for every $i$, where $\floor{\cdot}$ is the [[floor function|08GR54CKEA]] and $\lceil \cdot \rceil$ the ceiling function;
2. is *population monotone* if, for all $p, p'$, all $h \ge s$, all $a \in M(p, h)$, $a' \in M(p', h)$ and all states $i \ne j$ with $p'_i / p_i > p'_j / p_j$, either $a'_i \ge a_i$ or $a'_j \le a_j$.

If $s \ge 4$, then no apportionment method satisfies quota and is population monotone.

## Remarks

Population monotonicity forbids the population paradox: a state whose population grows relative to another state's cannot lose a seat while the other state gains one.
Hamilton's method of largest remainders satisfies quota, so it is not population monotone.
Divisor methods, such as the methods of Jefferson (D'Hondt) and Webster (Sainte-Laguë), are population monotone, so they do not satisfy quota for some populations.
Balinski and Young also showed that the population monotone methods are essentially the divisor methods, so the theorem forces a choice between staying within quota and avoiding the population paradox.

## Explanations

### L1 human

When seats are shared among states in proportion to population, two natural fairness demands are in conflict.
One demand is that each state get its exact fair share rounded up or down.
The other is that a state that grows faster than another should never lose a seat to it.
The theorem says no method can always meet both demands once there are four or more states.

### L2 human

The theorem is the central impossibility result of the mathematical theory of apportionment developed by Balinski and Young.
For example, the United States House of Representatives used Hamilton's method in the nineteenth century.
It now uses a divisor method, the Huntington–Hill method, which avoids the population paradox but may violate quota.
The same questions arise in proportional representation for party lists.
