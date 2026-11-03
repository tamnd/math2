---
tag: WHQE2KR445
kind: concept
name: Pi-calculus
msc: [68Q85, 68Q55]
specializes: [1CQRPEWCFD]
uses: [1CQRPEWCFD, BD756KR8FM]
sources:
  - url: https://en.wikipedia.org/wiki/Π-calculus
same_as:
  wikidata: Q602886
  wikipedia: Π-calculus
---

## Summary

The $\pi$-calculus is a [[process calculus|1CQRPEWCFD]] in which channel names can themselves be sent along channels.
It was introduced by Robin Milner, Joachim Parrow and David Walker as a calculus of mobile processes, whose links can change while they run.
Its main step is communication: $\overline{x}\langle y \rangle.P \mid x(z).Q$ becomes $P \mid Q[y/z]$, so the receiver learns the name $y$ and may later use it as a channel.
The [[lambda calculus|BD756KR8FM]] can be encoded in it, and it is a basic model for concurrent and distributed systems and for session types.

## Explanations

### L1 human

Imagine people who talk on telephone lines, and who can also tell each other telephone numbers.
After learning a new number, a person can call someone they could not reach before, so the network of connections changes over time.
The $\pi$-calculus is a small formal language for such systems: processes run side by side, send names over channels, and use received names as new channels.
For example, a server can create a private channel and send it to one client, so that only these two can then talk on it.
