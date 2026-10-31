---
records:
    - id: VVDJP1CNZ8
      kind: monograph
      title: Advanced Linear Algebra
      creators:
        - name: Steven Roman
          role: author
      date: "1992"
      expressions:
        - key: e1
          kind: edition
          date: "1992"
          ids:
            doi:
                - 10.1007/978-0-387-72831-5
                - 10.1007/978-1-4757-2178-2
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2008"
              ids:
                isbn:
                    - "9780387728285"
                    - "9780387728315"
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1992"
              ids:
                isbn:
                    - "9781475721805"
                    - "9781475721782"
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-0-387-72831-5
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-2178-2
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
