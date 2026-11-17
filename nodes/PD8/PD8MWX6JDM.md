---
tag: PD8MWX6JDM
kind: example
name: Words of even length in monadic second-order logic
msc: ["03B16", "03D05", "68Q45"]
topics: [MDHDYV8QZW]
audience: grad
instance_of: [3WHQFSHR58]
uses: [3WHQFSHR58, 18WVBDCS38, W65B6BKZRY, 2RE7YAZK8R]
sources:
  - url: https://en.wikipedia.org/wiki/Büchi–Elgot–Trakhtenbrot_theorem
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Monadic_second-order_logic
    locator: lead section
---

## Example

We read a nonempty word $w = a_1 \cdots a_n$ over the alphabet $\set{a, b}$ as the structure with domain $\set{1, \ldots, n}$, the order $<$, and the letter predicates $P_a$, $P_b$.
We use three first-order abbreviations:
$$\mathrm{first}(x) := \neg \exists y\, (y < x), \qquad \mathrm{last}(x) := \neg \exists y\, (x < y),$$
$$S(x, y) := x < y \land \neg \exists z\, (x < z \land z < y).$$
The [[monadic second-order|3WHQFSHR58]] sentence is
$$\varphi_{\mathrm{even}} := \exists X \bigl( \forall x\, (\mathrm{first}(x) \to X(x)) \land \forall x\, (\mathrm{last}(x) \to \neg X(x)) \land \forall x \forall y\, (S(x, y) \to (X(x) \leftrightarrow \neg X(y))) \bigr).$$
We show that $w \models \varphi_{\mathrm{even}}$ if and only if $n$ is even.

1. In the structure of $w$, $\mathrm{first}(x)$ holds only at $x = 1$, $\mathrm{last}(x)$ holds only at $x = n$, and $S(x, y)$ holds exactly when $y = x + 1$.
2. Let $X$ satisfy the first and the third conjunct. Then $1 \in X$, and $i \in X$ if and only if $i + 1 \notin X$, for $1 \leq i < n$.
3. By induction on $i$, step 2 gives $i \in X$ if and only if $i$ is odd. So $X$ is the set of odd positions, and no other set satisfies these two conjuncts.
4. The second conjunct asks that $n \notin X$. By step 3, this holds if and only if $n$ is even.
5. If $n$ is even, the set of odd positions satisfies all three conjuncts, so $w \models \varphi_{\mathrm{even}}$.
6. If $n$ is odd, the only candidate from step 3 contains $n$, so the second conjunct fails, and $w \not\models \varphi_{\mathrm{even}}$.

For example, $w = abab$ has $n = 4$ and $X = \set{1, 3}$, and $w = aba$ has $n = 3$, where the forced set $\set{1, 3}$ contains the last position.

## Remarks

The sentence does not mention the letters, so the language it defines is the set of all nonempty words of even length.
This language is [[regular|18WVBDCS38]]: a [[deterministic finite automaton|W65B6BKZRY]] with two states, "even" and "odd", recognises it, as the Büchi-Elgot-Trakhtenbrot theorem predicts.

No first-order sentence over $<$ and the letter predicates defines the same language.
For words over one letter, an [[Ehrenfeucht-Fraïssé game|2RE7YAZK8R]] argument shows that first-order sentences of quantifier rank $k$ cannot distinguish two finite linear orders with at least $2^k$ elements each.
So the set quantifier $\exists X$ is necessary here.

The idea changes with the parameter.
For "the length is divisible by $m$", we guess $m$ sets $X_0, \ldots, X_{m-1}$ that partition the positions.
We ask that the first position lies in $X_0$, and that the successor of a position in $X_j$ lies in $X_{j+1 \bmod m}$.
Then position $i$ lies in $X_{(i - 1) \bmod m}$, and $m$ divides $n$ exactly when the last position lies in $X_{m-1}$.

## Explanations

### L1 human

We want to check that a word has an even number of letters without counting to the end.
We put a mark on the first letter, no mark on the second, a mark on the third, and so on.
The word has even length exactly when the last letter has no mark.
For "abab" the marks fall on letters 1 and 3, and letter 4 is unmarked, so the length is even.
The logic can say "there is a way to place the marks", and this is the set quantifier.

### L2 human

We check the sentence on the word $w = abba$ of length $4$.

1. The first conjunct forces $1 \in X$.
2. The third conjunct with $S(1, 2)$ gives $2 \notin X$, with $S(2, 3)$ gives $3 \in X$, and with $S(3, 4)$ gives $4 \notin X$.
3. The second conjunct asks $4 \notin X$, and step 2 gives exactly this.
4. So $X = \set{1, 3}$ is a witness, and $w \models \varphi_{\mathrm{even}}$.

The typical use is a translation of a finite automaton into MSO: one set for each state, chosen as the set of positions where the run is in that state.
Here the set $X$ is the state "odd length so far", counted after reading each position.
A trap is to drop the first conjunct.
Then the set of even positions satisfies the other two conjuncts on every word of odd length, and the sentence holds for all nonempty words.
