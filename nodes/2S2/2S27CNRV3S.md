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
The histories are $h_k = \{m, m_k\}$ for $k = 1, 2, 3$, so $H_m = \{h_1, h_2, h_3\}$.
One agent $i$ has the following choice partition.
$$\mathrm{Choice}^m_i = \{\{h_1, h_2\}, \{h_3\}\}$$
The atom $p$ is true at $m/h_1$ and $m/h_2$, and false at $m/h_3$.
We evaluate the operators of [[STIT logic|WYY2JXWMYY]] at $m$.

1. The sets $\{h_1, h_2\}$ and $\{h_3\}$ are disjoint and nonempty, and they cover $H_m$.
   So they form a [[partition|09CCE86A6D]] of $H_m$.
2. With one agent, independence asks only that each cell be nonempty, and both are.
3. At $m/h_1$ the cell is $\{h_1, h_2\}$, and $p$ is true at $m/h_1$ and at $m/h_2$.
   So $[i]p$ is true at $m/h_1$.
4. The same holds at $m/h_2$, which lies in the same cell.
5. At $m/h_3$ the cell is $\{h_3\}$, and $p$ is false there.
   So $[i]p$ is false at $m/h_3$, and $[i]\neg p$ is true.
6. The box $\square p$ is false at every $m/h_k$, since $p$ fails at $m/h_3$.
7. So $[i\ \mathsf{dstit}]p = [i]p \wedge \neg\square p$ is true at $m/h_1$ and at $m/h_2$.
8. The formula $[i](p \vee \neg p)$ is true at all three pairs, but $\square(p \vee \neg p)$ is true as well.
   So $[i\ \mathsf{dstit}](p \vee \neg p)$ is false everywhere.
9. The formula $\lozenge[i]p \wedge \lozenge[i]\neg p$ is true, by steps 3 and 5.
   The agent has one option that guarantees $p$ and one that guarantees $\neg p$.

## Remarks

The example separates a guaranteed result from a settled one.
If $p$ were also true at $m/h_3$, then $\square p$ would hold, $[i]p$ would hold on all histories, and $[i\ \mathsf{dstit}]p$ would fail everywhere.
If the agent had only the trivial partition $\{H_m\}$, then $[i]\varphi$ would coincide with $\square\varphi$, and the agent would see to nothing in the deliberative sense.
If we split the first cell into $\{h_1\}$ and $\{h_2\}$, the agent gets full control, and $[i]\varphi$ becomes equivalent to $\varphi$ at every $m/h$.

## Explanations

### L1 human

A traveler stands at a crossroads with three possible futures.
Two of them start with the left road, and one starts with the right road.
It rains in neither of the two left futures, and it rains in the right future.
So by taking the left road the traveler sees to it that she stays dry.
This is a real choice, because on the right road it rains.

### L2 human

To test $[i]p$ at $m/h$, find the cell of $h$ and check $p$ on all its histories.
To test $\square p$, check $p$ on all of $H_m$.
The deliberative stit asks for the first test to pass and the second to fail, which happens at $m/h_1$ and at $m/h_2$.
The typical use is to model "could have done otherwise": at $m/h_1$ the agent sees to $p$, and $\lozenge\neg[i]p$ shows another option.
Watch out: $[i]p$ is false at $m/h_3$, but this does not mean that $i$ could not see to $p$.
The formula $\lozenge[i]p$ is true at $m/h_3$, because the other option guarantees $p$.
