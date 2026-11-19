---
tag: 8BKRJ0KPVD
kind: example
name: The two-point countermodel to excluded middle and Peirce's law
msc: ["03B20"]
topics: [38EQ20GR7M]
audience: grad
instance_of: [35VKJY77TY]
uses: [5GTQ69W47T, 480TCT5CJ9, 0RYYK8PG4S, GMSZ75D5WE, 0NFAGWH84K]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Semantics of intuitionistic logic
  - url: https://en.wikipedia.org/wiki/Intuitionistic_logic
    locator: Kripke semantics
---

## Example

Let $W = \set{u, v}$ with $u \leq v$, and let $V(p) = \set{v}$ and $V(q) = \emptyset$.
Both sets are up-sets, so this is an [[intuitionistic Kripke model|5GTQ69W47T]].

1. $u \nVdash p$, since $u \notin V(p)$. And $v \Vdash p$.
2. $u \nVdash \neg p$, since $v \geq u$ and $v \Vdash p$. Also $v \nVdash \neg p$.
3. So $u \nVdash p \vee \neg p$: the [[law of excluded middle|0RYYK8PG4S]] fails at $u$.
4. No world forces $\neg p$, by step 2. So every world forces $\neg\neg p$, in particular $u \Vdash \neg\neg p$.
5. With step 1, $u \nVdash \neg\neg p \to p$: [[double negation elimination|0NFAGWH84K]] fails at $u$.
6. $u \nVdash p \to q$ and $v \nVdash p \to q$, since $v$ forces $p$ and not $q$.
7. So no world forces $p \to q$, and $u \Vdash (p \to q) \to p$ holds vacuously.
8. With step 1, $u \nVdash ((p \to q) \to p) \to p$: [[Peirce's law|GMSZ75D5WE]] fails at $u$.
9. By [[soundness|480TCT5CJ9]], none of $p \vee \neg p$, $\neg\neg p \to p$ and $((p \to q) \to p) \to p$ is a theorem of $\mathsf{IPC}$.

## Remarks

The model is the smallest one that is not classical: a one-world model is a truth table and validates all classical laws.
The world $v$ alone forces all three laws, since it is a one-world model.
The same frame validates $\neg p \vee \neg\neg p$ and $(p \to q) \vee (q \to p)$, since it is a chain with a top element.
So the two-point chain is a frame of [[Gödel-Dummett logic|474SGS2N0X]], and it refutes no theorem of that logic.
Its logic is the logic of the three-element Heyting chain.

## Explanations

### L1 human

Picture two moments: today and tomorrow.
Today we do not know $p$, and tomorrow we will know $p$.
Today "$p$" is not known, and "not $p$" is not known either, since $p$ will become known.
So "$p$ or not $p$" is not known today.

### L2 human

1. List the up-sets of the frame: $\emptyset$, $\set{v}$ and $\set{u, v}$.
2. These are the possible truth sets, so the frame is a three-element Heyting chain $0 < \set{v} < 1$.
3. With $p = \set{v}$: $\neg p = \emptyset$ and $p \vee \neg p = \set{v} \neq 1$.
4. $\neg\neg p = \neg\emptyset = 1$, and $\neg\neg p \to p = \set{v} \neq 1$.

The typical use of this model is the first check of a formula that is classically valid: if it fails here, it is not intuitionistic.
A trap: the model does not refute $\neg p \vee \neg\neg p$; for that, a frame with two maximal worlds is needed.
