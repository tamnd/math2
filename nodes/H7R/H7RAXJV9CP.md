---
tag: H7RAXJV9CP
kind: statement
role: theorem
name: Jacobson radical of an Artinian ring is nilpotent
msc: [16N20, 16P20]
uses: [ZV04WWYE2Y, XA0DCNH7WY, 5N2CJZ47D4, C2H26BYWHE, 019NFGFPR5]
about: [XA0DCNH7WY, 20QEAM8AX2]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobson_radical
---

## Statement

Let $R$ be a left [[Artinian ring|ZV04WWYE2Y]], that is, a ring with identity whose [[left ideals|5N2CJZ47D4]] satisfy the descending chain condition.
Let $J = J(R)$ be its [[Jacobson radical|XA0DCNH7WY]], the intersection of all maximal left ideals of $R$.
Then $J$ is a [[nilpotent ideal|C2H26BYWHE]]: there is an integer $n \ge 1$ with $J^n = 0$.

## Remarks

The chain $J \supseteq J^2 \supseteq J^3 \supseteq \cdots$ becomes constant, say $J^n = J^{n+1} = I$, and one shows $I = 0$.
If $I \ne 0$, choose a left ideal $L$ minimal among those with $IL \ne 0$, and $x \in L$ with $Ix \ne 0$.
Minimality gives $L = Rx$ and, since $I(Ix) = I^2 x = Ix \ne 0$, also $Ix = Rx$.
So $x = yx$ for some $y \in I \subseteq J$; as $1 - y$ is a [[unit|019NFGFPR5]], $x = 0$, a contradiction.
Example: for the ring of upper triangular $2 \times 2$ matrices over a field, $J$ is the set of strictly upper triangular matrices and $J^2 = 0$.
The Artinian hypothesis is needed: the local ring $\Z_{(p)}$ is Noetherian, but $J = p\Z_{(p)}$ is not nilpotent, since $p^n \ne 0$ for all $n$.

## Explanations

### L1 human

In a ring with the descending chain condition, the Jacobson radical is "small" in a strong sense.
Multiplying enough elements of it together always gives zero.
So the radical consists of nilpotent elements, and it is even killed by a fixed power.

### L2 human

This is a key step in the structure theory of Artinian rings.
With the [[Artin–Wedderburn theorem|R1F271180N]], which describes $R/J$ as a product of matrix rings over division rings, it shows that every left Artinian ring is [[semiprimary|XVP517QRH5]].
It is also used in the proof of the [[Hopkins–Levitzki theorem|W29AA0266Z]], which says that a left Artinian ring is left Noetherian.
