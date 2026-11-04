---
tag: EDH0T8EKDE
kind: statement
role: proposition
name: Assignment axiom schema
sources:
  - wikipedia: en:182708@r1359292368
    locator: Hoare logic, section Rules > Assignment axiom schema
    note: adopted
    mention: wikipedia://en/182708#JQAJ
    sections: [Statement]
inventory: [9VC448M8FR]
---

## Statement

The assignment axiom states that, after the assignment, any predicate that was previously true for the right-hand side of the assignment now holds for the variable. Formally, let $P$ be an assertion in which the variable $x$ is free. Then:

$$\dfrac{}{\{P[E/x]\} x := E \{P\}}$$

where $P[E/x]$ denotes the assertion $P$ in which each free occurrence of $x$ has been replaced by the expression $E$.

The assignment axiom scheme means that the truth of $P[E/x]$ is equivalent to the after-assignment truth of $P$. Thus, were $P[E/x]$ true before the assignment, by the assignment axiom, then $P$ would be true afterwards. Conversely, were $P[E/x]$ false (i.e. $\neg P[E/x]$ true) prior to the assignment statement, $P$ must then be false afterwards.

Examples of valid triples include:

- $$\{ x+1 = 43 \} y := x + 1 \{ y = 43 \}$$
- $$\{ x + 1 \leq N \} x := x + 1 \{ x \leq N \}$$

All preconditions that are not modified by the expression can be carried over to the postcondition. In the first example, assigning $y:=x+1$ does not change the fact that $x+1=43$, so both statements may appear in the postcondition. Formally, this result is obtained by applying the axiom schema with $P$ being ($y=43$ and $x+1=43$), which yields $P[(x+1)/y]$ being ($x+1=43$ and $x+1=43$), which can in turn be simplified to the given precondition $x+1=43$.

The assignment axiom scheme is equivalent to saying that to find the precondition, first take the post-condition and replace all occurrences of the left-hand side of the assignment with the right-hand side of the assignment. Be careful not to try to do this backwards by following this *incorrect* way of thinking: $\{P\} x:=E \{P[E/x]\}$; this rule leads to nonsensical examples like:

$$\{ x = 5 \} x := 3 \{ 3 = 5 \}$$

Another *incorrect* rule looking tempting at first glance is $\{P\} x:=E \{P \wedge x=E\}$; it leads to nonsensical examples like:

$$\{ x = 5 \} x := x + 1 \{ x = 5 \wedge x = x + 1 \}$$

While a given postcondition $P$ uniquely determines the precondition $P[E/x]$, the converse is not true. For example:

- $$\{ 0 \leq y\cdot y \wedge y\cdot y \leq 9 \} x := y \cdot y \{ 0 \leq x \wedge x \leq 9 \},$$
- $$\{ 0 \leq y\cdot y \wedge y\cdot y \leq 9 \} x := y \cdot y \{ 0 \leq x \wedge y\cdot y \leq 9 \},$$
- $\{ 0 \leq y\cdot y \wedge y\cdot y \leq 9 \} x := y \cdot y \{ 0 \leq y\cdot y \wedge x \leq 9 \}$, and
- $$\{ 0 \leq y\cdot y \wedge y\cdot y \leq 9 \} x := y \cdot y \{ 0 \leq y\cdot y \wedge y\cdot y \leq 9 \}$$

are valid instances of the assignment axiom scheme.

The assignment axiom proposed by Hoare *does not apply* when more than one name may refer to the same stored value. For example,

$$\{ y = 3 \} x := 2 \{ y = 3 \}$$

is wrong if $x$ and $y$ refer to the same variable (aliasing), although it is a proper instance of the assignment axiom scheme (with both $\{P\}$ and $\{P[2/x]\}$ being $\{y=3\}$).
