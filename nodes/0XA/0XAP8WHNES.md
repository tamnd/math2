---
tag: 0XAP8WHNES
kind: statement
role: theorem
name: Handshaking lemma
msc: [05C07]
uses: [0WNGQBPPQX, 0T0F6CCS9W]
sources:
  - url: https://en.wikipedia.org/wiki/Handshaking_lemma
    locator: Definitions and statement
same_as:
  wikidata: Q954454
  wikipedia: Handshaking lemma
---

## Statement

Let $G$ be a finite [[graph|0JD5C82QMB]] with vertex set $V$ and [[edge set|0WNGQBPPQX]] $E$.
Then
$$\sum_{v \in V} \deg(v) = 2\, |E|.$$

## Remarks

Proof: count the pairs $(v, e)$ with $v \in e$. Each edge has two ends, and each vertex $v$ lies in $\deg(v)$ edges. This is [[double counting|0F8YBHF2W3]].
A direct consequence is that the [[number of odd-degree vertices is even|0QQQQCPZA8]].
For a $3$-regular graph on $n$ vertices, it gives $3n = 2 |E|$, so $n$ is even.

## Explanations

### L1 human

At a party, add up the number of hands each person shakes.
Each handshake is counted twice, once for each of the two people, so the total is twice the number of handshakes.
