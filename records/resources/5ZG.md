---
records:
    - id: 5ZGMWPE4JE
      kind: monograph
      title: Boundary Integral Equations
      creators:
        - name: George C. Hsiao
          role: author
        - name: Wolfgang L. Wendland
          role: author
      date: "2008"
      expressions:
        - key: e1
          kind: edition
          date: "2008"
          ids:
            doi:
                - 10.1007/978-3-030-71127-6
                - 10.1007/978-3-540-68545-6
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2021"
              ids:
                isbn:
                    - "9783030711269"
                    - "9783030711276"
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2008"
              ids:
                isbn:
                    - "9783540152842"
                    - "9783540685456"
      relations:
        - kind: part_of
          to: 2M0N86YNGA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-030-71127-6
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-540-68545-6
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
