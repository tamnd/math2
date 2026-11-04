---
tag: TPQ2M0X5D1
kind: proof
name: Proof that the number of odd-degree vertices is even
msc: [05C07]
proves: 0QQQQCPZA8
uses: [0T0F6CCS9W, 0XAP8WHNES]
sources:
  - url: https://en.wikipedia.org/wiki/Handshaking_lemma
    locator: Definitions and statement
---

## Proof

1. Let $V$ be the vertex set and $E$ the edge set of $G$. Let $V_o$ be the set of vertices of odd [[degree|0T0F6CCS9W]], and $V_e = V \setminus V_o$ the set of vertices of even degree.
2. By the [[handshaking lemma|0XAP8WHNES]], $\sum_{v \in V} \deg(v) = 2 \abs{E}$, which is even.
3. The sum $\sum_{v \in V_e} \deg(v)$ is a sum of even numbers, so it is even.
4. Hence $\sum_{v \in V_o} \deg(v) = 2\abs{E} - \sum_{v \in V_e} \deg(v)$ is even.
5. Each term of the sum in step 4 is odd, so it is congruent to $1$ modulo $2$. Thus that sum is congruent to $\abs{V_o}$ modulo $2$.
6. By steps 4 and 5, $\abs{V_o}$ is even.

## Idea

The total of all degrees is even. The even degrees do not change the parity, so the odd degrees must also add up to an even number, and that needs an even count of them.
