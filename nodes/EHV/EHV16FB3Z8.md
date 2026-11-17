---
tag: EHV16FB3Z8
kind: example
name: The language of words a^n b^n is not definable in monadic second-order logic
msc: ["03B16", "03D05", "68Q45"]
topics: [MDHDYV8QZW]
audience: grad
not_instance_of:
  - target: 3WHQFSHR58
    note: no sentence of monadic second-order logic over words defines the language of the words a^n b^n with n at least 1, because this language is not regular
uses: [3WHQFSHR58, 18WVBDCS38, CBR9WAGZGZ, 1P6EP01HZF]
sources:
  - url: https://en.wikipedia.org/wiki/Büchi–Elgot–Trakhtenbrot_theorem
    locator: Theorem statement
  - url: https://en.wikipedia.org/wiki/Pumping_lemma_for_regular_languages
    locator: lead section
---

## Example

Let $\Sigma = \set{a, b}$, and let $L = \set{a^n b^n : n \geq 1}$ be the language of the [[strings|1P6EP01HZF]] with a block of $a$'s followed by a block of $b$'s of the same length.
We read words as structures with the order $<$ and the letter predicates $P_a$, $P_b$, as in [[monadic second-order logic|3WHQFSHR58]].
We show that no MSO sentence $\varphi$ satisfies $w \models \varphi \iff w \in L$ for all nonempty words $w$.

1. Suppose that such a sentence $\varphi$ exists.
2. By the Büchi-Elgot-Trakhtenbrot theorem, every MSO-definable language of words is [[regular|18WVBDCS38]]. So $L$ is regular.
3. Let $p \geq 1$ be the constant of the [[pumping lemma|CBR9WAGZGZ]] for $L$, and take $w = a^p b^p \in L$, of length $2p \geq p$.
4. The pumping lemma gives $w = xyz$ with $|xy| \leq p$, $|y| \geq 1$, and $x y^i z \in L$ for every $i \geq 0$.
5. Since $|xy| \leq p$ and the first $p$ letters of $w$ are $a$'s, the piece $y$ is $a^j$ for some $j \geq 1$.
6. Then $x y^2 z = a^{p + j} b^p$. It has more $a$'s than $b$'s, so it is not in $L$, which contradicts step 4.
7. So $L$ is not regular, and by step 2 no MSO sentence defines $L$.

## Remarks

The example shows the limit of MSO on words: it cannot compare the sizes of two unbounded blocks.
Half of the definition of $L$ is still first-order.
The sentence $\neg \exists x \exists y\, (x < y \land P_b(x) \land P_a(y))$ says that no $b$ comes before an $a$, and $\exists x\, P_a(x) \land \exists x\, P_b(x)$ says that both letters occur.
These define the regular language $a^+ b^+$, and only the equality of the two lengths is out of reach.

Full second-order logic can define $L$, because it can quantify over binary relations.
The existential sentence "there is a binary relation $F$ that is a bijection from the positions with $a$ onto the positions with $b$", together with the first-order part above, defines $L$.
So $L$ separates MSO from existential second-order logic on words.

The proof changes little when the language changes.
For $\set{a^n b^m : n \leq m}$ the same word $a^p b^p$ and $i = 2$ work.
For $\set{a^n b^m : n \geq m}$ we pump down with $i = 0$ and get $a^{p - j} b^p$, which is not in the language.

## Explanations

### L1 human

Monadic second-order logic on words can only check what a machine with a fixed, finite memory can check.
To decide whether a word has as many $a$'s as $b$'s, a machine must remember how many $a$'s it has read.
With $100$ states it cannot tell $a^{200}$ from some other long block of $a$'s, so it confuses $a^{200} b^{200}$ with a word that has a different number of $a$'s.
So no sentence of this logic describes exactly the words $ab$, $aabb$, $aaabbb$, and so on.

### L2 human

We look at the same failure through finite automata.

1. A machine that checks "only $a$'s, then only $b$'s" needs three states: reading $a$'s, reading $b$'s, and rejected.
2. It accepts $ab$ and $aabb$, but it also accepts $aab$, which is not in $L$.
3. To reject $aab$, the machine must remember that it read two $a$'s, and for $a^n b^n$ it must remember $n$.
4. A machine with $k$ states cannot remember $k + 1$ different counts. This is the pumping argument of the example.

The typical use of this non-example is a test of a claim that MSO can express some counting property on words: first ask whether the property is regular.
A trap is to think that MSO fails here because the formula would be long.
The failure is not about length: no formula of any length works.
