---
tag: 1CQRPEWCFD
kind: concept
name: Process calculus
msc: [68Q85, 68Q55]
uses: [N8SGDCGJTW]
sources:
  - url: https://en.wikipedia.org/wiki/Process_calculus
same_as:
  wikidata: Q1970286
  wikipedia: Process calculus
---

## Summary

A process calculus, or process algebra, is a formal language for describing concurrent systems as processes that run in parallel and interact by communication.
Processes are built from a few primitives, such as sending or receiving on a channel, by operators such as parallel composition, choice and restriction.
Their behaviour is given by an [[operational semantics|N8SGDCGJTW]] as a labelled transition system, and processes are compared by behavioural equivalences such as bisimilarity.
The main examples are Milner's calculus of communicating systems (CCS), Hoare's communicating sequential processes (CSP), ACP and the pi-calculus.

## Explanations

### L1 human

A process calculus treats a concurrent program like an algebraic expression.
A process such as $a.P$ waits to perform the action $a$ and then behaves as $P$.
Writing $P \mid Q$ puts two processes side by side, and they can talk when one sends on a channel on which the other listens.
For example, $a.0 \mid \overline{a}.0$ is two processes that meet on channel $a$ and then both stop.
Two processes count as the same when no outside observer can tell their behaviour apart.
