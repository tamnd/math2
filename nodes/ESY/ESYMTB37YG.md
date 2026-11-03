---
tag: ESYMTB37YG
kind: example
name: Binary erasure channel
msc: [94A40, 94A24]
instance_of: [B9C5RBFATB]
uses: [J7MZ2XQP9M, A83CYGDXFG]
sources:
  - url: https://en.wikipedia.org/wiki/Binary_erasure_channel
same_as:
  wikidata: Q864142
  wikipedia: Binary erasure channel
---

## Example

Let $0 \le \alpha \le 1$.
The *binary erasure channel* with erasure probability $\alpha$ has input alphabet $\set{0, 1}$ and output alphabet $\set{0, 1, ?}$, where $?$ means "erased".
Its transition probabilities are
$$W(x \mid x) = 1 - \alpha, \qquad W(? \mid x) = \alpha \qquad (x \in \set{0, 1}),$$
and $W(1 - x \mid x) = 0$.
Each row is a probability vector, so this is a [[communication channel|B9C5RBFATB]]: a bit either arrives correctly or is lost, and the receiver knows which.

Its [[capacity|J7MZ2XQP9M]] is $C = 1 - \alpha$ bits.
The check: for an input $X$, the [[mutual information|A83CYGDXFG]] is $I(X; Y) = H(X) - H(X \mid Y)$.
If $Y \ne ?$ then $Y = X$, and if $Y = ?$, which happens with probability $\alpha$ independently of $X$, the receiver knows nothing about $X$.
So $H(X \mid Y) = \alpha H(X)$ and $I(X; Y) = (1 - \alpha) H(X) \le 1 - \alpha$, with equality for the uniform input.

For $\alpha = 1/4$, one can send about $3$ useful bits for every $4$ channel uses.

## Explanations

### L1 human

Here a bit is either delivered exactly or visibly lost, like a packet that never arrives.
A fraction $\alpha$ of the bits is lost on average, and the capacity says that exactly the remaining fraction $1 - \alpha$ can carry information.
Remarkably, this holds even though the sender does not know which bits will be lost.
The erasure channel is simple enough that many coding questions can be solved exactly for it.
