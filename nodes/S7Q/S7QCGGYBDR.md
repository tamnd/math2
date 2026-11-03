---
tag: S7QCGGYBDR
kind: concept
name: Shannon capacity of a graph
msc: [05C69, 94A24, 05C76]
sources:
  - url: https://en.wikipedia.org/wiki/Shannon_capacity_of_a_graph
same_as:
  wikidata: Q17105770
  wikipedia: Shannon capacity of a graph
---

## Summary

Consider a channel whose pairs of confusable symbols are the edges of a [[graph|00C0BR7D7H]] $G$.
The Shannon capacity $\Theta(G)$ measures how many messages per symbol can be sent over it with zero error.
It is the limit of $\alpha(G^{\boxtimes k})^{1/k}$, where $\alpha$ is the size of a largest [[independent set|08ANQHHG3P]] and $G^{\boxtimes k}$ is the $k$-th strong power.
Shannon introduced it in 1956 to study the zero-error capacity of a channel.
It is hard to compute: its value is unknown even for the cycle $C_7$ on seven vertices.
See the [[definition|29SCH1KERA]].

## Explanations

### L1 human

Think of an alphabet where some pairs of letters can be confused by the receiver; draw an edge between such letters.
With one letter per message, you can only use a set of letters with no edges among them.
With words of length $k$, two words are confusable when every position is equal or confusable, and sometimes long words allow more than the $k$-th power of the one-letter count.
For the five-cycle $C_5$, one letter gives $2$ safe messages, but words of length $2$ give $5$ safe messages, not $4$.
The Shannon capacity is the best growth rate per letter, and for $C_5$ it is $\sqrt5$.
