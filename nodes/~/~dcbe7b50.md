---
tag: ~dcbe7b50
kind: proof
name: Proof of the Beth definability theorem from Craig interpolation
aliases: [proof-of-beth-definability-via-craig]
msc: ["03C40"]
topics: [JYJHB4YBAH]
audience: grad
proves: RJBDSA2ETP
uses: [E2CBFNAVZY, 1NR3HAWG9D, EY20BF96SJ, 92SWXST1ZM, 1HK0VYWTV7]
methods: [0NTF6DMVAP, TFQ1845T84]
sources:
  - book: isbn:9780521587136
---

## Proof

**Explicit implies implicit.**
Let $T \models \forall \bar x \, (P(\bar x) \leftrightarrow \varphi(\bar x))$ with $\varphi$ an $L$-formula.
If $(\mathcal{M}, P_1)$ and $(\mathcal{M}, P_2)$ are models of $T$, then $P_1$ and $P_2$ both equal the set defined by $\varphi$ in $\mathcal{M}$.
This also proves part 2, Padoa's method.

**Implicit implies explicit.**

1. Let $P'$ be a new $n$-ary relation symbol, and let $T'$ be $T$ with $P$ replaced by $P'$ everywhere.
2. Claim: $T \cup T' \models \forall \bar x \, (P(\bar x) \rightarrow P'(\bar x))$. Let $\mathcal{N} \models T \cup T'$. The [[reduct|EY20BF96SJ]] of $\mathcal{N}$ to $L \cup \set{P}$ is a model of $T$, and so is the structure $\mathcal{N}'$ obtained from the reduct to $L \cup \set{P'}$ by reading $P'$ as $P$.
3. These two models of $T$ have the same domain and the same $L$-part, so $P^{\mathcal{N}} = P'^{\mathcal{N}}$ by implicit definability, and the claim holds in $\mathcal{N}$.
4. Let $c_1, \dots, c_n$ be new constants. Then $T \cup T' \models P(\bar c) \rightarrow P'(\bar c)$.
5. By the [[compactness theorem|1NR3HAWG9D]], finitely many sentences of $T \cup T'$ suffice. Let $\tau$ be the conjunction of the sentences of $T$ among them and of the sentences of $T$ whose copies are among them, and let $\tau'$ be the copy of $\tau$. Then $\tau \wedge \tau' \models P(\bar c) \rightarrow P'(\bar c)$.
6. Rearranging, $\tau \wedge P(\bar c) \models \tau' \rightarrow P'(\bar c)$. The left side uses symbols from $L \cup \set{P, \bar c}$ and the right side symbols from $L \cup \set{P', \bar c}$.
7. By [[Craig's interpolation theorem|E2CBFNAVZY]], there is a sentence $\theta$ whose non-logical symbols lie in $L \cup \set{\bar c}$, with $\tau \wedge P(\bar c) \models \theta$ and $\theta \models \tau' \rightarrow P'(\bar c)$.
8. Renaming $P'$ as $P$ preserves [[logical consequence|1HK0VYWTV7]], and $\theta$ does not contain $P'$. So $\theta \models \tau \rightarrow P(\bar c)$.
9. Steps 7 and 8 give $\tau \models P(\bar c) \leftrightarrow \theta$, so $T \models P(\bar c) \leftrightarrow \theta$.
10. Write $\theta$ as $\varphi(\bar c)$, where $\varphi(\bar x)$ is an $L$-formula. The constants $\bar c$ do not occur in $T$, so a model of $T$ satisfies $P(\bar a) \leftrightarrow \varphi(\bar a)$ for every tuple $\bar a$, by interpreting $\bar c$ as $\bar a$.
11. Hence $T \models \forall \bar x \, (P(\bar x) \leftrightarrow \varphi(\bar x))$, and $\varphi$ explicitly defines $P$.

## Idea

Implicit definability says that a copy $P'$ of $P$, constrained by a copy of $T$, must agree with $P$.
This is a consequence from a sentence about $P$ to a sentence about $P'$, and the interpolant between the two sides can only speak about the old symbols.
That interpolant is the explicit definition.

## Variants

- Robinson's [[joint consistency theorem|R6AN38DNBD]] gives a proof without interpolation: if no $L$-formula works, one builds two models of $T$ with a common $L$-part that disagree on $P$.
- A third proof uses [[saturated models|RMTZ5J64FX]] in place of interpolation.
- The same argument, with several copies of the new symbols, handles theories that implicitly define several symbols at once.
