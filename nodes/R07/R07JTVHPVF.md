---
tag: R07JTVHPVF
kind: definition
name: Process calculus
msc: [68Q85, 68Q55]
defines: 1CQRPEWCFD
uses: [N8SGDCGJTW, 0G8VEZ3WTK]
sources:
  - url: https://en.wikipedia.org/wiki/Process_calculus
---

## Definition

A *process calculus* is given by the following data.

1. A set of actions, usually names $a, b, \dots$, their co-names $\overline{a}, \overline{b}, \dots$, and an internal action $\tau$.
2. A grammar of process terms built from the inactive process $0$ by operators. Typical operators are action prefix $\alpha.P$, choice $P + Q$, parallel composition $P \mid Q$, restriction $(\nu a)P$, and recursion or replication.
3. An [[operational semantics|N8SGDCGJTW]]: a labelled transition relation $P \xrightarrow{\alpha} P'$ on process terms, defined by inference rules for each operator. In it, a parallel composition can perform $\tau$ when one component does $a$ and the other does $\overline{a}$.
4. A behavioural equivalence, an [[equivalence relation|0G8VEZ3WTK]] on process terms, such as strong or weak bisimilarity, used to say when two processes behave the same.

The standard example is Milner's calculus of communicating systems (CCS).
Its transition rules are the following, together with the symmetric rules for $+$ and $\mid$.
Prefix: $\alpha.P \xrightarrow{\alpha} P$.
Choice and parallel: if $P \xrightarrow{\alpha} P'$, then $P + Q \xrightarrow{\alpha} P'$ and $P \mid Q \xrightarrow{\alpha} P' \mid Q$.
Communication: if $P \xrightarrow{a} P'$ and $Q \xrightarrow{\overline{a}} Q'$, then $P \mid Q \xrightarrow{\tau} P' \mid Q'$.
Restriction: if $P \xrightarrow{\alpha} P'$ and $\alpha \notin \set{a, \overline{a}}$, then $(\nu a)P \xrightarrow{\alpha} (\nu a)P'$.

## Remarks

Example: in CCS, $(\nu a)(a.P \mid \overline{a}.Q) \xrightarrow{\tau} (\nu a)(P \mid Q)$.
The prefix rule gives $a.P \xrightarrow{a} P$ and $\overline{a}.Q \xrightarrow{\overline{a}} Q$, the communication rule gives the $\tau$ step of the parallel composition, and the restriction rule passes $\tau$ through since $\tau \notin \set{a, \overline{a}}$.
The restriction makes $a$ private, so neither process can talk on $a$ to the outside.

Non-example: the same process has no transition labelled $a$, since restriction blocks the action $a$.

The processes $a.(b.0 + c.0)$ and $a.b.0 + a.c.0$ have the same complete traces, $a b$ and $a c$, but they are not bisimilar: after $a$, the second has already chosen between $b$ and $c$.
This shows that process calculi distinguish more than sequences of actions.
