---
tag: VYRJ493MT8
kind: example
name: Z-channel
msc: [94A40, 94A24]
instance_of: [B9C5RBFATB]
uses: [J7MZ2XQP9M, A83CYGDXFG, GW25TGD33J]
sources:
  - url: https://en.wikipedia.org/wiki/Z-channel_(information_theory)
same_as:
  wikidata: Q17145032
  wikipedia: Z-channel (information theory)
---

## Example

Fix $p \in [0, 1]$.
The *Z-channel* with parameter $p$ is the discrete memoryless [[channel|B9C5RBFATB]] with input alphabet $\set{0, 1}$, output alphabet $\set{0, 1}$ and transition probabilities
$$P(0 \mid 0) = 1, \quad P(1 \mid 0) = 0, \quad P(0 \mid 1) = p, \quad P(1 \mid 1) = 1 - p.$$
So a $0$ is always received correctly, and a $1$ turns into a $0$ with probability $p$.

Check of the capacity: let the input $X$ take the value $1$ with probability $q$.
Then the output $Y$ is $1$ with probability $q(1 - p)$, and $H(Y \mid X) = q \, h(p)$, where $h$ is the [[binary entropy function|GW25TGD33J]].
So the [[mutual information|A83CYGDXFG]] is
$$I(X; Y) = h\big(q(1 - p)\big) - q \, h(p).$$
Maximizing over $q$ gives the [[capacity|J7MZ2XQP9M]], in bits per channel use,
$$C = \log_2\!\left(1 + (1 - p)\, p^{p/(1 - p)}\right) \quad (0 < p < 1).$$
For $p = 1/2$ this is $\log_2(5/4) \approx 0.32$.
For $p \to 0$ it tends to $1$, and for $p \to 1$ it tends to $0$.

The channel is not symmetric, so the uniform input is not optimal: for $0 < p < 1$ the best $q$ is below $1/2$.

## Explanations

### L1 human

The Z-channel models a link where only one kind of symbol can be damaged.
Think of light pulses: a dark slot stays dark, but a pulse can get lost, so a $1$ may arrive as a $0$.
Its diagram, with arrows $0 \to 0$, $1 \to 1$ and $1 \to 0$, looks like the letter Z.
Because $1$s are the risky symbol, a good code sends them a little less often than $0$s.
