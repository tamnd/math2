---
tag: 6AX5E50CZY
kind: concept
name: Network synthesis
msc: [94C05, 30C10]
sources:
  - url: https://en.wikipedia.org/wiki/Network_synthesis
same_as:
  wikidata: Q96395256
  wikipedia: Network synthesis
---

## Summary

Network synthesis is the design of an electrical network that has a prescribed response, such as a given impedance as a function of frequency.
It is the inverse of network analysis, which computes the response of a given network.
The central class of functions is the positive-real rational functions, which are exactly the impedances of passive networks of resistors, inductors, capacitors and transformers.
Classical results include [[Foster's reactance theorem|CPXHX475CW]] for lossless networks and [[Bott–Duffin synthesis|17KTEGVSZV]], which avoids transformers.

## Explanations

### L1 human

Analysis asks: here is a circuit, what does it do?
Synthesis asks the reverse: here is what I want the circuit to do, which circuit does it?
The answer is often not unique, and sometimes no circuit exists at all.
For example, the impedance $Z(s) = 2 + 3s$ is realized by a resistor of $2$ ohms in series with an inductor of $3$ henries.
Filter design for radios and telephones was the original motivation.
