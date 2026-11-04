---
tag: 5Z825PMQQP
kind: proof
name: Proof of Euler's identity
msc: [33B10]
proves: 09285XX7AE
uses: [04R3CY41VJ, 01A8JGR4JM, 0C1VYVNV2N, 0WB57D9488]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_identity
    locator: lead section
---

## Proof

1. Let $\pi$ be the real number [[pi|0C1VYVNV2N]].
2. Apply [[Euler's formula|04R3CY41VJ]] with $z = \pi$: $e^{i \pi} = \cos \pi + i \sin \pi$.
For the real number $\pi$, these power series are the real [[sine and cosine|0WB57D9488]].
3. By [[cos pi = -1|01A8JGR4JM]], $\cos \pi = -1$ and $\sin \pi = 0$. So $e^{i \pi} = -1 + 0 i = -1$.
4. Adding $1$ to both sides gives $e^{i \pi} + 1 = 0$.

## Idea

Euler's formula turns $e^{i \pi}$ into the point of the unit circle at angle $\pi$.
That point is $-1$, half a turn from $1$.
