---
tag: PC8ASRWARE
kind: statement
role: theorem
name: Shannon's source coding theorem
msc: [94A29, 94A24, 68P30]
uses: [0PNRKMRC55, 0WQNRCNY3M, G1ZAWMBNE1]
sources:
  - url: https://en.wikipedia.org/wiki/Shannon%27s_source_coding_theorem
same_as:
  wikidata: Q2411312
  wikipedia: Shannon's source coding theorem
---

## Statement

Let $X$ be a [[random variable|0PNRKMRC55]] with values in a finite set $\mathcal{X}$ and law $p$, and let $D \ge 2$ be an integer.
Assume that $p(x) > 0$ for every $x \in \mathcal{X}$.
Let $H_D(X) = -\sum_{x \in \mathcal{X}} p(x) \log_D p(x)$ be its [[entropy|Y86E072V0V]] in base $D$.
For a code $C$ that maps each $x \in \mathcal{X}$ to a string $C(x)$ over a $D$-symbol alphabet, let $L(C) = \sum_{x} p(x) \abs{C(x)}$ be its [[expected|0WQNRCNY3M]] length.

1. Every [[uniquely decodable code|MWBRNBXW1Y]] $C$ for $X$ satisfies $L(C) \ge H_D(X)$.
2. There is a [[prefix code|GNB3T6TD0M]] $C$ for $X$ with $L(C) < H_D(X) + 1$.
3. Let $X_1, X_2, \dots$ be independent with the same law as $X$. Let $L_k^*$ be the least expected length of a uniquely decodable code for $(X_1, \dots, X_k)$. Then $L_k^* / k \to H_D(X)$ as $k \to \infty$.

## Remarks

For part 1, the [[Kraft–McMillan inequality|G1ZAWMBNE1]] gives $\sum_x D^{-\abs{C(x)}} \le 1$.
Then $L(C) - H_D(X)$ is a relative entropy plus the non-negative number $-\log_D \sum_x D^{-\abs{C(x)}}$, so it is non-negative by Gibbs' inequality.
For part 2, the lengths $\ell(x) = \lceil -\log_D p(x) \rceil$ satisfy the Kraft inequality, so a prefix code with these lengths exists, and $\ell(x) < -\log_D p(x) + 1$.
Part 3 follows by applying parts 1 and 2 to the block, since its entropy is $k H_D(X)$, which gives $k H_D(X) \le L_k^* < k H_D(X) + 1$.

Equality holds in part 1 if and only if $p(x) = D^{-\abs{C(x)}}$ for every $x$.
Example: if $X$ takes the values $a, b, c$ with probabilities $1/2, 1/4, 1/4$, then $H_2(X) = 3/2$, and the binary prefix code $a \mapsto 0$, $b \mapsto 10$, $c \mapsto 11$ has expected length exactly $3/2$.
Without unique decodability part 1 fails: the code $a \mapsto 0$, $b \mapsto 1$, $c \mapsto 01$ has expected length $5/4 < 3/2$, but it cannot be decoded without ambiguity.

## Explanations

### L1 human

The entropy of a random source measures how much information each symbol carries, in bits when $D = 2$.
The theorem says that, on average, no lossless code can use fewer symbols than the entropy.
It also says that the entropy can be nearly reached, within one symbol for single letters and within any small margin per letter when long blocks are coded together.
So entropy is exactly the limit of lossless data compression.

### L2 human

Part 1 is the converse and part 2 the achievability; together they fix the optimal compression rate as $H_D(X)$ per symbol.
The [[Huffman code|JS11GWK9HF]] gives an optimal prefix code for each block, so it also achieves the bound of part 3.
Shannon also stated a fixed-length version.
Blocks of $k$ source symbols can be coded with about $k H_D(X)$ code symbols and an error probability tending to $0$.
This fails at any rate below $H_D(X)$ code symbols per source symbol.
That version rests on the asymptotic equipartition property.
The theorem is the model for the channel coding theorem, which plays the same role for transmission over a noisy channel.
