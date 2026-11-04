---
tag: 7TQK5EC8B8
kind: statement
role: theorem
name: Flow value is at most cut capacity
msc: [05C21, 90B10, 90C35]
uses: [0R5HTV7REV, ZSNXTW5E2K]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_networkflow_flows-cuts.ptx#L36
    locator: source/s_networkflow_flows-cuts.ptx:36
---

## Statement

Let $G$ be a [[flow network|ZSNXTW5E2K]] on a finite [[directed graph|0R5HTV7REV]]. It has a source $s$, a sink $t$, and a capacity $c(e) \ge 0$ on each edge $e$.

Let $\phi$ be a flow in $G$. That is, $0 \le \phi(e) \le c(e)$ for each edge $e$, and at each vertex other than $s$ and $t$ the flow in equals the flow out.

Let $V = L \cup U$ be a cut. That is, $L$ and $U$ are disjoint, $s \in L$ and $t \in U$. The capacity of the cut is the sum of $c(e)$ over the edges that go from $L$ to $U$.

Then the value of $\phi$ is at most the capacity of the cut.
