---
kind: statement
msc:
- 05C10
name: K5 is not planar
role: theorem
sources:
- locator: ptx/sec_gt-planar.ptx:299
  url: https://github.com/oscarlevin/discrete-book/blob/a8e4949bc45daf100930c1182983778f56ab689f/ptx/sec_gt-planar.ptx#L299
tag: SKNVHHVVK7
uses:
- 03WKB2H474
- 029JQEK15B
- 0SM1REAVYJ
---

## Statement

The [[complete graph|03WKB2H474]] on five vertices, $K_5$, is not [[planar|029JQEK15B]]. No drawing of it in the plane avoids edge crossings.

## Remarks

The graph $K_5$ has $5$ vertices and $10$ edges. The [[edge bound for planar graphs|0SM1REAVYJ]] says that a planar graph with $v \ge 3$ vertices has at most $3v - 6$ edges. For $v = 5$ this is $9$, which is less than $10$.

So $K_5$ cannot be planar.
