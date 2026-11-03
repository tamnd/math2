---
tag: 23FN5QGCQ9
kind: definition
name: Sardinas–Patterson algorithm
msc: [94A45, 68P30, 68Q45]
defines: NCQ698EVMT
uses: [MWBRNBXW1Y, 9DMSG5HAQX, 1P6EP01HZF]
sources:
  - url: https://en.wikipedia.org/wiki/Sardinas%E2%80%93Patterson_algorithm
---

## Definition

Let $\Sigma$ be a finite alphabet, let $\Sigma^*$ be the set of [[strings|1P6EP01HZF]] over $\Sigma$, and let $\varepsilon$ be the empty string.
Let $C \subseteq \Sigma^*$ be a finite set of non-empty strings.
For sets $U, V \subseteq \Sigma^*$, put $U^{-1} V = \set{w \in \Sigma^* : uw \in V \text{ for some } u \in U}$.
The *Sardinas–Patterson algorithm* computes the sets
$$S_1 = C^{-1} C \setminus \set{\varepsilon}, \qquad S_{i+1} = C^{-1} S_i \cup S_i^{-1} C \quad (i \ge 1).$$
It stops when some $S_i$ contains a codeword, and answers that $C$ is not [[uniquely decodable|MWBRNBXW1Y]].
It also stops when $S_i$ equals an earlier set $S_j$ with $j < i$, and answers that $C$ is uniquely decodable.

## Remarks

The theorem of Sardinas and Patterson says that $C$ is uniquely decodable if and only if no $S_i$ contains a codeword.
Each $S_i$ is a set of suffixes of codewords, a finite family, so the sequence repeats and the [[algorithm|9DMSG5HAQX]] terminates.
Example: for $C = \set{0, 01, 10}$, one gets $S_1 = \set{1}$ from $0 \cdot 1 = 01$.
Then $S_2 = \set{0}$ from $1 \cdot 0 = 10$, and $0 \in C$, so $C$ is not uniquely decodable.
Indeed $010 = 0 \cdot 10 = 01 \cdot 0$.
Contrast: for $C = \set{0, 01, 11}$, one gets $S_1 = \set{1}$ and $S_2 = \set{1}$ from $1 \cdot 1 = 11$.
The sequence repeats without meeting a codeword, so this code is uniquely decodable.
