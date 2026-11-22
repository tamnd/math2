---
tag: YYH67TQ9GV
kind: statement
role: proposition
name: The quotient space is a vector space
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
about: [0BR3FY5Q8M]
uses: [0SVR29SV1V, 0J0SK5FF4M, 0EPTJA5QV4, 05EGHEQZAW, 02YFME3RGW]
formal:
  - system: lean4
    library: mathlib
    decl: Submodule.Quotient.eq
    match: partial
  - system: lean4
    library: mathlib
    decl: Submodule.ker_mkQ
    match: partial
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_space_(linear_algebra)
    locator: Definition
  - book: isbn:9783031410253
    locator: Section 3E
---

## Statement

The cosets of a subspace can be added and scaled through representatives, and they form a vector space onto which $V$ maps linearly.
Let $V$ be a vector space over a field $F$ and let $U$ be a [[subspace|0EPTJA5QV4]] of $V$.

1. For $v, w \in V$, the cosets $v + U$ and $w + U$ are equal if and only if $v - w \in U$.
   Two distinct cosets are disjoint, and each vector $v$ lies in its own coset $v + U$.
2. The addition $(v + U) + (w + U) = (v + w) + U$ and the scalar multiplication $a(v + U) = av + U$ on the [[quotient space|0SVR29SV1V]] $V / U$ are well defined.
   That is, they do not depend on the choice of the representatives $v$ and $w$.
3. With these operations, $V / U$ is a [[vector space|05EGHEQZAW]] over $F$, with zero vector $0 + U = U$ and with $-(v + U) = (-v) + U$.
4. The [[quotient map|0J0SK5FF4M]] $\pi \colon V \to V / U$, $\pi(v) = v + U$, is linear and surjective, and its [[kernel|02YFME3RGW]] is $U$.

## Remarks

### Why each hypothesis is needed

Each closure property of a subspace does one job, and a set that lacks it breaks one part of the statement.

The set must contain $0$.
Otherwise $v - v = 0$ is not in the set, so the relation "$v - w$ lies in the set" is not reflexive, and $v$ need not lie in its own class.
[[The line $y = 1$ in the plane|E3MQ50YQNR]] fails in this way.

The set must be closed under scalar multiplication.
Take $S = \Z$ in $V = \R$.
It is closed under addition and negatives, so $v - w \in \Z$ is an equivalence relation, and $1 \sim 0$.
But $\tfrac12 \cdot 1 - \tfrac12 \cdot 0 = \tfrac12 \notin \Z$, so $\tfrac12 \cdot 1 \not\sim \tfrac12 \cdot 0$, and scalar multiplication of classes is not defined.
The classes still form the group $\R / \Z$, but not a vector space.

The set must be closed under addition.
Take $S = \Z \cup \sqrt2\, \Z$ in $\R$.
Then $1 - 0$ and $\sqrt2 - 0$ lie in $S$, but $(1 + \sqrt2) - (0 + 0)$ does not, so the sum of classes depends on the representatives.

### What it gives you

Part 4 shows that every subspace is the kernel of a linear map, namely of $\pi$.
Since $\pi$ is surjective, a linear map $g$ on $V / U$ is determined by $g \circ \pi$.
So to build a linear map on $V / U$, it is enough to give a linear map on $V$ that vanishes on $U$, by the [[universal property of the quotient|0ZERJX6PH6]].
For example, $(x, y) \mapsto x - y$ vanishes on $U = \R(1, 1)$, so $(x, y) + U \mapsto x - y$ is a linear map on $\R^2 / U$.

### The converse

Let $S$ be any subset of $V$ such that the relation "$u - v \in S$" is an equivalence relation that is compatible with addition and scalar multiplication.
Then $S$ is a subspace.
Reflexivity gives $0 \in S$.
If $s, t \in S$, then $s \sim 0$ and $t \sim 0$, so compatibility gives $s + t \sim 0$ and $as \sim 0$, that is, $s + t \in S$ and $as \in S$.
So the subspaces are exactly the subsets that give a quotient vector space in this way.

## History

The method of computing with classes through representatives, and checking that the result does not depend on the choice, goes back at least to Gauss's congruences in the *Disquisitiones Arithmeticae* of 1801.

## Explanations

### L1 human

We want to compute with cosets by computing with any vector inside them.
This works because changing the chosen vector by something in $U$ changes the answer only by something in $U$.
So the answer lands in the same coset whichever vector we chose.

### L2 human

Let $U = \R(1, 1)$ in $\R^2$, and test the statement on numbers.
First, $(2, 0) + U = (3, 1) + U$, since
$$(3, 1) - (2, 0) = (1, 1) \in U.$$
Add $(0, 1) + U$ to both: we get $(2, 1) + U$ and $(3, 2) + U$, and these agree, since the difference is again $(1, 1)$.
Multiply both by $5$: we get $(10, 0) + U$ and $(15, 5) + U$, and these agree, since the difference is $(5, 5) \in U$.
Watch out: a rule such as $(x, y) + U \mapsto x$ gives $2$ and $3$ on the same coset, so it does not define a map on $V / U$.

### L3 human

The relation $v \equiv w \pmod U$ is a congruence of the vector space structure, that is, an equivalence relation compatible with the operations.
In universal algebra, the quotients of an algebraic structure correspond to its congruences.
For groups the congruences correspond to normal subgroups, and for vector spaces and modules they correspond to subspaces and submodules, through the class of $0$.
Mathlib builds `V ⧸ U` as a quotient type and proves that `Submodule.mkQ U` is linear with kernel `U`.
