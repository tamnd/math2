---
tag: TPDMV6ZXN3
kind: concept
name: RP
msc: [68Q15, 68Q10, 68W20]
specializes: [ESPYW94XGR]
sources:
  - url: https://en.wikipedia.org/wiki/RP_(complexity)
same_as:
  wikidata: Q1190846
  wikipedia: RP (complexity)
---

## Summary

RP, for randomized polynomial time, is the [[complexity class|ESPYW94XGR]] of decision problems solved by a polynomial-time [[probabilistic Turing machine|K99S0Q0814]] with one-sided error.
On a "no" instance the machine always rejects, and on a "yes" instance it accepts with probability at least $1/2$.
So an accepting run is a proof that the answer is "yes".
It satisfies $\mathrm{P} \subseteq \mathrm{RP} \subseteq \mathrm{NP}$ and $\mathrm{RP} \subseteq$ [[BPP|PTD7E1PKV4]].

## Explanations

### L1 human

An RP algorithm never says "yes" by mistake, but it may miss a "yes" answer with probability up to one half.
Repeating it $k$ times and saying "yes" if any run says "yes" lowers the chance of a miss to $2^{-k}$.
The [[Miller–Rabin primality test|0SZCSYHW60]] is an example: it finds a witness of compositeness with probability at least $3/4$ when $n$ is composite, and never when $n$ is prime.
So the set of composite numbers is in RP.
