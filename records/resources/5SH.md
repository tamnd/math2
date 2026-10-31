---
records:
    - id: 5SHED29H9V
      kind: course
      title: Algebraic Topology
      creators:
        - name: G.K. Srinivasan
          role: instructor
      ids:
        course: 02qyf5152:111101002
      expressions:
        - key: e1
          kind: edition
          language: en
          manifestations:
            - key: m1
              kind: page
              publisher: IIT Bombay
              ids:
                nptel: "111101002"
      scope:
        value: in
        rule: S6
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111101002"
          level: manifestation
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to deferred
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.4 scope/1
          note: from deferred to in
    - id: 5SHYB7TPS1
      kind: monograph
      title: On Dirichlet's Boundary Value Problem
      creators:
        - name: Christian G. Simader
          role: author
      date: "1972"
      expressions:
        - key: e1
          kind: edition
          date: "1972"
          ids:
            doi: 10.1007/bfb0058774
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1972"
              ids:
                isbn:
                    - "9783540059035"
                    - "9783540375890"
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0058774
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
