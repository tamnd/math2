---
tag: ~41feef1d
kind: example
name: The word "any" as "every" and as "some"
msc: ["97E40"]
topics: [WMY13MXY3W]
audience: ug1
instance_of: [~ea809f7c]
uses: [~ea809f7c, ~aec76a22, 0GHS47PDAQ, 0MSRQHCNN9]
sources:
  - url: https://en.wikipedia.org/wiki/Quantifier_(logic)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Ambiguity
    locator: lead section
---

## Example

The word "any" is a [[quantifier|~aec76a22]] whose meaning depends on the sentence.
We compare two sentences and show that "any" changes sense between them, an instance of [[ambiguity in mathematical language|~ea809f7c]].

1. Sentence A: "$x^2 \geq 0$ for any real $x$". Here "any" means "every". The statement is $\forall x \in \mathbb{R}, \, x^2 \geq 0$, and it is true.
2. Sentence B: "if $x^2 < 0$ for any real $x$, then the theory fails". Here "any" means "some". The hypothesis is $\exists x \in \mathbb{R}, \, x^2 < 0$.
3. Read B with "every" instead: "if $x^2 < 0$ for every real $x$, then the theory fails". The hypothesis is now much stronger.
4. The two readings of B are different statements. With "some", B claims that one bad $x$ breaks the theory. With "every", B claims this only when all $x$ are bad.
5. The pattern: "any" in a positive claim is a [[universal quantifier|0GHS47PDAQ]], and "any" after "if", "not" or in a question is often an [[existential quantifier|0MSRQHCNN9]].

## Remarks

The negation shows the same split.
"$f$ is not zero at any point" means "for every point $x$, $f(x) \neq 0$", which is "there is no point where $f$ is zero".
"$f$ is not zero at every point" means "there is a point where $f$ is not zero".
So "not any" and "not every" have different meanings, and replacing "any" by "every" in a negated sentence changes the claim.

The safe rule, which Paul Halmos also gave, is to write "every" or "some" and not "any".
Sentence A becomes "$x^2 \geq 0$ for every real $x$", and sentence B becomes "if $x^2 < 0$ for some real $x$, then the theory fails".

## Explanations

### L1 human

"Any child can join the club" means every child can join.
"Is any child here?" asks whether at least one child is here.
The same word "any" means "every" in the first sentence and "at least one" in the second.
In mathematics, "every" and "some" say each meaning without a doubt.

### L2 human

We rewrite three sentences with "any" in terms of "every" or "some".

1. "Any continuous function on $[0, 1]$ is bounded." This is a general claim, so "any" means "every". The rewrite is "every continuous function on $[0, 1]$ is bounded".
2. "If $f(x) > 1$ for any $x$ in $[0, 1]$, then $f$ is not bounded above by $1$." This is a hypothesis after "if", so "any" means "some". The rewrite is "if $f(x) > 1$ for some $x \in [0, 1]$, then $f$ is not bounded above by $1$".
3. "$f$ has no root in any interval of length $1$." This is a negation, and "no ... any" means "for every interval $I$ of length $1$, $f$ has no root in $I$".

The typical use of this rewriting is in reading a definition or a theorem that contains "any", before the proof starts.

A trap: in step 3, "any" is universal, but it sits inside a negation.
The negation of the whole sentence is "there is an interval of length $1$ that contains a root of $f$".
