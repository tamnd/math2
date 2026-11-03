---
tag: J0K163SEAF
kind: statement
role: proposition
name: Economic order quantity
msc: [90B05]
uses: [MX7JX6SS7Z]
about: [NQH9JRA8EX]
sources:
  - url: https://en.wikipedia.org/wiki/Economic_order_quantity
same_as:
  wikidata: Q451299
  wikipedia: Economic order quantity
---

## Statement

Consider a single item with constant demand rate $D > 0$ units per unit of time.
Each order has a fixed cost $K > 0$, and holding one unit for one unit of time costs $h > 0$.
Orders are delivered at once, no shortage is allowed, and each order has the same size $Q > 0$, placed when the stock reaches $0$.
Then the average cost per unit of time is
$$C(Q) = \frac{K D}{Q} + \frac{h Q}{2}.$$
It is minimized over $Q > 0$ exactly at the *economic order quantity*
$$Q^* = \sqrt{\frac{2 D K}{h}},$$
with minimal cost $C(Q^*) = \sqrt{2 D K h}$.

## Remarks

The stock falls linearly from $Q$ to $0$ in each cycle of length $Q / D$.
So its average level is $Q / 2$, and there are $D / Q$ orders per unit of time; this gives $C(Q)$.
The function $C$ is strictly convex on $(0, \infty)$, and $C'(Q) = -K D / Q^2 + h / 2$ vanishes only at $Q^*$.
At the optimum the two terms are equal: ordering cost and holding cost are each $\sqrt{D K h / 2}$.
Example: take $D = 1200$ units per year, $K = 50$ and $h = 3$ per unit per year.
Then $Q^* = \sqrt{40000} = 200$, so one orders six times a year at a total cost of $600$ per year.
The cost is flat near the optimum: $C(Q) / C(Q^*) = \frac12 (Q / Q^* + Q^* / Q)$, so an order size $50\%$ too large raises the cost by only about $8\%$.

## Explanations

### L1 human

Ordering in big batches saves on delivery fees but fills the storeroom; ordering small batches does the reverse.
The economic order quantity is the batch size that balances the two costs.
It grows only like the square root of demand, so a shop with four times the demand should order only twice as much each time.

### L2 human

The formula is usually credited to Ford W. Harris (1913) and is the first model of [[inventory theory|NQH9JRA8EX]].
It is the deterministic, continuous-time base case; the [[newsvendor model|RMQ4JB26AT]] treats random demand in one period, and $(s, S)$ policies treat random demand over many periods.
Standard extensions add a production rate, planned shortages, or quantity discounts, and each changes the formula in a predictable way.
