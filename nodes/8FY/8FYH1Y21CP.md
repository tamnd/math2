---
tag: 8FYH1Y21CP
kind: definition
name: Boolean-valued model
msc: ["03E40", "03C90"]
defines: FVMNKJ3DT8
uses: [0XADJKM699, 983GZBQYT4]
sources:
  - url: https://en.wikipedia.org/wiki/Boolean-valued_model
---

## Definition

Let $B$ be a complete [[Boolean algebra|0XADJKM699]], that is, one in which every subset has a supremum and an infimum.
Let $\mathcal{L}$ be a first-order language.
A *$B$-valued model* $\mathcal{M}$ of $\mathcal{L}$ consists of a nonempty set $M$ and of the following data:

1. For each $n$-ary relation symbol $R$ (including equality), a map $M^n \to B$, written $(a_1, \ldots, a_n) \mapsto \norm{R(a_1, \ldots, a_n)}$.
2. For each $n$-ary function symbol $f$, a map $f^{\mathcal{M}} \colon M^n \to M$.

These data must satisfy, for all elements of $M$:

3. $\norm{a = a} = 1$ and $\norm{a = b} = \norm{b = a}$.
4. $\norm{a = b} \wedge \norm{b = c} \le \norm{a = c}$.
5. $\norm{a_1 = b_1} \wedge \cdots \wedge \norm{a_n = b_n} \wedge \norm{R(a_1, \ldots, a_n)} \le \norm{R(b_1, \ldots, b_n)}$ for each relation symbol $R$.
6. $\norm{a_1 = b_1} \wedge \cdots \wedge \norm{a_n = b_n} \le \norm{f^{\mathcal{M}}(a_1, \ldots, a_n) = f^{\mathcal{M}}(b_1, \ldots, b_n)}$ for each function symbol $f$.

The truth value of a formula with parameters from $M$ is defined by recursion: $\norm{\neg \varphi} = \neg \norm{\varphi}$, $\norm{\varphi \wedge \psi} = \norm{\varphi} \wedge \norm{\psi}$, and
$$\norm{\exists x \, \varphi(x)} = \sup_{a \in M} \norm{\varphi(a)}, \qquad \norm{\forall x \, \varphi(x)} = \inf_{a \in M} \norm{\varphi(a)}.$$

## Remarks

Example: if $B = \set{0, 1}$ and $\norm{a = b} = 1$ exactly when $a = b$, then a $B$-valued model is an ordinary [[structure|983GZBQYT4]], where $R(a_1, \ldots, a_n)$ holds when its value is $1$.
Non-example: if $B$ is not complete, a supremum over $M$ may not exist, and then the value of $\exists x \, \varphi(x)$ is not defined.
This is why the definition asks for a complete algebra.
For a complete Boolean algebra $B$, the Boolean-valued model $V^B$ of set theory gives every axiom of ZFC the value $1$.
Some authors also give function symbols values in $B$, by treating them as relation symbols.
