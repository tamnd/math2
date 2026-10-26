---
tag: 09GQ3ZTQJ9
kind: statement
role: proposition
name: Closed sets contain their limits
msc: ["54E35"]
uses: [0G5AV9Q4RR, 06JYPJ4WHH, 0A26X79RTB]
sources:
  - url: https://en.wikipedia.org/wiki/Closed_set
    locator: More about closed sets
---

## Statement

Let $(X, d)$ be a [[metric space|063W5JMY85]] and let $F$ be a [[closed subset|0G5AV9Q4RR]] of $X$.
Let $(x_n)$ be a sequence of points of $F$ that [[converges|06JYPJ4WHH]] to a point $x \in X$.
Then $x \in F$.

## Remarks

Proof: if $x \notin F$, then $X \setminus F$ is open and contains $x$. Thus some ball $B(x, \varepsilon)$ misses $F$. But $x_n \in B(x, \varepsilon)$ for large $n$, a contradiction.
In a metric space the converse is also true: a set that contains the limits of all its convergent sequences is closed. This follows from [[closure is the set of limits of sequences|003QP7A8HG]].
The statement holds in every [[topological space|0CNQXVBHCX]], with the same proof.

## Explanations

### L1 human

You cannot leave a closed set by a limit of a sequence.
For example, $1/n \to 0$ in $\mathbb{R}$, and $0$ is not in $(0, 1]$, which shows that $(0, 1]$ is not closed.
