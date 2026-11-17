---
tag: 2E6Y7GNDAT
kind: example
name: An evaluation game with a negation
msc: ["03B10"]
topics: [NJDME6F845]
audience: grad
instance_of: [D45Z7HETDA]
uses: [D45Z7HETDA, 1WTCZB4DVB]
sources:
  - url: https://en.wikipedia.org/wiki/Game_semantics
    locator: lead section
---

## Example

Let $\mathcal{M}$ have domain $\set{0, 1}$ and $R^{\mathcal{M}} = \set{(0, 1), (1, 0)}$.
Let $\varphi = \forall x \, \exists y \, R(x, y) \wedge \neg \exists x \, R(x, x)$.
We list every play of the [[evaluation game|D45Z7HETDA]] $G(\mathcal{M}, \varphi)$ and find Eloise's winning strategy.

1. At $\wedge$, Abelard, the falsifier, chooses a conjunct.
2. Left conjunct $\forall x \, \exists y \, R(x, y)$: Abelard picks $a \in \set{0, 1}$, then Eloise picks $b$.
3. Eloise's strategy is $b = 1 - a$. The play ends at $R(x, y)$ with $(a, 1 - a) \in R^{\mathcal{M}}$, and Eloise, the verifier, wins.
4. Right conjunct $\neg \exists x \, R(x, x)$: at $\neg$ the roles exchange, so Abelard becomes the verifier of $\exists x \, R(x, x)$.
5. At $\exists x$, the verifier Abelard picks $a \in \set{0, 1}$.
6. The play ends at $R(x, x)$ with $x \mapsto a$. The pair $(a, a)$ is not in $R^{\mathcal{M}}$, so the current verifier Abelard loses, and Eloise wins.
7. All four plays that follow Eloise's strategy end with her win: two through step 3 and two through step 6.

So Eloise has a winning strategy, and by the equivalence theorem, $\mathcal{M} \models \varphi$, in agreement with Tarski's [[satisfaction|1WTCZB4DVB]].

## Remarks

The example shows the role exchange at $\neg$: the choice in $\neg \exists x$ belongs to Abelard, exactly as in the equivalent formula $\forall x \, \neg R(x, x)$.
Eloise has no move on the right branch; she wins because Abelard, as verifier, cannot find a loop.
In the structure with $R = \set{(0, 1), (1, 0), (1, 1)}$, Abelard wins by choosing the right conjunct and then $a = 1$, and $\varphi$ is false.

## Explanations

### L1 human

The formula says "everyone is related to someone, and no one is related to themselves".
Abelard can attack either half.
If he attacks the first half, Eloise answers with the other point.
If he attacks the second half, he must now find a point related to itself, and there is none.

### L2 human

We play the right branch with the extra loop $(1, 1)$ in $R$.

1. Abelard chooses the right conjunct; at $\neg$ he becomes the verifier of $\exists x \, R(x, x)$.
2. He picks $a = 1$, and $(1, 1) \in R$, so the verifier Abelard wins.

The typical use is to compute truth values of formulas with negations in the game style.
A trap is to let Eloise keep the verifier role after $\neg$; then she would be the one to pick $x$, and the game would compute the wrong value.
