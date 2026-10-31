---
records:
    - id: RD8GYJ31BP
      kind: monograph
      title: Basic Linear Algebra
      creators:
        - name: T. S. Blyth
          role: author
        - name: E. F. Robertson
          role: author
      date: "1998"
      expressions:
        - key: e1
          kind: edition
          date: "1998"
          ids:
            doi:
                - 10.1007/978-1-4471-0681-4
                - 10.1007/978-1-4471-3496-1
          manifestations:
            - key: m1
              kind: print
              publisher: Springer London
              date: "2002"
              ids:
                isbn:
                    - "9781852336622"
                    - "9781447106814"
            - key: m2
              kind: print
              publisher: Springer London
              date: "1998"
              ids:
                isbn:
                    - "9783540761228"
                    - "9781447134961"
      relations:
        - kind: part_of
          to: 3YXAC8SZBF
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4471-0681-4
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4471-3496-1
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
