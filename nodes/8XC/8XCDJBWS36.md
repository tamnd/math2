---
tag: 8XCDJBWS36
kind: example
name: Unreliable messages never create common knowledge
msc: ["03B42", "68M14"]
topics: [CQM9SRN8PM]
audience: grad
not_instance_of:
  - target: 7BCMKF2P7X
    note: after any finite number of delivered messages, the plan is known to some finite depth only, and is never common knowledge
uses: [RRRHWH9F6Y, 8K0CMPQXXB, 0G8VEZ3WTK, 0ASJVEFA9J]
sources:
  - book: isbn:9780262562003
    locator: Fagin, Halpern, Moses and Vardi, Reasoning about Knowledge, chapter 6
  - url: https://en.wikipedia.org/wiki/Two_Generals%27_Problem
    locator: lead section
---

## Example

Two generals must attack together, and they talk by messengers who may be caught.
Agent $a$ may form a plan $p$ to attack and send it to agent $b$.
Every delivered message is acknowledged, so message 1 goes from $a$ to $b$, message 2 from $b$ to $a$, and so on.
Any message may be lost, and after a loss nobody sends again.

World $0$ has no plan and no message.
World $k \ge 1$ has a plan, and in it messages $1$ to $k - 1$ arrive and message $k$ is lost.
So $p$ is true exactly at the worlds $k \ge 1$.
Agent $a$ knows whether there is a plan and counts the even messages she received, which is $\lfloor (k - 1)/2 \rfloor$ at world $k \ge 1$.
Agent $b$ counts the odd messages he received, which is $0$ at world $0$ and $\lfloor k/2 \rfloor$ at world $k \ge 1$.
So the relations are [[equivalence relations|0G8VEZ3WTK]].
The classes of $a$ are $\{0\}, \{1, 2\}, \{3, 4\}, \dots$, and the classes of $b$ are $\{0, 1\}, \{2, 3\}, \{4, 5\}, \dots$.

Let $G = \{a, b\}$ and $E_G^0 p = p$.
We show by [[induction|0ASJVEFA9J]] on $j \ge 0$ that $E_G^j p$ is true at world $k$ exactly when $k \ge j + 1$.

1. For $j = 0$ the claim is the definition of $p$.
2. Assume the claim for $j$.
   Then $E_G^{j+1} p$ holds at $k$ exactly when both classes of $k$ lie inside $\{j + 1, j + 2, \dots\}$.
3. At $k = 0$, agent $a$'s class is $\{0\}$, so this fails.
4. For odd $k \ge 1$ the classes are $\{k, k + 1\}$ for $a$ and $\{k - 1, k\}$ for $b$, and for even $k$ they are $\{k - 1, k\}$ for $a$ and $\{k, k + 1\}$ for $b$.
   In both cases the smallest world in the two classes is $k - 1$.
5. So both classes lie above $j$ exactly when $k - 1 \ge j + 1$, that is, $k \ge j + 2$, which is the claim for $j + 1$.

At world $k \ge 1$ this makes $E_G^{k-1} p$ true and $E_G^k p$ false.
In particular $C_G p$ is false at every world, by the definition of [[common knowledge|RRRHWH9F6Y]].

## Remarks

Each delivered message adds exactly one level of "everyone knows", and no finite number of messages gives common knowledge.
The worlds form one chain $0, 1, 2, 3, \dots$ under the two relations, so every world reaches world $0$, where $p$ is false.
That is the same conclusion by [[the reachability clause|8K0CMPQXXB]].

A simultaneous attack needs common knowledge of the plan, so no protocol over this channel can guarantee one.
Halpern and Moses proved the general form: when delivery is not guaranteed, sending messages cannot create common knowledge.
If the channel were reliable, world $k$ would not exist for any $k$, and a single message would make the plan common knowledge.

## Explanations

### L1 human

General A sends "attack at dawn".
General B gets it, but A does not know that, so B sends a reply.
Now A knows that B knows, but B does not know that A got the reply.
Every reply adds one level, and the sender of the last message is always in doubt.
So they never reach common knowledge.

### L2 human

At world $4$, messages 1, 2 and 3 arrived and message 4 was lost.
The claim gives $E_G^3 p$ at $4$, since $4 \ge 3 + 1$, and it denies $E_G^4 p$, since $4 < 4 + 1$.
We can see the failure as a path of four steps to world $0$:
$$4 \xrightarrow{a} 3 \xrightarrow{b} 2 \xrightarrow{a} 1 \xrightarrow{b} 0.$$
Check: $\{3, 4\}$ is a class of $a$, $\{2, 3\}$ of $b$, $\{1, 2\}$ of $a$ and $\{0, 1\}$ of $b$.
The typical use is to explain why protocols over lossy channels cannot achieve simultaneous action.
Watch out: the depth of knowledge grows with the number of messages, but common knowledge is not a limit that is ever reached.

### L3 human

The model is a chain in which the two partitions interleave, so their meet has a single block.
Rubinstein's electronic mail game (1989) uses the same chain to show that behavior under very deep mutual knowledge can differ from behavior under common knowledge.
