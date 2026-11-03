---
tag: CBR9WAGZGZ
kind: statement
role: lemma
name: Pumping lemma for regular languages
msc: [68Q45]
uses: [18WVBDCS38, W65B6BKZRY, 1P6EP01HZF]
about: [18WVBDCS38]
sources:
  - url: https://en.wikipedia.org/wiki/Pumping_lemma_for_regular_languages
same_as:
  wikidata: Q2292874
  wikipedia: Pumping lemma for regular languages
---

## Statement

Let $L \subseteq \Sigma^*$ be a [[regular language|18WVBDCS38]].
Then there is an integer $p \ge 1$ such that every [[string|1P6EP01HZF]] $w \in L$ with length $\abs{w} \ge p$ can be written as $w = xyz$ with $x, y, z \in \Sigma^*$ and:

1. $\abs{y} \ge 1$;
2. $\abs{xy} \le p$;
3. $x y^i z \in L$ for every integer $i \ge 0$.

## Remarks

Take a [[DFA|W65B6BKZRY]] for $L$ and let $p$ be its number of states.
While reading the first $p$ letters of $w$, the automaton visits $p + 1$ states, so by the pigeonhole principle some state repeats.
Let $y$ be the nonempty piece read between the two visits; this loop can be skipped or repeated any number of times without changing the final state.
Example of use: suppose $\set{a^n b^n : n \ge 0}$ were regular with constant $p$, and take $w = a^p b^p$.
By clause 2 the piece $y$ lies inside the $a$'s, so $x y^2 z$ has more $a$'s than $b$'s, which is a contradiction.
The converse fails: there are non-regular languages that satisfy the conclusion, so the lemma can only show that a language is not regular.

## Explanations

### L1 human

A machine with $p$ states that reads a word longer than $p$ must pass through some state twice.
The letters read between the two visits form a loop, and the machine cannot tell how often the loop was taken.
So every long enough word of a regular language contains a piece that can be repeated, or removed, while staying in the language.

### L2 human

The lemma is the usual first tool for proving that a language is not regular.
One assumes regularity and picks a clever word of length at least $p$.
Then one shows that every allowed split leads to a pumped word outside the language.
It is often combined with [[closure properties|446KZ8HJ5F]] to reduce a hard case to a known one.
Since the condition is only necessary, the [[Myhill–Nerode theorem|96BRMR4P3N]], which gives a characterization, is needed in some cases.
A similar pumping lemma holds for context-free languages, with two pumped pieces.
