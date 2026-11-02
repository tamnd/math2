---
tag: 3RT74FQYG1
kind: statement
role: theorem
name: Transfer principle
msc: ["03H05", "26E35"]
uses: [421QMTFG9T, 08J2M1JYAG, 086QKPF0A6, AGYBSTD7BG]
about: [421QMTFG9T]
sources:
  - url: https://en.wikipedia.org/wiki/Transfer_principle
same_as:
  wikidata: Q17157202
  wikipedia: Transfer principle
---

## Statement

Let ${}^*\R$ be the field of [[hyperreal numbers|421QMTFG9T]] built as an ultrapower of the [[real numbers|08J2M1JYAG]].
For each $k$-ary function $f$ on $\R$, let ${}^*f$ be its extension to ${}^*\R$, defined termwise on sequences.
Extend relations on $\R$ in the same way.
Let $\varphi$ be a sentence of [[first-order logic|086QKPF0A6]] built from real constants, functions and relations on $\R$.
Let ${}^*\varphi$ be the sentence obtained by replacing each function $f$ by ${}^*f$ and each relation $R$ by ${}^*R$.
Then $\varphi$ is true in $\R$ if and only if ${}^*\varphi$ is true in ${}^*\R$.

## Remarks

The principle is a special case of [[Łoś's theorem|AGYBSTD7BG]].
That theorem says that a first-order formula holds at a tuple of classes exactly when it holds termwise on a set of indices in the ultrafilter.

Example: the sentence $\forall x \, (x > 0 \to \exists y \, (y \cdot y = x))$ is true in $\R$.
By transfer, every positive hyperreal has a square root in ${}^*\R$.

The restriction to first-order sentences, where quantifiers range over elements and not over arbitrary subsets, is necessary.
Every nonempty subset of $\R$ that is bounded above has a supremum, but in ${}^*\R$ the set of infinitesimals is bounded above by $1$ and has no supremum.
Indeed, a supremum $s$ would be positive; if $s$ were infinitesimal then $2s$ would be a larger infinitesimal, and otherwise $s/2$ would be a smaller upper bound.

## Explanations

### L1 human

The hyperreals contain new numbers, infinitely small and infinitely large ones.
The transfer principle says that despite this, the hyperreals obey exactly the same elementary rules as the reals.
Take any statement that uses only "for all numbers", "there is a number" and the usual functions and relations.
It is true for the reals exactly when it is true for the hyperreals.

### L2 human

Transfer is what makes nonstandard proofs valid.
One proves a statement in ${}^*\R$ using infinitesimals, checks that it is the star version of a first-order statement, and transfers it back to $\R$.
For instance, a real function $f$ is continuous at a real $a$ exactly when ${}^*f(x) - f(a)$ is infinitesimal for every $x$ with $x - a$ infinitesimal.
Transfer is the key step in proving this equivalence.
Statements about all subsets of $\R$ transfer only to statements about internal subsets of ${}^*\R$, such as ${}^*A$ for $A \subseteq \R$.
