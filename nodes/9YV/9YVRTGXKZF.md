---
tag: 9YVRTGXKZF
kind: example
name: Markov's principle under the Dialectica interpretation
msc: ["03F10", "03F55"]
topics: [8XY7JYZKFW]
audience: grad
instance_of: [HZ17ES9PDY]
uses: [ZREF8MTYNW, A4WR995XZP, 6QFRG42QQR, RXHJPVMPJH]
sources:
  - url: https://en.wikipedia.org/wiki/Dialectica_interpretation
    locator: Characterisation principles
---

## Example

Let $\varphi(m)$ be a quantifier-free formula, possibly with other free number variables.
Markov's principle for $\varphi$ is the formula $M = \neg \neg \exists m\, \varphi(m) \to \exists m\, \varphi(m)$.
We compute its [[Dialectica interpretation|ZREF8MTYNW]] and find a witness in [[system T|A4WR995XZP]].

1. By the clauses for atoms and $\exists$, $(\exists m\, \varphi(m))^D = \exists m\, \varphi(m)$: the witness is $m$, and there is no challenge.
2. By the clause for $\to$ with conclusion $\bot$, $(\neg \exists m\, \varphi(m))^D = \forall m\, \neg \varphi(m)$: no witness, and the challenge is $m$.
3. Again by the clause for $\to$, $(\neg \neg \exists m\, \varphi(m))^D = \exists m\, \neg \neg \varphi(m)$: the witness is a number $m$, and there is no challenge.
4. By clause 4 of the definition, $M^D = \exists g\, \forall m\, (\neg \neg \varphi(m) \to \varphi(g\, m))$, since neither side has a challenge.
5. Take $g = \lambda m.\, m$, the identity. Then the matrix is $\neg \neg \varphi(m) \to \varphi(m)$.
6. T proves $\varphi(m) \vee \neg \varphi(m)$, since $\varphi$ is quantifier-free. In the case $\neg \varphi(m)$, the premise gives $\bot$.
7. So T proves the matrix, and the identity witnesses $M$.

## Remarks

[[Heyting arithmetic|RXHJPVMPJH]] does not prove Markov's principle, but its interpretation has a witness.
So the [[soundness theorem|6QFRG42QQR]] has no converse for HA, and the interpretation validates principles beyond HA.
The reason is that the interpretation of $\neg \neg \exists m\, \varphi$ already contains the witness $m$: a double negation in front of $\exists$ is invisible to it.
The computation uses that $\varphi$ is quantifier-free.
For $\varphi(m) = \forall k\, \psi(m, k)$ the interpretation of $\neg \neg \exists m\, \varphi(m)$ has a witness of higher type, and the identity no longer applies.

## Explanations

### L1 human

Markov's principle says: if it is impossible that a search finds nothing, then the search finds something.
Many constructive mathematicians reject it, because it does not say how long the search takes.
The Dialectica interpretation accepts it with no work at all.
For example, for the search "find $m$ with $m \cdot m = 49$", the interpretation already treats "impossible to find nothing" as "here is $m$", so the program just passes $m = 7$ on.

### L2 human

We check step 4 against the clause for $\to$.

1. The premise has witness tuple $x = (m)$ and empty challenge tuple.
2. The conclusion has witness tuple $u = (m')$ and empty challenge tuple.
3. Clause 4 gives $\exists f, g\, \forall x, v\, (A_D(x, f x v) \to B_D(g x, v))$, and with empty $f$ and $v$ this is $\exists g\, \forall m\, (\neg \neg \varphi(m) \to \varphi(g\, m))$.
4. With $g$ the identity, the matrix holds by decidability of $\varphi$.

The typical use of this example is to explain why the characterization theorem of the interpretation includes Markov's principle.
A trap is to conclude that HA proves Markov's principle; the interpretation is sound for HA, but it is not complete for HA.
