---
tag: MGR5JY7H71
kind: proof
name: Proof that closed sets contain their limits
msc: ["54E35"]
proves: 09GQ3ZTQJ9
uses: [063W5JMY85, 0G5AV9Q4RR, 06JYPJ4WHH, 0A26X79RTB, 0DC3MPR7C9]
sources:
  - url: https://en.wikipedia.org/wiki/Closed_set
---

## Proof

We argue by contradiction.

1. Let $(X, d)$ be a [[metric space|063W5JMY85]] and let $F$ be a [[closed subset|0G5AV9Q4RR]] of $X$.
2. Let $(x_n)$ be a sequence of points of $F$ that [[converges|06JYPJ4WHH]] to $x \in X$.
3. Suppose that $x \notin F$. Then $x \in X \setminus F$, and $X \setminus F$ is open because $F$ is closed.
4. By the [[description of the open sets of a metric space|0A26X79RTB]], there is $\varepsilon > 0$ with $B(x, \varepsilon) \subseteq X \setminus F$. Here $B(x, \varepsilon)$ is the [[open ball|0DC3MPR7C9]].
5. Since $x_n \to x$, there is an integer $N$ with $d(x_n, x) < \varepsilon$ for all $n \ge N$.
6. By the symmetry of $d$, $d(x, x_N) < \varepsilon$, so $x_N \in B(x, \varepsilon) \subseteq X \setminus F$.
7. This contradicts $x_N \in F$. Hence $x \in F$.

## Idea

If the limit were outside $F$, it would have a ball around it that misses $F$. The terms of the sequence eventually enter every ball around the limit. They would then leave $F$, which they never do.
