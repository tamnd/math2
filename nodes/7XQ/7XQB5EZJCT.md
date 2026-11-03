---
tag: 7XQB5EZJCT
kind: problem
name: Dynamic lot-size model
msc: [90B05, 90C39]
uses: [R3FXF08WBH]
about: [NQH9JRA8EX]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamic_lot-size_model
same_as:
  wikidata: Q2539221
  wikipedia: Dynamic lot-size model
history:
  posed_by: "Harvey M. Wagner and Thomson M. Whitin"
  first_stated: "1958"
  notes: "Introduced in their paper on a dynamic version of the economic lot size model, together with the dynamic programming algorithm now named after them."
---

## Problem

Let $T \ge 1$ be a number of periods, and let $d_1, \dots, d_T \ge 0$ be known demands.
Let $K_t \ge 0$ be the fixed cost of ordering in period $t$.
Let $h_t \ge 0$ be the cost of holding one unit from period $t$ to period $t + 1$.
An order plan is a vector $(x_1, \dots, x_T)$ of nonnegative order quantities, and the stock at the end of period $t$ is $I_t = \sum_{k \le t} (x_k - d_k)$, starting from $I_0 = 0$.
The plan is feasible if $I_t \ge 0$ for all $t$, so that no demand is backlogged.
The problem asks for a feasible plan that minimizes
$$\sum_{t=1}^{T} \big( K_t \mathbf{1}[x_t > 0] + h_t I_t \big).$$

## Remarks

Wagner and Whitin showed that some optimal plan has the zero-inventory ordering property: $I_{t-1} x_t = 0$ for all $t$.
So an order is placed only when the stock is empty, and each order covers the demand of a block of consecutive periods.
This gives a [[dynamic programming|R3FXF08WBH]] recursion over the periods, with $F(0) = 0$:
$$F(t) = \min_{1 \le j \le t} \Big( F(j - 1) + K_j + \sum_{k = j}^{t - 1} h_k \sum_{m = k + 1}^{t} d_m \Big).$$
Here $F(t)$ is the minimal cost of meeting the demands of periods $1$ to $t$ and $j$ is the period of the last order.
The answer is $F(T)$, computed in $O(T^2)$ steps; later work reduced this to $O(T \log T)$.
Example: $T = 2$, $d = (10, 10)$, $K_1 = K_2 = 30$, $h_1 = 2$; ordering $20$ in period $1$ costs $30 + 20 = 50$, ordering $10$ twice costs $60$, so the first plan is optimal.
A linear purchase cost that is the same in every period does not change the optimal plan, since the total amount ordered is fixed.

## Explanations

### L1 human

A factory knows its orders for the next weeks and must decide in which weeks to run production.
Each production run has a fixed setup cost, and making goods early means storing them.
The model finds the cheapest schedule, and the key insight is that one should only start a run when the storeroom is empty.
