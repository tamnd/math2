---
tag: 2S27CNRV3S
kind: example
name: One agent at one moment in a STIT model
msc: ["03B45"]
topics: [CQM9SRN8PM]
audience: research
instance_of: [WYY2JXWMYY]
uses: [WYY2JXWMYY, 09CCE86A6D]
sources:
  - url: https://en.wikipedia.org/wiki/STIT_logic
    locator: Chellas and deliberative STIT operators
---

## Example

Take a tree with a root moment $m$ and three later moments $m_1, m_2, m_3$, each directly after $m$.
The histories are $h_k = \set{m, m_k}$ for $k = 1, 2, 3$, so $H_m = \set{h_1, h_2, h_3}$.
One agent $i$ has the choice partition $\mathrm{Choice}^m_i = \set{\set{h_1, h_2}, \set{h_3}}$.
The atom $p$ is true at $m/h_1$ and $m/h_2$, and false at $m/h_3$.
We evaluate the operators of [[STIT logic|WYY2JXWMYY]] at $m$.

1. The two sets $\set{h_1, h_2}$ and $\set{h_3}$ are disjoint, non-empty and cover $H_m$. So they form a [[partition|09CCE86A6D]] of $H_m$.
2. With one agent, independence holds: each cell is non-empty.
3. At $m/h_1$, the cell is $\set{h_1, h_2}$, and $p$ is true at $m/h_1$ and $m/h_2$. So $[i]p$ is true.
4. The same holds at $m/h_2$, since it has the same cell.
5. At $m/h_3$, the cell is $\set{h_3}$, and $p$ is false there. So $[i]p$ is false, and in fact $[i]\neg p$ is true.
6. $\square p$ is false at every $m/h_k$, since $p$ fails at $m/h_3$.
7. So $[i\ \mathsf{dstit}]p = [i]p \wedge \neg\square p$ is true at $m/h_1$ and $m/h_2$.
8. $[i](p \vee \neg p)$ is true at all three pairs, but $\square(p \vee \neg p)$ is also true. So $[i\ \mathsf{dstit}](p \vee \neg p)$ is false everywhere.
9. $\lozenge[i]p \wedge \lozenge[i]\neg p$ is true: the agent has one option that guarantees $p$ and one that guarantees $\neg p$.

## Remarks

The example shows the difference between a guaranteed result and a settled one.
If $p$ were also true at $m/h_3$, then $\square p$ would hold, $[i]p$ would hold on all histories, and $[i\ \mathsf{dstit}]p$ would fail everywhere.
If the agent had only the trivial partition $\set{H_m}$, then $[i]\varphi$ would coincide with $\square\varphi$, and the agent would see to nothing in the deliberative sense.
Splitting the first cell into $\set{h_1}$ and $\set{h_2}$ gives the agent full control, and $[i]$ becomes the identity on formulas about $m$ and the history.

## Explanations

### L1 human

A traveller stands at a crossroads with three possible futures.
Two of them start with the left road, one with the right road.
It rains in neither of the two left futures, and it rains in the right future.
So by taking the left road the traveller sees to it that she stays dry.
This is a real choice, because on the right road it rains.

### L2 human

1. Write down the cells of the partition: $\set{h_1, h_2}$ and $\set{h_3}$.
2. For $[i]p$ at $m/h$, find the cell of $h$ and check $p$ on all its histories.
3. For $\square p$, check $p$ on all of $H_m$.
4. For the deliberative stit, require the first test to pass and the second to fail.

The typical use is to model "could have done otherwise": at $m/h_1$ the agent sees to $p$, and $\lozenge\neg[i]p$ shows another option.
A trap: $[i]p$ at $m/h_3$ is false, but this does not mean that $i$ could not see to $p$; the formula $\lozenge[i]p$ is true at $m/h_3$.
