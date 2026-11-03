---
tag: MX7JX6SS7Z
kind: definition
name: Inventory theory
msc: [90B05, 90C39, 90B06]
defines: NQH9JRA8EX
uses: [PP7H534BV7, 0WQNRCNY3M, 0DVDCMA2DK]
sources:
  - url: https://en.wikipedia.org/wiki/Inventory_theory
---

## Definition

*Inventory theory* is the study of inventory models and of the policies that are optimal for them.
A *periodic-review inventory model* over $T$ periods consists of:

1. an initial inventory level $x_1 \in \R$;
2. demands $D_1, \dots, D_T$, which are nonnegative random variables with known joint law;
3. an ordering cost $c(q) = K \mathbf{1}[q > 0] + c q$ for an order of size $q \ge 0$, with fixed cost $K \ge 0$ and unit cost $c \ge 0$;
4. a holding and shortage cost $L(y) = h \max(y, 0) + p \max(-y, 0)$ on the level $y$ at the end of a period, with $h \ge 0$ and $p \ge 0$.

In period $t$ the decision maker sees the level $x_t$, orders $q_t \ge 0$, which arrives at once, and then the demand $D_t$ occurs.
The next level is $x_{t+1} = x_t + q_t - D_t$; negative levels are backlogged demand.
A *policy* chooses $q_t$ as a function of the information seen so far, and an *optimal policy* minimizes $\mathbb{E}\big[\sum_{t=1}^{T} \big(c(q_t) + L(x_{t+1})\big)\big]$.

## Remarks

Example: $T = 1$, $K = 0$, $x_1 = 0$ and $D_1$ uniform on $[0, 100]$, with $c = 1$, $h = 1$ and $p = 3$.
All four clauses hold, and the cost $q + \mathbb{E}[\max(q - D_1, 0)] + 3\, \mathbb{E}[\max(D_1 - q, 0)]$ is minimized where $1 + P(D_1 \le q) - 3 P(D_1 > q) = 0$, that is, at $q = 50$.

Non-example: with quantity discounts, the price of each unit falls with the order size in steps.
Then the ordering cost is not of the form in clause 3, so the model is an inventory model outside this class.

Other standard models use continuous review, lead times between order and delivery, lost sales instead of backlogging, several items or several locations.
For the model above with $K > 0$ and independent demands, Scarf proved in 1960 that an $(s, S)$ policy is optimal.
Such a policy orders up to $S_t$ when the level is below $s_t$, and does not order otherwise.
