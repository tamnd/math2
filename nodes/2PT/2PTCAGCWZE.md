---
tag: 2PTCAGCWZE
kind: concept
name: Glossary of mathematical symbols
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: school
uses: [QKEX4PD029]
sources:
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_symbols
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_symbols
    locator: Symbols that do not belong to formulas
  - url: https://en.wikipedia.org/wiki/ISO/IEC_80000
    locator: lead section
---

## Summary

Every mathematical symbol is a short name for a word or a phrase, and every formula can be read aloud as a sentence.
Take the formula
$$\{x \in \mathbb{R} : \lvert x - 1 \rvert < 2\} = (-1, 3).$$
Read aloud, it says: "the set of real numbers $x$ such that the absolute value of $x$ minus $1$ is less than $2$ equals the open interval from $-1$ to $3$."
Each mark has a reading, and only after you can say the sentence can you check whether it is true.

A glossary of mathematical symbols is a reference table that gives, for each common symbol, a reading aloud, its meaning, and a link to the node that defines the idea behind it.
The tables below sort the symbols by field and use the conventions of the site.
Where one sign has several meanings, the glossary lists them side by side and says how to tell them apart.

## Motivation

A new course brings new symbols, and a textbook defines each one only once, often many chapters before you need it again.
So you need one place where you can look up a sign, say it in words, and follow a link to its definition.
[[Mathematical notation|QKEX4PD029]] explains why the signs look the way they do, and the glossary is the dictionary that goes with it.

A second reason is conflict.
The sign $\equiv$ means "is congruent to" in number theory and "is identically equal to" in analysis.
The bars $\lvert \cdot \rvert$ give an absolute value, a number of elements or a determinant, depending on what is between them.
A reader who knows only one meaning will misread the other, so the glossary names each meaning and the clue that selects it.

## Notation

Each table has three columns: the symbol, a reading aloud, and the meaning with a link.
The letters $a, b, x, y$ stand for numbers, $A, B$ for sets, $f, g$ for functions, $P, Q$ for statements, and $n$ for a natural number.
The site writes $\subseteq$ for "is a subset of" and $\subsetneq$ for "is a proper subset of", counts $0$ as a natural number, and writes $\log$ for the natural logarithm.
[[Conflicting conventions|CSFEP56A7D]] gives the other options and the reasons for these choices.
The international standard ISO 80000-2 recommends signs and symbols for mathematics in the sciences, and most rows below agree with it.

## Remarks

### Reading a formula aloud

Go back to the formula of the Summary and check it.
The condition $\lvert x - 1 \rvert < 2$ says that the distance from $x$ to $1$ is less than $2$.
Remove the absolute value and add $1$ to each part:
$$\lvert x - 1 \rvert < 2 \iff -2 < x - 1 < 2 \iff -1 < x < 3.$$
So the set is the open interval $(-1, 3)$, and the formula is true.
Check: $x = 2.9$ gives $\lvert 1.9 \rvert < 2$, and $x = 3$ gives $\lvert 2 \rvert = 2$, which is not less than $2$.

The same habit works for every formula.
Find the main verb first: here it is $=$, "equals".
Then read each side as a noun phrase, from the outside in.
The tables give the words for each mark.

### Arithmetic and comparison

These are the signs of school arithmetic, with the readings that lectures use.

| Symbol | Reading | Meaning |
|---|---|---|
| $a + b$, $a - b$ | "$a$ plus $b$", "$a$ minus $b$" | sum and difference |
| $a \times b$, $a \cdot b$, $ab$ | "$a$ times $b$" | product |
| $a \div b$, $a / b$, $\frac{a}{b}$ | "$a$ divided by $b$", "$a$ over $b$" | quotient, for $b \neq 0$ |
| $\pm$ | "plus or minus" | two values, one with each sign |
| $a < b$, $a \leq b$ | "$a$ is less than $b$", "$a$ is less than or equal to $b$" | order of real numbers |
| $a > b$, $a \geq b$ | "$a$ is greater than $b$", "$a$ is at least $b$" | order of real numbers |
| $a^n$ | "$a$ to the power $n$" | the product of $n$ factors equal to $a$ |
| $\sqrt{a}$, $\sqrt[n]{a}$ | "the square root of $a$", "the $n$-th root of $a$" | the nonnegative [[square root|0F7FQS6XY6]], for $a \geq 0$ |
| $n!$ | "$n$ factorial" | the [[factorial|0XWG0JGDFW]] $1 \cdot 2 \cdots n$, with $0! = 1$ |
| $\lvert x \rvert$ | "the absolute value of $x$" | the [[absolute value|0FFXKTKKQC]] |
| $\lfloor x \rfloor$, $\lceil x \rceil$ | "the floor of $x$", "the ceiling of $x$" | the [[floor function|08GR54CKEA]] and the ceiling function |

### Equality and related relations

Several signs look like $=$ and say less than equality, or something else.

| Symbol | Reading | Meaning |
|---|---|---|
| $a = b$ | "$a$ equals $b$" | [[equality|E918704SKV]]: the two sides name the same object |
| $a \neq b$ | "$a$ is not equal to $b$" | the negation of $a = b$ |
| $x := 3$ | "$x$ is defined to be $3$" | a definition of the left side |
| $a \equiv b \pmod{n}$ | "$a$ is congruent to $b$ modulo $n$" | [[congruence modulo n|0WAY5WX8NY]]: $n$ divides $a - b$ |
| $f \equiv 0$ | "$f$ is identically zero" | $f(x) = 0$ for every $x$ |
| $a \approx b$ | "$a$ is approximately $b$" | informal closeness, with no exact meaning |
| $G \cong H$ | "$G$ is isomorphic to $H$" | an [[isomorphism|PZMGQMDN25]] exists |
| $x \sim y$ | "$x$ is related to $y$" | an [[equivalence relation|0G8VEZ3WTK]] or another relation that the text fixes |
| $y \propto x$ | "$y$ is proportional to $x$" | $y = cx$ for a constant $c$ |

[[Equality, definition and equivalence signs|BCGR3NPPXC]] compares these signs in detail, with the one-way $=$ of big O.

### Logic

These signs build statements from statements.
In running text, the site writes the words, and it keeps the signs for displayed formulas.

| Symbol | Reading | Meaning |
|---|---|---|
| $\neg P$ | "not $P$" | [[negation|029JBBF693]] |
| $P \wedge Q$ | "$P$ and $Q$" | [[conjunction|025YZN3VJW]] |
| $P \vee Q$ | "$P$ or $Q$" | [[disjunction|0F72FK8EKB]], inclusive |
| $P \Rightarrow Q$ | "$P$ implies $Q$", "if $P$, then $Q$" | [[implication|0NMG7W7Q11]] |
| $P \Leftrightarrow Q$ | "$P$ if and only if $Q$" | the [[biconditional|0S6GMNJ62Y]] |
| $\forall x$ | "for every $x$" | the [[universal quantifier|0GHS47PDAQ]] |
| $\exists x$ | "there is an $x$" | the [[existential quantifier|0MSRQHCNN9]] |
| $\exists! x$ | "there is exactly one $x$" | existence and uniqueness |

### Sets: elements and subsets

The two signs $\in$ and $\subseteq$ are the ones students mix up most, so they sit next to each other here.

| Symbol | Reading | Meaning |
|---|---|---|
| $x \in A$, $x \notin A$ | "$x$ is an element of $A$", "$x$ is not in $A$" | [[membership|0QM0T7T3PZ]] |
| $\varnothing$ | "the empty set" | the [[empty set|0ECVK59Y03]] |
| $\{x \in A : P(x)\}$ | "the set of $x$ in $A$ such that $P(x)$" | [[set-builder notation|0TMZ89Q5KA]]; some books write a bar for the colon |
| $A \subseteq B$ | "$A$ is a subset of $B$" | every element of $A$ is in $B$; see [[subset|0BJR9QR08E]] |
| $A \subsetneq B$ | "$A$ is a proper subset of $B$" | $A \subseteq B$ and $A \neq B$ |
| $\lvert A \rvert$, $\# A$ | "the cardinality of $A$" | the [[cardinality|0G0ASKNA6Z]]; for a finite set, its number of elements |

### Sets: operations

These signs take sets and give a new set.

| Symbol | Reading | Meaning |
|---|---|---|
| $A \cup B$, $A \cap B$ | "$A$ union $B$", "$A$ intersect $B$" | [[union|0X1GSWNBN1]] and [[intersection|0ZNMMA9TF5]] |
| $A \setminus B$ | "$A$ minus $B$" | the [[set difference|05WTQ6FFPS]] |
| $A^c$ | "the complement of $A$" | the [[complement|0RKF1ZT5JJ]] in a fixed universe |
| $\mathcal{P}(A)$ | "the power set of $A$" | the [[power set|00E0YZCERH]], the set of all subsets of $A$ |
| $A \times B$ | "$A$ cross $B$" | the [[Cartesian product|09CEDJYBKP]], the set of pairs $(a, b)$ |

### Number systems and constants

The blackboard bold letters name the standard number systems.

| Symbol | Reading | Meaning |
|---|---|---|
| $\mathbb{N}$ | "N", "the natural numbers" | the [[natural numbers|0MWKJ44V5A]] $0, 1, 2, \ldots$; the site includes $0$ |
| $\mathbb{Z}$ | "Z", "the integers" | the [[integers|0C4JS9RF5M]] |
| $\mathbb{Q}$ | "Q", "the rationals" | the [[rational numbers|0NCJ5WXN6Z]] |
| $\mathbb{R}$ | "R", "the reals" | the [[real numbers|08J2M1JYAG]] |
| $\mathbb{C}$ | "C", "the complex numbers" | the [[complex numbers|09FTAET5Z4]] |
| $\pi$ | "pi" | the [[ratio of the circumference of a circle to its diameter|0C1VYVNV2N]] |
| $e$ | "e" | the [[base of the natural logarithm|0MVCFMW7S4]] |
| $i$ | "i" | the [[imaginary unit|0ESCX36MMC]], with $i^2 = -1$ |
| $\infty$ | "infinity" | [[infinity|YZR3KZMQNZ]], used in limits and intervals; not a real number |

### Functions

The arrow signs say where a function starts and ends, and where it sends each point.

| Symbol | Reading | Meaning |
|---|---|---|
| $f \colon A \to B$ | "$f$ from $A$ to $B$" | a [[function|0EPAT51DXQ]] with domain $A$ and codomain $B$ |
| $x \mapsto x^2$ | "$x$ maps to $x$ squared" | the function that sends $x$ to $x^2$ |
| $g \circ f$ | "$g$ after $f$" | the [[composition|0THBK9V825]] $x \mapsto g(f(x))$ |
| $f^{-1}$ | "$f$ inverse" | the [[inverse function|0J2WAR83WP]] of a bijection |
| $f(A)$ | "the image of $A$ under $f$" | the [[image of a set|07XF282NWH]] $\{f(x) : x \in A\}$ |
| $f^{-1}(B)$ | "the preimage of $B$ under $f$" | the set $\{x : f(x) \in B\}$; it exists for every $f$ |

The last row is a trap.
For $f(x) = x^2$ on $\mathbb{R}$, the function has no inverse, yet $f^{-1}(\{4\}) = \{-2, 2\}$ is a well-defined set.

### Sums, limits and calculus

These signs carry a running variable, and the reading names it.

| Symbol | Reading | Meaning |
|---|---|---|
| $\sum_{i=1}^{n} a_i$ | "the sum of $a_i$ for $i$ from $1$ to $n$" | $a_1 + a_2 + \cdots + a_n$ |
| $\prod_{i=1}^{n} a_i$ | "the product of $a_i$ for $i$ from $1$ to $n$" | $a_1 a_2 \cdots a_n$ |
| $\lim_{x \to a} f(x)$ | "the limit of $f(x)$ as $x$ tends to $a$" | the [[limit of a function|0PKRYB8ATM]] |
| $f'(x)$, $\frac{dy}{dx}$ | "$f$ prime of $x$", "d y by d x" | the [[derivative|0V1EJCT8G6]] |
| $\frac{\partial f}{\partial x}$ | "partial f by partial x" | the [[partial derivative|09EGC6F8PT]] |
| $\int_a^b f(x)\,dx$ | "the integral from $a$ to $b$ of $f(x)$ d x" | the [[definite integral|04TMP0XGMJ]] |
| $\nabla f$ | "grad f", "nabla f" | the [[gradient|0ABK9V9Y64]] |
| $f = O(g)$ | "$f$ is big O of $g$" | [[big O notation|0TGV80E6A4]]: $\lvert f \rvert \leq C \lvert g \rvert$ eventually |

### Linear algebra

| Symbol | Reading | Meaning |
|---|---|---|
| $A^{\top}$ | "A transpose" | the [[transpose|09DXWYRD43]] |
| $\det A$ | "the determinant of $A$" | the [[determinant|00KDZRW4C0]] |
| $I_n$ | "the $n$ by $n$ identity matrix" | the [[identity matrix|06DW9BAWB1]] |
| $v \cdot w$ | "v dot w" | the [[dot product|0S52TNNTH9]] |
| $\langle v, w \rangle$ | "the inner product of $v$ and $w$" | an [[inner product|0NB0AWGJBW]] |
| $\lVert v \rVert$ | "the norm of $v$" | a [[norm|0V2WP9B1MF]] |

### Number theory and algebra

| Symbol | Reading | Meaning |
|---|---|---|
| $a \mid b$ | "$a$ divides $b$" | [[divisibility|0PG2H7WKGG]]: $b = ak$ for an integer $k$ |
| $\gcd(a, b)$ | "the gcd of $a$ and $b$" | the [[greatest common divisor|0C8WYW4KYQ]] |
| $\mathbb{Z}/n\mathbb{Z}$ | "Z mod n Z" | the [[integers modulo $n$|03VFZ2WETT]] |
| $\langle g \rangle$ | "the subgroup generated by $g$" | a [[cyclic group|0KVGH0J5B3]] |
| $G/N$ | "G mod N" | the [[quotient group|0KYX2N69J0]] |
| $\ker \varphi$ | "the kernel of phi" | the [[kernel of a homomorphism|0W88CEGQP1]] |

Watch the difference between $a \mid b$ and $a / b$.
The first is a statement, true or false: $3 \mid 12$ is true.
The second is a number: $3 / 12 = 0.25$.

### Probability

| Symbol | Reading | Meaning |
|---|---|---|
| $P(A)$ | "the probability of $A$" | a [[probability measure|059TJN0NZ1]] applied to the event $A$ |
| $P(A \mid B)$ | "the probability of $A$ given $B$" | the [[conditional probability|0990W5PN13]] |
| $E[X]$ | "the expectation of $X$" | the [[expected value|0WQNRCNY3M]] |
| $\operatorname{Var}(X)$ | "the variance of $X$" | the [[variance|0477R9PYAE]] |

### Symbols outside formulas

Some marks belong to the text of a proof, not to any formula.

| Symbol | Reading | Meaning |
|---|---|---|
| $\blacksquare$, $\square$ | "end of proof" | the tombstone; see [[end of proof marks|ET9J6R9T5C]] |
| $\therefore$ | "therefore" | the next line follows from the lines before |
| $\because$ | "because" | the reason for the line before |

The written short forms, such as `iff` and `wlog`, are words, not symbols, and [[mathematical abbreviations|4ZNYMYRRY3]] lists them.

### One sign, several meanings

The worst traps are signs with two common meanings.
Each row below gives both readings side by side and the clue that tells you which one the author uses.

| Sign | First reading | Second reading | How to tell |
|---|---|---|---|
| $\lvert X \rvert$ | absolute value of a number | number of elements of a set, or $\det X$ of a matrix | the type of $X$ |
| $\equiv$ | congruence, followed by $\pmod{n}$ | "identically equal" between functions | a modulus is written, or the sides are functions |
| $A \subset B$ | subset, equality allowed | proper subset | the notation list of the book, or whether it also uses $\subsetneq$ |
| $f^{-1}$ | inverse function | preimage $f^{-1}(B)$ of a set | the argument is a point or a set |
| $(a, b)$ | open interval | ordered pair, or $\gcd(a, b)$ in older number theory | the sentence says "interval", "point" or "divisor" |
| $\log x$ | base $e$ | base $10$ or base $2$ | the field: analysis, school and engineering, computer science |

When no clue decides, test the formula on a small case under each reading, and keep the reading that makes the text true.

### What is not a formula

A string of signs can break the types, and then it means nothing.
In $x \in \subseteq A$, the sign $\in$ needs a set on its right, and "$\subseteq A$" is not a set.
In $2 \mid 6 = 3$, the part $2 \mid 6$ is the statement "$2$ divides $6$", and a statement cannot equal the number $3$.
The tombstone $\blacksquare$ at the end of a proof is not part of any formula either; it works like a full stop.

### Watch out

The arrow $\Rightarrow$ means "implies", not "the next line is".
A student who writes $x^2 = 4 \Rightarrow x = 2$ claims a false implication, because $x = -2$ also satisfies $x^2 = 4$.
Write words such as "so" between the steps of a computation, and keep $\Rightarrow$ for real implications.

Next, $\in$ and $\subseteq$ are not interchangeable.
We have $1 \in \{1, 2\}$ and $\{1\} \subseteq \{1, 2\}$, but $\{1\} \notin \{1, 2\}$, because the elements of $\{1, 2\}$ are the numbers $1$ and $2$, not sets.

### History

Robert Recorde introduced the equals sign $=$ in 1557.
Gottfried Wilhelm Leibniz introduced the integral sign $\int$ and the letter $d$ for differentials in the 1670s.
Leonhard Euler's books made the letters $e$, $\pi$ and $i$ and the notation $f(x)$ standard.
Paul Halmos is credited with the tombstone $\blacksquare$ as an end of proof mark.

### Try it

First, read $\forall \varepsilon > 0 \; \exists N \in \mathbb{N} : 1/N < \varepsilon$ aloud and decide whether it is true.
It says "for every $\varepsilon$ greater than $0$ there is a natural number $N$ such that $1/N$ is less than $\varepsilon$", and it is true: take any natural number $N > 1/\varepsilon$.

Second, compute $\lvert \{x \in \mathbb{Z} : x^2 < 5\} \rvert$.
The integers with $x^2 < 5$ are $-2, -1, 0, 1, 2$, so the bars give the cardinality $5$.

## Explanations

### L1 human

A mathematical symbol is a short way to write a word or a phrase.
The sign $<$ means "is less than", so $2 < 5$ is the sentence "two is less than five".
Every symbol can be read aloud, and a good habit is to read each formula as a full sentence.
The glossary works like a dictionary: it lists the symbols, tells you how to say each one, and points to a page that explains it.
Some symbols mean different things in different parts of mathematics, so the glossary also says how to tell the meanings apart.

### L2 human

Read and check the formula $\forall n \in \mathbb{N} \; \exists m \in \mathbb{N} : m > n^2$.
The first part, $\forall n \in \mathbb{N}$, reads "for every natural number $n$".
The second part, $\exists m \in \mathbb{N}$, reads "there is a natural number $m$", and the colon reads "such that".
So the whole sentence is "for every natural number $n$ there is a natural number $m$ with $m$ greater than $n$ squared".
It is true, because for a given $n$ the number $m = n^2 + 1$ works:
$$m = n^2 + 1 > n^2.$$
Now swap the two quantifiers: $\exists m \in \mathbb{N} \; \forall n \in \mathbb{N} : m > n^2$.
The same signs in a new order say that one $m$ beats every square, and this is false, since $n = m$ gives $m^2 \geq m$.
So translating a formula into words comes before any proof, and the order of the words carries the meaning.

### L3 human

A symbol is a name, and a table of symbols is a small type system.
Each sign has an arity and a type: $\in$ takes an element and a set and gives a statement, while $\cap$ takes two sets and gives a set.
Proof assistants such as Lean make these types explicit, and they reject a formula with a type error before any proof starts.
Overloading is resolved by the same types: $\lvert x \rvert$ is an absolute value when $x$ is a number and a cardinality when $x$ is a set.
Some meanings also depend on a context that the text fixes once, such as the modulus of $\equiv$ or the universe of a complement.
[[Conflicting conventions|CSFEP56A7D]] and [[abuse of notation|JV68YRB5YZ]] study the places where one sign carries several meanings on purpose.
