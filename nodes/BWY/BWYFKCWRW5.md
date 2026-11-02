---
tag: BWYFKCWRW5
kind: definition
name: Upper set
msc: [06A06]
defines: ETCE287E2R
uses: [011C29Q1S1, 0FE8Q5S42Y]
sources:
  - url: https://en.wikipedia.org/wiki/Upper_and_lower_sets
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|011C29Q1S1]] and let $U$ be a [[subset|0FE8Q5S42Y]] of $P$.
The set $U$ is an *upper set* when, for all $x, y \in P$, if $x \in U$ and $x \le y$, then $y \in U$.
Dually, a subset $L$ of $P$ is a *lower set* when, for all $x, y \in P$, if $y \in L$ and $x \le y$, then $x \in L$.

## Remarks

In $(\N, \le)$, the set $\set{n \in \N : n \ge 5}$ is an upper set: if $n \ge 5$ and $n \le m$, then $m \ge 5$.
The set of even numbers is not an upper set of $(\N, \le)$, since $2$ is in it, $2 \le 3$, and $3$ is not.
A subset is an upper set if and only if its complement is a lower set.
Unions and intersections of any family of upper sets are upper sets.
Other names are up-set and upward closed set for upper sets, and down-set, decreasing set and order ideal for lower sets.
The smallest lower set containing a subset $S$ is its [[down-closure|TGW5NTV3AA]].

## Explanations

### L1 human

An upper set never stops partway up: whatever lies above a member is also a member.
A lower set is the same thing turned upside down.
