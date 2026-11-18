---
tag: RBTX5HWXBB
kind: example
name: The Barcan formula fails on an S4 model with growing domains
msc: ["03B45"]
topics: [SPQVNPZDTB]
audience: research
not_instance_of:
  - target: 9PYDNBA5X4
    note: the frame is reflexive and transitive but a new object appears along R, so the domains do not decrease and the instance of the Barcan formula with P x fails at w
uses: [9PYDNBA5X4, D2H3S12V7X, 0X8NMST0J2, 0GJZW9JFZQ]
sources:
  - url: https://en.wikipedia.org/wiki/Barcan_formula
    locator: The Barcan formula
---

## Example

Let $\mathfrak{M} = (W, R, D, I)$ be the Kripke model with domains given by:

- $W = \{w, v\}$ and $R = \{(w, w), (w, v), (v, v)\}$;
- $D(w) = \{1\}$ and $D(v) = \{1, 2\}$;
- $I(P, w) = I(P, v) = \{1\}$.

We check that $(W, R)$ is a frame of $\mathsf{S4}$, that the domains do not decrease, and that the [[Barcan formula|9PYDNBA5X4]] fails at $w$.

1. $R$ contains $(w, w)$ and $(v, v)$, so $R$ is [[reflexive|0X8NMST0J2]].
2. The chains $a R b R c$ in $R$ are $w R w R w$, $w R w R v$, $w R v R v$ and $v R v R v$. In each chain $a R c$ holds, so $R$ is [[transitive|0GJZW9JFZQ]].
3. $w R v$ and $D(v) = \{1, 2\} \not\subseteq \{1\} = D(w)$. So the domains do not decrease. They increase, since $D(w) \subseteq D(v)$.
4. At $w$, $\forall x \square P x$ needs $\square P x$ under $x \mapsto 1$ only, since $D(w) = \{1\}$.
5. The successors of $w$ are $w$ and $v$, and $1 \in I(P, w)$ and $1 \in I(P, v)$. So $\mathfrak{M}, w \models \forall x \square P x$.
6. At $w$, $\square \forall x P x$ needs $\forall x P x$ at $v$. But $2 \in D(v)$ and $2 \notin I(P, v)$, so $\mathfrak{M}, v \not\models \forall x P x$.
7. So $\mathfrak{M}, w \not\models \square \forall x P x$, and by step 5 the instance $\forall x \square P x \to \square \forall x P x$ fails at $w$.

## Remarks

The new object $2$ at $v$ is the whole reason for the failure.
The antecedent at $w$ speaks only about the object $1$, and so it says nothing about $2$.
The model is a model of $\mathsf{QS4}$ in the semantics where formulas at $w$ are evaluated under assignments into $D(w)$, because the domains increase.
So BF is not a theorem of $\mathsf{QS4}$.
The frame is not symmetric: $w R v$ holds and $v R w$ does not.
If we add $(v, w)$ to $R$, the frame becomes an $\mathsf{S5}$ frame, and then the domain condition of $\mathsf{QS5}$ would force $D(w) = D(v)$.
If we instead change $D(v)$ to $\{1\}$, the domains are constant, and the instance holds at $w$.

## Explanations

### L1 human

World $w$ has one object, and world $v$, a possible future of $w$, has two objects.
The object $1$ is $P$ in both worlds, so "everything now is necessarily $P$" is true at $w$.
The new object $2$ in $v$ is not $P$, so "necessarily everything is $P$" is false at $w$.
The Barcan formula fails because a new object appears.

### L2 human

We check that the converse Barcan formula still holds at $w$ for the same predicate.

1. The converse is $\square \forall x P x \to \forall x \square P x$.
2. By step 6, the antecedent $\square \forall x P x$ is false at $w$, so the instance holds at $w$.
3. At $v$, the only successor is $v$. The antecedent needs $\forall x P x$ at $v$, which fails by step 6, so the instance holds at $v$ too.

The typical use of this model is to show that BF is independent of $\mathsf{QS4}$.
A trap: the failure needs a world that is seen from $w$; a new object at a world that $w$ does not see would not matter.
