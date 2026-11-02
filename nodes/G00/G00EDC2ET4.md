---
tag: G00EDC2ET4
kind: definition
name: Nonstandard analysis
msc: ["26E35", "03H05"]
defines: WM62GKCBWN
uses: [08J2M1JYAG, 421QMTFG9T, 3RT74FQYG1, 1ZBY4W4E81, 0V1EJCT8G6]
sources:
  - url: https://en.wikipedia.org/wiki/Nonstandard_analysis
---

## Definition

Nonstandard analysis is the part of mathematics that develops analysis with the following tools.

1. A proper extension ${}^*\R$ of the [[real numbers|08J2M1JYAG]], such as the field of [[hyperreal numbers|421QMTFG9T]], that contains nonzero infinitesimals.
2. For each set, function and relation on $\R$, an extension of it to ${}^*\R$.
3. The [[transfer principle|3RT74FQYG1]], under which a first-order statement about $\R$ holds if and only if the corresponding statement about ${}^*\R$ holds.

Notions of analysis are then expressed with infinitesimals and the [[standard part function|1ZBY4W4E81]].

## Remarks

Example: in nonstandard analysis, a function $f \colon \R \to \R$ has [[derivative|0V1EJCT8G6]] $L$ at $x$ if $\operatorname{st}\bigl(({}^*f(x + \varepsilon) - f(x))/\varepsilon\bigr) = L$ for every nonzero infinitesimal $\varepsilon$, where ${}^*f$ is the extension of $f$ to ${}^*\R$.
For $f(x) = x^2$ the quotient is $2x + \varepsilon$, whose standard part is $2x$.

Non-example: smooth infinitesimal analysis also uses infinitesimals, but they are nilpotent and its logic is intuitionistic.
It does not use an extension of $\R$ with transfer, so it is not nonstandard analysis.

The theorems of nonstandard analysis about standard objects can also be proved by ordinary methods, but the nonstandard proofs are often shorter.
