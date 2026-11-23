---
tag: WSHWNR803P
kind: example
name: A model where the de dicto formula holds and the de re formula fails
msc: ["03B45"]
topics: [SPQVNPZDTB]
audience: research
instance_of: [D2H3S12V7X]
uses: [D2H3S12V7X, VC3A2VWXND]
sources:
  - url: https://en.wikipedia.org/wiki/Barcan_formula
    locator: lead section
---

## Example

We give a Kripke model with domains for [[quantified modal logic|D2H3S12V7X]] in which $\square \exists x P x$ is true at a world and $\exists x \square P x$ is false there.
Let $\mathfrak{M} = (W, R, D, I)$ with $W = \{w, v\}$ and $R = W \times W$, so that $(W, R)$ is a frame of [[S5|VC3A2VWXND]].
Take the constant domain $D(w) = D(v) = \{a, b\}$, and let $I(P, w) = \{a\}$ and $I(P, v) = \{b\}$.

First we check $\square \exists x P x$ at $w$.

1. The worlds that $w$ sees are $w$ and $v$.
2. At $w$, the object $a$ lies in $D(w)$ and in $I(P, w)$, so $\mathfrak{M}, w \models \exists x P x$.
3. At $v$, the object $b$ lies in $D(v)$ and in $I(P, v)$, so $\mathfrak{M}, v \models \exists x P x$.
4. By steps 1 to 3, $\mathfrak{M}, w \models \square \exists x P x$.

Then we check that $\exists x \square P x$ fails at $w$.

5. The candidates for $x$ are the elements of $D(w) = \{a, b\}$.
6. For $x \mapsto a$: $w R v$ and $a \notin I(P, v)$, so $\square P x$ fails at $w$.
7. For $x \mapsto b$: $w R w$ and $b \notin I(P, w)$, so $\square P x$ fails at $w$.
8. No candidate works, so $\mathfrak{M}, w \not\models \exists x \square P x$.

## Remarks

The example shows that the de dicto formula $\square \exists x P x$ does not imply the de re formula $\exists x \square P x$, even in $\mathsf{S5}$ with a constant domain.
The witness may change from world to world, and that is all the de dicto formula asks.

The converse implication $\exists x \square P x \to \square \exists x P x$ is valid on every frame with increasing domains.
A witness $d$ for $\square P x$ at $w$ still exists at each successor, by the domain condition, and it serves as a witness there.
If we change $I(P, v)$ to $\{a, b\}$, then $a$ becomes a witness for $\exists x \square P x$ at $w$, and both formulas hold.

## Explanations

### L1 human

Think of $P$ as "wins the game", in two possible worlds.
In world $w$ the player $a$ wins, and in world $v$ the player $b$ wins.
In every world somebody wins, so "necessarily somebody wins" is true.
But no single player wins in both worlds, so "somebody necessarily wins" is false.

### L2 human

We check the converse implication in the changed model, with $I(P, v) = \{a, b\}$ and the rest as before.
Under $x \mapsto a$, the object $a$ lies in $I(P, w)$ and in $I(P, v)$, so $\square P x$ holds at $w$.
So $w \models \exists x \square P x$, with the witness $a$.
At each world $u$ that $w$ sees, $a$ lies in $D(u)$ and in $I(P, u)$, so $u \models \exists x P x$, and $w \models \square \exists x P x$.
The typical use of the original model is to refute the inference from de dicto to de re.
Watch out: the step "$a$ lies in $D(u)$" needs the domain condition, and here it holds because the domain is constant.
