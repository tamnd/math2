---
tag: XRGSKJVF0M
kind: definition
name: Descending chain condition
msc: [06A06, "13E10"]
defines: 6SVWAP8WP5
uses: [0QV2JS9RJ3, 0G9EKM0E15, 55WD0H03CZ, 0GZ6Y1H4RN, 20QEAM8AX2]
sources:
  - url: https://en.wikipedia.org/wiki/Ascending_chain_condition
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|0QV2JS9RJ3]].
The poset $P$ satisfies the *descending chain condition* when every [[sequence|0G9EKM0E15]] $x_1 \ge x_2 \ge x_3 \ge \cdots$ in $P$ is eventually constant.
That is, there is an index $n$ such that $x_m = x_n$ for all $m \ge n$.

## Remarks

Example: the ideals of the ring $\Z / 12\Z$, ordered by inclusion, satisfy the descending chain condition.
Check: there are only six ideals, so a decreasing sequence of ideals takes finitely many values and must be eventually constant.
Rings whose ideals satisfy the condition are the [[Artinian rings|20QEAM8AX2]].

Non-example: the ideals of $\Z$ do not satisfy it, since $2\Z \supsetneq 4\Z \supsetneq 8\Z \supsetneq \cdots$ never stops.

The condition is the [[ascending chain condition|0GZ6Y1H4RN]] for the opposite order.
A poset satisfies it if and only if every nonempty subset has a minimal element, that is, the order is [[well-founded|55WD0H03CZ]].
The direction from the descending chain condition to minimal elements uses the axiom of dependent choice.
The abbreviation DCC is common, and the minimal-element form is called the minimal condition.
