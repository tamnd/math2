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

Let $\mathcal{M}$ have domain $\{0, 1\}$ and $R^{\mathcal{M}} = \{(0, 1), (1, 0)\}$, and let
$$\varphi = \forall x \, \exists y \, R(x, y) \wedge \neg \exists x \, R(x, x).$$
We list every play of the [[evaluation game|D45Z7HETDA]] $G(\mathcal{M}, \varphi)$ in which Eloise follows one fixed strategy, and we check that she wins them all.

1. At $\wedge$, Abelard, the falsifier, chooses a conjunct.
2. If he chooses the left conjunct $\forall x \, \exists y \, R(x, y)$, he picks some $a \in \{0, 1\}$, and then Eloise picks $b$.
3. Eloise's strategy is $b = 1 - a$.
   The play ends at $R(x, y)$ with $(a, 1 - a) \in R^{\mathcal{M}}$, so Eloise, the verifier, wins.
4. If he chooses the right conjunct $\neg \exists x \, R(x, x)$, the roles exchange at $\neg$, and Abelard becomes the verifier of $\exists x \, R(x, x)$.
5. At $\exists x$ the current verifier moves, so Abelard picks some $a \in \{0, 1\}$.
6. The play ends at $R(x, x)$ with $x \mapsto a$.
   The pair $(a, a)$ is not in $R^{\mathcal{M}}$, so the current verifier Abelard loses, and Eloise wins.
7. There are four plays in all, two through step 3 and two through step 6, and Eloise wins each of them.

So Eloise has a winning strategy, and by the [[equivalence theorem|G6MKG8YQ6M]] we get $\mathcal{M} \models \varphi$, in agreement with Tarski's [[satisfaction|1WTCZB4DVB]].

## Remarks

The example shows the role exchange at $\neg$.
The choice in $\neg \exists x$ belongs to Abelard, exactly as in the equivalent formula $\forall x \, \neg R(x, x)$.
On the right branch Eloise makes no move at all; she wins because Abelard, as verifier, cannot find a loop.

Change one pair and the answer changes.
With $R^{\mathcal{M}} = \{(0, 1), (1, 0), (1, 1)\}$, Abelard chooses the right conjunct and then $a = 1$, and $(1, 1) \in R^{\mathcal{M}}$, so the verifier Abelard wins and $\varphi$ is false.

## Explanations

### L1 human

The formula says "everyone is related to someone, and no one is related to themselves".
Abelard can attack either half.
If he attacks the first half, he names a point, and Eloise answers with the other point.
If he attacks the second half, the burden flips: now he must find a point related to itself, and there is none.

### L2 human

We play the right branch after adding the loop $(1, 1)$ to $R$.
Abelard chooses the right conjunct, and at $\neg$ he becomes the verifier of $\exists x \, R(x, x)$.
He picks $a = 1$, and since $(1, 1)$ is now in $R$, the atomic formula $R(1, 1)$ holds, so the verifier Abelard wins.
To compute a truth value in game style, keep track at each step of who the current verifier is.
Watch out: if Eloise kept the verifier role after $\neg$, she would pick $x$, and the game would compute the value of $\exists x \, \neg R(x, x)$ instead.
