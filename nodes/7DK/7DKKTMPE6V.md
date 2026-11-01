---
tag: 7DKKTMPE6V
kind: definition
name: Purely transcendental extension
msc: [12F20]
defines: G5PVJMM37Z
uses: [0WQ1A8SHTZ, KV4PT6KW10, 4V81611P9N, AVCZ6HVBA7]
sources:
  - url: https://en.wikipedia.org/wiki/Transcendental_extension
---

## Definition

Let $L/K$ be a [[field extension|0WQ1A8SHTZ]].
The extension $L/K$ is *purely transcendental* if $L = K(S)$ for a subset $S \subseteq L$ that is [[algebraically independent|KV4PT6KW10]] over $K$.

## Remarks

Then $L$ is isomorphic over $K$ to the [[field of rational functions|4V81611P9N]] $K(x_s : s \in S)$, by sending $x_s$ to $s$.
Example: $\Q(\pi)/\Q$ is purely transcendental, with $S = \set{\pi}$.
Non-example: $\Q(\sqrt 2, t)/\Q$ with $t$ transcendental is not purely transcendental.
Indeed, $K$ is algebraically closed in $K(S)$ for independent $S$, but $\sqrt 2$ is algebraic over $\Q$ and not in $\Q$.
By [[Lüroth's theorem|AVCZ6HVBA7]], every field strictly between $K$ and $K(t)$ is again purely transcendental over $K$.
