---
tag: CSFEP56A7D
kind: concept
name: Conflicting conventions
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: ug1
uses: [QKEX4PD029, 0MWKJ44V5A, 0BJR9QR08E, 0A7KV2WB7A, 0J2WAR83WP, 01AHG4G9RT, 04DXAFN2ES]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_number
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Subset
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Inverse_function
    locator: Notation
  - url: https://en.wikipedia.org/wiki/Logarithm
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Sign_(mathematics)
    locator: Terminology for signs
---

## Summary

Some symbols and words have two meanings, each used by a large group of careful authors, and a sentence can be true under one meaning and false under the other.
"The floor function $x \mapsto \lfloor x \rfloor$ is increasing" is true in one book and false in another, and neither book has made a mistake.

A *convention* is a choice of meaning for a symbol or a word that mathematicians fix by agreement, not by proof.
Two conventions *conflict* when different groups of authors give the same symbol or word different meanings, each consistent in itself.
The standard conflicts concern whether $0$ is a natural number, whether $\subset$ allows equality, whether "increasing" and "positive" are strict, what $f^{-1}$, $f^2$ and $\sin^{-1} x$ mean, which base $\log$ has, and how to bracket an open interval.

## Motivation

Go back to the floor function.
Under the weak reading, "increasing" means $x \le y \Rightarrow f(x) \le f(y)$, and the floor function passes.
Under the strict reading, it means $x < y \Rightarrow f(x) < f(y)$, and the floor function fails, since
$$0.1 < 0.2 \quad \text{but} \quad \lfloor 0.1 \rfloor = \lfloor 0.2 \rfloor = 0.$$
No proof can decide between the two meanings, because each one is a definition.

So a careful text states its conventions, usually in a preface or a list of notation, and a careful reader checks them before quoting a theorem from another text.
When a book states nothing, the first use often tells you: a book that writes "strictly increasing" somewhere uses the weak reading for "increasing".
The conflicts here are small, but they cause many off-by-one errors and wrong citations.
[[Abuse of notation|JV68YRB5YZ]] treats a different thing: shortcuts that all readers expand in the same way.

## Notation

The pages of this site use one option for each conflict, and they follow Mathlib where Mathlib makes a choice.
A page that uses another option says so.

| Item | Reading A | Reading B | This site |
|---|---|---|---|
| $\mathbb{N}$ | $\{0, 1, 2, \ldots\}$ | $\{1, 2, 3, \ldots\}$ | A; positive integers are $\mathbb{Z}_{>0}$ |
| $A \subset B$ | allows $A = B$ | proper subset only | $\subseteq$ and $\subsetneq$, never bare $\subset$ |
| increasing | $x \le y \Rightarrow f(x) \le f(y)$ | $x < y \Rightarrow f(x) < f(y)$ | A; B is "strictly increasing" |
| positive | $x > 0$ | $x \ge 0$ | A; "nonnegative" for $x \ge 0$ |
| $f^2(x)$ | $(f(x))^2$ | $f(f(x))$ | A for $\sin$, $\cos$, $\log$; B is $f \circ f$ |
| $\sin^{-1} x$ | $\arcsin x$ | $1 / \sin x$ | neither; we write $\arcsin x$ |
| $\log x$ | base $e$ | base $10$ or $2$ | A; $\log_b x$ for other bases |
| open interval | $(a, b)$ | $]a, b[$ | A |
| countable | finite or countably infinite | countably infinite only | A |
| $0^0$ | $1$ | undefined | A |

## Remarks

### Zero and the natural numbers

Is $0$ a [[natural number|0MWKJ44V5A]]?
Logic, set theory, computer science, the standard ISO 80000-2 and Mathlib say yes.
Many books in number theory and analysis say no.
The choice changes counts:
$$\{n \in \mathbb{N} : n < 5\} = \{0, 1, 2, 3, 4\} \quad \text{or} \quad \{1, 2, 3, 4\},$$
so the set has $5$ elements under reading A and $4$ under reading B.
[[The two conventions for the natural numbers|373G4N3P6R]] shows a sentence that changes its truth value as well.

To tell which reading a book uses, look for the induction principle: a book that starts induction at $0$ by default uses reading A.
Notations such as $\mathbb{N}_0$, $\mathbb{N}^*$, $\mathbb{Z}_{\ge 0}$ and $\mathbb{Z}_{>0}$ are also signals.
A book that writes $\mathbb{N}_0$ for $\{0, 1, 2, \ldots\}$ uses reading B for $\mathbb{N}$.

### Subset, increasing and positive

Three order words have a weak and a strict reading.
With $A = B = \{1\}$, the sentence "$A \subset B$" is true if $\subset$ allows equality and false if $\subset$ means a proper [[subset|0BJR9QR08E]].
A book that also uses $\subsetneq$ reads $\subset$ as "subset", and a book that also uses $\subseteq$ usually reads $\subset$ as "proper subset".

The word "increasing" for a [[monotone function|0A7KV2WB7A]] works the same way, as the floor function showed.
A book with the term "nondecreasing" reads "increasing" as strict, and a book with "strictly increasing" reads it as weak.
The two readings agree on [[injective|09NWETVTNY]] functions: if $x < y$ gives $f(x) \le f(y)$ and $f(x) \ne f(y)$, then $f(x) < f(y)$.

"Positive" means $x > 0$ in English texts, while the French "positif" means $x \ge 0$ and "strictement positif" means $x > 0$.
So "$0$ is positive" is false in English and true in a French book.
English texts write "nonnegative" for $x \ge 0$, and that word is the signal.

### Inverse signs and powers

Take $f(x) = x^2$ on $\mathbb{R}$, which has no [[inverse function|0J2WAR83WP]], since $f(2) = f(-2) = 4$.
A book still writes $f^{-1}([1, 4])$, and it means the [[preimage|01AHG4G9RT]], the set of $x$ with $f(x) \in [1, 4]$:
$$f^{-1}([1, 4]) = [-2, -1] \cup [1, 2].$$
The preimage is defined for every function and every set, so the sign $f^{-1}$ in front of a set never claims that $f$ is invertible.
Applied to a number, $f^{-1}(y)$ needs a bijection, and then $f^{-1}(\{y\}) = \{f^{-1}(y)\}$.

The exponent on a function name is a true conflict.
By the pattern of $\sin^2 x = (\sin x)^2$, the sign $\sin^{-1} x$ would be $\frac{1}{\sin x}$, but most books and calculators read it as $\arcsin x$.
At $x = \tfrac{1}{2}$ the readings differ:
$$\arcsin \tfrac{1}{2} = \tfrac{\pi}{6} \approx 0.524, \qquad \frac{1}{\sin \tfrac{1}{2}} \approx 2.086.$$
In dynamics, $f^2$ means $f \circ f$, and for $f(x) = x + 1$ the two readings give $f(f(3)) = 5$ and $(f(3))^2 = 16$.
A book that speaks of iterates or fixed points uses $f^2 = f \circ f$.

### Logarithms, intervals and other small conflicts

The sign $\log 8$ is about $2.079$ with base $e$, about $0.903$ with base $10$ and exactly $3$ with base $2$, as [[the value of log 8 under three conventions|AT3Y92P9RK]] works out.
Pure mathematics uses base $e$ (the [[natural logarithm|04DXAFN2ES]]), school and engineering texts often use base $10$, and computer science often uses base $2$.
To tell, look at a calculus formula: a book that writes $\frac{d}{dx} \log x = \frac{1}{x}$ uses base $e$, and a book that also writes $\ln$ usually means base $10$ by $\log$.
Statements up to a constant factor, such as $\log_2 n = O(\log n)$ in [[big O notation|0TGV80E6A4]], do not depend on the base, because $\log_b x = \frac{\ln x}{\ln b}$.

The open interval from $a$ to $b$ is $(a, b)$ in English texts and often $]a, b[$ in French texts.
The bracket form avoids a clash with the ordered pair $(a, b)$.
"Countable" means finite or countably infinite in some books and countably infinite only in others, and the phrase "at most countable" signals the second reading.
Combinatorics and algebra set $0^0 = 1$, so that $x^0 = 1$ for every $x$ and the binomial theorem holds at $x = 0$, while analysis often calls $0^0$ an indeterminate form of limits.

### What is not a conflict

[[The expression 2 + 3 · 4 has one value under every convention|5RERQ21MAF]].
Every standard source gives multiplication precedence over addition, so the value $14$ never depends on the book.
The same expression with a slash and juxtaposition, $6/2(1 + 2)$, is a real conflict, and careful authors add brackets.

Two names for one meaning are not a conflict either.
The signs $\mathbb{N}_0$ and $\mathbb{Z}_{\ge 0}$ both denote $\{0, 1, 2, \ldots\}$, and no sentence changes its truth value when you swap them.
A conflict needs one sign with two meanings, not two signs with one meaning.

### Watch out

The first trap is to quote a theorem across conventions.
A book with $0 \notin \mathbb{N}$ proves "for every $n \in \mathbb{N}$, $2^{n-1}$ is an integer", and a reader with $0 \in \mathbb{N}$ applies it at $n = 0$, where $2^{-1} = \tfrac{1}{2}$.
The fix is to translate first: the theorem is about $\mathbb{Z}_{>0}$.

The second trap is to read $\sin^{-1} x$ as $\frac{1}{\sin x}$, which at $x = \tfrac{1}{2}$ turns $0.524$ into $2.086$.
The third trap is to read $f^{-1}(B)$ as a claim that $f$ has an inverse.
For $f(x) = x^2$ the preimage $f^{-1}(\{4\}) = \{-2, 2\}$ exists, though $f^{-1}(4)$ as a number does not.

### History

The standard ISO 80000-2, first published in 2009 and revised in 2019, includes $0$ in $\mathbb{N}$.
It recommends $\ln$, $\lg$ and $\operatorname{lb}$ for the logarithms to the bases $e$, $10$ and $2$, which removes the conflict for readers who follow it.
The history of each symbol belongs to the history of mathematical notation.

### Try it

First, is $x \mapsto x^3$ increasing in the weak sense, the strict sense, or both?
Both: if $x < y$ then $y^3 - x^3 = (y - x)(x^2 + xy + y^2) > 0$, since $x^2 + xy + y^2 > 0$ when $x$ and $y$ are not both $0$.

Second, with $f(x) = x^2$, compute $f^{-1}(\{9\})$ and $f^{-1}(\{-1\})$.
The first is $\{-3, 3\}$, and the second is the empty set, since no real square is negative.

## Explanations

### L1 human

Mathematicians agree on most symbols, but not on all of them.
For example, some books count $0$ as a natural number and some do not.
Neither group is wrong, because each one uses the word in its own fixed way.
If a book says "there are $5$ natural numbers below $5$", it counts $0, 1, 2, 3, 4$.
A book of the other kind counts only $1, 2, 3, 4$, which is $4$ numbers.
So before we use a fact from a book, we check what its words mean.

### L2 human

Book X uses $\mathbb{N} = \{1, 2, 3, \ldots\}$ and states three facts about every $n \in \mathbb{N}$.
We translate each one into the notation of this site, where the set is $\mathbb{Z}_{>0}$, and test the extra case $n = 0$.

The first fact is $2^n \ge n + 1$.
At $n = 0$ it reads $2^0 = 1 \ge 1$, so it still holds when $0$ joins the set.
The second fact is "$2^{n-1}$ is an integer", and at $n = 0$ it fails, since $2^{-1} = \tfrac{1}{2}$.
The third fact is $n \ge 1$, which is true in book X and false at $n = 0$.

So some statements survive the change of convention and some do not, and only a check of the extra case tells you which.
Watch out: a statement that survives can still have a proof that uses $n \ge 1$, so the proof needs a check for $n = 0$ as well.

### L3 human

Conventions are choices of definition, and the content of a theorem does not change once the definitions are translated.
A proof assistant makes the translation explicit.
Mathlib has $\mathbb{N}$ with $0$, the type `ℕ+` of positive natural numbers, `Monotone` and `StrictMono` for the two readings of "increasing", and `⊆` and `⊂` with `⊂` strict.
Mathlib also makes some partial operations total by "junk values": $x / 0 = 0$, subtraction on $\mathbb{N}$ gives $3 - 5 = 0$, the real square root of a negative number is $0$, and $\log 0 = 0$.
These values never make a false theorem true, because each theorem that needs a nonzero divisor states that hypothesis.

Larger conflicts of the same kind appear in later areas.
Authors differ on whether a ring has a unit element, whether a compact space must be Hausdorff, and whether a field is commutative.
Each choice changes the scope of the theorems, and the pages of those areas state the option they use.
