---
tag: 2MY68TKRRB
kind: definition
name: Operations research
msc: [90B99, 90C90]
defines: PSE3NRBXKY
uses: [W3ZXKT3DS1, NS0Q42Y3FX, P64V0HTE78]
sources:
  - url: https://en.wikipedia.org/wiki/Operations_research
---

## Definition

*Operations research* is the discipline that applies mathematical models and methods to decision problems in the operation of organizations and systems.
Its work has three stages:

1. building a model of the decision problem, with decision variables, constraints and an objective, or with random inputs;
2. analyzing the model with methods such as [[mathematical optimization|W3ZXKT3DS1]], probability, [[queueing theory|P64V0HTE78]] and simulation;
3. turning the results into a recommended decision.

## Remarks

Many models of operations research are [[optimization problems|NS0Q42Y3FX]]: linear and integer programs, network flow problems, and scheduling problems.
Others are stochastic, such as queueing systems, inventory models and Markov decision processes.

Example: a factory makes chairs and tables with profits $3$ and $5$ per unit.
A chair uses $1$ unit of wood and a table $2$ units, with $8$ units available; each item uses $1$ hour of labour, with $5$ hours available.
The model "maximize $3c + 5t$ subject to $c + 2t \le 8$, $c + t \le 5$, $c, t \ge 0$" is an operations research model.
Its optimum is $c = 2$, $t = 3$, with profit $21$, at the vertex where both constraints are tight.

Non-example: proving that there are infinitely many primes is mathematics, but not operations research, since no decision problem is modelled.

The field is also called *operational research*, especially in British English.
