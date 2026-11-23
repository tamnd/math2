---
tag: PMN32E37BW
kind: example
name: The MIU system
aliases: [mu-puzzle]
msc: ["03B22", "00A08"]
topics: [H8QZY0RZXZ]
audience: ug1
instance_of: [439M8B4DY2]
uses: [439M8B4DY2, 1P6EP01HZF, T62EJ749R5]
sources:
  - url: https://en.wikipedia.org/wiki/MU_puzzle
    locator: lead section
---

## Example

The MIU system is a [[formal system|439M8B4DY2]] with three letters, one axiom and four rules, and the question it poses is whether the string $MU$ is a theorem.
Its alphabet is $\{ M, I, U \}$, and every finite [[string|1P6EP01HZF]] over the alphabet is a formula.
The only axiom is $MI$.
In the rules, $x$ and $y$ stand for any strings, including the empty string:
$$\begin{aligned} &\text{R1: from } xI \text{ infer } xIU, &&\text{R2: from } Mx \text{ infer } Mxx, \\ &\text{R3: from } xIIIy \text{ infer } xUy, &&\text{R4: from } xUUy \text{ infer } xy. \end{aligned}$$
In words, R1 adds $U$ after a final $I$, R2 doubles the part after an initial $M$, R3 replaces $III$ by $U$, and R4 deletes $UU$.

First we check that the four parts meet the definition.

1. The alphabet is finite and every string is a formula, so it is [[decidable|T62EJ749R5]] whether a string is a formula.
2. There is one axiom, so it is decidable whether a string is an axiom.
3. Each rule has one premise.
   To decide whether a rule turns a given premise into a given conclusion, we try the finitely many positions in the premise.

Next we derive the theorem $MUIIU$.
Each line names the rule and the strings $x$ and $y$ that it uses:
$$\begin{array}{lll} 1. & MI & \text{axiom} \\ 2. & MII & \text{R2 on 1, } x = I \\ 3. & MIIII & \text{R2 on 2, } x = II \\ 4. & MIIIIU & \text{R1 on 3, } x = MIII \\ 5. & MUIU & \text{R3 on 4, } x = M,\ y = IU \\ 6. & MUIUUIU & \text{R2 on 5, } x = UIU \\ 7. & MUIIU & \text{R4 on 6, } x = MUI,\ y = IU \end{array}$$

Finally we prove that $MU$ is not a theorem.
Let $n(w)$ be the number of letters $I$ in a string $w$.

1. The axiom has $n(MI) = 1$, which is not divisible by $3$.
2. R1 and R4 add or delete only letters $U$, so they do not change $n$.
3. R3 removes exactly three letters $I$, so $n$ drops by $3$ and its remainder modulo $3$ stays the same.
4. R2 doubles $n$, because $n(Mxx) = 2\, n(x) = 2\, n(Mx)$.
   Doubling turns remainder $1$ into remainder $2$, and remainder $2$ into $4$, which has remainder $1$.
5. So each rule turns a string whose count is not divisible by $3$ into another such string.
6. By induction on the length of a derivation, no theorem has a count divisible by $3$: each line is the axiom (step 1) or comes from an earlier line by a rule (step 5).
7. The string $MU$ has $n(MU) = 0$, which is divisible by $3$, so $MU$ is not a theorem.

## Remarks

### The invariant

The number of letters $I$ modulo $3$ is an invariant: the axiom has a nonzero value, and every rule keeps the value nonzero.
Invariants are the standard way to show that a formula is not a theorem.
The proof of [[soundness|4A84VHDTHV]] has the same shape, with "true under every valuation" as the property that the axioms have and the rules keep.
The choice of axiom matters.
With the axiom $MII$ the same invariant still excludes $MU$, because $2$ is not divisible by $3$; with the axiom $MIII$, rule R3 gives $MU$ in one step.

### All the theorems

The invariant does more than exclude $MU$: it describes every theorem.
A string is a theorem exactly when it is $M$ followed by a string $x$ of letters $I$ and $U$ such that $n(x)$ is not divisible by $3$.
One direction is the proof above, together with the fact that no rule creates or moves an $M$.
For the other direction, take such an $x$ with $n$ letters $I$ and $u$ letters $U$, and put $N = n + 3u$, which is not divisible by $3$.

1. Applying R2 $k$ times to $MI$ gives $M I^{2^k}$, where $I^m$ means $m$ letters $I$.
2. The powers $1, 2, 4, 8, \dots$ have remainders $1, 2, 1, 2, \dots$ modulo $3$.
   So some $k$ has $2^k \geq N$ and $2^k - N = 3j$ with $j \geq 0$.
3. If $j$ is even, replace the last $3j$ letters $I$ by $U^j$ with R3, and delete $U^j$ with R4 in $j/2$ steps.
   This gives $M I^N$.
4. If $j$ is odd, first apply R1 to get $M I^{2^k} U$.
   Then R3 gives $M I^N U^{j+1}$, and R4 deletes the even number $j + 1$ of letters $U$.
5. Replace each $U$ of $x$ by $III$; the result is $I^N$.
   Starting from $M I^N$, apply R3 once at each block $III$ that stands for a $U$ of $x$, and you reach $Mx$.

So the set of theorems is decidable: check that the string is $M$ followed by letters $I$ and $U$, and count the letters $I$.

### Try it

Is $MUUIII$ a theorem?
No, because it has three letters $I$.

Derive $M I^7$.
Here $N = 7$ and $2^4 - 7 = 9$, so $k = 4$ and $j = 3$, which is odd.
Apply R2 four times to get $M I^{16}$, R1 to get $M I^{16} U$, R3 three times to get $M I^7 U^4$, and R4 twice to get $M I^7$.

## Explanations

### L1 human

The MIU system is a puzzle with three letters.
You start with MI, and four rules let you make new strings.
For example, MI becomes MII by doubling the part after M, and MIIII becomes MUI by replacing three I's by one U.
The puzzle asks whether you can reach MU.
Count the I's: you start with 1, doubling turns 1 into 2 and 2 into 4, and the other rules keep the count or remove exactly 3.
So the count is never a multiple of 3, and MU, with zero I's, is out of reach.

### L2 human

Suppose you meet the MIU system with no hint and want to settle $MU$.
A search finds many theorems, such as $MII$, $MIIII$, $MUI$ and $MUIIU$, but never $MU$, and a failed search proves nothing.
So you look for a quantity that the rules control.
The letters $U$ come and go freely, so they are a poor choice.
The letters $I$ are better: R3 changes their number by $3$ and R2 doubles it, so the count modulo $3$ is the natural thing to follow.
The axiom gives $1$, doubling moves between $1$ and $2$, and nothing reaches $0$.
This is the typical use of an invariant: find a quantity, check the axiom, check each rule.
Watch out for a quantity that the rules only keep in one direction, such as "the count is odd": R3 turns $3$ letters $I$ into $0$, so oddness is not kept.

### L3 human

The MIU system is a string rewriting system, and its set of theorems turns out to be decidable by the counting test above.
That is unusual: for a general formal system the set of theorems is only computably enumerable, and for first-order logic it is undecidable by [[Church's theorem|VA6BNNY2YC]].
Hofstadter used the puzzle in *Gödel, Escher, Bach* to contrast reasoning inside a system, which only applies rules, with reasoning about the system, which finds the invariant.
That contrast is the distinction between [[object language and metalanguage|D9G8M42GKC]], and the incompleteness theorems rest on it.
